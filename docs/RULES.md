# RULES.md — AI Coding Rules

**Created:** 2026-10-07

## Conventions
- Follow existing project conventions (set per stack once chosen; until then, TODO).
- TODO: naming, exports, formatting rules once the stack is picked.

## Reuse & scope
- Reuse existing components/utilities before creating new ones.
- Do not unnecessarily rewrite working code.
- Do not add dependencies without justification.
- Keep changes focused.
- Ask before making major architectural changes.

## Honesty
- Never fabricate APIs, files, functions, credentials, or requirements.
- Never hide errors just to make tests pass.
- Never claim something works unless verified.
- Update `docs/MEMORY.md` after meaningful implementation work.

## Process
- Inspect existing code before modifying it.
- Handle errors properly; validate at boundaries.
- Run appropriate tests/type checks/linting after changes.
- Preserve backward compatibility unless explicitly instructed otherwise.

## Security
- Follow security and privacy best practices.
- Never commit secrets; `.env` stays local, `.env.example` carries placeholders only.
