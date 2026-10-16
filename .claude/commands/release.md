Prepare a release: $ARGUMENTS

Checklist:
1. Run full quality suite: `uv run ruff check src/ tests/ && uv run pyright src/ && uv run pytest tests/ -v --cov=deepwatch`
2. Verify all tests pass and no lint errors
3. Check for uncommitted changes: `git status`
4. Review git log since last tag: `git log --oneline $(git describe --tags --abbrev=0 2>/dev/null || echo HEAD~10)..HEAD`
5. Update version in pyproject.toml if needed
6. Update CHANGELOG.md with categorized changes:
   - ✨ Features
   - 🐛 Bug Fixes
   - 🔒 Security
   - 📚 Documentation
   - ⚡ Performance
   - 🔧 Internal
7. Verify docs/MEMORY.md is current
8. Verify docs/TRACKER.md reflects completed work
9. Run `uv build` to verify the package builds clean
10. Summarize what's in this release and any known issues

Do NOT push, tag, or publish without explicit approval.
