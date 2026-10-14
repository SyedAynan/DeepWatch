# TECHSPEC.md — Technical Specification (DeepWatch)

**Status:** Stack decided for DeepWatch; dependency versions pinned at scaffold time
**Created:** 2026-10-07
**Updated:** 2026-10-14
**Role:** concrete technology choices. `ARCHITECTURE.md` owns system shape;
this file owns stack details.

> Supersedes the earlier placeholder stack (MediaPipe/WebGL2), which the user
> confirmed was never a real choice.

## 1. Runtimes & languages
- **Python 3.11+ (uv-managed):** all ML/training/inference code. Machine has
  Python 3.14 + uv; project pins ≥ 3.11 for ML-ecosystem compatibility.
- **JavaScript/TypeScript or plain HTML/JS:** minimal web frontend for
  upload/visualisation (decision deferred to Phase 3 — plain JS preferred to
  keep build-free).
- **Node 20+:** only if a JS toolchain is needed for the frontend.

Package manager: **uv** for Python (fast, lockfile-reproducible); npm for any JS.

## 2. Frameworks & key libraries

| Technology | Role / reason |
| --- | --- |
| PyTorch (+ torchvision) | Model training/inference; base papers' reference code is PyTorch |
| timm / pretrained backbones (Xception, ConvNeXt, ResNet) | Detection and attribution backbones matching base papers [1][3] |
| OpenCV + ffmpeg | Video frame extraction, audio extraction, compression augmentation |
| librosa / torchaudio | Speech anti-spoofing feature extraction (ASVspoof protocol) |
| MediaPipe or dlib (face crop) | Face-region extraction for detection/attribution inputs |
| FastAPI + Uvicorn | Local REST API serving models to the frontend |
| ReportLab / WeasyPrint | Forensic PDF report generation |
| SQLite (via SQLAlchemy or stdlib) | Analysis-log storage (append-only audit trail) |
| hashlib (stdlib) | SHA-256 evidence hashing (FR-01) |
| Grad-CAM / saliency utilities | Explanation heatmaps (D4) |
| pytest | Unit/integration tests |

Exact versions pinned in `pyproject.toml`/`uv.lock` at scaffold time.

## 3. Build, run, test
Planned commands:

| Command | Purpose | Passing means |
| --- | --- | --- |
| `uv run api` (or `uvicorn app:api`) | Serve the local API | API answers on localhost |
| `uv run pytest` | Run test suite | All tests pass |
| `uv run eval --benchmark ff++` | Reproduce base-paper eval | Metrics computed on the benchmark split |
| `npm run dev` (if JS UI) | Serve frontend | UI reachable, calls API |

## 4. Configuration & environment
`.env.example` holds placeholders: model checkpoint paths, dataset root,
device (cuda/cpu), blockchain testnet endpoint (optional). Real `.env` is
git-ignored. No secrets are required for core function.

## 5. External services & dependencies
- **Public datasets (download once, stored locally):** FaceForensics++,
  Celeb-DF, DFDC, OW-DFA, ASVspoof 2021 LA/DF partitions.
- **Pretrained backbones:** torchvision/timm checkpoints (public weights).
- **Optional test blockchain:** public testnet RPC for report-hash anchoring
  (D5) — optional; platform works without it.
- No paid services, no API keys for core features.

## 6. Error handling & logging
- Every analysis run writes an append-only analysis log (SQLite + file):
  input hash, model versions, parameters, outputs, timestamps (FR-06).
- Never log raw user media contents or secrets; log hashes and metadata only.
- Model failures surface as explicit "analysis failed" states — never silently
  return a confident-looking default score.

## 7. Performance targets
- Single-media analysis < 60 s on student hardware (CPU fallback required).
- Detection target: ≥ UCF baseline (0.828 mean cross-dataset AUC) on the same
  benchmarks — improvement is a goal, not a guarantee.
- Memory: run on ≤ 8 GB VRAM or CPU; batch size 1 acceptable.

## 8. Key technical decisions

| Decision | Why | Date |
| --- | --- | --- |
| Python + PyTorch stack | Base papers' reference implementations and the whole deepfake-forensics ecosystem are PyTorch | 2026-10-14 |
| uv for Python packaging | Fast, lockfile-reproducible; already on the machine | 2026-10-14 |
| Local-first processing (no cloud APIs) | PRD NFR-04: user media must not leave the device | 2026-10-14 |
| FastAPI + minimal web UI | Demo needs an upload/visualise surface without a heavy frontend stack | 2026-10-14 |
| SQLite analysis log | Zero-config append-only audit trail suitable for forensic traceability | 2026-10-14 |

> Rule: every choice needs a why. Never invent capabilities a library doesn't have.
