# PHASES.md — Development Roadmap (DeepWatch)

**Status:** Phase 0 complete; Phase 1 ready to start
**Updated:** 2026-10-14

| Phase | Objective | Status |
| --- | --- | --- |
| 0 — Definition | Direction, IEEE base papers, gap analysis, PRD, stack | DONE (pending only user IEEE Xplore access check) |
| 1 — Scaffold + baseline | Env, datasets, baseline detection reproducing UCF-style eval | READY TO START |
| 2 — Fusion + attribution | Audio anti-spoofing, lip–speech sync, open-set attribution, score fusion | NOT STARTED |
| 3 — Explain + report + UI | Heatmaps, forensic PDF, analysis log, web UI | NOT STARTED |
| 4 — Evaluation + polish | Benchmark vs baselines, FP/FN report, docs, demo | NOT STARTED |

## Phase 0 — Project definition (DONE)
- Direction: DeepWatch — unified deepfake forensics + attribution platform.
- Base papers: UCF (ICCV 2023), up-sampling artifacts (CVPR 2024), OW-DFA/CPL
  (ICCV 2023), ASVspoof 2021 (IEEE/ACM TASLP).
- Gap → implementation mapping (L1–L4 → D1–D5) in PRD §4 and the report PDF.
- **Outstanding:** user verifies base-paper access on IEEE Xplore via college
  library (formality — venues are confirmed IEEE/CVF).

## Phase 1 — Scaffold + baseline detector
- **Objective:** reproducible environment + a visual detection baseline that
  runs on FaceForensics++ and reports AUC, in the spirit of UCF.
- **Acceptance:** `uv run pytest` passes; `uv run eval --benchmark ff++`
  produces a numeric AUC on the benchmark split; a single image can be
  analysed end-to-end via CLI.
- **Verification:** metric printed on the standard split; commit the log.
- **Status:** READY TO START

## Phase 2 — Fusion + attribution
- **Objective:** speech anti-spoofing channel (ASVspoof protocol), lip–speech
  consistency, open-set attribution module, fused score.
- **Acceptance:** a video file yields visual + audio + sync scores and a fused
  verdict; attribution returns a method label or explicit "unseen" abstention.
- **Status:** NOT STARTED

## Phase 3 — Explainability + forensic report + UI
- **Objective:** heatmaps, plain-language reasons, forensic PDF, append-only
  analysis log, minimal upload/visualise web UI.
- **Acceptance:** end-to-end via UI — upload → scores → heatmap → PDF; every
  run logged with hashes.
- **Status:** NOT STARTED

## Phase 4 — Evaluation + polish
- **Objective:** benchmark vs base-paper numbers, separate FP/FN reporting,
  compression-robustness check, final docs + demo script.
- **Acceptance:** an honest evaluation table exists; demo runs in < 1 min per
  media.
- **Status:** NOT STARTED
