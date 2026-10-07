# TECHSPEC.md — Technical Specification

**Status:** Awaiting PRD — TODO throughout; no technology is chosen without justification
**Created:** 2026-10-07
**Role:** concrete technology choices. `ARCHITECTURE.md` owns system shape
(components, data flow, folder structure); this file owns stack details.

## 1. Runtimes & languages
TODO — language, version, package manager. Machine already has: Python 3.14 + uv,
Node 24 + npm, JDK 21, Docker Desktop. Prefer those unless the project needs otherwise.

## 2. Frameworks & key libraries
TODO — name, version, and why for each (one line per choice)

## 3. Build, run, test
TODO — exact commands for dev / build / test / lint, and what "passing" means for each

## 4. Configuration & environment
TODO — env vars (placeholders in `.env.example`, never real secrets), config
files, per-environment differences

## 5. External services & APIs
TODO — provider, purpose, auth method, cost/limits, offline fallback

## 6. Error handling & logging
TODO — strategy, log format, what is never logged (secrets, PII)

## 7. Performance targets
TODO — only if the PRD demands them

## 8. Key technical decisions

| Decision | Why | Date |
| --- | --- | --- |
| (none yet) | | |

> Rule: every choice needs a why. Never invent capabilities a library doesn't have.
