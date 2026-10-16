"""DeepWatch Project Health Report

Aggregates lint, type-check, test, coverage, and TODO metrics
into a JSON summary and readable Markdown report.

Usage: uv run python scripts/health_report.py
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"
TESTS_DIR = PROJECT_ROOT / "tests"


def run_cmd(args: list[str], cwd: Path | None = None) -> tuple[int, str, str]:
    """Run a command and return (returncode, stdout, stderr)."""
    result = subprocess.run(
        args,
        cwd=cwd or PROJECT_ROOT,
        capture_output=True,
        text=True,
        timeout=120,
    )
    return result.returncode, result.stdout, result.stderr


def count_todos() -> dict:
    """Count TODO/FIXME/HACK/XXX in source files."""
    patterns = {"TODO": 0, "FIXME": 0, "HACK": 0, "XXX": 0}
    for root, _, files in os.walk(SRC_DIR):
        for fname in files:
            if not fname.endswith(".py"):
                continue
            fpath = Path(root) / fname
            content = fpath.read_text(encoding="utf-8", errors="ignore")
            for tag in patterns:
                patterns[tag] += len(re.findall(rf"\b{tag}\b", content))
    return patterns


def check_lint() -> dict:
    """Run ruff check and count errors."""
    code, stdout, stderr = run_cmd(["uv", "run", "ruff", "check", "src/", "tests/", "--output-format=json"])
    try:
        issues = json.loads(stdout) if stdout.strip() else []
    except json.JSONDecodeError:
        issues = []
    return {
        "passed": code == 0,
        "error_count": len(issues),
        "errors": [{"file": i.get("filename", ""), "code": i.get("code", ""), "message": i.get("message", "")} for i in issues[:10]],
    }


def check_typecheck() -> dict:
    """Run pyright and extract summary."""
    code, stdout, stderr = run_cmd(["uv", "run", "pyright", "src/", "--outputjson"])
    try:
        data = json.loads(stdout) if stdout.strip() else {}
        summary = data.get("summary", {})
        return {
            "passed": code == 0,
            "errors": summary.get("errorCount", -1),
            "warnings": summary.get("warningCount", -1),
            "informations": summary.get("informationCount", -1),
        }
    except json.JSONDecodeError:
        return {"passed": code == 0, "errors": -1, "warnings": -1, "informations": -1}


def check_tests() -> dict:
    """Run pytest and extract results."""
    code, stdout, stderr = run_cmd([
        "uv", "run", "pytest", "tests/", "-v", "--tb=short",
        "--cov=deepwatch", "--cov-report=json:coverage.json",
        "-q",
    ])
    # Parse pytest output for pass/fail counts
    result = {"passed": code == 0, "test_passed": 0, "test_failed": 0, "test_errors": 0, "coverage_pct": None}

    for line in (stdout + stderr).splitlines():
        m = re.search(r"(\d+) passed", line)
        if m:
            result["test_passed"] = int(m.group(1))
        m = re.search(r"(\d+) failed", line)
        if m:
            result["test_failed"] = int(m.group(1))
        m = re.search(r"(\d+) error", line)
        if m:
            result["test_errors"] = int(m.group(1))

    # Read coverage JSON if available
    cov_file = PROJECT_ROOT / "coverage.json"
    if cov_file.exists():
        try:
            cov_data = json.loads(cov_file.read_text())
            result["coverage_pct"] = round(cov_data.get("totals", {}).get("percent_covered", 0), 1)
        except (json.JSONDecodeError, KeyError):
            pass

    return result


def count_source_stats() -> dict:
    """Count Python files and lines in src/."""
    files = 0
    lines = 0
    for root, _, filenames in os.walk(SRC_DIR):
        for fname in filenames:
            if fname.endswith(".py"):
                files += 1
                lines += len((Path(root) / fname).read_text(encoding="utf-8", errors="ignore").splitlines())
    return {"python_files": files, "python_lines": lines}


def generate_report() -> dict:
    """Generate the full health report."""
    print("🔍 Running lint check...")
    lint = check_lint()

    print("🔬 Running type check...")
    typecheck = check_typecheck()

    print("🧪 Running tests...")
    tests = check_tests()

    print("📊 Counting source stats...")
    source = count_source_stats()
    todos = count_todos()

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "project": "DeepWatch",
        "source": source,
        "todos": todos,
        "lint": lint,
        "typecheck": typecheck,
        "tests": tests,
    }

    # Compute overall health
    checks = [lint["passed"], tests["passed"]]
    report["overall_healthy"] = all(checks)
    report["checks_passed"] = sum(1 for c in checks if c)
    report["checks_total"] = len(checks)

    return report


def render_markdown(report: dict) -> str:
    """Render the report as Markdown."""
    lines = [
        "# 📊 DeepWatch Health Report",
        "",
        f"> Generated: {report['timestamp']}",
        "",
        "## Overall Status",
        "",
        f"**{'✅ HEALTHY' if report['overall_healthy'] else '⚠️ ISSUES FOUND'}** "
        f"({report['checks_passed']}/{report['checks_total']} checks passed)",
        "",
        "## Source",
        "",
        f"| Metric | Value |",
        f"|---|---|",
        f"| Python files | {report['source']['python_files']} |",
        f"| Python lines | {report['source']['python_lines']:,} |",
        f"| TODOs | {report['todos'].get('TODO', 0)} |",
        f"| FIXMEs | {report['todos'].get('FIXME', 0)} |",
        "",
        "## Lint (Ruff)",
        "",
        f"{'✅ Clean' if report['lint']['passed'] else f\"⚠️ {report['lint']['error_count']} issues\"}",
        "",
        "## Type Check (Pyright)",
        "",
        f"{'✅ Clean' if report['typecheck']['passed'] else f\"⚠️ {report['typecheck']['errors']} errors, {report['typecheck']['warnings']} warnings\"}",
        "",
        "## Tests",
        "",
        f"| Metric | Value |",
        f"|---|---|",
        f"| Passed | {report['tests']['test_passed']} |",
        f"| Failed | {report['tests']['test_failed']} |",
        f"| Errors | {report['tests']['test_errors']} |",
        f"| Coverage | {report['tests']['coverage_pct']}% |" if report['tests']['coverage_pct'] is not None else "| Coverage | N/A |",
        "",
    ]
    return "\n".join(lines)


def main():
    report = generate_report()

    # Write JSON
    json_path = PROJECT_ROOT / "health_report.json"
    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    # Write Markdown
    md_path = PROJECT_ROOT / "HEALTH.md"
    md_path.write_text(render_markdown(report), encoding="utf-8")

    # Print summary
    print("\n" + render_markdown(report))
    print(f"\n📄 JSON report: {json_path}")
    print(f"📄 Markdown report: {md_path}")

    sys.exit(0 if report["overall_healthy"] else 1)


if __name__ == "__main__":
    main()
