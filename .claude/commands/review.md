Review the current diff or specified changes: $ARGUMENTS

Check for:
1. **Correctness** — Logic errors, off-by-one, null/None handling, edge cases
2. **Security** — Injection, path traversal, unsafe deserialization, hardcoded secrets
3. **Maintainability** — Naming, complexity, duplication, separation of concerns
4. **Type safety** — Missing type hints, incorrect types, Any abuse
5. **Tests** — Are new/changed behaviors tested? Are tests meaningful (not just coverage)?
6. **Regressions** — Could this break existing functionality? Check related tests
7. **Documentation** — Are docstrings updated? Do docs match the code?
8. **Performance** — Unnecessary allocations, N+1 queries, blocking I/O in async paths

For each finding, state:
- Severity: 🔴 Critical / 🟡 Warning / 🔵 Suggestion
- File and line
- What's wrong and why
- Recommended fix

Run `uv run ruff check src/ tests/` and `uv run pytest tests/ -v` to verify current state.
