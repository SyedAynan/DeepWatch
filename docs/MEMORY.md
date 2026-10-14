# MEMORY.md — Project State

**Last updated:** 2026-10-14
**Current phase:** Research gates 1–6 DONE (blueprint committed); GATE 7 —
awaiting user approval to start building
**Current task:** user is enabling the machine GPU, then will approve/ revise
the research blueprint; on approval start Milestone 0 (uv init + skeleton +
ingest/hashing + eval harness)

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
Start Phase 1 per IMPLEMENTATIONPLAN: uv init → skeleton → ingest+hashing →
baseline detector via **DeepfakeBench** (which already implements UCF +
8 more detectors + the FF++/Celeb-DF/DFDC eval protocols). User checks
IEEE access in parallel; record DOIs verified in RESEARCH.md §1 when confirmed.

## Pre-build audit findings (2026-10-14)
- **Tooling OK:** Python 3.13.5, uv 0.12.10, ffmpeg 9.0.2, git, Node 24.
  Torch not installed yet (installs with `uv sync`). Disk: 158 GB free on S:.
- **No GPU detected** on this machine (nvidia-smi fails) — training must be
  CPU-realistic or planned around cloud/Colab GPU. Affects Phase 1 scope:
  baseline reproduction, not from-scratch training.
- **FF++ access is gated:** Google Form → emailed download script (can take a
  week). c23 version ≈10 GB, c40 ≈2 GB. Action: user submits the form NOW;
  meanwhile bootstrap with **DeepfakeBench's preprocessed data links** or the
  DFDC/DF40 sets which are more open.
- **DeepfakeBench (NeurIPS 2023, SCLBD, 1.1k stars) already implements UCF**
  and 35 other detectors, with eval protocols for exactly our datasets — using
  it as the Phase 1 baseline saves weeks and gives honest baseline numbers.
  License CC BY-NC-4.0 (fine for academic mini-project, not for commercial).
- **OW-DFA code:** Sun et al. arXiv:2309.11132 (verify repo exists when starting
  Phase 2; if none, reimplement CPL per paper).
- **ASVspoof 2021 data:** requires agreement via the challenge site — same
  pattern as FF++, request early.
