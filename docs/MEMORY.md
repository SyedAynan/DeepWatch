# MEMORY.md — Project State

**Last updated:** 2026-10-10
**Current phase:** 0 — project definition (IN PROGRESS)
**Current task:** user supplies the IEEE base paper + picks direction D1–D3 (see docs/RESEARCH.md)

## Completed
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
