# MEMORY.md — Project State

**Last updated:** 2026-10-14
**Current phase:** PINNED — Milestone 0 + dataset loader complete; awaiting user
signal to resume DeepWatch build
**Current task:** user pivoted to a different project in a new repo; DeepWatch
is frozen at a clean, resumable checkpoint

## Resume point (pinned 2026-10-14, REVISED 2026-10-17 on resume)
DeepWatch is at a clean checkpoint — pick up exactly here on "resume DeepWatch":
- ✅ GATE 1–7 complete (research blueprint, 84-paper review, decision report)
- ✅ Milestone 0: uv project, package skeleton, ingest (SHA-256 hash +
  immutable preserve + append-only audit log), `deepwatch ingest` CLI
- ✅ Dataset manifest loader (`ingest/datasets.py`) — folder-marker +
  CSV/JSON manifest scan
- ✅ Milestone 1 IN PROGRESS (2026-10-17): `detect/model.py` (Xception loader:
  imagenet bootstrap + DeepfakeBench checkpoint slot), `detect/pipeline.py`
  (face-crop → score, image + frame-sampled video), `eval/benchmark.py`
  (AUC/AP/FP/FN/separated), `deepwatch detect` CLI, `tests/test_detect.py`
  (torch-free stubs) — code written, awaiting env sync to run.
- ✅ ENV RESOLVED (2026-10-17): `.venv` was empty because dev tools were an
  `[project.optional-dependencies]` extra named `dev`, which `uv sync --dev`
  never installs. Moved to `[dependency-groups] dev` — plain `uv sync` now
  installs the toolchain. Also pinned `opencv-python<5` (cv2 5.x removed
  `CascadeClassifier`/Haar cascades and broke face-crop). VERIFIED GREEN:
  14/14 pytest, ruff clean, pyright clean, format clean, coverage 60%.
- **Blocked on:** a first real `detect` score (needs a real media file) and
  FF++ dataset access.
- **External pending:** user submits FF++ Google-form request; IEEE Xplore
  access check for the 4 base papers (formality).

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
- **Env regression (2026-10-17, resume):** `.venv` was EMPTY — only virtualenv
  bootstrap files, no packages. The "8/8 green + CUDA torch" checkpoint state
  did not survive on disk. Root cause of slow `uv run`: re-resolving the full
  tree, not a code problem. Fix: re-run `uv sync`.
- **C: drive is 99% full (~2.3 GB free, 2026-10-17):** CUDA torch wheel (~3 GB)
  fails to extract with `os error 112`. Fix: `UV_CACHE_DIR="S:/uv-cache"` (S:
  has ~150 GB free) + `UV_LOCK_TIMEOUT=600`. Always prefix uv commands with
  these env vars until C: is cleaned up. Consider a per-project `.env`/`.venv`
  note so this isn't rediscovered on the next resume.
- User-side formality (carried over): confirm the 4 base papers are accessible
  via IEEE Xplore through the college library.

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
- **GPU: RTX 3050 A Laptop (4 GB VRAM, driver 610.88) — CONFIRMED present**
  after user enabled it. 4 GB VRAM: inference + modest fine-tuning feasible
  (batch 1–4, fp16); full from-scratch training still better on cloud/Colab.
  Torch not installed yet — installs with `uv sync` in Milestone 0.
  UPDATE (2026-10-14): GPU found, replaces earlier "no GPU" note.
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
