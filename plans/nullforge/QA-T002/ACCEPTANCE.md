# QA-T002 Acceptance Criteria

## Required Outputs

The later implementor must create only these QA-T002 implementation outputs:

- `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`
- `reports/nullforge/QA-T002/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T002/CHANGED_FILES.md`
- `reports/nullforge/QA-T002/TEST_RESULTS.md`
- `reports/nullforge/QA-T002/AUDITOR_PROMPT.md`

The later implementor may update only these existing docs if needed:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`

No NullForge implementation code has started.

## Triage Document Criteria

`docs/nullforge/qa/ENVIRONMENT_TRIAGE.md` must include:

- Ticket ID `QA-T002`.
- Clear statement that QA-T002 is local environment and CLI/runtime blocker triage only.
- `QA-T001` and `HY-T001` audit `PASS` evidence.
- Summary of the inherited blocker:
  - `<local-temp-editable-install>` editable install evidence.
  - `python -m research_core.cli --help` failed with `No module named research_core.cli`.
  - `python -m research_core --help` failed because `research_core` has no `__main__`.
  - `research-core --help` was not recognized.
- Source facts from `pyproject.toml` and `src/research_core/cli.py`.
- Current observed local package/module visibility from bounded read-only diagnostics.
- A distinction between:
  - source-tree facts,
  - current local environment observations,
  - expected unsupported commands,
  - unresolved blockers.
- Side-effect review for `.pytest_cache/`, `__pycache__/`, `exec_outputs/`, docs build output, generated docs, source, package, test, schema, fixture, and CI changes.
- Human gates and recommended next decision.
- Exact sentence: `No NullForge implementation code has started.`

## Required Report Criteria

`reports/nullforge/QA-T002/IMPLEMENTATION_REPORT.md` must include:

- branch/status summary,
- ticket ID,
- summary of work,
- files changed,
- acceptance status,
- commands run,
- commands failed,
- commands skipped,
- side effects observed,
- dependency/package/source/test/CI/generated-doc status,
- human gates,
- readiness verdict.

`reports/nullforge/QA-T002/CHANGED_FILES.md` must list every changed file, why it changed, whether it was allowed, and whether any forbidden file changed.

`reports/nullforge/QA-T002/TEST_RESULTS.md` must list all bounded checks and diagnostics with pass/fail/skipped results.

`reports/nullforge/QA-T002/AUDITOR_PROMPT.md` must provide the next independent auditor with:

- files to read,
- audit focus,
- known blocker,
- required checks,
- forbidden actions,
- requested `PASS` / `HOLD` / `REJECT` verdict.

## Required Checks

The later implementor must run and record:

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

## Allowed Read-Only Diagnostics

The later implementor may run bounded diagnostics if they are included in the implementor prompt:

- `python -B -m pip show research-core`
- `python -B -c "import sys; print('executable=' + sys.executable); print('prefix=' + sys.prefix); print('base_prefix=' + sys.base_prefix); print('path0=' + (sys.path[0] if sys.path else ''))"`
- `python -B -c "import importlib.util; print('research_core=' + str(importlib.util.find_spec('research_core'))); print('research_core.cli=' + str(importlib.util.find_spec('research_core.cli')))"`
- `python -B -m research_core.cli --help`
- `python -B -m research_core --help`
- `research-core --help`

The implementor must record exit status and summarized output for each diagnostic. Failures are acceptable when they are the blocker being triaged.

## Forbidden-Pass Conditions

QA-T002 must not pass if:

- The implementor runs install, uninstall, editable install, dependency sync, package build, or environment repair commands.
- The implementor runs full tests, docs generation, docs build, quickstart commands, or CI smoke commands.
- Source, package metadata, dependency files, tests, schemas, fixtures, CI, generated docs, README, or ResearchCore Engine docs/code are modified.
- `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work starts.
- A real blocker is hidden or reclassified as success without evidence.
- Unexpected side effects appear and are not recorded.
- `No NullForge implementation code has started.` is removed from current status or QA-T002 docs.

## Done Definition

QA-T002 is ready for independent audit when:

- All required outputs exist.
- Required checks were run and recorded.
- Read-only diagnostics are recorded with clear outcomes.
- No forbidden files or actions occurred.
- Human gates are explicitly listed.
- The implementation verdict states whether local CLI/runtime readiness is still blocked, resolved by observation only, or requires human-approved repair.

## Ready-For-Implementor Verdict

Ready for implementor handoff.

The implementor must treat environment-changing repair as out of scope and stop for human direction if repair is needed.
