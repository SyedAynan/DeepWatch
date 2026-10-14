# GAP_ANALYSIS.md — Cross-Paper Disadvantage Analysis (DeepWatch)

**Status:** GATE 3 — evidence-backed gaps distilled from the 84-paper review
**Date:** 2026-10-14
**Companion:** `RESEARCH_REVIEW.md` (paper IDs R1–R35 refer to that matrix)

Each gap lists supporting papers, the technical cause, real-world consequence,
whether newer work resolved it, fix difficulty, and a validation experiment.
Confidence labels: **HIGH** (multiple papers + quantified), **MEDIUM**
(supported but thinner evidence), **INFERENCE** (our reading, needs our own
experiment to confirm).

## G1 — Cross-dataset / unseen-generator generalization collapse

- **Evidence:** UCF (R2) reports 0.996 in-set → **0.828 mean cross-dataset AUC**;
  audio analog: "Does Audio DF Generalize?" (R11) shows poor cross-corpus EER;
  DeepfakeBench tables (R29) show nearly every detector loses 10–20 AUC points
  cross-dataset.
- **Cause:** models overfit dataset-specific artifacts and identity features
  rather than forgery invariants; benchmark training sets share a narrow
  distribution.
- **Consequence:** a detector that scores ~99% in the lab may be near-chance on
  a real social-media fake — the single biggest deployment risk.
- **Resolved?** No — 2024–2026 papers still report the gap; it is THE open
  problem. Confidence: **HIGH**.
- **Fix difficulty:** HARD (research-level, not an afternoon).
- **Validation experiment:** train on FF++ only, evaluate untouched on
  Celeb-DF/DFDC — publish both numbers; any improvement must beat UCF's 0.828
  on *the same splits*.

## G2 — Audio and video detection never meet (unimodal evaluation)

- **Evidence:** ASVspoof 2021 (R10) is audio-only; UCF (R2), Multi-attentional
  (R1) are visual-only; true AV benchmarks (BabelFake R26, AuViRe R28) only
  appeared in 2026.
- **Cause:** the communities and datasets grew separately; no shared eval.
- **Consequence:** a real fake video call has *both* a fake face and a fake
  voice — checking one channel misses half the evidence and lets a
  real-looking video with cloned audio pass.
- **Resolved?** Partly emerging (AuViRe, BabelFake) but not a usable platform.
  Confidence: **HIGH**.
- **Fix difficulty:** MEDIUM (engineering + eval design, not new theory).
- **Validation experiment:** fused score vs unimodal baselines on a bimodal
  test set, including one-degraded-modality cases; report fused AUC lift.

## G3 — Generation-method attribution is immature and face-only

- **Evidence:** OW-DFA/CPL (R14) is the SOTA and is face-only; "Do attribution
  models generalize?" (R16) shows poor transfer; Artificial Fingerprinting
  (R13) needs generator-owner cooperation (unrealistic for adversaries).
- **Cause:** attribution signatures are subtle, method-specific, and the open
  world contains unknown generators.
- **Consequence:** forensic value of "which tool made it" is low today; courts
  can't rely on it.
- **Resolved?** No — actively open. Confidence: **HIGH**.
- **Fix difficulty:** HARD.
- **Validation experiment:** open-set eval on OW-DFA protocol; report top-k
  accuracy + explicit abstention precision (we add abstention as the delta).

## G4 — Explainability outputs are unvalidated (pretty ≠ faithful)

- **Evidence:** XAI detectors (R18–R20) emit heatmaps but rarely verify the
  maps cover the actual manipulated region; the field lacks a faithfulness
  metric standard.
- **Cause:** saliency methods explain *what the model looked at*, which may not
  be the manipulation itself.
- **Consequence:** an investigator could be shown a confident-looking but
  meaningless map — worse than no explanation.
- **Resolved?** Largely open. Confidence: **MEDIUM**.
- **Fix difficulty:** MEDIUM.
- **Validation experiment:** mask-region ground truth where datasets provide
  it → IoU between heatmap and true manipulated region; report it.

## G5 — Artifact-bound detectors expire as generators evolve

- **Evidence:** up-sampling-artifact detection (R4/CVPR'24) keys on
  CNN-generator fingerprints; DIRE (R5) shows diffusion generators need a
  different signal entirely.
- **Cause:** methods latch onto a generation artifact that new architectures
  don't share.
- **Consequence:** a detector can be SOTA today and useless next year — an
  arms race.
- **Resolved?** No — each new generator family resets the problem. Confidence:
  **HIGH**.
- **Fix difficulty:** HARD (perpetual).
- **Validation experiment:** evaluate the pipeline on a generator class held
  out from all training sources (e.g., a diffusion set for a CNN-trained
  detector) — report the drop honestly.

## G6 — Uncalibrated / overconfident scores; no abstention path

- **Evidence:** detectors output real/fake probabilities; few report
  calibration (ECE/Brier) or an "inconclusive" option; OW-DFA abstention is
  the exception, not the rule.
- **Cause:** softmax confidence ≠ probability of correctness; benchmarks score
  accuracy, not calibrated risk.
- **Consequence:** a system says "fake 97%" when it's actually right only ~60%
  on that class — dangerous for accusations.
- **Resolved?** Under-addressed — few dedicated papers (the L query returned
  thin results; itself evidence of a gap). Confidence: **MEDIUM→INFERENCE**.
- **Fix difficulty:** MEDIUM.
- **Validation experiment:** temperature scaling + ECE before/after; measure
  selective-prediction AUC when abstaining on low-confidence inputs.

## G7 — Compression / post-processing destroys detection signal

- **Evidence:** DFDC (R24) and DeepfakeBench show detection degrades under
  h264 compression, resizing, re-encoding — exactly what social media does.
- **Cause:** low-level forgery artifacts are erased by compression.
- **Consequence:** lab-accurate detectors fail on the media people actually
  share.
- **Resolved?** Improved but not solved. Confidence: **HIGH**.
- **Fix difficulty:** MEDIUM.
- **Validation experiment:** evaluate on c23 and c40 FF++ tiers + re-encoded
  copies; compression-augmented training vs baseline.

## G8 — No evidence-integrity / chain-of-custody layer

- **Evidence:** none of the detection papers (R1–R20) handle input hashing,
  provenance logs, or human-readable forensic reports; provenance work
  (R21, R30–R32) exists but is separate from detection.
- **Cause:** research optimizes accuracy, not deployable forensics.
- **Consequence:** a detection score can't be presented as defensible
  evidence — the missing link between research and real use.
- **Resolved?** No integrated system in the reviewed set. Confidence: **HIGH**
  (absence of work is the evidence).
- **Fix difficulty:** LOW–MEDIUM (engineering, not research).
- **Validation experiment:** end-to-end run → hash-verified report +
  reproducible log replay.

## G9 — Efficiency vs accuracy trade unresolved for deployment

- **Evidence:** lightweight detectors (R22 DefakeHop++, R23 FakeFormer) cut
  cost but drop several AUC points vs heavy models; R1 is accurate but heavy.
- **Cause:** compression/pruning removes subtle-feature capacity.
- **Consequence:** can't run strong detection on ordinary hardware in
  real-time — relevant since our target machine has **no GPU**.
- **Resolved?** No. Confidence: **MEDIUM**.
- **Fix difficulty:** MEDIUM.
- **Validation experiment:** latency + AUC on CPU across model sizes; pick the
  knee of the curve, document the trade.

## G10 — Face-swap-specific failure on sophisticated swaps

- **Evidence:** Implicit-Identity (R7) exists *because* generic detectors miss
  identity-preserving swaps; FSGAN-class generators (R8) create fakes that
  defeat earlier detectors.
- **Cause:** high-quality swaps preserve identity/global structure, defeating
  artifact-only cues.
- **Consequence:** the most convincing fakes are the least detected.
- **Resolved?** Improving but not closed. Confidence: **MEDIUM**.
- **Fix difficulty:** MEDIUM–HARD.
- **Validation experiment:** evaluate on FaceShifter/megapixel-swap subsets
  vs generic fakes.

## Priority ordering for DeepWatch

| Gap | Value | Feasibility | Role |
| --- | --- | --- | --- |
| G2 AV fusion | Very high | MEDIUM | **Primary research delta (Innovation E)** |
| G6 calibrated abstention | High | MEDIUM | Supporting (Innovation D) |
| G1 generalization | Very high | HARD | Supporting/eval (Innovation C) — improve honestly, don't promise |
| G8 integrity ledger | High (practical) | LOW–MED | Differentiator (Innovation G/D5) |
| G4 explainable evidence | High | MEDIUM | Differentiator (Innovation B/D4) |
| G3 attribution | High | HARD | Extended (Innovation F/D3) — abstention is our honest angle |
| G5 diffusion-aware | High | HARD | Scoped extension (part of D1/D2) |
| G7 compression robustness | High | MEDIUM | Evaluation requirement (Innovation C) |
| G9 efficiency | Medium | MEDIUM | Deployment constraint (Innovation H) |
| G10 face-swap | Medium | MEDIUM–HARD | Folded into detection experts (Innovation A) |

> Every gap is tied to papers; none is assumed from a single source. G6 is the
> only INFERENCE-flagged gap and is included because the *absence* of
> calibration work in the L-query is itself a documented gap.
