# SECURITY_AND_PRIVACY.md — Threat Model & Data-Handling Policy

**Status:** Defined for DeepWatch
**Date:** 2026-10-14
**Companion:** `PRD.md`, `ARCHITECTURE.md`

## 1. Threat model

| Threat | Vector | Mitigation |
| --- | --- | --- |
| Malicious upload (parser exploit) | crafted image/video/audio | parse in isolated worker; strict allow-list of codecs; size caps |
| Decompression / zip-bomb | huge decompressed media | byte + pixel + duration caps before decode |
| Resource exhaustion | many/large uploads | job queue, per-job timeout, memory limits |
| Biometric data exposure | faces/voices in uploads | local-only processing (NFR-04); no cloud calls; pseudonymised filenames in logs |
| Evidence tampering | modified media/log | SHA-256 at ingest; append-only log; report hashing; optional chain anchor |
| Model-weight tampering | swapped checkpoints | checkpoint hash registry verified at load |
| API abuse | open endpoint | localhost-only binding by default; no auth needed in v1 |

## 2. Privacy policy

- **Local-first:** user media never leaves the device; no telemetry of media.
- **Retention:** uploads persist only until the user deletes them; logs record
  hashes + metadata, not media content.
- **Biometric data:** treated as sensitive — processed in-memory/on-disk only,
  never uploaded, never used for training.
- **Logs:** record hashes, model versions, parameters, timestamps — not raw
  media or personal identifiers.

## 3. Responsible-forensics constraints

- Outputs are **probabilistic indicators, not legal proof** — every report and
  the UI state this.
- **False accusations have real cost** — false-positive rate reported
  separately, abstention offered, no definitive-guilt language.
- **Attribution limits:** "likely generation family" with confidence — never
  "definitely made by X."
- **Blockchain anchoring limit:** proves report integrity after creation, not
  the truth of contents.
- **Bias:** evaluate per-subgroup error where datasets allow; unequal error
  rates disclosed.

## 4. Licensing & data-use compliance

- Project code: MIT.
- **DeepfakeBench (baseline): CC BY-NC-4.0** — academic/non-commercial only;
  we comply (mini-project is non-commercial) and must not ship it in any
  commercial product.
- Datasets (FF++, Celeb-DF, DFDC, ASVspoof, OW-DFA): research-agreement terms —
  used for evaluation only, not redistributed.
- Model weights: verify each pretrained checkpoint's license before bundling.

## 5. Residual risks (documented, not hidden)

- Detection is an arms race — new generators will degrade it.
- Compression/re-encoding erases artifacts detectors rely on.
- Small demographic groups may see worse error rates; disclosed, not denied.
- A sophisticated adversary can attempt to evade — we measure robustness,
  not invulnerability.
