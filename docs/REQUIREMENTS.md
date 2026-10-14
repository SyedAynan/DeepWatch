# REQUIREMENTS.md — What Must Be Supplied Before Phase 1

**Status:** OPEN — project cannot start until every item below is resolved
**Created:** 2026-10-14
**Role:** single, obvious list of external inputs this project is waiting on.
Everything here is a decision only the user can make — never invent answers.

## Required inputs

| # | Item | Why it's needed | Where it goes once supplied | Status |
| --- | --- | --- | --- | --- |
| 1 | **Project title** | Identity for README, PRD, repo description, all docs | README.md, docs/PRD.md, docs/MEMORY.md | TODO |
| 2 | **IEEE base paper** | Anchor for novelty positioning and literature grounding | docs/RESEARCH.md, docs/PRD.md | TODO |
| 3 | **Direction pick (D1 / D2 / D3 or new)** | Determines what the PRD specifies; see docs/RESEARCH.md | docs/PRD.md, docs/PHASES.md | TODO |

## Blocked until resolved

- `docs/PRD.md` — problem statement, users, goals/non-goals, FRs/NFRs, success criteria
- `docs/APPFLOW.md`, `docs/SCHEMA.md`, `docs/IMPLEMENTATIONPLAN.md` — all marked "Awaiting PRD"
- Phase 1 scaffold (code skeleton, package.json, tooling) — cannot pick shape before the PRD

## Notes

- The currently selected stack (JavaScript, HTML5/CSS3, MediaPipe Hand Landmarker,
  WebGL2, Transform Feedback, Node.js, Playwright) is recorded in
  `docs/ARCHITECTURE.md` and `docs/TECHSPEC.md` and assumed stable unless the
  direction pick changes it.
- Once items 1–3 are supplied, this file should be marked CLOSED and the PRD
  filled in a single pass.
