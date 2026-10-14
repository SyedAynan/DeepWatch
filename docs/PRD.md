# PRD.md — OmniShield: Multimodal Scam & Fraud Detection Ecosystem

**Status:** DRAFT — direction locked 2026-10-14; pending base-paper IEEE verification and user approval
**Created:** 2026-10-07
**Updated:** 2026-10-14

## 1. Problem statement
Scams reach victims through multiple channels — voice calls, text messages, and
video calls — but current detection tools only handle ONE channel. A victim
protected from phishing emails is still vulnerable to an AI-cloned voice call or
a deepfake video call. There is no unified system that detects scams across all
three modalities, explains the verdict, and reports it tamper-proof.

## 2. Target users
- General public receiving suspicious calls, texts, and video calls (primary)
- Banks, telecoms, and institutions wanting to protect customers
- Law enforcement / investigators tracking scam campaigns

## 3. Goals / non-goals
- Goals:
  - Detect scams across voice, text, and video in one unified system
  - Fuse all three modalities into a single verdict with confidence
  - Explain why a message/call/video was flagged
  - Provide real-time alerts and a threat-intelligence dashboard
  - Record scam reports tamper-proof on a blockchain ledger
- Non-goals:
  - Not a replacement for carrier-level authentication (STIR/SHAKEN)
  - Not a full antivirus / endpoint protection suite
  - Not a general-purpose content moderation platform

## 4. Core features
1. Voice scam detector (AI-cloned voice detection on calls)
2. Text phishing/smishing detector (scam texts and emails)
3. Deepfake video detector (fake video calls)
4. Unified AI fusion engine (combines all three into one verdict)
5. Real-time alert system (warns users across channels)
6. Threat-intelligence dashboard (tracks scam campaigns and trends)
7. Blockchain report ledger (tamper-proof, shareable scam reports)

## 5. Functional requirements
- FR-01: The system SHALL analyze voice call audio and output a scam probability.
- FR-02: The system SHALL analyze text messages and emails and output a phishing probability.
- FR-03: The system SHALL analyze video call streams and output a deepfake probability.
- FR-04: The system SHALL fuse voice, text, and video signals into a single unified verdict.
- FR-05: The system SHALL generate a plain-language explanation for each verdict.
- FR-06: The system SHALL alert the user in real time when a scam is detected.
- FR-07: The system SHALL record scam reports on a blockchain ledger.

## 6. Non-functional requirements
- NFR-01: Detection SHOULD run in near-real-time (< 2 s per input).
- NFR-02: The system SHOULD remain accurate on compressed/phone-quality audio and low-resolution video.
- NFR-03: No raw user audio, text, or video SHALL leave the device unencrypted.
- NFR-04: The blockchain ledger SHALL be on a test network (no real-money cost).
- NFR-05: The system SHALL be evaluated against single-modality baselines to demonstrate the value of fusion.

## 7. Success criteria
- The unified system detects scams that single-modality tools miss (e.g., a scam that looks safe in text but is a deepfake in video).
- Detection accuracy on each modality matches or beats published single-modality benchmarks.
- A working demo: paste a scam text, play a fake voice, show a deepfake video — all caught and explained live.

## 8. Constraints
- Student mini-project scope and timeline.
- Uses free/open models and public datasets (ASVspoof, phishing datasets, deepfake benchmarks).
- Blockchain layer uses a test network (no real-money gas costs).
- Must differ from existing single-modality tools by unifying all three and adding explainability + blockchain reporting.

## 9. Novelty statement (delta vs base papers)
Existing tools detect scams in only ONE modality. This project unifies voice,
text, and video detection into a single ecosystem with a fused AI engine,
real-time alerts, and blockchain-backed tamper-proof reporting — a combination
no prior published system provides.

> Rule: never invent requirements. Anything unknown stays TODO.
