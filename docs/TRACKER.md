# TRACKER.md — Task Tracker

**Status:** Phase 1 tasks defined (from `IMPLEMENTATIONPLAN.md`); none started
**Created:** 2026-10-07
**Updated:** 2026-10-14

## Legend
- [ ] not started · [~] in progress · [x] done (add date) · [!] blocked (add note)

## Current task
None. Phase 1 is planned but not yet started — see `docs/REQUIREMENTS.md` for
the external inputs (title, base paper, direction pick) the user may supply
first, though Phase 1 itself is engineering-only and can start without them.

## Phase 1 — Runnable scaffold
- [ ] 1.1 npm init: package.json, engines ≥ 20, ES modules, npm scripts
- [ ] 1.2 Static dev server + entry page loads with no console errors
- [ ] 1.3 ESLint flat config, `npm run lint` exits 0
- [ ] 1.4 Playwright setup + smoke spec, `npm test` passes headless
- [ ] 1.5 WebGL2 capability check + user-visible error on unsupported browsers
- [ ] 1.6 CI runs lint + tests and is green

## Blockers / notes
None for Phase 1. Phases 2+ are blocked on the PRD (see `docs/REQUIREMENTS.md`).

> Keep entries one line; explanations and outcomes belong in `MEMORY.md`.
