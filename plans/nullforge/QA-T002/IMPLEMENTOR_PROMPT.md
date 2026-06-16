# QA-T002 Implementor Prompt

You are Codex working in `C:\Users\Filip\Desktop\Repos\research-core`.

Task: implement `QA-T002` only. Do not commit.

## Context

- `QA-T002` planner artifacts exist under `plans/nullforge/QA-T002/`.
- `QA-T001` and `HY-T001` have audit `PASS`.
- `QA-T001` found a local Python environment and CLI/runtime blocker:
  - `python -m pip show research-core` reported editable install provenance from `<local-temp-editable-install>`, not this workspace.
  - `python -m research_core.cli --help` failed with `No module named research_core.cli`.
  - `python -m research_core --help` failed because `research_core` has no `__main__`.
  - `research-core --help` was not recognized.
- `pyproject.toml` is the package metadata source.
- `src/research_core/cli.py` exists.
- No console script is declared in `pyproject.toml`.
- `src/research_core/__main__.py` is absent in current planning context.
- No NullForge implementation code has started.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, package changes, dependency changes, install commands, test creation, schema creation, fixture creation, or downstream work.

## Read First

- `plans/nullforge/QA-T002/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T002/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/QA-T002/PLAN.md`
- `plans/nullforge/QA-T002/ACCEPTANCE.md`
- `plans/nullforge/QA-T002/IMPLEMENTOR_PROMPT.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`
- `reports/nullforge/QA-T001/TEST_RESULTS.md`
- `audits/nullforge/HY-T001/AUDIT_REPORT.md`
- `reports/nullforge/HY-T001/TEST_RESULTS.md`
- `pyproject.toml`
- `docs/how-to/run_ci_locally.md`
- `docs/reference/cli/overview.md`
- `src/research_core/cli.py`

## Allowed Files

- `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/QA-T002/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T002/CHANGED_FILES.md`
- `reports/nullforge/QA-T002/TEST_RESULTS.md`
- `reports/nullforge/QA-T002/AUDITOR_PROMPT.md`

## Treat As Read-Only

- `plans/nullforge/QA-T002/*`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- all prior plans, reports, and audits
- `pyproject.toml`
- `requirements-docs.txt`
- `README.md`
- `.github/`
- `docs/` except the allowed NullForge status/source-index/QA triage files
- `tools/`
- `src/`
- `tests/`
- `schemas/`
- `fixtures/`
- package files
- generated docs
- ResearchCore Engine docs/code

## Forbidden

- Do not create audits for QA-T002.
- Do not create tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, or downstream artifacts.
- Do not modify ResearchCore Engine docs/code.
- Do not modify `pyproject.toml`, source files, tests, schemas, fixtures, CI, generated docs, README, dependencies, or package metadata.
- Do not run install, uninstall, editable install, dependency sync, package build, or environment repair commands.
- Do not run full test commands, docs generation, docs build, quickstart commands, or CI smoke commands.
- Do not run `python -m pytest`, `python -m pytest -q`, `pytest -q`, `python tools/docs/gen_cli_ref.py`, `python tools/docs/gen_schema_ref.py`, `python tools/docs/gen_artifact_catalog.py`, `python tools/docs/verify_generated_docs_clean.py`, `python -m mkdocs build`, `pip install`, `python -m pip install`, or `python -m research_core.cli ci run --config .github/ci/ci.github.json`.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

## Required Work

1. Verify current status and `QA-T001` / `HY-T001` audit `PASS`.
2. Run only bounded read-only diagnostics listed below.
3. Create `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`.
4. Update `docs/nullforge/CURRENT_STATUS.md` only if needed for QA-T002 in-progress/readiness state while preserving `No NullForge implementation code has started.` and `REPO_SOURCE_IMPORT_BASELINE`.
5. Update `docs/nullforge/SOURCE_INDEX.md` only if needed to link the QA-T002 triage doc and report artifacts after creation.
6. Create QA-T002 implementation reports:
   - `reports/nullforge/QA-T002/IMPLEMENTATION_REPORT.md`
   - `reports/nullforge/QA-T002/CHANGED_FILES.md`
   - `reports/nullforge/QA-T002/TEST_RESULTS.md`
   - `reports/nullforge/QA-T002/AUDITOR_PROMPT.md`
7. Run and record required bounded checks.

## Allowed Read-Only Diagnostics

Use `python -B` for Python diagnostics to avoid bytecode/cache writes where practical.

Allowed:

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `Test-Path -LiteralPath pyproject.toml`
- `Test-Path -LiteralPath src\research_core\cli.py`
- `Test-Path -LiteralPath src\research_core\__main__.py`
- `Test-Path -LiteralPath package.json`
- `Test-Path -LiteralPath pnpm-workspace.yaml`
- `Test-Path -LiteralPath pnpm-lock.yaml`
- `rg -n "\[project\.scripts\]|console_scripts|package-dir|pythonpath|typer|def main|if __name__ == \"__main__\"" pyproject.toml src\research_core\cli.py`
- `python -B -m pip show research-core`
- `python -B -c "import sys; print('executable=' + sys.executable); print('prefix=' + sys.prefix); print('base_prefix=' + sys.base_prefix); print('path0=' + (sys.path[0] if sys.path else ''))"`
- `python -B -c "import importlib.util; print('research_core=' + str(importlib.util.find_spec('research_core'))); print('research_core.cli=' + str(importlib.util.find_spec('research_core.cli')))"`
- `python -B -m research_core.cli --help`
- `python -B -m research_core --help`
- `research-core --help`

If any command would require install, repair, or environment mutation, skip it and record the human gate.

## Triage Doc Requirements

`docs/nullforge/qa/ENVIRONMENT_TRIAGE.md` must include:

- Ticket ID `QA-T002`.
- Purpose and non-goals.
- `QA-T001` and `HY-T001` audit `PASS` evidence.
- Inherited blocker summary from `QA-T001`.
- Package/source facts from `pyproject.toml` and `src/research_core/cli.py`.
- Current observed local package/module/CLI visibility from diagnostics.
- Explicit distinction between source facts, environment observations, expected unsupported commands, and unresolved blockers.
- Side-effect review for `.pytest_cache/`, `__pycache__/`, `exec_outputs/`, docs build output, generated docs, source, package, tests, schemas, fixtures, and CI.
- Human gates and recommended next decision.
- Exact sentence: `No NullForge implementation code has started.`

## Required Checks

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `Test-Path -LiteralPath pyproject.toml`
- `Test-Path -LiteralPath src\research_core\cli.py`
- `Test-Path -LiteralPath src\research_core\__main__.py`
- `Test-Path -LiteralPath docs\nullforge\qa\ENVIRONMENT_TRIAGE.md`
- `Test-Path -LiteralPath reports\nullforge\QA-T002\IMPLEMENTATION_REPORT.md`
- `Test-Path -LiteralPath reports\nullforge\QA-T002\CHANGED_FILES.md`
- `Test-Path -LiteralPath reports\nullforge\QA-T002\TEST_RESULTS.md`
- `Test-Path -LiteralPath reports\nullforge\QA-T002\AUDITOR_PROMPT.md`
- `rg -n "Decision: PASS" audits\nullforge\QA-T001\AUDIT_REPORT.md audits\nullforge\HY-T001\AUDIT_REPORT.md`
- `rg -n "local-temp-editable-install|python -m research_core.cli|No module named research_core.cli|research-core --help" docs\nullforge\qa\COMMAND_DISCOVERY.md reports\nullforge\QA-T001\TEST_RESULTS.md`
- `rg -n "\[project\.scripts\]|console_scripts|package-dir|pythonpath|typer|def main|if __name__ == \"__main__\"" pyproject.toml src\research_core\cli.py`
- `rg -n "QA-T002|environment|CLI|python -m research_core.cli|No NullForge implementation code has started" docs\nullforge\qa\ENVIRONMENT_TRIAGE.md reports\nullforge\QA-T002\IMPLEMENTATION_REPORT.md reports\nullforge\QA-T002\TEST_RESULTS.md`
- `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools`
- `Test-Path -LiteralPath tickets`
- `Test-Path -LiteralPath milestones`
- `Test-Path -LiteralPath prompts`
- `Test-Path -LiteralPath audits\nullforge\QA-T002`

## Report Requirements

Report:

- changed files,
- checks run,
- diagnostics run, failed, and skipped,
- side effects observed,
- human gates,
- whether QA-T002 is ready for independent audit.

Do not commit.
