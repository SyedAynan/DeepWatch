# IMPLEMENTATIONPLAN.md — Implementation Plan (DeepWatch)

**Status:** Phases 1–4 planned; execution starts on user go-ahead
**Created:** 2026-10-07
**Updated:** 2026-10-14
**Role:** detailed task breakdown. `PHASES.md` holds roadmap/status;
`TRACKER.md` holds live per-task progress.

## Phase 1 — Scaffold + baseline detector

**Objective:** reproducible env + visual detection baseline on FaceForensics++.
**Depends on:** — (engineering-only)

| # | Task | Files (expected) | Acceptance / verification |
| --- | --- | --- | --- |
| 1.1 | uv project init: pyproject, deps (torch, timm, opencv, fastapi, pytest) | `pyproject.toml`, `uv.lock` | `uv sync` clean; `uv run pytest` runs |
| 1.2 | Project skeleton per ARCHITECTURE §5 | `src/deepwatch/*` packages | imports resolve; placeholder tests pass |
| 1.3 | Dataset bootstrap: FF++ download instructions + manifest loader | `data/datasets/`, `ingest/datasets.py` | loader enumerates real/fake samples |
| 1.4 | Ingest + hashing: preserve original, SHA-256, metadata log | `ingest/hasher.py`, `ingest/preserve.py` | uploaded file copied + hash logged |
| 1.5 | Baseline detector: Xception backbone, face-crop preprocessing | `detect/model.py`, `detect/pipeline.py` | single image → score via CLI |
| 1.6 | Eval harness: AUC on FF++ split | `eval/benchmark.py` | prints numeric AUC on the split |

## Phase 2 — Fusion + attribution

**Objective:** audio + sync + attribution + fused verdict.
**Depends on:** Phase 1

| # | Task | Files (expected) | Acceptance / verification |
| --- | --- | --- | --- |
| 2.1 | Audio channel: extract + anti-spoofing model (ASVspoof protocol) | `audio/` | audio file → spoof score |
| 2.2 | Lip–speech consistency check | `sync/` | video → sync score |
| 2.3 | Open-set attribution (CPL-style) + "unseen" abstention | `attribute/` | input → method label or abstain |
| 2.4 | Score fusion + calibrated confidence | `fuse/` | video → one fused verdict + confidence |

## Phase 3 — Explainability + forensic report + UI

**Objective:** heatmaps, reasons, PDF, log, web UI.
**Depends on:** Phase 2

| # | Task | Files (expected) | Acceptance / verification |
| --- | --- | --- | --- |
| 3.1 | Grad-CAM/saliency heatmaps per region | `explain/` | heatmap image generated per run |
| 3.2 | Plain-language reason strings | `explain/` | reasons rendered alongside scores |
| 3.3 | Forensic PDF generator (+ optional hash anchor) | `report/` | PDF downloads with scores+hashes |
| 3.4 | Append-only analysis log (SQLite) | `analysis_log.db` | every run queryable by hash |
| 3.5 | Minimal web UI: upload → results | `web/`, `api/` | end-to-end via browser |

## Phase 4 — Evaluation + polish

**Objective:** honest benchmarking + demo readiness.
**Depends on:** Phase 3

| # | Task | Files (expected) | Acceptance / verification |
| --- | --- | --- | --- |
| 4.1 | Benchmark vs baselines (UCF numbers), FP/FN separated | `eval/results.md` | comparison table exists |
| 4.2 | Compression-robustness eval | `eval/` | metrics on compressed media |
| 4.3 | Demo script + README refresh | `README.md`, demo notes | rehearsed < 1 min/media demo |
| 4.4 | Reproducibility check: fresh `uv sync` → eval runs | docs + lockfile | clean-env reproduction notes |

> Every task needs a verifiable acceptance step; a task without one is not ready
> to be worked.
