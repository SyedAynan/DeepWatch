# PRD.md — AI Smart-Contract Vulnerability Auditor

**Status:** DRAFT — direction locked 2026-10-14; pending base-paper IEEE verification and user approval
**Created:** 2026-10-07
**Updated:** 2026-10-14

## 1. Problem statement
Cross-chain bridges (the smart contracts that move crypto between blockchains)
have lost billions to exploitable verification bugs. The 2026 base study
cataloged these vulnerabilities across 36 real bridge projects, but the best
automated detector (an LLM) reached only **51.2% Macro-F1** — barely better than
a 29.3% constant baseline. Developers have no tool that reliably finds these
bugs **and** explains them before deployment. Result: preventable, catastrophic
financial losses.

## 2. Target users
- Smart-contract developers (primary) — catch bugs before deploying
- Security auditors — speed up manual review with AI pre-screening
- Bridge / DeFi projects — reduce exploit risk

## 3. Goals / non-goals
- Goals:
  - Detect cross-chain verification vulnerabilities in smart contracts
  - Beat the base paper's 51.2% Macro-F1 detection bar (measurable improvement)
  - Explain each finding in plain language (what the bug is, why it's dangerous)
  - Provide a simple interface to submit a contract and get findings
- Non-goals:
  - Not a full formal-verification tool (no mathematical proofs)
  - Not a guarantee of "bug-free" contracts (it's an aid, not a proof)
  - Not a general smart-contract linter for unrelated bug classes (scoped to cross-chain verification)

## 4. Core features
1. Contract input (paste/upload Solidity contract files)
2. AI vulnerability detection (fine-tuned / purpose-built model)
3. Plain-language explanation of each finding (location + why it's dangerous)
4. Severity rating per finding
5. Evaluation dashboard comparing against the base paper's benchmark

## 5. Functional requirements
- FR-01: The system SHALL accept Solidity smart-contract source as input.
- FR-02: The system SHALL detect cross-chain verification vulnerabilities and output their locations.
- FR-03: The system SHALL generate a plain-language explanation for each finding.
- FR-04: The system SHALL assign a severity level to each finding.
- FR-05: The system SHALL report detection metrics (precision/recall/F1) on the base paper's 830-instance benchmark.

## 6. Non-functional requirements
- NFR-01: Detection SHOULD beat the base paper's 51.2% Macro-F1 on the same benchmark.
- NFR-02: Explanations SHOULD be understandable by a developer who is not a security expert.
- NFR-03: Analysis of a single contract SHOULD complete in seconds, not minutes.
- NFR-04: No user contract source SHALL be sent to third parties without consent.

## 7. Success criteria
- Detection accuracy (Macro-F1) measurably exceeds 51.2% on the base benchmark.
- The tool correctly flags at least one known real-world vulnerable contract and explains why.
- A working demo: paste a vulnerable contract → tool highlights the bug + explains it, live.

## 8. Constraints
- Student mini-project scope and timeline.
- Uses the base paper's public dataset (830 instances, 786 contract files) and open models.
- Scoped to cross-chain verification vulnerabilities (not all smart-contract bugs).
- Must differ from the base paper by improving detection accuracy and adding explanations.

## 9. Novelty statement (delta vs base paper)
The base paper (Cross-chain Verification Vulnerabilities, 2026) cataloged the
bugs and benchmarked LLMs at 51.2% Macro-F1, but did not build a purpose-trained
detector or provide explanations. This project builds a fine-tuned/purpose-built
detector that beats that bar and explains each finding — a measurable improvement
plus an explainability contribution the base lacks.

> Rule: never invent requirements. Anything unknown stays TODO.
