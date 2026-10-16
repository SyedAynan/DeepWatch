# DeepWatch

Unified multimodal deepfake forensics and generation-method attribution platform.

## Quick Reference

- **Stack**: Python 3.11 · PyTorch · FastAPI · SQLAlchemy · timm
- **Package manager**: uv (run all commands via `uv run`)
- **Source**: `src/deepwatch/` · **Tests**: `tests/`
- **Docs**: `docs/` (19 files — read PRD.md → ARCHITECTURE.md → TECHSPEC.md first)

## Commands

```bash
uv sync --dev              # Install/sync all dependencies
uv run ruff check src/     # Lint
uv run ruff format src/    # Format
uv run pyright src/        # Type check
uv run pytest tests/ -v    # Run tests
uv run pytest tests/ --cov=deepwatch  # Tests + coverage
uv run pre-commit install  # Install git hooks
uv run pre-commit run -a   # Run all pre-commit checks
uv run python scripts/health_report.py  # Project health
```

## Claude Code Commands

| Command | Purpose |
|---|---|
| `/project:plan <task>` | Analyze requirements, produce implementation plan |
| `/project:implement <plan>` | Execute approved plan with validation |
| `/project:review [files]` | Code review for correctness, security, tests |
| `/project:test [pattern]` | Run tests, diagnose failures, report coverage |
| `/project:security-audit` | Dependencies, secrets, input validation scan |
| `/project:research-papers <topic>` | Literature review with verified citations |
| `/project:experiment <name>` | Reproducible experiment with metrics |
| `/project:release [version]` | Pre-release checklist and changelog |

## Rules

1. **Read before write** — inspect relevant source and docs before modifying
2. **Small changes** — one logical unit per commit
3. **Verify** — run lint + tests after every change; never claim green if red
4. **No fabrication** — mark unknowns as `TODO`, never invent project state
5. **Docs stay current** — update `docs/MEMORY.md` after meaningful work
6. **Source of truth**: working code > tests > PRD > ARCHITECTURE > RULES > PHASES

## Workflow (before coding tasks)

Read in order: `docs/PRD.md` → `docs/RESEARCH_REVIEW.md` → `docs/ARCHITECTURE.md`
→ `docs/TECHSPEC.md` → `docs/PHASES.md` → `docs/MEMORY.md`

Work only the current phase unless explicitly told otherwise.
