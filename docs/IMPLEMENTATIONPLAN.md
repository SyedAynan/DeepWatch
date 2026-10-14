# IMPLEMENTATIONPLAN.md — Implementation Plan

**Status:** Phase 1 planned (engineering scaffold — does not depend on the PRD);
Phases 2+ await the PRD
**Created:** 2026-10-07
**Updated:** 2026-10-14
**Role:** detailed task breakdown. `PHASES.md` holds the roadmap and phase
status; `TRACKER.md` holds live per-task progress. Update the tracker, not this
file, as tasks complete.

## Phase 1 — Runnable scaffold

**Objective:** a minimal app skeleton that serves in a browser and passes a
runnable test command, with all tooling configured. No product features.
**Depends on:** — (engineering-only; does not require the PRD)

| # | Task | Files (expected) | Acceptance / verification |
| --- | --- | --- | --- |
| 1.1 | npm init: package.json, `engines` ≥ 20, ES modules, npm scripts | `package.json` | `npm run dev` script exists |
| 1.2 | Static dev server + entry page | `index.html`, `src/main.js`, dev-server script | Page loads at localhost with no console errors |
| 1.3 | ESLint flat config | `eslint.config.js` | `npm run lint` exits 0 |
| 1.4 | Playwright setup + smoke spec | `playwright.config.js`, `tests/e2e/smoke.spec.js` | `npm test` passes headless |
| 1.5 | WebGL2 capability check + error surface | `src/sim/capabilities.js`, UI error element | Unsupported browser shows a readable message |
| 1.6 | CI runs lint + tests | `.github/workflows/ci.yml` | CI green on a push |

## Phase 2 — Vision pipeline (TODO — name/details pending PRD)

**Objective:** TODO
**Depends on:** Phase 1

| # | Task | Files (expected) | Acceptance / verification |
| --- | --- | --- | --- |
| 2.1 | TODO | TODO | TODO |

> Every task needs a verifiable acceptance step; a task without one is not ready
> to be worked. Phases beyond what the PRD justifies stay TODO.
