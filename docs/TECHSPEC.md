# TECHSPEC.md — Technical Specification

**Status:** Technology stack selected; implementation and version choices pending
**Created:** 2026-10-07
**Role:** concrete technology choices. `ARCHITECTURE.md` owns system shape
(components, data flow, folder structure); this file owns stack details.

## 1. Runtimes & languages
- **JavaScript:** application language for browser logic and Node.js tooling.
- **HTML5 & CSS3:** document structure and visual styling.
- **Node.js:** runtime for development scripts and test tooling.

Machine tooling previously recorded: Node 24 + npm. Project runtime constraints,
JavaScript target, and package-manager configuration remain TODO.

## 2. Frameworks & key libraries
The user selected the following technologies. These are planned roles;
no application code or dependency configuration exists yet.

| Technology | Planned role / reason |
| --- | --- |
| MediaPipe Hand Landmarker | Detect hand landmarks for hand-based interaction |
| WebGL2 | Provide browser GPU graphics and transform feedback support |
| GPU Particle Rendering | Render particle visuals with GPU acceleration |
| WebGL Transform Feedback | Capture shader outputs into buffers to update particle state on the GPU |
| Computer Vision | Interpret visual input using detected hand landmarks |
| Playwright | Automate browser tests for implemented user flows |

GPU Particle Rendering and Computer Vision describe techniques or domains, not
separate packages. Dependency versions, model assets, browser support, and
integration details remain TODO.

## 3. Build, run, test
TODO — exact commands for dev / build / test / lint, and what "passing" means for each

Use Node.js for development tooling and Playwright for browser tests. Commands
will be recorded when the runnable scaffold is implemented.

## 4. Configuration & environment
TODO — env vars (placeholders in `.env.example`, never real secrets), config
files, per-environment differences

## 5. External services & APIs
TODO — provider, purpose, auth method, cost/limits, offline fallback

**Git & GitHub:** Git tracks changes; GitHub hosts the private repository at
https://github.com/SyedAynan/amber-orbit-7c4f9a. These are already in use.

## 6. Error handling & logging
TODO — strategy, log format, what is never logged (secrets, PII)

## 7. Performance targets
TODO — only if the PRD demands them

## 8. Key technical decisions

| Decision | Why | Date |
| --- | --- | --- |
| Adopt the user-selected stack listed above | Explicit project technology requirement; implementation awaits the PRD | 2026-10-10 |

> Rule: every choice needs a why. Never invent capabilities a library doesn't have.
