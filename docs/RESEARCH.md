# RESEARCH.md — Base Paper & Novelty Scan

**Status:** Phase 0 — landscape scanned 2026-10-07; base paper TODO
**Purpose:** this project must NOT repeat existing IEEE/arXiv work. Before any
feature is built, the chosen direction is checked against prior art, and the
user's official IEEE base paper is recorded here.

## 1. Base paper (official)

TODO — user supplies (typically assigned by the institution/department).
When provided, record: title, authors, venue, year, DOI, and the one-sentence
gap the project will fill relative to it.

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

> **Note (2026-10-14):** The D1–D4 scan below was for a biosignal/medical
> direction. The stack selected by the user (MediaPipe + WebGL2) points at the
> **hand-gesture recognition** direction instead — see §5b for the current scan.

### 5a. Earlier biosignal scan (superseded by the hand-gesture direction)

| # | Direction | Novelty claim | Feasibility | Risk |
| --- | --- | --- | --- | --- |
| D1 | **Uncertainty-aware edge triage with deferral** — wearable/biosignal classifier that outputs calibrated confidence (conformal prediction) and an explicit "defer to clinician" decision, not just a class label | Calibrated abstention on-device is far less published than plain classifiers; matches the UQ trend above | High (public ECG/PPG datasets, Python; optional edge demo) | Conformal + medical claims need careful framing |
| D2 | **LLM explanation layer over deterministic edge evidence** — rule/model evidence rendered into clinician-readable reports with anti-hallucination guards; measured by explanation-fidelity metrics | LLM-as-explainer (not diagnoser) with fidelity metrics is a thin, real gap | High | LLM cost/API dependence; evaluation design |
| D3 | **Label-efficient personalization under drift** — few-label per-user adaptation of a biosignal model with drift detection (extends the EEG-style approach to cardiac/PPG) | Personalization benchmarks exist for EEG/gait; cardiac/PPG + drift angle less covered | Medium-high | Needs solid evaluation methodology |
| D4 | Contactless radar vitals | Hot but hardware-heavy | Low (budget) | Skip unless hardware available |

### 5b. Hand-gesture direction scan (2026-10-14, arXiv listing — current stack fit)

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
- Note: IEEE Xplore blocks automated access (HTTP 418), so IEEE-specific
  novelty must be verified manually at https://ieeexplore.ieee.org before
  locking the topic.
