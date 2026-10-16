Perform a security audit of the project: $ARGUMENTS

Inspect:
1. **Dependencies** — Run `uv run pip audit` or check for known CVEs in uv.lock deps
2. **Secrets exposure** — Scan for hardcoded keys, tokens, passwords in source and config
3. **Input validation** — Check API endpoints in src/deepwatch/api/ for injection, path traversal
4. **File handling** — Verify safe path construction in ingest, report, and data modules
5. **Authentication/Authorization** — Review any auth mechanisms in the API
6. **Serialization** — Check for unsafe pickle/yaml loading
7. **SQL injection** — Review SQLAlchemy queries for raw SQL with user input
8. **CORS/Headers** — Check FastAPI CORS and security header configuration
9. **Environment** — Verify .env.example doesn't contain real secrets, .gitignore covers sensitive files

For each finding:
- Severity: 🔴 Critical / 🟡 Medium / 🔵 Low
- Location (file:line)
- Description and attack scenario
- Recommended remediation

Reference docs/SECURITY_AND_PRIVACY.md for project security requirements.
