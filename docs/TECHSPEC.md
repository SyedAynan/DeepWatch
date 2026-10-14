# TECHSPEC.md — Technical Specification

**Status:** Stack and tooling decisions recorded; dependency versions pinned at scaffold time
**Created:** 2026-10-07
**Updated:** 2026-10-14
**Role:** concrete technology choices. `ARCHITECTURE.md` owns system shape
(components, data flow, folder structure); this file owns stack details.

## 1. Runtimes & languages
- **JavaScript (ES2022+, ES modules):** application language for browser logic and
  Node.js tooling. `"type": "module"` in package.json; `.js` files only — no
  TypeScript (keep the mini-project build-free).
- **HTML5 & CSS3:** document structure and visual styling.
- **Node.js:** development tooling and test runner. Local machine has Node 24;
  CI runs Node 20. **Project baseline: Node ≥ 20** (`engines` field).

Package manager: **npm** (ships with Node; no extra tooling needed).
Browser target: **WebGL2-capable evergreen browsers** (Chrome/Edge/Firefox;
WebGL2 is required for transform feedback — no WebGL1 fallback planned).

## 2. Frameworks & key libraries
The user selected the following technologies. Planned roles:

| Technology | Planned role / reason |
| --- | --- |
| MediaPipe Hand Landmarker (`@mediapipe/tasks-vision`) | Detect 21 hand landmarks per hand for interaction |
| WebGL2 | Browser GPU graphics API; required for transform feedback |
| GPU Particle Rendering | Technique: particle state updated in vertex shaders |
| WebGL Transform Feedback | Capture vertex shader outputs back into VBOs (GPU-only particle updates) |
| Computer Vision | Domain: interpreting hand landmarks as control signals |
| Playwright (`@playwright/test`) | Headless browser E2E tests and frame-latency checks |

GPU Particle Rendering and Computer Vision are techniques/domains, not packages.
Exact dependency versions are pinned in `package.json` at scaffold time (Phase 1).
MediaPipe model assets are loaded from CDN or vendored — decide in Phase 1.

## 3. Build, run, test
**No build step.** Static HTML/CSS/JS served by a dev server (`npx serve` or a
tiny Node static server script). Planned npm scripts:

| Command | Purpose | Passing means |
| --- | --- | --- |
| `npm run dev` | Serve the app locally | App reachable on localhost |
| `npm test` | Run Playwright E2E suite | All specs pass headless |
| `npm run lint` | Lint JS (ESLint, flat config) | Zero errors |

Commands are recorded as they are implemented in Phase 1.

## 4. Configuration & environment
Placeholders live in `.env.example`; real values go in `.env` (git-ignored).
The browser app itself is expected to be config-free; env vars would only serve
tooling (ports, model asset paths). Per-environment differences: TODO if any arise.

## 5. External services & APIs
- **Git & GitHub:** version control and hosting (private repo at
  https://github.com/SyedAynan/Mini-Project). Already in use.
- **MediaPipe model CDN:** serves the hand-landmarker model weights. No auth.
  Offline fallback: vendor the model file into `public/models/` — decide in Phase 1.
- No other external services planned.

## 6. Error handling & logging
TODO — decided with the PRD. Baseline rule: never log secrets or raw camera
frames; camera/permission failures must surface as user-visible messages, not
console-only errors.

## 7. Performance targets
Planned targets (from README, unverified until implementation):
≥ 60 FPS with 100,000 particles, < 15 ms landmark latency, < 100 MB VRAM,
< 10% CPU. Playwright frame-latency checks enforce these once built.

## 8. Key technical decisions

| Decision | Why | Date |
| --- | --- | --- |
| Adopt the user-selected stack listed above | Explicit project technology requirement; implementation awaits the PRD | 2026-10-10 |
| Plain JS + ES modules, no TypeScript/build step | Mini-project scope; browser-native modules remove toolchain complexity | 2026-10-14 |
| npm (not pnpm/yarn/uv) | Ships with Node; one less tool to install | 2026-10-14 |
| Node ≥ 20 baseline | Matches CI runner; local Node 24 is forward-compatible | 2026-10-14 |
| Playwright over Cypress/Puppeteer | User-selected; first-class headless Chromium + frame timing APIs | 2026-10-14 |

> Rule: every choice needs a why. Never invent capabilities a library doesn't have.
