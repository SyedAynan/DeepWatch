# ARCHITECTURE.md — DeepWatch

**Status:** Architecture defined for DeepWatch (direction locked 2026-10-14)
**Created:** 2026-10-07
**Updated:** 2026-10-14

## 1. System overview
DeepWatch is a local-first forensic analysis platform for suspected deepfake
media. A user uploads an image, video, or audio file; the platform preserves
the original (SHA-256 hash + immutable copy), runs a multi-stage analysis
pipeline (visual detection, speech anti-spoofing, lip–speech consistency,
generation-method attribution, explanation), fuses the channel scores into one
assessment, and emits an explainable forensic PDF report. All processing is
local; no user media leaves the device.

## 2. Technology stack
Decided (details in TECHSPEC.md): Python 3.11+ with uv, PyTorch, timm/vision
backbones (Xception, ConvNeXt), OpenCV + ffmpeg, librosa/torchaudio, FastAPI,
SQLite (analysis log), ReportLab/WeasyPrint (PDF), minimal HTML/JS frontend,
pytest. Optional: public test blockchain for report-hash anchoring.

## 3. Data model / storage
No cloud database. Local storage only:
- `evidence/` — preserved original uploads (immutable, hashed)
- `runs/` — per-analysis artifacts (frames, audio, heatmaps, logs)
- `analysis_log.db` (SQLite) — append-only audit trail: input hash, model
  versions, parameters, outputs, timestamps
- `models/` — model checkpoints with recorded hashes

Key entities: EvidenceItem(hash, path, metadata), AnalysisRun(id, evidence_id,
channel_scores, fused_score, attribution, status, timestamps),
ExplanationMap(run_id, kind, artifact_path), Report(run_id, pdf_path,
report_hash).

## 4. API / interfaces
Local REST (FastAPI), JSON:
- `POST /analyze` — upload file → returns run_id
- `GET /runs/{id}` — status + scores + attribution + artifact links
- `GET /runs/{id}/report.pdf` — forensic report
- `GET /runs/{id}/explain` — heatmap assets + plain-language reasons
Internal module boundaries:
- `ingest/` — hashing, preservation, metadata, media splitting (frames/audio)
- `detect/` — visual detection model (after UCF [1])
- `audio/` — speech anti-spoofing (ASVspoof protocol [4])
- `sync/` — lip–speech consistency
- `attribute/` — open-set attribution (after OW-DFA/CPL [3])
- `fuse/` — score fusion + calibrated confidence
- `explain/` — heatmaps + plain-language reasons
- `report/` — forensic PDF + optional hash anchoring

## 5. Folder structure
```
├── pyproject.toml / uv.lock        # Python project, reproducible env
├── src/deepwatch/
│   ├── ingest/  detect/  audio/  sync/  attribute/  fuse/  explain/  report/
│   ├── api/                        # FastAPI app
│   └── models/                     # checkpoint registry + hashes
├── web/                            # minimal upload/visualise UI
├── data/
│   ├── evidence/  runs/            # preserved inputs + run artifacts
│   └── datasets/                   # FF++, Celeb-DF, DFDC, OW-DFA, ASVspoof
├── tests/                          # pytest unit + integration tests
├── docs/                           # this documentation system
└── assets/                         # repo branding
```

## 6. External services & dependencies
- Public datasets (one-time download, stored locally).
- torchvision/timm pretrained weights (public).
- Optional test-blockchain RPC (report-hash anchoring; platform works without).
- No paid services; no API keys required for core function.

## 7. Security considerations
- Local-first: user media never leaves the device (PRD NFR-04).
- Originals preserved immutable; all processing on copies.
- Analysis log is append-only; model checkpoint hashes recorded to guarantee
  result reproducibility.
- API binds to localhost only by default.
- No PII collection; filenames may be pseudonymised to hashes in logs.

## 8. Scalability considerations
Single-user local tool by design. Compute scales with model size; CPU fallback
required, GPU optional. Future: batch-mode scanning for a folder of media.

## 9. Key decisions and why

| Decision | Why | Date |
| --- | --- | --- |
| Docs-first context system | project stays understandable across chats, sessions, and AI tools | 2026-10-07 |
| Local-first, no cloud | forensic use case demands media stays on-device | 2026-10-14 |
| PyTorch + published base methods | reproducibility against base papers' public code/benchmarks | 2026-10-14 |
| Append-only SQLite audit log | forensic traceability without infra cost | 2026-10-14 |
| Fuse audio + video | real fake video calls carry both channels; unimodal tools miss half the evidence | 2026-10-14 |
