# MEMORY.md — Project State

**Last updated:** 2026-10-14
**Current phase:** 0 — project definition (IN PROGRESS)
**Current task:** user supplies the project title, IEEE base paper + picks direction D1–D3
(see docs/RESEARCH.md and docs/REQUIREMENTS.md)

## Completed
- 2026-10-14: pre-development workspace audit. Added `.env.example` (config
  placeholder) and `docs/REQUIREMENTS.md` (single list of inputs the project is
  waiting on: title, IEEE base paper, direction pick). Corrected the README
  performance table to mark benchmarks as planned targets, not measured results
  (no code exists yet). Linked REQUIREMENTS.md from README and CLAUDE.md.
  LICENSE verified (MIT, 2026 Syed Ayan); CI already passes as a docs check.
- 2026-10-10: upgraded GitHub repository showcase — created custom cyber neon header banner (`assets/banner.png`), wrote comprehensive showcase `README.md` with interactive architecture diagrams and technology badges, and added full GitHub open-source scaffolding (`LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `.github/workflows/ci.yml`, issue/PR templates).
- 2026-10-10: recorded the user-selected technology stack in README,
  ARCHITECTURE, and TECHSPEC. Git and GitHub are already in use; application
  technologies are selected but not yet implemented or configured.
- 2026-10-07: repository scaffolded — `docs/` context system (PRD, ARCHITECTURE,
  RULES, PHASES, DESIGN, MEMORY), README, .gitignore, `CLAUDE.md`; git initialized
  with the scaffold commit (8552ed9).
- 2026-10-07: doc set extended — TECHSPEC, APPFLOW, SCHEMA, IMPLEMENTATIONPLAN,
  TRACKER templates (commit 21dd84d).
- 2026-10-07: novelty/landscape scan → `docs/RESEARCH.md`: current publishing
  trends (arXiv eess.SP/cs.LG/cs.AI, 2026-10-07), saturated areas to avoid,
  self-repetition guard vs the previous Patient Monitoring Mesh project, and
  candidate directions D1–D3 (D1 uncertainty-aware edge triage with clinician
  deferral; D2 LLM explanation layer with fidelity metrics; D3 label-efficient
  personalization under drift). No code, no stack chosen, nothing invented.

## Important decisions
- Docs-first workflow (see `CLAUDE.md`, `docs/RULES.md`).
- Selected stack: JavaScript, HTML5 & CSS3, MediaPipe Hand Landmarker, WebGL2,
  GPU Particle Rendering, WebGL Transform Feedback, Computer Vision, Node.js,
  Playwright, and Git & GitHub. Product requirements remain TODO.

## Known issues / blockers
- None. "Project undefined" is the current state, not a problem.

## Tests / results
- None applicable yet (no code).

## Next recommended step
Provide the IEEE base paper and choose D1/D2/D3 (docs/RESEARCH.md), then:
fill `docs/PRD.md` → verify novelty on IEEE Xplore → plan Phase 1 using the selected stack.
