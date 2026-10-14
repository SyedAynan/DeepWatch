<div align="center">

  <img src="assets/banner.png" alt="DeepWatch Banner" width="100%" />

  <br/>
  <br/>

  <h1>🔍 DeepWatch — Unified Deepfake Forensics & Attribution Platform</h1>

  <p>
    <strong>Multimodal AI forensic lab that detects manipulated media, attributes the generation method, explains the evidence, and issues integrity-protected forensic reports</strong>
  </p>

  <p>
    <a href="https://github.com/SyedAynan/Mini-Project/actions"><img src="https://img.shields.io/badge/CI_Build-Passing-00F0FF?style=flat-square&color=00F0FF&labelColor=161b22&logo=githubactions&logoColor=white" alt="CI Status"/></a>
    <a href="https://github.com/SyedAynan/Mini-Project"><img src="https://img.shields.io/badge/Status-Active_Development-00E676?style=flat-square&color=00F0FF&labelColor=161b22" alt="Status"/></a>
    <a href="https://github.com/SyedAynan/Mini-Project/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square&color=00F0FF&labelColor=161b22" alt="License"/></a>
    <img src="https://img.shields.io/badge/PyTorch-Deepfake_Detection-EE4C2C?style=flat-square&color=00F0FF&labelColor=161b22&logo=pytorch&logoColor=white" alt="PyTorch"/>
    <img src="https://img.shields.io/badge/Base-IEEE%2FCVF%20ICCV%202023-990000?style=flat-square&color=00F0FF&labelColor=161b22&logo=ieee&logoColor=white" alt="IEEE ICCV"/>
    <img src="https://img.shields.io/badge/Forensics-Evidence_Preserving-00E676?style=flat-square&color=00F0FF&labelColor=161b22" alt="Forensics"/>
  </p>

  <p>
    <a href="#-the-problem">Problem</a> &bull;
    <a href="#-what-deepwatch-does">What It Does</a> &bull;
    <a href="#-architecture--pipeline">Architecture</a> &bull;
    <a href="#-base-papers--novelty">Base Papers</a> &bull;
    <a href="#-tech-stack">Tech Stack</a> &bull;
    <a href="#-docs-first-architecture">Docs</a> &bull;
    <a href="#-roadmap">Roadmap</a>
  </p>

</div>

<br/>

---

> [!IMPORTANT]
> **Docs-First Architecture:** This repository enforces strict documentation discipline (`PRD.md`, `TECHSPEC.md`, `ARCHITECTURE.md`, `MEMORY.md`). All system design changes are captured in specification documents before implementation. The full research proposal is at [`docs/DeepWatch-Report.pdf`](docs/DeepWatch-Report.pdf).

---

## ⚠️ The Problem

Generative AI can now fabricate convincing faces, voices, and videos in minutes — and it is being used for real crime: voice-clone scam calls, fabricated videos of private individuals, and unverifiable digital "evidence." Yet today's research tools each solve only a fragment of the problem:

- **Detectors** output a bare probability — no explanation, trained on clean lab data
- **Attribution methods** identify which tool made a fake — but only for faces
- **Speech anti-spoofing** checks the audio — but is never fused with video
- **No published system** produces evidence a victim can hand to police or a platform

DeepWatch closes that gap: **one platform that detects, attributes, explains, and documents.**

<br/>

## 🔍 What DeepWatch Does

| Component | Feature | Answers base-paper gap |
| :--- | :--- | :--- |
| **D1** | Visual deepfake detection (common-forgery features, after UCF) | Cross-dataset degradation + no explanation |
| **D2** | Audio–video fusion (speech anti-spoofing + lip-sync check) | Unimodal audio/visual evaluation |
| **D3** | Open-set generation-method attribution with abstention | Face-only, closed-set attribution |
| **D4** | Explainable evidence — artifact heatmaps + plain-language reasons | Opaque bare-score outputs |
| **D5** | Forensic PDF report — SHA-256 hashed, integrity-logged, optional blockchain anchor | No usable evidence output |

> [!NOTE]
> **Honest framing:** DeepWatch outputs are *indicators supporting an assessment*, not definitive proof. All claims are evaluated against the base papers' published benchmarks.

<br/>

## 🏗️ Architecture & Pipeline

### 1. Forensic Analysis Pipeline

```mermaid
flowchart TD
    subgraph Ingest ["1. Evidence Ingest (Integrity-First)"]
        A[📁 Media Upload] --> B[🔐 SHA-256 Hash + Immutable Copy]
        B --> C[📋 Append-Only Analysis Log]
    end

    subgraph Analysis ["2. Multimodal Analysis"]
        C --> D[🖼️ Visual Detector<br/>common-forgery features]
        C --> E[🔊 Speech Anti-Spoofing<br/>ASVspoof protocol]
        C --> F[👄 Lip–Speech<br/>Consistency]
    end

    subgraph Reason ["3. Attribution & Explanation"]
        D --> G[🧩 Open-Set Attribution<br/>method or 'unseen' abstain]
        D --> H[🗺️ Artifact Heatmaps<br/>+ plain-language reasons]
    end

    D & E & F --> I[⚖️ Fused Verdict + Calibrated Confidence]
    G --> I
    I --> J[📄 Forensic PDF Report<br/>hashes + logs + scores]
    H --> J
    J --> K[⛓️ Optional: hash anchored<br/>on test blockchain]
```

### 2. Sequence Flow

```mermaid
sequenceDiagram
    autonumber
    participant User as 👤 User
    participant API as ⚙️ Local API
    participant Store as 💾 Evidence Store
    participant Models as 🧠 Models
    participant Log as 📋 Audit Log

    User->>API: Upload suspicious media
    API->>Store: SHA-256 hash + preserve original
    API->>Log: Record ingest event
    API->>Models: Visual + audio + sync analysis
    Models-->>API: Channel scores + heatmaps
    API->>Models: Attribution (open-set)
    Models-->>API: Method label or 'unseen'
    API->>Log: Append every step + model versions
    API-->>User: Fused verdict + explanation + forensic PDF
```

<br/>

## 📄 Base Papers & Novelty

| Base Paper | Venue | Contribution | Limitation DeepWatch addresses |
| :--- | :--- | :--- | :--- |
| **UCF** — Yan et al. | IEEE/CVF ICCV 2023 | Common-forgery-feature detection; 0.996 in-dataset AUC | 0.828 cross-dataset AUC; needs per-method labels; no explanation |
| **Up-sampling artifacts** — Tan et al. | IEEE/CVF CVPR 2024 | Detects CNN-generator up-sampling artifacts | Tied to CNN artifact classes; unaddressed generator families |
| **OW-DFA / CPL** — Sun et al. | IEEE/CVF ICCV 2023 | Open-world attribution of unseen forgery methods | Face-only; limited unseen-method accuracy |
| **ASVspoof 2021** — Liu et al. | IEEE/ACM TASLP 2023 | Standard speech anti-spoofing benchmark | Audio-only; never fused with visual analysis |

**Delta:** detection + attribution + explanation + integrity-protected reporting in one pipeline — a combination absent from the reviewed literature (scoped claim, verified in `docs/RESEARCH.md`).

<br/>

## 🔬 Forensic Integrity

- 🔐 **SHA-256** hashing of every submitted file before analysis
- 🗄️ **Original media preserved** unmodified; all processing on copies
- 📋 **Append-only analysis log** — every step, model version, and parameter
- ⚖️ **False positives and false negatives reported separately** — they cost differently in the real world
- 🔁 **Reproducible** — code, configs, model hashes, and eval scripts released
- 🧾 Optional **test-blockchain hash anchoring** (tamper evidence, not truth claims)

<br/>

## 🛠️ Tech Stack

- **ML & Analysis:** ![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-Models-EE4C2C?style=flat-square&logo=pytorch&logoColor=white) ![OpenCV](https://img.shields.io/badge/OpenCV-Frames-5C3EE8?style=flat-square&logo=opencv&logoColor=white) `timm` `librosa` `torchaudio` `ffmpeg`
- **Baseline Benchmark:** [DeepfakeBench](https://github.com/SCLBD/DeepfakeBench) (NeurIPS 2023 — implements UCF + eval protocols)
- **API & UI:** FastAPI · minimal HTML/JS frontend
- **Forensics:** `hashlib` (SHA-256) · SQLite audit log · ReportLab/WeasyPrint (PDF)
- **Tooling:** uv · pytest · Git & GitHub

<br/>

## 📚 Docs-First Architecture

| Document | Focus |
| :--- | :--- |
| [`docs/PRD.md`](docs/PRD.md) | Product requirements — D1–D5 features, FR-01..06, NFR-01..06 |
| [`docs/DeepWatch-Report.pdf`](docs/DeepWatch-Report.pdf) | 2-page research proposal (base papers, gaps, innovations) |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Forensic pipeline, module boundaries, security model |
| [`docs/TECHSPEC.md`](docs/TECHSPEC.md) | Stack, datasets, evaluation plan |
| [`docs/RESEARCH.md`](docs/RESEARCH.md) | Domain scans, base-paper verification, gap analysis |
| [`docs/IMPLEMENTATIONPLAN.md`](docs/IMPLEMENTATIONPLAN.md) | Phase 1–4 tasks with acceptance criteria |
| [`docs/TRACKER.md`](docs/TRACKER.md) | Live task progress |
| [`docs/MEMORY.md`](docs/MEMORY.md) | Sprint log and current state |

<br/>

## 💻 Getting Started

```bash
# 1. Clone
git clone https://github.com/SyedAynan/Mini-Project.git
cd Mini-Project

# 2. Inspect the spec
head -n 40 docs/PRD.md

# 3. Environment (once Phase 1 scaffold lands)
uv sync
uv run pytest
```

<br/>

## 🗺️ Roadmap

- [x] **Phase 0:** Direction, IEEE base papers, gap analysis, PRD, stack, proposal PDF
- [ ] **Phase 1:** Scaffold + baseline detector on a public benchmark (via DeepfakeBench)
- [ ] **Phase 2:** Audio anti-spoofing, lip–speech sync, open-set attribution, fusion
- [ ] **Phase 3:** Explainability heatmaps, forensic PDF, audit log, web UI
- [ ] **Phase 4:** Honest benchmarking vs baselines (FP/FN separated), demo, docs polish

> ⚠️ **Pending user actions:** IEEE Xplore access check for the 4 base papers; FaceForensics++ download agreement (Google form) submitted.

<br/>

## 📄 License

Distributed under the **MIT License** for project code. Note: DeepfakeBench baseline code is CC BY-NC-4.0 (non-commercial). See [`LICENSE`](LICENSE).

<br/>

## 👨‍💻 Author

<div align="center">

  <h3>Syed Ayan</h3>
  <p><strong>Full Stack Developer &bull; Web3 Engineer &bull; System Architect</strong></p>

  <a href="https://github.com/SyedAynan">
    <img src="https://img.shields.io/badge/GitHub-SyedAynan-161b22?style=flat-square&logo=github&logoColor=white" alt="GitHub"/>
  </a>
  <a href="https://vercel.com/elight1">
    <img src="https://img.shields.io/badge/Vercel-Portfolio-161b22?style=flat-square&logo=vercel&logoColor=white" alt="Vercel"/>
  </a>

</div>
