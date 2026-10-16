# TRACKER.md — Task Tracker (DeepWatch)

**Status:** Phase 1 tasks defined; awaiting start signal
**Created:** 2026-10-07
**Updated:** 2026-10-14

## Legend
- [ ] not started · [~] in progress · [x] done (add date) · [!] blocked (add note)

## Current task
PINNED (2026-10-14): user pivoted to a different project in a new repo.
DeepWatch frozen at clean checkpoint — Milestone 0 + dataset loader done,
CUDA torch working, 8/8 tests green. Next on resume: Milestone 1 baseline
detector + eval harness.

## Phase 1 — Scaffold + baseline detector
- [x] 1.1 uv project init (pyproject, deps), `uv sync` — 2026-10-14 (CUDA wheel resolving)
- [x] 1.2 Package skeleton per ARCHITECTURE §5 — 2026-10-14
- [x] 1.4 Ingest + SHA-256 hashing + preservation log — 2026-10-14 (tested)
- [ ] 1.3 Dataset bootstrap: DeepfakeBench packs / DFDC manifest loader
- [ ] 1.5 Baseline detector (Xception/UCF via DeepfakeBench) → score via CLI
- [ ] 1.6 Eval harness prints AUC on benchmark split

## Phase 2 — Fusion + attribution
- [ ] 2.1 Audio anti-spoofing channel (ASVspoof protocol)
- [ ] 2.2 Lip–speech consistency score
- [ ] 2.3 Open-set attribution + "unseen" abstention
- [ ] 2.4 Score fusion + calibrated confidence

## Phase 3 — Explainability + report + UI
- [ ] 3.1 Region-level heatmaps
- [ ] 3.2 Plain-language reasons
- [ ] 3.3 Forensic PDF generator (+ optional hash anchor)
- [ ] 3.4 Append-only analysis log (SQLite)
- [ ] 3.5 Minimal web UI end-to-end

## Phase 4 — Evaluation + polish
- [ ] 4.1 Benchmark vs baselines, FP/FN separated
- [ ] 4.2 Compression-robustness eval
- [ ] 4.3 Demo script + README refresh
- [ ] 4.4 Reproducibility check (fresh env)

## Blockers / notes
- None technical. User-side: verify base-paper access on IEEE Xplore via
  college library (formality; venues confirmed IEEE/CVF).

> Keep entries one line; explanations and outcomes belong in `MEMORY.md`.
