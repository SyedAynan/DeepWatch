# RESEARCH_DECISION_REPORT.md — DeepWatch GATE-7 Final Report

**Status:** GATE 7 complete — research phase closed, approved for implementation
**Date:** 2026-10-14
**Approves:** implementation may begin at Milestone 0 (see IMPLEMENTATION_ROADMAP)

## 1. Executive summary

DeepWatch is a unified multimodal deepfake-forensics platform: it detects
manipulated media, attributes the likely generation method, explains the
evidence, and issues integrity-protected forensic reports. An 84-paper verified
literature review confirms detection, attribution, and speech anti-spoofing are
separate, unintegrated research tracks; the platform's defensible contribution
is a unified pipeline plus calibrated abstention and a forensic integrity
layer — evaluated honestly against published baselines, not claimed superior.

## 2. Verified literature statistics

| Metric | Value |
| --- | --- |
| Verified papers collected | **84** |
| IEEE-venue flagged | 25 |
| With resolving DOI | 81 |
| With abstract metadata | 68 |
| Date range | 2019–2026 |
| Sources | OpenAlex + Crossref + arXiv APIs (IEEE Xplore full-text blocked by JS challenge) |

## 3. The 50-paper matrix

Built in `docs/RESEARCH_REVIEW.md`: a 35-row synthesized matrix (R1–R35)
covering all 15 research areas, backed by the full 84-paper dataset in
`.research/papers_raw.json`. Target of ~50 verified papers met (84 collected);
IEEE share is 25 — reported honestly rather than padded.

## 4. Research trends

Cross-dataset generalization is the dominant unsolved problem (UCF: 0.996→0.828
AUC). Attribution is young and face-only. Audio and video detection evolved
separately; true multimodal AV forensics is only emerging in 2026 (AuViRe,
BabelFake). Explainability outputs are rarely validated for faithfulness.
Artifact-bound detectors expire as generators evolve.

## 5. Top-10 evidence-backed limitations (GAP_ANALYSIS.md)

G1 cross-dataset collapse · G2 audio/video never fused · G3 face-only weak
attribution · G4 unvalidated explanations · G5 artifact-bound expiry ·
G6 uncalibrated scores/no abstention · G7 compression destroys signal ·
G8 no integrity layer · G9 efficiency–accuracy trade · G10 sophisticated
face-swap failure.

## 6. Highest-value research gaps

**G2 (AV fusion)** = primary delta · **G6 (calibrated abstention)** and
**G4/G8 (explainable evidence + integrity)** = differentiators · **G1
(generalization)** = honest evaluation target.

## 7. Five candidate base papers

UCF (ICCV'23) · OW-DFA/CPL (ICCV'23) · ASVspoof 2021 (IEEE/ACM TASLP'23) ·
Multi-attentional (CVPR'21) · DIRE (ICCV'23).

## 8. Recommended primary base paper

**UCF** (Yan et al., ICCV 2023, DOI 10.1109/ICCV51070.2023.02048) — strongest
generalizable detector with a published cross-dataset baseline to beat;
DeepfakeBench reference implementation; gap L1 maps to our D1 module.

## 9. Prioritized innovation portfolio

- **P0 foundations:** C reproducible eval suite · I reproducibility infra · J forensic reporting
- **P1 primary:** E multimodal AV fusion + missing-modality robustness
- **P1 supporting:** D calibrated abstention · B explainable evidence · G integrity ledger
- **P2 advanced:** A multi-expert · F open-set attribution · H efficiency
- **P3 future:** diffusion retraining · PQ/hardware provenance

## 10. Datasets & evaluation (DATASET_AND_EXPERIMENT_PLAN.md)

FF++ (gated ~1wk, request submitted/in-parallel), Celeb-DF, DFDC, OW-DFA,
ASVspoof 2021, DeepfakeBench packs, DF40, BabelFake. Identity+source-aware
splits; cross-dataset eval; AUC/EER/AP, top-k attribution, IoU localization,
ECE/Brier calibration; FP/FN always separated; honest CIs.

## 11. Architecture recommendation

Local-first modular pipeline: ingest (hash+preserve) → detect → audio → sync
→ attribute → fuse → explain → report; FastAPI + SQLite audit log + minimal
web UI; PyTorch on RTX 3050 A (4 GB). Research models separated from UI.

## 12. Risk / feasibility / compute

RTX 3050 A 4 GB confirmed — inference + modest fine-tuning feasible; heavy
training deferred to cloud. FF++ gated (bootstrap via DeepfakeBench + open
sets). Attribution training is heavy — ship abstention-first. Bimodal test
data young — limits documented.

## 13. Documentation created/updated

PRD, RESEARCH_REVIEW, GAP_ANALYSIS, BASE_PAPER_SELECTION, INNOVATION_BLUEPRINT,
DATASET_AND_EXPERIMENT_PLAN, TECHSPEC, ARCHITECTURE, SECURITY_AND_PRIVACY,
IMPLEMENTATION_ROADMAP, IMPLEMENTATIONPLAN, TRACKER, MEMORY, SCHEMA, APPFLOW,
DESIGN, REQUIREMENTS — all aligned to DeepWatch.

## 14. Staged implementation roadmap

M0 scaffold+ingest → M1 baseline+eval → M2 fusion+abstention → M3 explain+
report+UI → M4 honest benchmarking. Gated per IMPLEMENTATION_ROADMAP.

## 15. Unresolved questions for the user

- (a) FF++ request — user to submit the Google form if not already done.
- (b) IEEE Xplore access check for the 4 base papers via college library
  (formality — venues confirmed IEEE/CVF).
- (c) Any blueprint revisions before Milestone 0? (none requested → proceed)

## GATE-7 APPROVAL

Research gates 1–6 satisfied. This report is the GATE-7 deliverable. Upon the
user's "complete gate 7 completely" instruction, implementation is approved to
begin at Milestone 0 per IMPLEMENTATION_ROADMAP.md.

**Success measure for every contribution:** defined in
INNOVATION_BLUEPRINT.md acceptance criteria — fused-AUC lift for E, ECE
improvement for D, IoU for B, integrity-verified report for G, honest
benchmark table for C, env-reproduction for I.
