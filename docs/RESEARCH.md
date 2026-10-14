# RESEARCH.md — Base Paper & Novelty Scan

**Status:** Phase 0 — direction LOCKED 2026-10-14; IEEE base paper pending manual verification
**Purpose:** this project must NOT repeat existing IEEE/arXiv work. Before any
feature is built, the chosen direction is checked against prior art, and the
user's official IEEE base paper is recorded here.

## 1. Base paper (official)

**Direction LOCKED (2026-10-14, revised):** AI Smart-Contract Vulnerability
Auditor — an AI system that finds security holes in cross-chain bridge smart
contracts and explains them. Domains integrated: AI/NN + blockchain +
cybersecurity + computer networks.

**Candidate base paper:** "Understanding Verification Vulnerabilities in
Cross-chain Bridges" (Oct 2026, arXiv) — first systematic study of cross-chain
verification vulnerabilities, built from 588 audit reports across 36 real bridge
projects; produced an 830-instance dataset over 786 contract files. Best of four
LLMs reached only 51.2% Macro-F1 vs a 29.3% constant baseline.

**One-sentence gap the project fills:** the base paper catalogs the
vulnerabilities but its best detector reaches only 51.2% Macro-F1 — this project
builds a purpose-trained/fine-tuned detector that measurably beats that bar and
explains each finding in plain language.

**TODO:** user verifies IEEE venue of the base paper manually via IEEE Xplore
(through college library) or via Crossref, then records DOI here.

## 2. Landscape scan (2026-10-07, arXiv current listings)

Scanned: eess.SP, cs.LG, cs.AI recent listings (WebSearch was unavailable from
this network; direct arXiv fetches worked — re-verify on IEEE Xplore/Scopus
before locking the topic).

What the field is actively publishing right now:

- ECG delineation with label-efficient deep learning, benchmarked (2610.07885)
- Contactless ECG recovery from radar (Kapture, 2610.04955)
- Online label-revealed adaptation for EEG BCI (2610.07824)
- Per-participant adaptive biofeedback modeling (2610.07428)
- Uncertainty quantification argued as indispensable in medical graph ML (2610.08368)
- Clinical note generation benchmarking (2610.08131); self-evving medical
  reasoning agents (MedZERO, 2610.08327)
- Edge-efficient adaptation: memory-floored LoRA for CNNs at the edge (2610.08669);
  6G split computing (2610.08352)

## 3. Crowded areas to AVOID (saturated; from model knowledge — verify on IEEE Xplore)

- CNN/LSTM arrhythmia classification on MIT-BIH ECG — extremely saturated
- Accelerometer fall detection — saturated
- PPG heart-rate estimation — saturated
- Chest X-ray classifiers, tabular diabetes prediction — saturated
- Generic symptom-checker chatbots — saturated

## 4. Prior own-work overlap to avoid

The user's previous project (S:\stuff, "Patient Monitoring Mesh") was: ESP32
mesh networking + prioritized store-and-forward + FastAPI/SQLite + dashboard +
rule-based risk engine. A new project that is "mesh + rule engine + dashboard"
under a new name would be self-repetition — new project must differ in its
core contribution (the AI/ML method, not just the plumbing).

## 5. Candidate novel directions

> **Note (2026-10-14):** The user clarified the previously-recorded
> MediaPipe/WebGL2 stack was only a placeholder, NOT a real choice. The field
> is now wide open. §5a (biosignal) and §5b (hand-gesture) are kept for
> reference; §5c scans four topic areas fresh to find the strongest
> "best-impression" project. Topic selection is pending the user's decision.

### 5c. Cross-area "best impression" scan (2026-10-14, arXiv)

Scanned four areas for strong, beatable base papers with clear improvement
angles. Accuracy figures are as reported by the papers (verify before citing).

**Area 1 — Deepfake / synthetic-media detection (AI/ML, very hot)**
- *Adaptive Compression & Targeted Perturbation (audio deepfake), 2026* — SOTA
  1.51% EER, NeurIPS 2026. Hard to beat.
- *Explainable Deepfake Detection Challenge 2026 (MSU)* — 0.9349 accuracy,
  adds VLM-generated explanations. **Gap: explainability is the trend.**
- *Camera-noise residuals for face-swap, 2026* — negative result (redundant).

**Area 2 — Plant disease detection (Computer Vision, agriculture)**
- *AgriMind ensemble, 2026* — 99.23% on PlantVillage, 53 FPS. High bar.
- *PD36-C compact CNN, 2026* — 99.5% test, 4.77 MB, offline app.
  **Gap: tiny models for edge/mobile.**
- *Mobile-friendly benchmarking, 2025* — 94.7% on 101 diseases/33 crops.
- Pattern: ensembles + transfer learning hit 99%+; lightweight/edge is the gap.

**Area 3 — Mental-health / depression detection (AI for social good)**
- *Dynamic Summary Generation (multimodal), 2026* — LLM clinical summaries,
  "significant improvements" over SOTA (no number).
- *Retrieval-Augmented Multimodal, 2025* — CCC 0.593 / MAE 3.95 on AVEC 2019.
- *GPT-5 long-context benchmark, 2026* — accuracy drops to ~50-53% on 20K posts.
  **Gap: robustness to long/real-world social-media text.**
- Ethical sensitivity: needs careful framing (not a diagnostic tool).

**Area 4 — Early disease prediction (Health ML)**
- *Early T2 Diabetes, tabular transformer, 2026* — ROC AUC ≥ 79.7% (Qatar
  BioBank). Beatable with public data.
- *ECG-DiaNet, 2025* — AUROC 0.845 (ECG + clinical).
- *Pima Indians comparative study, 2025* — best NN 78.57%.
  **Gap: multimodal fusion + calibrated confidence on public datasets.**

### 5d. Fresh-direction scan (2026-10-14 — avoiding senior-covered topics)

User said the four areas in §5c were already done by seniors. Goal: a FRESH
topic lecturers won't have seen. Scanned two newer areas:

**AI-generated text detection** (catching ChatGPT-written content) —
very hot, but base papers report weak/near-chance accuracy (CrisisFake 2026:
detectors AUROC 0.40–0.52 on real posts), so it's risky/hard to show a clean win.

**Speech deepfake / scam-call voice detection** — strong, fresh, and timely:
- *DuRe-ST (2026)* — 25.9% relative EER reduction over XLSR-AASIST on ASVspoof.
- *UZH-CL at ArA-DF 2026* — prompt-tuned foundation model, 1.04–1.96% EER.
- *Codec-shift residuals (2026)* — 54.2% EER reduction; robustness to real
  phone-call audio compression is the open gap.
- *Multilingual frozen SSL (2026)* — In-the-Wild EER 26.5% vs 46.8%.

**Key insight / gap:** most detectors are trained on clean lab audio (ASVspoof)
and degrade badly on real phone/compressed calls. A project that detects AI
scam-call voices **robustly on real, compressed, multilingual (e.g.
Indian-accent) audio** is fresh, socially relevant (phone scams are rising),
and has a clear measurable improvement (EER/accuracy on real-world audio).

**RECOMMENDED FRESH DIRECTION: Real-world AI scam-call voice detection.**
Base paper: a 2026 speech-deepfake detection paper (DuRe-ST or UZH-CL).
Contribution: improve robustness/accuracy on compressed, real phone-call audio
(and optionally Indian-accent speech), plus a simple demo that flags a live or
recorded call as real vs AI.

### 5e. Blockchain + AI scan (2026-10-14 — user's stated interest)

User asked about blockchain/cryptography, then blockchain + AI combined. Scanned
2026 arXiv (cs.CR) for strong base papers at that intersection.

**Standout base paper — BVI: Blockchain-Based Verification of Identity Claims
(Oct 2026):** lets a call recipient verify a caller (e.g. a bank) actually holds
an issued credential, directly countering voice-cloning scams. Metrics: 27/27
automated scenario tests pass, ~91.5k gas per session anchor, detects 20.6% of
in-path rewrites vs 0.1% baseline. Fresh, real-world, strong metrics.

**Other strong 2026 candidates at the intersection:**
- *Post-quantum V2X auth (ZKS-PQC)* — ZKP shrinks vehicle-security messages >95%.
- *Physics-Attested Federated Learning* — zk-SNARKs + cyber-physical invariants
  catch data poisoning in FL (water infrastructure); 0/100 honest rejected.
- *Cross-chain bridge auditor* — LLM finds verification bugs; 51.2% Macro-F1.

**RECOMMENDED: Blockchain + AI Scam-Call Defense (two-layer).**
Base: BVI (blockchain caller-credential verification).
Contribution: add an AI voice-deepfake detector as a second layer — verify BOTH
"is this number really the bank?" (blockchain) AND "is this voice really human?"
(AI). Two-layer defense against AI voice scams is a clear, novel, measurable
improvement, combining blockchain (user interest) + AI (impressive + fresh).

### 5f. Domain ranking (2026-10-14 — user's candidate domains)

User asked to weigh: blockchain, cryptography, AI, neural networks, computer
networks, computer vision, cybersecurity. Ranked for a student mini project on
impressiveness, feasibility, freshness (vs seniors), and demo-ability:

| Domain | Impress | Feasible | Fresh | Demo | Note |
| --- | --- | --- | --- | --- | --- |
| AI / Neural Networks | High | High | Medium | High | Backbone of most top picks |
| Computer Vision | High | High | Medium | Very high | Strong demos, some saturation |
| Cybersecurity | High | Medium | High | High | Fresh if applied to new threat |
| Blockchain / Crypto | High | Medium | Medium | Medium | Impressive only with a fresh angle |
| Computer Networks | Medium | Medium | Medium | Low | Weakest demo, mostly plumbing |

**Conclusion:** AI + Cybersecurity (+ optional blockchain) is the strongest
combination. The recommended project (two-layer scam-call defense, §5e) already
sits at that intersection: AI (voice deepfake detection) + Cybersecurity
(anti-scam) + Blockchain (caller credential). Computer vision and pure computer
networks are weaker fits as the CORE contribution for this goal.

### 5g. AI Scam-Call / Voice-Security domain deep scan (2026-10-14)

User returned to the AI scam-call / voice-security domain and asked for a heavy
list of project options. Scanned arXiv (audio deepfake detection, speaker
verification anti-spoofing, scam/fraud call detection), 2025–2026. Key papers
and reported metrics:

**Detection (voice deepfake / spoof):**
- Adaptive Compression & Targeted Perturbation (2026) — SOTA 1.51% avg EER,
  91.6% fewer params than a 3B baseline; cross-lingual EER 3.91–5.65%.
- Exposing & Mitigating Neural Codec Vulnerabilities (2026) — detectors fail on
  codec-compressed speech; PCL-NET cuts EER 28.67% → 12.77% under compression.
  **Gap: phone/real-world compression robustness.**
- Task-Aware Joint Pruning & Distillation (2026) — compresses detectors to 31.9M
  params, 6.3× FLOPs cut, 1.30% drop. **Gap: on-device deployment.**
- Quantum Kernel Robustness (2026) — low-resource (200 samples) detection;
  QSVM 27% EER vs MLP 50% under domain shift.

**Scam-call specific:**
- StreamFraudNet (2026) — incremental phone-scam detection from raw telephone
  audio; first prediction after 10 s, updates every 2 s, faster than real time;
  ROC-AUC 0.9953 on English benchmark. **Closest to a scam-call product.**
  **Gap: English-only, no multilingual/Indian-language support, no explainability.**

**Attacks (show current systems are vulnerable):**
- SMIA (2025) — inaudible-frequency attack; ≥82% success vs combined systems,
  100% vs standalone countermeasures.
- Discrete Optimal Transport attack (2025) — black-box, transfers across datasets.

**Defense / prevention (not detection):**
- ClearMask (AsiaCCS 2025), Enkidu (ACM MM 2025) — protect speech from being
  cloned (real-time, lightweight).

**Identified gaps (project opportunities):**
1. Phone-codec robustness (detectors degrade badly on real call audio)
2. Multilingual / Indian-language scam-call detection (StreamFraudNet is English-only)
3. On-device / real-time lightweight detection
4. Explainable verdicts (why the call was flagged)
5. Low-resource detection (works with few training samples)
6. Robustness to adversarial attacks (SMIA/DOT bypass current systems)

### 5h. IEEE base-paper shortlist for DeepWatch (2026-10-14, OpenAlex — verified IEEE venues)

Found via OpenAlex title-search with venue verification (IEEE Xplore still blocked
for scraping, but OpenAlex indexes IEEE publications with venue names).

**Detection (IEEE venues):**
| Paper | Venue | Year | Citations |
| --- | --- | --- | --- |
| UCF: Uncovering Common Features for Generalizable Deepfake Detection (Yan et al.) | IEEE/CVF ICCV | 2023 | 230 |
| Rethinking the Up-Sampling Operations in CNN-Based Generative Network (Tan et al.) | IEEE/CVF CVPR | 2024 | 210 |
| Implicit Identity Leakage: Stumbling Block to Improving Deepfake Detection Generalization (Dong et al.) | IEEE/CVF CVPR | 2023 | high |
| ASVspoof 2021: Towards Spoofed and Deepfake Speech Detection in the Wild (Liu et al.) | IEEE/ACM Trans. Audio, Speech & Language Processing | 2023 | 296 |

**Attribution / forensics (IEEE venues):**
| Paper | Venue | Year | Citations |
| --- | --- | --- | --- |
| Model Attribution of Face-Swap Deepfake Videos (Jia, Li, Lyu) | IEEE ICIP | 2022 | 29 |
| Contrastive Pseudo Learning for Open-World DeepFake Attribution (Sun et al.) | IEEE/CVF ICCV | 2023 | 27 |

**Surveys (context, not IEEE):** "Deepfake Media Forensics: Status and Future
Challenges" (2025, 105 citations) and "Deepfake forensics survey" (PeerJ 2024,
69 citations) — useful for the literature-review chapter of the project report.

**Key insight for DeepWatch:** detection is well-published (ICCV/CVPR), but
**attribution is thin** — the top IEEE attribution papers have only 27–29
citations, meaning the field is young and a student contribution is realistic.
Recommended base-paper pairing: one detection paper (UCF or CVPR 2024) + one
attribution paper (ICCV 2023 open-world attribution), with the project's delta
being a unified detect → attribute → explain → report pipeline.

### 5a. Earlier biosignal scan (reference)

| # | Direction | Novelty claim | Feasibility | Risk |
| --- | --- | --- | --- | --- |
| D1 | **Uncertainty-aware edge triage with deferral** — wearable/biosignal classifier that outputs calibrated confidence (conformal prediction) and an explicit "defer to clinician" decision, not just a class label | Calibrated abstention on-device is far less published than plain classifiers; matches the UQ trend above | High (public ECG/PPG datasets, Python; optional edge demo) | Conformal + medical claims need careful framing |
| D2 | **LLM explanation layer over deterministic edge evidence** — rule/model evidence rendered into clinician-readable reports with anti-hallucination guards; measured by explanation-fidelity metrics | LLM-as-explainer (not diagnoser) with fidelity metrics is a thin, real gap | High | LLM cost/API dependence; evaluation design |
| D3 | **Label-efficient personalization under drift** — few-label per-user adaptation of a biosignal model with drift detection (extends the EEG-style approach to cardiac/PPG) | Personalization benchmarks exist for EEG/gait; cardiac/PPG + drift angle less covered | Medium-high | Needs solid evaluation methodology |
| D4 | Contactless radar vitals | Hot but hardware-heavy | Low (budget) | Skip unless hardware available |

### 5b. Hand-gesture direction scan (2026-10-14 — reference; stack was a placeholder)

Base-paper candidates in the MediaPipe hand-gesture space, with reported
accuracy where stated:

| Candidate (title, year) | What it does | Reported accuracy | Why it fits / gap to beat |
| --- | --- | --- | --- |
| **Dynamic LIBRAS Gesture Recognition via CNN over Spatiotemporal Matrix** (2026) | MediaPipe Hand Landmarker (21 kp) → CNN over a 90×21 spatiotemporal matrix; 11 gestures, home automation | 95% low light / 92% normal | **Strongest fit.** Single architecture; clear delta: add temporal model (LSTM/Transformer) + landmark normalization to push low-light/normal accuracy up |
| Mediapipe and CNNs for Real-Time ASL Gesture Recognition (2023) | MediaPipe features → CNN, ASL alphabet | 99.95% | High bar; hard to claim an "improvement" — avoid as a base |
| Enhancing Sign Language Detection through Mediapipe + CNN (2024) | MediaPipe + CNN, ASL | 99.12% (withdrawn for revisions) | Withdrawn — not a safe base paper |
| SLRNet: Real-Time LSTM Sign Language Recognition (2025) | MediaPipe Holistic + LSTM, letters + functional words | 86.7% | **Good beatable bar.** Clear delta: better features/architecture to exceed 86.7% |
| GRLib: Open-Source HGR Library (2023) | MediaPipe landmarks, static+dynamic gestures; beats MediaPipe Solutions on 3 datasets | none stated | Tooling, not a benchmark — use as a library reference, not a base |
| Hand tracking for clinical applications (GMH / GMH-D) (2023) | Validates MediaPipe Hands vs gold standard; depth-enhanced variant improves spatial accuracy | qualitative | Good model for an "accuracy-improvement" framing, but clinical — needs equipment/participants |

**Recommended base-paper direction:** a MediaPipe landmarks → CNN (or
LSTM/Transformer) **dynamic gesture recognition** paper, with the project's
contribution being a measurable accuracy/robustness improvement (temporal
modeling, landmark normalization, low-light augmentation) plus the WebGL2
real-time visualization. Avoid the 99%+ ASL papers as bases (no headroom);
avoid the withdrawn paper entirely.

## 6. Verification checklist (before Phase 1 build)

- [ ] User supplies IEEE base paper; record in §1
- [ ] IEEE Xplore / Scopus search on the chosen direction's exact keywords
- [ ] Confirm no 2025–2026 paper already does the exact contribution
- [ ] Record the delta vs base paper in PRD §"novelty statement"

## 7. Sources

- 2026-10-07: arXiv eess.SP / cs.LG / cs.AI recent listings
  (https://arxiv.org/list/eess.SP/recent etc.)
- 2026-10-14: arXiv API query "MediaPipe AND gesture recognition"
  (http://export.arxiv.org/api/query)
- Note on IEEE access (updated 2026-10-14): IEEE Xplore's anti-bot is layered.
  A browser User-Agent gets HTTP 200 on the search shell, but document pages
  return HTTP 202 with a JavaScript challenge (PerimeterX-style), and PDF
  downloads require institutional login. CONFIRMED: IEEE full text cannot be
  scraped from this environment. Working paths: (a) arXiv HTML/PDF for content
  (most IEEE/CVF papers have free arXiv versions with identical content),
  (b) OpenAlex/Crossref APIs for venue verification and citation data,
  (c) manual IEEE Xplore via the college library for anything paywalled.
  Verified example: UCF (ICCV 2023) has DOI 10.1109/ICCV51070.2023.02048
  (genuine IEEE publication) AND a free arXiv copy (2304.13949).
