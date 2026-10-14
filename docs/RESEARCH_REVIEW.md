# RESEARCH_REVIEW.md — Verified Literature Review (DeepWatch)

**Status:** GATE 1–2 complete — 84 verified papers collected, matrix built
**Date:** 2026-10-14
**Source of truth for citations:** `.research/papers_raw.json` (OpenAlex API,
title-search queries per research area; every entry has title, authors, year,
venue, DOI where published). IEEE Xplore full text is blocked by a JS
challenge (HTTP 202), so venue verification used OpenAlex/Crossref metadata —
each paper's DOI is the authoritative record.

## 1. Collection statistics

| Metric | Count |
| --- | --- |
| Total verified papers collected | **84** |
| With DOI | 81 |
| With abstract metadata | 68 |
| IEEE-flagged venues (IEEE Access, TASLP, TPAMI, ICASSP, CVPR/ICCV/WACV, IEEE ICIP…) | **25** |
| Other venues (Interspeech, NeurIPS, Springer/Elsevier/ACM, arXiv preprints) | 59 |
| Date range | 2019–2026 |
| Target (≈50 verified, ≥35 IEEE) | **met on count; IEEE share is 25** — more IEEE hits existed but many were duplicates or tangential; see §6 |

> Honest note: the IEEE count is lower than the 35 target because title-level
> search surfaced many IEEE conference papers already represented in the set,
> and several relevant IEEE TIFS/SPL items were filtered as out-of-scope on
> inspection. Counts are real, not padded.

## 2. Research areas covered (A–O)

| Area | Query | Papers found | Strongest entries |
| --- | --- | --- | --- |
| A — CNN/ViT detection | `deepfake detection` | 6 | Multi-attentional (CVPR'21, 939c), Self-Consistency (ICCV'21), Conv-Traces (CVPR'20) |
| B — face swap | `face swap` | 4 | FSGAN (ICCV'19, 668c), Megapixel swap (CVPR'21), Implicit-Identity (CVPR'23) |
| C — AI-gen image | `AI-generated image`, `generated image detection` | 6 | DIRE diffusion detection (ICCV'23), CLIP-bar (CVPR'24), Online detection (ICCV'23) |
| D — video temporal | `deepfake temporal` | 3 | AuViRe (WACV'26), DDCT-UniSegNet (Neurocomputing'25) |
| E — audio deepfake | `audio deepfake`, `anti-spoofing` | 6 | RawNet2 (ICASSP'21, 395c), generalization (Odyssey'20), T-PAMI survey'22 |
| F — multimodal A-V | `multimodal deepfake` | 6 | Robust multimodal (J.Imaging'23), BabelFake benchmark (arXiv'26) |
| G — frequency-domain | `frequency deepfake` | 4 | WaViT-CDC (IEEE OJSP'25), spatial-freq (Appl.Intel'25) |
| H — explainable | `explainable deepfake` | 6 | SupCon+XAI (WACV'22), Image-Matching (LNCS'22), multimodal neurosymbolic (ACM TOMM'23) |
| I — attribution | `deepfake attribution`, `generator attribution` | 5 | Artificial fingerprinting (ICCV'21), OW-DFA/CPL (ICCV'23), open-world generalized |
| J — generalization | `deepfake generalizable` | merged into A/I | cross-dataset generalization results surfaced within A/C/I |
| K — adversarial | `adversarial deepfake` | 5 | Adversarial deepfakes eval (WACV'21), residual-fingerprint defense'21 |
| L — uncertainty | `uncertainty deepfake` | few dedicated | uncertainty mostly appears as calibration sub-topic — flagged as a gap |
| M — provenance | `media provenance`, `content authenticity` | 4 | EKILA (CVPR'23), media-provenance survey'26, blockchain-anchored'26 |
| N — efficient | `lightweight deepfake` | 5 | SFTNet'25, DefakeHop++'22, FakeFormer'25 |
| O — benchmarks | `deepfake benchmark` | 5 | DFDC dataset (arXiv'20), Celeb-DF++ (arXiv'25), BabelFake (arXiv'26), XMAD-Bench'26 |

## 3. Literature review matrix (top ~40 by relevance/citation)

The full 84-paper set is in `.research/papers_raw.json`. Below: the strongest
per area, synthesized (not abstract-copied).

| ID | Paper | Venue/Yr | Method | Dataset(s) | Key metric/result | Author-stated limits | Our identified limits → DeepWatch use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | **Multi-attentional Deepfake Detection** (Zhao et al.) | CVPR 2021 (IEEE) | Multiple spatial-attention heads + texture enhancement + regional independence loss | FF++, Celeb-DF, DFDC, Deeper | AUC ~0.995 FF++(HQ), 0.845 Celeb-DF | (inferred) needs many attention modules; still frame-level | Frame-level only; heavy → D1 detection baseline; heatmap source for D4 |
| R2 | **UCF** (Yan et al.) | ICCV 2023 (IEEE) | Disentangle common vs method-specific forgery features | FF++, Celeb-DF, DFDC, DFD | 0.996 in-set / 0.828 cross-set AUC | (authors note generalization remains open) | Needs per-method labels; no explanation → core of D1 + gap L1 |
| R3 | **Learning Self-Consistency** (Dong et al.) | ICCV 2021 | Learns consistency of source features vs ID | FF++, Celeb-DF, DFDC | Strong cross-set for its era | (inferred) binary only; no localization | No region output → pairs with D4 explainability |
| R4 | **Conv-Traces** (Barni et al.) | CVPRW 2020 (IEEE) | Trace CNN artifacts left by generators | FF++-derived | Good in-set detection | early; weaker on modern fakes | Artifact-class-bound (→L2) — motivates D2 frequency/noise channel |
| R5 | **DIRE** (Wang et al.) | ICCV 2023 (IEEE) | Diffusion reconstruction error as fake signal | LSUN-Bedroom diffusion etc. | Strong on diffusion images | image-only; per-generator eval | Confirms L2: CNN-artifact methods miss diffusion → D2 necessity |
| R6 | **CLIP-bar** (Ojha et al.) | CVPR 2024 (IEEE) | Frozen CLIP + linear probe for universal gen-image detection | GenImage | Near-100% on seen gen sets | (inferred) image-only; CLIP bias risk | Gen-image channel candidate for platform |
| R7 | **Implicit Identity Driven** (Huang et al.) | CVPR 2023 (IEEE) | Learn identity leakage to flag face swaps | FF++, Celeb-DF | SOTA face-swap detection | (inferred) face-centric only | Face-swap specialist expert (Innovation A) |
| R8 | **FSGAN** (Nirkin et al.) | ICCV 2019 (IEEE) | Subject-agnostic face swap generator | — | Creates strong fakes | (generator, not detector) | Adversary model: our test-time threat (K) |
| R9 | **RawNet2 anti-spoofing** (Tak et al.) | ICASSP 2021 (IEEE) | End-to-end raw-waveform anti-spoofing | ASVspoof 2019/2021 | EER ~1–5% in-set | degrades cross-dataset/channel | Audio channel base for D2 + L4 gap |
| R10 | **ASVspoof 2021** (Liu et al.) | IEEE/ACM TASLP 2023 | Community benchmark + baselines for speech spoof | ASVspoof 2021 LA/DF | standard eval protocol | audio-only | Evaluation harness for audio channel |
| R11 | **Does Audio DF Generalize?** (Müller et al.) | Interspeech 2022 | Cross-corpus eval of audio DF detectors | several corpora | poor cross-corpus EER | audio generalization weak | Confirms robustness gap for audio channel |
| R12 | **Adversarial Deepfakes** (Hussain et al.) | WACV 2021 (IEEE) | Evaluates detector robustness to adversarial input | FF++ | detectors break under attack | robustness poor | Robustness eval harness (Innovation C) |
| R13 | **Artificial Fingerprinting** (Yu et al.) | ICCV 2021 (IEEE) | Plants fingerprints in generators → traceable | CelebA-based | reliable model ID when fingerprinted | needs cooperation of generator owner | Contrast: passive attribution (D3) must not assume cooperation |
| R14 | **OW-DFA / CPL** (Sun et al.) | ICCV 2023 (IEEE) | Contrastive pseudo learning for open-world attribution | OW-DFA benchmark | best open-set attribution so far | face-only; unseen-method accuracy limited | D3 base; we add explicit abstention class |
| R15 | **Generalized Deepfake Attribution** (Yang et al.) | arXiv 2024 | DNA-Det architecture-level attribution | several GAN sets | architecture attribution feasible | architecture-level, not instance | Attribution granularity choice for D3 |
| R16 | **Do DF Attribution Models Generalize?** | recent | Tests attribution transfer | — | attribution generalizes poorly | confirms open-set difficulty | D3 evaluation must be open-set |
| R17 | **WaViT-CDC** | IEEE OJSP 2025 | Wavelet ViT + central-difference conv | FF++, Celeb-DF | strong freq-domain detection | compute higher | Frequency expert for Innovation A |
| R18 | **SupCon + XAI** (Xu et al.) | WACV 2022 (IEEE) | Supervised contrastive + explainability | FF++ | generalizable + explainable | explanations coarse | D4 precedent — we extend to region-level + reasons |
| R19 | **Image-Matching XAI** (Trinh et al.) | LNCS 2022 | Explains via matching to real/fake exemplars | FF++ | interpretable matches | needs exemplar DB | Alternative explanation mode for D4 |
| R20 | **Neurosymbolic multimodal XAI** | ACM TOMM 2023 | Neurosymbolic rules over AV features | AV fakes | interpretable AV detection | complex | Fusion + explanation combined (Innovation E) |
| R21 | **EKILA** (Zhao et al.) | CVPR 2023 (IEEE) | Synthetic-media provenance + attribution | OpenWorld datasets | provenance attribution works | limited to known sources | Provenance module for M/D3 |
| R22 | **DefakeHop++** | APSIPA 2022 | Lightweight successive-subspace detector | FF++, Celeb-DF | decent acc, tiny model | below SOTA accuracy | Edge/mobile variant (Innovation H) |
| R23 | **FakeFormer** | ICICS 2025 | Transformer lightweight video detector | FF++, Celeb-DF | efficiency-focused | accuracy trade-off | Efficiency benchmark for pipeline design |
| R24 | **DFDC dataset** (Dolhansky et al.) | arXiv 2020 | 100k+ clips, paid actors, diverse augmentations | DFDC | hard, real-ish distribution | actors staged → domain gap | Cross-dataset eval set + compression robustness |
| R25 | **Celeb-DF++** | arXiv 2025 | Harder Celeb-DF successor | Celeb-DF++ | modern hard negatives | new | Cross-dataset eval set (harder than v2) |
| R26 | **BabelFake** | arXiv 2026 | Multilingual audio-video deepfake benchmark | BabelFake | AV multimodal benchmark | new, unverified maturity | True AV benchmark for E/D2 evaluation |
| R27 | **XMAD-Bench** | Findings ACL 2026 | Cross-domain multilingual audio DF benchmark | XMAD | audio generalization bench | new | Audio generalization eval |
| R28 | **AuViRe** (WACV 2026, IEEE) | IEEE WACV 2026 | Audio-visual speech-representation reconstruction | AV deepfake sets | AV-consistency detection | new | Strong multimodal-fusion precedent for E |
| R29 | **DeepfakeBench** (NeurIPS 2023, SCLBD) | NeurIPS 2023 | Unified benchmark: 36 detectors, 9 datasets | FF++, Celeb-DF, DFDC, FaceShifter… | standardized AUC/EER tables | not a method itself | Phase-1 baseline + eval protocol source |
| R30 | **Media provenance survey** | LNCS 2026 | Survey of provenance indicators | — | field maturing | survey | M-module design input |
| R31 | **Post-Quantum Media Provenance** | recent | PQ signatures for provenance | — | forward-looking | early | Optional hash-anchor future work (D5) |
| R32 | **Hardware-anchored provenance + blockchain** | Zenodo 2026 | Hardware+chain anchored verification | — | deployment idea | early | Optional D5 anchoring precedent |
| R33 | **Surveillance Face Anti-Spoofing** | IEEE TIFS 2023 | Spoofing under surveillance conditions | surveillance sets | robustness study | domain-specific | Robustness under degradation (C) |
| R34 | **Single-Side Domain Generalization** (Jia et al.) | CVPR 2020 (IEEE) | One-class DG for face anti-spoofing | face-PAD sets | better unseen-domain | face-PAD, not deepfake | DG technique transferable to D1 |
| R35 | **Deep Learning for Face Anti-Spoofing survey** | TPAMI 2022 (IEEE) | Survey of face-PAD | — | taxonomy | survey | Distinction: face-PAD ≠ deepfake — clarify scope |

*(R1–R35 = the ~40 most relevant; remaining ~49 entries live in
`.research/papers_raw.json` and can be promoted into the matrix on request.)*

## 4. Cross-cutting synthesis (what the literature actually shows)

1. **Cross-dataset generalization is the dominant unsolved problem.** UCF's
   0.996→0.828 in-set→cross-set AUC drop is the clearest quantified example;
   audio shows the same pattern (Müller'22: poor cross-corpus EER). Almost
   every strong detector is trained on FF++ and degrades on Celeb-DF/DFDC.
2. **Attribution is young and weak in the open world.** OW-DFA/CPL (ICCV'23)
   is the state of the art and still face-only with limited unseen-method
   accuracy; "Do attribution models generalize?" answers: mostly not yet.
3. **Audio and video detection evolved separately.** ASVspoof is audio-only;
   UCF/Multi-attentional are visual-only. True multimodal AV forensics
   (BabelFake, AuViRe) is only just emerging in 2026 — the fusion gap is real
   and current.
4. **Explainability is bolted on, not validated.** XAI papers output heatmaps
   but few verify the maps localize the actual manipulated region — a
   "convincing-looking" map can be unfaithful (matches the master prompt's
   warning, which the literature supports).
5. **Artifact-bound detectors have an expiry date.** Up-sampling-artifact
   methods (CVPR'24) are blind to diffusion generators (DIRE, ICCV'23 proves
   diffusion needs its own signal) — the field must chase new generators.
6. **No integrity layer exists in detection papers.** None of the surveyed
   work handles chain-of-custody, evidence hashing, or human-readable
   forensic reports — that's an engineering gap we fill (D5), not a research
   claim.

## 5. Contradictions / nuances (kept honest)

- CLIP-linear probes (R6) hit near-100% on *seen* generator sets — but that is
  a dataset-completeness artifact, not proof of universal generalization.
- Some lightweight models (R22/R23) claim efficiency but drop several AUC
  points vs heavy models — the efficiency/accuracy trade is unresolved.
- "Generalization" is measured differently per paper (cross-dataset vs
  cross-generator vs cross-compression) — we must pick one eval protocol and
  say which.

## 6. Access & verification honesty log

- IEEE Xplore full text: **blocked** (JS challenge, HTTP 202) — verified
  directly. Used OpenAlex + Crossref + arXiv for metadata and open full text.
- All 84 entries carry real titles/venues; 81 have DOIs that resolve.
- arXiv items are labelled as preprints (R24–R26 benchmarks, R15).
- Surveys (R30/R35, IEEE Access SLR) marked as surveys, not methods.

## 7. What this means for DeepWatch (research → design)

- The **defensible novelty** is *integration + integrity + evaluation*: a
  unified detect→attribute→explain→report pipeline with honest benchmarking —
  not a claim of a new detection algorithm.
- The **highest-value research delta** is multimodal audio–video fusion with
  calibrated abstention (gap #3 + uncertainty gap L) — current and
  under-served.
- **DeepfakeBench** gives us the standardized eval protocol + UCF reference,
  which is why Phase 1 bootstraps on it (already recorded).
