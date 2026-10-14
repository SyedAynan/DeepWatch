# DATASET_AND_EXPERIMENT_PLAN.md — Datasets, Splits, Metrics, Reproducibility

**Status:** GATE 5 — evaluation plan defined
**Date:** 2026-10-14
**Companion:** `BASE_PAPER_SELECTION.md`, `GAP_ANALYSIS.md`

## 1. Datasets (verified availability + access path)

| Dataset | Modality | Access | Size (smallest tier) | Role | Known limitation |
| --- | --- | --- | --- | --- | --- |
| FaceForensics++ | video/image | **Gated** — Google form → emailed script (~1 wk) | c40 ≈2 GB, c23 ≈10 GB | Detection training + in-set eval | staged actors; gated access |
| Celeb-DF / Celeb-DF++ | video | public research links | v2 ~tens of GB | Cross-dataset eval (hard) | celebrity-only domain |
| DFDC (+preview) | video | public (FAIR) | preview ~4 GB, full large | Cross-dataset + augmentation eval | staged actors |
| OW-DFA | image | public research | ~GB-scale | Open-set attribution eval | face-only |
| ASVspoof 2021 LA/DF | audio | agreement via challenge site | ~GB-scale | Audio channel training + eval | audio-only; channel mismatch risk |
| DeepfakeBench preprocessed | image/video | public Drive/Baidu links | packaged | Phase-1 baseline bootstrap | preprocessing fixed by authors |
| DF40 | image | companion repo (public) | packaged | Newer-generator eval | recent |
| BabelFake | audio+video | arXiv 2026 (new) | TBD | Multimodal eval (Innovation E) | new; maturity to verify |
| AV-Deepfake1M | audio+video | public research | large | Alternative AV eval set | large download |

> **Practical plan:** submit the FF++ request immediately (gated ~1 week).
> Bootstrap Phase 1 on DeepfakeBench's preprocessed packs + DFDC-preview +
> Celeb-DF (open) — no blocked-on-FF++.

## 2. Split & leakage strategy

- **Identity-aware split:** no person appears in both train and test (the
  FF++ official 720/140/140 split already respects this — we keep it).
- **Source/generator-aware split:** hold out at least one generator family for
  open-set/generalization eval (DIRE/DF40 as held-out generator).
- **Cross-dataset eval:** train on FF++, test untouched on Celeb-DF + DFDC —
  the honest generalization number (UCF's 0.828 is the bar).
- **Compression axis:** evaluate on c23 AND c40 tiers + re-encoded copies.

## 3. Metrics (per task, with baselines)

| Task | Metrics | Baseline to beat/compare |
| --- | --- | --- |
| Detection (D1) | AUC, EER, ACC, AP | UCF 0.828 cross-set / 0.996 in-set; Xception 0.702 |
| Audio anti-spoof (D2a) | EER, min-tDCF | ASVspoof 2021 baselines (RawNet2 ~1–5% in-set) |
| Fusion (E) | fused AUC vs unimodal AUC/EER | max(audio-only, video-only) on same split |
| Attribution (D3) | top-k acc, open-set rejection | OW-DFA/CPL protocol |
| Localization (D4) | IoU heatmap↔manipulated region | where masks exist; else proxy eval |
| Calibration (D) | ECE, Brier, precision-vs-coverage | uncalibrated baseline |
| Efficiency (H) | latency, throughput, VRAM/RAM | report the AUC-vs-cost curve |

## 4. Reporting rules (honesty)

- FP and FN **always reported separately** — different real-world costs.
- Every number accompanied by dataset, split, and confidence interval.
- Compression-degraded results shown next to clean results — never only clean.
- No target accuracy promised pre-test; improvements reported, not asserted.

## 5. Ablations & failure analysis

- Fusion ablation: visual-only vs audio-only vs sync-only vs fused.
- Channel-degradation ablation: mute audio / drop frames → graceful behavior?
- Compression ablation: clean vs c23 vs c40.
- Failure-case log: every confident error recorded in `eval/results.md` with
  the probable cause — not hidden.

## 6. Reproducibility requirements

- `uv.lock` pinned env; `uv sync` reproduces it.
- Model checkpoints hashed + registered; dataset manifests versioned.
- One command (`uv run eval --benchmark <name>`) reproduces any table.
- `eval/results.md` committed — numbers traceable to a run id in the audit log.

## 7. Experiment backlog (first three)

1. Reproduce UCF-baseline eval via DeepfakeBench on DFDC-preview/Celeb-DF —
   confirm our harness matches published cross-set ballpark.
2. Fused vs unimodal AUC on a bimodal test set (Innovation E hypothesis test).
3. Calibration + abstention on the detection channel (Innovation D).

> Nothing here is a result — these are the experiments that produce them.
