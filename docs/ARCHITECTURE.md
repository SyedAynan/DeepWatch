# ARCHITECTURE.md — Mini Project

**Status:** Stack + engineering shape recorded; product-level boundaries await the PRD
**Created:** 2026-10-07
**Updated:** 2026-10-14

## 1. System overview
A browser-based computer-vision application: webcam input is processed by
MediaPipe Hand Landmarker to produce hand landmark coordinates; those landmarks
drive a WebGL2 transform-feedback particle simulation rendered to a full-screen
canvas. All particle physics run on the GPU; the CPU only handles vision input
and uniform uploads. Exact product features and behaviors await `docs/PRD.md`.

## 2. Technology stack
Selected by the user: JavaScript, HTML5 & CSS3, MediaPipe Hand Landmarker,
WebGL2, GPU Particle Rendering, WebGL Transform Feedback, Computer Vision,
Node.js, Playwright, and Git & GitHub.

Existing machine tooling remains recorded: Python 3.14 + uv, Node 24 + npm,
Next.js 16 / React 19 experience, Docker Desktop, and JDK 21.

Version/runtime decisions are in `TECHSPEC.md`.

## 3. Data model / storage
No persistent storage. Runtime state only: landmark arrays (per frame),
particle VBO buffers (GPU), and uniform values. Detailed shapes in `SCHEMA.md`
(awaiting PRD for product entities).

## 4. API / interfaces
No backend. Internal module interfaces (planned):
- **Vision module** → exposes per-frame landmark data to the app loop
- **Simulation module** → accepts landmarks as shader uniforms, owns VBO state
- **Render module** → draws the current particle buffer each frame

Exact function signatures are defined when the modules are implemented (Phase 1+).

## 5. Folder structure
Planned scaffold (created in Phase 1):

```
├── index.html              # entry point
├── src/
│   ├── main.js             # app loop & wiring
│   ├── vision/             # MediaPipe hand tracking
│   ├── sim/                # WebGL2 transform feedback particle sim
│   ├── render/             # draw pass & shaders wiring
│   └── ui/                 # DOM overlays (status, errors, controls)
├── public/
│   ├── shaders/            # .glsl files (update + draw)
│   └── models/             # vendored MediaPipe model (if not CDN)
├── tests/e2e/              # Playwright specs
├── docs/                   # this documentation system
├── assets/                 # repo branding (banner, screenshots)
└── package.json
```

## 6. External services & dependencies
- MediaPipe model CDN (or vendored model) — hand landmarker weights; no auth.
- GitHub — repo hosting and CI. Already in use.
- No backend, database, or paid services planned.

## 7. Security considerations
- Camera access requires a secure context (https or localhost) and explicit
  user permission; denial must be handled gracefully.
- No raw camera frames leave the device; only derived landmark coordinates are
  used in-process.
- No secrets in the repo; `.env` is git-ignored.

## 8. Scalability considerations
Client-side only; scalability is per-device GPU capacity. Particle count will be
adaptive (drop to fewer particles on weak GPUs) — confirm against PRD targets.

## 9. Key decisions and why

| Decision | Why | Date |
| --- | --- | --- |
| Docs-first context system | project stays understandable across chats, sessions, and AI tools | 2026-10-07 |
| No backend / static-only hosting | CV + GPU sim run entirely client-side; zero infra cost | 2026-10-14 |
| GPU-only particle updates via transform feedback | CPU particle loops bottleneck ~5k particles; VBO ping-pong scales to 100k+ | 2026-10-14 |
