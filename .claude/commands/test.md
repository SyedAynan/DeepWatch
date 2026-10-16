Run the test suite and diagnose any failures: $ARGUMENTS

Steps:
1. Run: `uv run pytest tests/ -v --tb=long`
2. If specific test file or pattern given, run that instead
3. For each failure:
   a. Read the failing test to understand intent
   b. Read the source code being tested
   c. Identify root cause (bug in code vs. bug in test vs. missing fixture)
   d. Propose a fix with rationale
4. After fixing, re-run to confirm the fix works
5. Run `uv run pytest tests/ -v --cov=deepwatch --cov-report=term-missing` for coverage

Report:
- Total pass/fail/skip counts
- Coverage percentage
- Any tests that are fragile or slow (>2s)
- Recommendations for missing test coverage
