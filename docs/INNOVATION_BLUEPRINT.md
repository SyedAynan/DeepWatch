# INNOVATION_BLUEPRINT.md — Proposed Contributions & Validation Plan

**Status:** GATE 4 — prioritized portfolio (P0–P3)
**Date:** 2026-10-14
**Companion:** `GAP_ANALYSIS.md` (G1–G10), `RESEARCH_REVIEW.md` (R1–R35)

Each innovation: supporting papers, exact change, hypothesis, datasets/compute,
complexity, evaluation, risks, novelty tier (engineering / experimental /
potentially-publishable), acceptance criteria. Nothing here is presented as a
finished result — all are testable hypotheses.

## Innovation E — Multimodal Audio–Video Cross-Verification  [PRIMARY — P1]

- **Supports:** ASVspoof (R10), AuViRe (R28), BabelFake (R26), multimodal
  neurosymbolic XAI (R20).
- **Gap:** G2 — audio and video detection never meet in a usable system.
- **Exact change:** run the visual detector (D1) + speech anti-spoofing (D2a)
  + a lip–speech consistency check (D2b); fuse the three into one calibrated
  verdict; degrade gracefully when a channel is absent or corrupt.
- **Hypothesis:** fused AUC > max(audio-only, video-only) AUC on bimodal media,
  including one-degraded-channel cases.
- **Datasets:** a bimodal deepfake set (BabelFake / AV-Deepfake1M / DFDC video
  with audio); ASVspoof for the audio model.
- **Compute:** MEDIUM — pretrained components, fusion head only.
- **Evaluation:** fused vs unimodal AUC/EER; missing-modality ablation;
  confidence intervals.
- **Risks:** bimodal test data is young; lip-sync needs a reliable aligner.
- **Novelty tier:** experimental (fusion + missing-modality robustness is a
  real, current gap — AuViRe 2026 shows the field is only now arriving).
- **Acceptance:** fused score beats both unimodal baselines on the same split;
  abstains correctly when a channel is missing.

## Innovation D — Calibrated Confidence + Explicit Abstention  [SUPPORTING — P1]

- **Supports:** thin dedicated literature = the gap (GAP_ANALYSIS G6).
- **Exact change:** temperature-scale scores; add an "inconclusive / needs
  human review" verdict band instead of forcing binary output.
- **Hypothesis:** selective prediction (abstain on low-confidence) yields
  higher precision on answered cases than forced classification.
- **Datasets:** the same eval sets as D1/E.
- **Compute:** LOW.
- **Evaluation:** ECE + Brier before/after calibration; precision vs coverage
  curve; false-accusation rate at fixed recall.
- **Risks:** abstention can look like "worse accuracy" if reported naively —
  must report coverage alongside.
- **Novelty tier:** engineering→experimental (few forensic systems abstain).
- **Acceptance:** ECE improves after calibration; abstention lifts precision at
  a documented coverage cost.

## Innovation B — Evidence-Grounded Explainability  [SUPPORTING — P1]

- **Supports:** SupCon+XAI (R18), image-matching XAI (R19), multi-attentional
  attention maps (R4/C4).
- **Gap:** G4 — explanations are unvalidated.
- **Exact change:** Grad-CAM/saliency heatmaps + region callouts +
  plain-language reasons; verify maps against manipulation ground truth where
  datasets provide it.
- **Hypothesis:** explanations that localize true manipulated regions
  (measurable IoU) are more faithful than generic saliency.
- **Datasets:** sets with manipulation masks (FF++ masks, OW-DFA regions).
- **Compute:** MEDIUM.
- **Evaluation:** IoU between heatmap and ground-truth manipulated region;
  human-readable reason coverage.
- **Risks:** few datasets have region ground truth — may need proxy evaluation.
- **Novelty tier:** experimental (faithfulness-measured, not just shown).
- **Acceptance:** measured localization quality reported honestly, even if low.

## Innovation G — Forensic Evidence Ledger + Reporting  [DIFFERENTIATOR — P1]

- **Supports:** provenance surveys (R30–R32), EKILA (R21); absence in
  detection papers = the gap (G8).
- **Exact change:** SHA-256 hashing at ingest, immutable original, append-only
  analysis log, PDF report with scores+hashes+metadata, optional test-chain
  hash anchor.
- **Hypothesis:** an integrity-protected, human-readable report is the missing
  link between a detection score and usable evidence.
- **Datasets:** n/a (platform feature).
- **Compute:** LOW.
- **Evaluation:** end-to-end run → hash-verified report + reproducible log
  replay; honest statement that anchoring proves integrity, not truth.
- **Risks:** over-claiming "blockchain proves it" — we explicitly qualify.
- **Novelty tier:** engineering (deployable forensic layer absent in research).
- **Acceptance:** tamper-evident report + replayable audit trail works.

## Innovation C — Robustness & Generalization Evaluation Suite  [P0 foundation]

- **Supports:** DFDC (R24), Celeb-DF++ (R25), DeepfakeBench (R29), adversarial
  eval (R12), compression tiers (FF++ c23/c40).
- **Exact change:** standardized eval harness — in-set vs cross-dataset vs
  compression-level vs held-out-generator, with identity-aware splitting.
- **Hypothesis:** honest multi-axis evaluation reveals the true generalization
  boundary of each component (measured, not assumed).
- **Compute:** MEDIUM (inference-heavy, no training required for baselines).
- **Evaluation:** the eval suite itself is the deliverable — AUC/EER/FP/FN per
  axis with confidence intervals.
- **Novelty tier:** experimental (reproducible honest benchmarking).
- **Acceptance:** one command produces the full comparison table.

## Innovation A — Multi-Expert Forensic Engine  [P2 — advanced extension]

- **Supports:** Multi-attentional (R1), WaViT-CDC (R17), frequency methods (R27),
  implicit-identity face-swap (R7).
- **Exact change:** modular experts (spatial / frequency / temporal /
  modality-specific) combined by a calibrated aggregator — only if fusion beats
  the best single expert (no assumed gain).
- **Datasets/compute:** HIGH — needs per-expert training; GPU-scale.
- **Evaluation:** each expert vs ensemble vs simple baseline; honest ablation.
- **Risks:** combining models does not automatically help (literature is mixed).
- **Novelty tier:** experimental — deferred to P2 pending Phase-2 evidence.

## Innovation F — Open-Set Generator Attribution  [P2 — extended]

- **Supports:** OW-DFA/CPL (R14), DNA-Det (R15), "do models generalize" (R16),
  Artificial Fingerprinting (R13 as contrast).
- **Exact change:** CPL-based open-set attribution + explicit abstention,
  extended beyond face-only where data permits; outputs a **ranked hypothesis
  with confidence**, not definitive provenance.
- **Compute:** HIGH (open-set training).
- **Evaluation:** OW-DFA protocol; top-k + abstention precision.
- **Novelty tier:** experimental — the abstention framing is our honest delta.

## Innovation H — Efficient Analysis Pipeline  [P2 — deployment constraint]

- **Supports:** DefakeHop++ (R22), FakeFormer (R23), lightweight fusion (R27).
- **Exact change:** frame sampling, adaptive resolution, batching, caching,
  model-size selection — sized for **no-GPU** operation.
- **Evaluation:** latency/throughput/memory vs AUC on CPU; document the
  accuracy–efficiency trade curve.
- **Novelty tier:** engineering.

## Innovation I — Reproducible Evaluation Infrastructure  [P0 foundation]

- **Exact change:** versioned configs, dataset manifests, model hash registry,
  model cards, error-analysis reports, lockfile env.
- **Evaluation:** fresh-env `uv sync` → eval reproduces identical metrics.
- **Novelty tier:** engineering (required for everything else to count).

## Innovation J — Human-Readable Forensic Reporting  [P0 foundation]

- **Exact change:** structured PDF — findings, evidence, calibrated confidence,
  limitations, model versions, analysis metadata; outputs explicitly labelled
  as model estimates, not verified facts.
- **Evaluation:** report completeness + hash integrity; clarity review.
- **Novelty tier:** engineering (G8).

## Priority decision (GATE 4)

- **Primary research contribution:** **Innovation E** (multimodal AV fusion +
  missing-modality robustness) — biggest evidence-backed gap, feasible.
- **Supporting contributions:** **D** (calibrated abstention), **B**
  (explainable evidence with faithfulness check), **G+J** (integrity ledger +
  forensic report) as the differentiating product layer.
- **Foundations (P0):** **C+I** — the evaluation suite and reproducibility
  infra must exist before any claim is measurable.
- **P2 advanced:** **A** (multi-expert), **F** (open-set attribution), **H**
  (efficiency) — pursued only after P0/P1 validate.
- **P3 future:** diffusion-specific detector retraining, PQ-anchored
  provenance, hardware attestation — recorded, not promised.

> Selection principle: a small set of well-validated improvements over many
> untested features. Every item has a defined success metric before a line of
> code is written.
