# BASE_PAPER_SELECTION.md — Base-Paper Shortlist & Primary Selection

**Status:** GATE 4 — five candidates evaluated, primary + supporting chosen
**Date:** 2026-10-14
**Companion:** `RESEARCH_REVIEW.md` (paper IDs R1–R35), `GAP_ANALYSIS.md`

## 1. Shortlist (5 candidates)

| # | Paper | Venue | Why shortlisted |
| --- | --- | --- | --- |
| C1 | **UCF** — Yan et al. | ICCV 2023 (IEEE/CVF) | Strongest generalizable-detection method; published 0.828 cross-dataset AUC baseline we must beat; reference impl via DeepfakeBench |
| C2 | **OW-DFA / CPL** — Sun et al. | ICCV 2023 (IEEE/CVF) | The open-world attribution benchmark; the field's best attribution so far; our D3 builds directly on it |
| C3 | **ASVspoof 2021** — Liu et al. | IEEE/ACM TASLP 2023 | The standard audio anti-spoofing protocol; needed for the audio half of multimodal fusion |
| C4 | **Multi-attentional** — Zhao et al. | CVPR 2021 (IEEE/CVF) | Highest-cited modern detector (939c); attention maps feed D4 explainability; strong single-frame baseline |
| C5 | **DIRE** — Wang et al. | ICCV 2023 (IEEE/CVF) | The diffusion-detection method; proves CNN-artifact detectors (CVPR'24) can't cover new generators |

## 2. Evaluation against selection criteria

| Criterion | C1 UCF | C2 OW-DFA | C3 ASVspoof | C4 Multi-attn | C5 DIRE |
| --- | --- | --- | --- | --- | --- |
| Reproducible method? | ✅ DeepfakeBench impl | ⚠️ paper + OW-DFA bench | ✅ public protocol | ⚠️ heavier impl | ⚠️ diffusion pipeline |
| Clear improvement target? | ✅ 0.828 cross-set AUC | ✅ face-only, no abstain | ✅ audio-only (fusion is our delta) | ✅ frame-level only | ✅ per-generator bound |
| Dataset availability | ⚠️ FF++ gated (form) | ✅ OW-DFA public | ⚠️ ASVspoof agreement | ⚠️ FF++ gated | ✅ gen sets public |
| Compute (no GPU) | ✅ CPU inference OK | ⚠️ needs training | ✅ light | ⚠️ heavy | ⚠️ diffusion decode |
| Gap the project fills | L1 generalization | L3 attribution | L4 audio isolation | L2 artifact-bound | L2 diffusion blind spot |
| Relationship to others | Core visual | Attribution module | Audio channel | Alt detection | Extension target |
| Reproduction difficulty | Medium | Medium–high | Low–medium | High | High |
| Risk | dataset gate | open-set eval | data agreement | compute | compute |

## 3. Primary base paper — **UCF (C1)**

**Justification:** DeepWatch's core task is detection; UCF is the strongest,
best-documented generalizable detector and the only one with a *published
cross-dataset baseline we can honestly measure against*. Its documented
weakness (cross-set drop, label cost, no explanation) is exactly gap L1 → D1.
DeepfakeBench already implements it, so Phase 1 can reproduce its eval without
reinventing training. It does not cover the whole platform — no single paper
does — but it anchors the hardest, best-measured part.

## 4. Supporting base papers (module-anchoring)

- **C2 OW-DFA/CPL** → attribution module (D3): we add an explicit open-set
  abstention as the honest delta.
- **C3 ASVspoof 2021** → audio channel (D2): protocol + baselines for speech
  anti-spoofing; fusion with the visual score is our contribution.
- **C4 Multi-attentional** → explainability source (D4): its attention maps
  seed the region-level evidence layer.
- **C5 DIRE** → diffusion-aware extension (part of D1/D2): the target when we
  test generalization beyond CNN generators.

## 5. What we reproduce vs what we add (honest boundary)

- **Reproduce:** UCF-style detection eval on the benchmark splits (C1), the
  ASVspoof audio baseline (C3), the OW-DFA attribution protocol (C2).
- **Add (our contributions):** the audio–video fusion with a fused verdict,
  calibrated confidence + explicit abstention, region-level explainable
  evidence, integrity-preserving forensic reports, and a reproducible eval
  suite — integration + integrity + honest evaluation, not a new detection
  algorithm claimed as novel.

> No claim that combining these papers is automatically novel — the novelty
> assessment lives in INNOVATION_BLUEPRINT.md, and every delta is tied to a
> documented gap in GAP_ANALYSIS.md.
