# PRD.md — Two-Layer AI Scam-Call Defense

**Status:** DRAFT — direction locked 2026-10-14; pending base-paper IEEE verification and user approval
**Created:** 2026-10-07
**Updated:** 2026-10-14

## 1. Problem statement
AI voice-cloning scams are exploding: a scammer clones a trusted voice (bank,
family member, executive) and calls a victim, who has no way to tell the voice
is fake. Existing defenses check only ONE thing — either caller ID (easily
spoofed) or voice (deepfake detectors fail on compressed phone audio). No
consumer system checks BOTH the caller's verified identity AND the voice's
authenticity together. Result: billions lost to voice scams annually.

## 2. Target users
- General public receiving suspicious calls (primary)
- Banks / institutions wanting to prove their calls are genuine
- Elderly and non-technical users most targeted by voice scams

## 3. Goals / non-goals
- Goals:
  - Verify caller identity via blockchain-registered credentials (Layer 1)
  - Detect AI-cloned / deepfake voices in real time, robust on compressed phone audio (Layer 2)
  - Combine both into a single clear verdict: "Verified real" / "Suspected scam"
  - Show a measurable improvement over the single-layer base (BVI)
- Non-goals:
  - Not a full phone app (demo/prototype scope)
  - Not a replacement for carrier-level call authentication (STIR/SHAKEN)
  - Not a medical, legal, or law-enforcement tool

## 4. Core features
1. Blockchain caller-credential verification (is this number registered to the claimed institution?)
2. AI voice-deepfake detection on live/recorded call audio (is this voice human?)
3. Two-layer fusion into one verdict + confidence score
4. Demo interface: play/upload a call, see both layer results + final verdict
5. Robustness handling for compressed / noisy phone-quality audio

## 5. Functional requirements
- FR-01: The system SHALL verify whether a caller holds a valid on-chain credential for the claimed institution.
- FR-02: The system SHALL analyze call audio and output a deepfake probability score.
- FR-03: The system SHALL combine FR-01 and FR-02 into a single verdict with a confidence level.
- FR-04: The system SHALL display the per-layer results and the final verdict in a UI.
- FR-05: The system SHALL flag a call as "suspected scam" if EITHER layer fails.

## 6. Non-functional requirements
- NFR-01: Voice analysis SHOULD run in near-real-time (< 2 s per audio segment).
- NFR-02: The system SHOULD remain accurate on compressed/phone-quality audio, not just clean lab audio.
- NFR-03: No raw user audio or credentials SHALL leave the device unencrypted.
- NFR-04: The system SHALL be evaluated against a single-layer baseline (blockchain-only) to demonstrate improvement.

## 7. Success criteria
- Two-layer system catches scam calls that the blockchain-only baseline misses (i.e., real-looking number + fake voice).
- Voice-deepfake detection maintains accuracy on compressed phone audio within an acceptable drop vs clean audio (target set after base-paper verification).
- A working demo shows a fake "bank" call flagged on at least one layer, live.

## 8. Constraints
- Student mini-project scope and timeline.
- Uses free/open models and public datasets (e.g. ASVspoof) for the voice layer.
- Blockchain layer uses a test network (no real-money gas costs).
- Must differ from the base paper (BVI) by adding the AI voice layer.

## 9. Novelty statement (delta vs base paper)
Base (BVI, 2026) verifies caller *identity* on-chain but not voice authenticity.
This project adds an AI voice-deepfake detection layer and fuses both into a
single verdict — a two-layer defense against AI voice scams that, to our
knowledge, no prior published system combines.

> Rule: never invent requirements. Anything unknown stays TODO.
