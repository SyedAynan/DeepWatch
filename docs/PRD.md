# PRD.md — DeepWatch: Deepfake Forensics and Attribution Platform

**Status:** APPROVED DRAFT — direction locked 2026-10-14; pending user sign-off
and IEEE Xplore access verification of base papers
**Created:** 2026-10-07
**Updated:** 2026-10-14
**Companion document:** `docs/DeepWatch-Report.pdf` (research proposal)

## 1. Problem statement
Deepfake media — AI-generated faces, voices, and video — is used for fraud and
fabricated evidence. Existing research detectors return opaque scores, are
evaluated on controlled data, degrade on unseen generators and compressed media,
treat audio and video as separate problems, and produce no evidence a victim or
investigator can reuse. There is no accessible tool that detects fakes, explains
the evidence, attributes the likely generation method, and documents the result
in a forensically defensible report.

## 2. Target users
- General public verifying suspicious media/calls (primary)
- Small investigative units and journalists checking viral content
- Platform moderators needing triage evidence

## 3. Goals / non-goals
- Goals:
  - Integrate detection, attribution, explanation, and forensic reporting in one
    platform, on top of published IEEE/CVF base methods
  - Improve robustness on compressed/unseen-generator media vs the base papers'
    published numbers (modest, honestly measured targets)
  - Fuse audio and video analysis for video-call media
  - Preserve evidence integrity (hashing, logs, reproducibility)
- Non-goals:
  - Not a definitive proof tool — outputs are probabilistic indicators, not proof
  - Not real-time call interception (prototype works on uploaded media)
  - Not a general content-moderation or fact-checking platform
  - Not a replacement for professional forensic laboratories

## 4. Core features (mapped to base-paper limitations L1–L4)
1. **D1 — Detection module:** common-forgery-feature detection after UCF [1],
   trained with compression/resolution augmentation; explains scores via
   artifact localisation. (Answers L1: cross-dataset degradation, label cost,
   no explanation.)
2. **D2 — Audio–video fusion:** visual score + speech anti-spoofing score
   (ASVspoof protocol [4]) + lip–speech consistency → one fused assessment.
   (Answers L2, L4.)
3. **D3 — Open-set attribution:** estimates the likely generation method after
   OW-DFA/CPL [3], with explicit "unseen method" abstention. (Answers L3.)
4. **D4 — Explainable evidence:** region-level heatmaps + plain-language
   reasons, presented as indicators, not proof.
5. **D5 — Forensic reporting:** structured PDF report bundling scores,
   heatmaps, SHA-256 hashes, and analysis metadata; optional hash anchoring on
   a test blockchain.

## 5. Functional requirements
- FR-01: The system SHALL accept image/video/audio uploads and preserve the
  original file unmodified, logging its SHA-256 hash.
- FR-02: The system SHALL output a manipulation-probability score for each
  channel (visual, audio) and a fused score for bimodal media.
- FR-03: The system SHALL output a generation-method attribution or an explicit
  "unseen method" abstention.
- FR-04: The system SHALL render region-level explanation heatmaps for visual
  media.
- FR-05: The system SHALL generate a downloadable forensic PDF containing all
  outputs, hashes, and analysis metadata.
- FR-06: The system SHALL record every analysis step, model version, and
  parameter in an append-only analysis log.

## 6. Non-functional requirements
- NFR-01: Detection AUC on unseen-dataset evaluation SHOULD meet or exceed the
  UCF baseline (0.828 mean cross-dataset AUC) on the same benchmarks; any
  improvement claim MUST be honestly measured.
- NFR-02: The system SHOULD remain functional on social-media-compressed media;
  robustness MUST be evaluated, not assumed.
- NFR-03: A single-media analysis SHOULD complete in under one minute on
  student-grade hardware (GPU optional, CPU fallback required).
- NFR-04: User uploads SHALL NOT be sent to third parties; all processing is local.
- NFR-05: False-positive and false-negative rates SHALL be reported separately
  in evaluation — never collapsed into a single accuracy figure.
- NFR-06: All code, configs, model hashes, and evaluation scripts SHALL be
  reproducible and documented.

## 7. Success criteria
- Baseline detector reproduces (within reasonable margin) the UCF in-dataset
  result on FaceForensics++.
- Fused audio–video score evaluated on bimodal test media; fusion contribution
  shown via ablation.
- Open-set attribution evaluated on the OW-DFA protocol.
- Working demo: upload a known deepfake → score, heatmap, attribution, and
  forensic PDF produced end-to-end.

## 8. Constraints
- Student mini-project scope, timeline, and hardware.
- Public datasets only: FaceForensics++, Celeb-DF, DFDC (detection); OW-DFA
  (attribution); ASVspoof 2021 (audio). Diffusion-era evaluation sets are less
  standardized — treated as a documented limitation.
- All processing local; test blockchain only (no real-money cost).
- Must not claim definitive proof of manipulation — outputs are indicators.

## 9. Novelty statement
The four IEEE/CVF base papers [1]–[4] validate detection, attribution, and
speech anti-spoofing as separate tasks but leave documented gaps: cross-dataset
degradation, CNN-artifact dependence, face-only attribution, and unimodal audio
evaluation. DeepWatch integrates these capabilities and adds explainable
evidence plus integrity-preserving forensic reporting — a combination not
present in the reviewed literature (scoped claim, not exhaustive).

## 10. Base papers
- [1] Yan et al., "UCF: Uncovering Common Features for Generalizable Deepfake
  Detection," ICCV 2023. DOI: 10.1109/ICCV51070.2023.02048. arXiv:2304.13949
- [2] Tan et al., "Rethinking the Up-Sampling Operations in CNN-Based
  Generative Network for Generalizable Deepfake Detection," CVPR 2024.
  DOI: 10.1109/CVPR52733.2024.02657
- [3] Sun et al., "Contrastive Pseudo Learning for Open-World DeepFake
  Attribution," ICCV 2023. arXiv:2309.11132
- [4] Liu et al., "ASVspoof 2021: Towards Spoofed and Deepfake Speech
  Detection in the Wild," IEEE/ACM TASLP 2023. DOI: 10.1109/TASLP.2023.3285283.
  arXiv:2210.02437

> Rule: never invent requirements. Anything unknown stays TODO.
