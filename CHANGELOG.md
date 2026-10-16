# Changelog

All notable changes to DeepWatch will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### ✨ Added
- VS Code workspace configuration (settings, tasks, launch configs, recommended extensions)
- Pre-commit hooks (ruff lint/format, trailing whitespace, secret detection, gitleaks)
- Claude Code custom commands: `/plan`, `/implement`, `/review`, `/test`, `/security-audit`, `/research-papers`, `/experiment`, `/release`
- Pyright type checking configuration
- Coverage reporting configuration (pytest-cov)
- Project health report script
- GitHub Actions CI workflow with full Python quality gates
- CHANGELOG.md

### 🔧 Changed
- Improved `CLAUDE.md` with concise quick-reference format and command table
- Updated `pyproject.toml` with ruff lint rules, pyright config, coverage config
- Updated `.gitignore` to track `.vscode/` workspace configs selectively
- VS Code tasks now use `uv run` (correct for uv-managed venvs)

## [0.1.0] - 2026-10-14

### ✨ Added
- Initial project scaffold with research-driven documentation
- Multimodal deepfake detection architecture (12 subpackages)
- Dataset manifest loader and 84-paper literature comparison
- Forensic media ingest pipeline
- FastAPI application structure
- Basic CI workflow
- Research documentation suite (PRD, ARCHITECTURE, TECHSPEC, etc.)
