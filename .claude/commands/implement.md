Implement the approved plan: $ARGUMENTS

Rules:
1. Work in small, atomic changes — one logical unit per step
2. After each change: run `uv run ruff check src/ tests/` and fix issues
3. After modifying any module: run relevant tests with `uv run pytest tests/ -v --tb=short`
4. Never skip error handling or input validation
5. Add or update tests for every new function or changed behavior
6. Use type hints on all public functions
7. Follow the existing code patterns in src/deepwatch/
8. Update docs/MEMORY.md with what was implemented and any decisions made

After completing all changes, provide a summary:
- Files created/modified
- Tests added/updated and their results
- Any remaining TODOs or follow-up items
