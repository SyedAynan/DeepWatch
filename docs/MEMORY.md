# MEMORY.md — Project State

**Last updated:** 2026-10-14
**Current phase:** 0 — DONE; Phase 1 READY TO START
**Current task:** awaiting user go-ahead to build Phase 1; user verifies IEEE
Xplore access to the four base papers in parallel (formality)

## Completed
- 2026-10-14: **PROJECT DEFINED — "DeepWatch"**: a unified multimodal deepfake
  forensics and generation-method attribution platform. Wrote full PRD
  (problem, users, 5 features D1–D5 mapped to base-paper limitations L1–L4,
  FR-01..06, NFR-01..06, success criteria, novelty statement, base papers).
  Set the real tech stack in TECHSPEC (Python 3.11+ uv, PyTorch, FastAPI,
  SQLite audit log, minimal web UI — supersedes the placeholder
  MediaPipe/WebGL2 stack). ARCHITECTURE rewritten (local-first forensic
  pipeline, module boundaries, folder structure, security). PHASES,
  IMPLEMENTATIONPLAN, TRACKER rewritten for Phases 1–4 with acceptance
  criteria. REQUIREMENTS.md closed (all inputs supplied). Two-page styled
  research proposal PDF produced (docs/DeepWatch-Report.pdf).
- 2026-10-14: domain exploration → deepfake forensics chosen as the strongest
  "era + real-world problem" direction. IEEE base papers identified and
  verified via OpenAlex/Crossref: UCF (ICCV 2023, 0.996 in-dataset vs 0.828
  cross-dataset AUC), up-sampling artifacts (CVPR 2024), OW-DFA/CPL open-world
  attribution (ICCV 2023), ASVspoof 2021 (IEEE/ACM TASLP). IEEE Xplore
  full-text scraping confirmed blocked (HTTP 202 JS challenge); arXiv copies
  used for content, OpenAlex/DOIs for venue verification.
- 2026-10-14: pre-development workspace audit. Added `.env.example` and
  `docs/REQUIREMENTS.md`; corrected README benchmark table to planned targets;
  LICENSE verified (MIT, 2026 Syed Ayan); CI passes as a docs check.
- 2026-10-10: upgraded GitHub repository showcase — cyber neon banner
  (`assets/banner.png`), showcase README, LICENSE, CONTRIBUTING, SECURITY,
  CI workflow, issue/PR templates.
- 2026-10-07: repository scaffolded — `docs/` context system, README,
  .gitignore, `CLAUDE.md`; git initialized (8552ed9). Doc set extended —
  TECHSPEC, APPFLOW, SCHEMA, IMPLEMENTATIONPLAN, TRACKER (21dd84d).
  Novelty/landscape scan → `docs/RESEARCH.md`.

## Important decisions
- Docs-first workflow (see `CLAUDE.md`, `docs/RULES.md`).
- **Project = DeepWatch** (locked 2026-10-14). Domains integrated: AI/NN +
  cybersecurity + computer vision + (optional) blockchain hash-anchoring.
- Tech stack: Python 3.11+/uv, PyTorch, timm backbones, OpenCV+ffmpeg,
  librosa/torchaudio, FastAPI, SQLite, ReportLab/WeasyPrint, minimal web UI.
- Local-first processing — user media never leaves the device (PRD NFR-04).

## Known issues / blockers
- None technical. User-side formality: confirm the 4 base papers are
  accessible via IEEE Xplore through the college library.

## Tests / results
- None applicable yet (no code; Phase 1 not started).

## Next recommended step
Start Phase 1 per IMPLEMENTATIONPLAN: uv init → skeleton → FF++ loader →
ingest+hashing → baseline detector → AUC eval. User checks IEEE access
in parallel; record DOIs verified in RESEARCH.md §1 when confirmed.
