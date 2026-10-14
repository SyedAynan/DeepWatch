# IMPLEMENTATION_ROADMAP.md — Staged Build Plan (DeepWatch)

**Status:** Research gates 1–6 satisfied; awaiting GATE-7 approval to build
**Date:** 2026-10-14
**Companion:** `INNOVATION_BLUEPRINT.md` (P0–P3), `IMPLEMENTATIONPLAN.md` (tasks)

> Execution order follows the innovation priority, not the module list.
> P0 foundations land first because every later claim depends on them.

## Milestone 0 — Environment & scaffolding (Phase 1.1–1.4)
- uv project, pyproject, deps, package skeleton per ARCHITECTURE §5.
- ingest: SHA-256 hashing, immutable preservation, analysis-log schema.
- Dataset bootstrap: DeepfakeBench preprocessed packs + DFDC-preview +
  Celeb-DF; FF++ request submitted in parallel (gated ~1 wk).
- **Deliverable:** `uv run pytest` green; upload→hash→preserve→log works.
- **Exit:** evidence item + analysis log round-trip on a sample file.

## Milestone 1 — Baseline detector + eval harness (Phase 1.5–1.6)
- DeepfakeBench UCF/Xception config + pretrained weights, CPU inference.
- Eval harness: AUC/EER on the benchmark split, FP/FN separated.
- **Deliverable:** `uv run eval --benchmark <set>` prints honest metrics.
- **Acceptance:** numbers in the published ballpark (harness sanity-checked).
- **Gate:** proves the eval path before any "improvement" is claimed.

## Milestone 2 — Multimodal fusion + abstention (Phase 2; Innovation E+D)
- Audio anti-spoofing channel (ASVspoof/RawNet2), lip–speech consistency.
- Score fusion + temperature-scaled confidence + "inconclusive" band.
- **Deliverable:** video → visual+audio+sync scores → fused calibrated verdict.
- **Acceptance:** fused ≥ unimodal baselines on a bimodal test set; abstains
  on missing channel; ECE measured.
- **This is the primary research delta — evaluated, not asserted.**

## Milestone 3 — Explainability + forensic report + UI (Phase 3; B+G+J)
- Grad-CAM/saliency heatmaps + region callouts + plain-language reasons.
- Forensic PDF generator; append-only log; optional test-chain hash anchor.
- Minimal web UI: upload → status → verdict → evidence → report → history.
- **Deliverable:** end-to-end browser demo on a sample deepfake.
- **Acceptance:** report contains scores + hashes + model versions; log replays.

## Milestone 4 — Honest benchmarking + polish (Phase 4; C+I)
- Full eval suite: in-set vs cross-dataset vs compression vs held-out-generator.
- FP/FN separated; CIs; failure-case log; reproducibility check (fresh `uv sync`).
- **Deliverable:** `eval/results.md` comparison table + rehearsed demo.
- **Acceptance:** every claim in the report is backed by a logged run.

## Risk register
| Risk | Impact | Mitigation |
| --- | --- | --- |
| No local GPU | Phase 2 training constrained | CPU inference for baselines; Colab/edge GPU for any training; keep training optional |
| FF++ gated ~1 wk | in-set eval delayed | bootstrap on DeepfakeBench packs + DFDC/Celeb-DF (open) |
| Bimodal test data immature | Innovation E eval weaker | use AV-Deepfake1M / DFDC-with-audio; document dataset limits |
| Attribution training heavy | D3 slips | ship abstention-first version; extend if compute allows |
| Time | scope creep | P0+P1 only; P2 (multi-expert, open-set training, efficiency) explicitly deferred |

## What is NOT in this roadmap (deferred, P2/P3)
Multi-expert ensembles, open-set attribution *training* (vs abstention-first),
efficiency-optimized variants, diffusion-specific retraining, PQ/hardware
provenance anchoring — recorded in INNOVATION_BLUEPRINT.md, not promised here.

## Go/no-go
**GATE 7:** this research blueprint + roadmap awaits your approval before any
application code is written. On approval, Milestone 0 starts.
