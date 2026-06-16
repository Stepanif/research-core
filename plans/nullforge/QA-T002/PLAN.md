# QA-T002 Plan

## Goal

Create a bounded docs-only implementation path for `QA-T002`, the NullForge M1 readiness ticket for local Python environment and CLI/runtime blocker triage.

`QA-T002` should investigate and record the local environment mismatch that blocked `QA-T001` CLI readiness discovery. It must not repair the environment, change package metadata, change source code, run full tests, generate docs, or start downstream implementation.

No NullForge implementation code has started.

## Source Context Used

- `plans/nullforge/QA-T002/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T002/CONTEXT_BUNDLE_MANIFEST.md`
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

## Key Facts

- `QA-T001` audit decision is `PASS`.
- `HY-T001` audit decision is `PASS`.
- `QA-T001` found local executable readiness blockers:
  - `python -m pip show research-core` reported editable install provenance from `<local-temp-editable-install>`, not this workspace.
  - `python -m research_core.cli --help` failed with `No module named research_core.cli`.
  - `python -m research_core --help` failed because `research_core` has no `__main__`.
  - `research-core --help` was not recognized as a command.
- `pyproject.toml` is the package metadata source.
- `pyproject.toml` declares `package-dir = {"" = "src"}` and package discovery under `src`.
- `pyproject.toml` declares no `[project.scripts]` console entry point.
- `src/research_core/cli.py` exists and defines a Typer app, `main()`, and an `if __name__ == "__main__"` guard.
- `src/research_core/__main__.py` is absent, so `python -m research_core` failing is expected unless a later scoped ticket adds that module.
- Existing docs and CI reference `python -m research_core.cli`.

## Assumptions

- `QA-T002` is a readiness/triage ticket, not an environment repair ticket.
- Local package visibility may currently point to a stale editable install rather than the current workspace.
- The later implementor may run bounded read-only diagnostics, but not commands that mutate the Python environment.
- A CLI help command may be used only as a read-only diagnostic and should be run with bytecode/cache protections.
- Any repair requiring install, uninstall, editable install, venv change, package metadata change, or source change requires explicit human direction and likely a separate scoped ticket.

## Implementation Scope For Later Implementor

The later implementor should:

1. Verify the working tree state and prerequisite audit `PASS` evidence.
2. Run only bounded read-only environment and CLI diagnostics.
3. Create a QA-T002 triage document that records:
   - current local package visibility,
   - current Python executable/prefix context,
   - `research_core` and `research_core.cli` module resolution status,
   - expected source-tree facts from `pyproject.toml` and `src/research_core/cli.py`,
   - whether missing `__main__` and missing console script are expected limitations,
   - what remains blocked,
   - what human decision is needed before repair.
4. Update NullForge status/source-index docs only within the allowed implementation scope.
5. Create implementation reports for QA-T002.
6. Record commands run, failures, skipped commands, side effects, and human gates.

## Diagnostic Command Policy

The later implementor may run read-only diagnostics only.

Allowed diagnostic categories:

- Git status and diff checks.
- `Test-Path` file existence checks.
- `rg` text searches.
- Python metadata visibility checks that do not install, uninstall, sync, build, or mutate the environment.
- CLI help probes limited to the documented blocker commands and only as read-only diagnostics.

Environment-changing repair is not allowed in `QA-T002`. If diagnostics show that `pip install -e .`, uninstall/reinstall, venv recreation, dependency changes, package metadata changes, or source changes are needed, the implementor must stop and record the human gate.

## Python Side-Effect Policy

Python diagnostics must avoid bytecode/cache writes where practical:

- Prefer `python -B` for all Python diagnostic commands.
- Do not run full tests, docs generation, docs build, quickstart commands, CI smoke commands, or artifact-generating CLI commands.
- Do not run `pip install`, `python -m pip install`, uninstall, sync, build, editable install, or dependency update commands.
- After diagnostics, run status/diff checks and explicitly review for unexpected `.pytest_cache/`, `__pycache__/`, `exec_outputs/`, docs build output, generated docs, source, package, test, schema, fixture, or CI changes.
- If unexpected side effects appear, stop and report them. Do not silently clean or rewrite unrelated files.

## Explicitly Out Of Scope

- Installing, uninstalling, repairing, or changing the Python environment.
- Editing `pyproject.toml`, package metadata, dependencies, lockfiles, or package manager files.
- Editing source files, tests, schemas, fixtures, CI, generated docs, README, or ResearchCore Engine docs.
- Adding `[project.scripts]`, `src/research_core/__main__.py`, CLI commands, tests, fixtures, or schemas.
- Running full tests, docs generation, docs build, quickstart commands, or CI smoke commands.
- Creating audits for `QA-T002`.
- Creating tickets, milestones, prompt files, app files, desktop shell, bridge, sidecar, app scaffolding, `ADR-T003`, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

## Proposed Allowed Files For Later Implementor

- `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/QA-T002/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T002/CHANGED_FILES.md`
- `reports/nullforge/QA-T002/TEST_RESULTS.md`
- `reports/nullforge/QA-T002/AUDITOR_PROMPT.md`

The later implementor must treat all plans, audits, prior reports, package metadata, source, tests, schemas, fixtures, CI, generated docs, and ResearchCore Engine docs/code as read-only unless the implementor prompt explicitly allows otherwise.

## Planned Steps

1. Verify initial status with `git status --short --branch` and `git status --short --untracked-files=all`.
2. Confirm `QA-T001` and `HY-T001` audit `PASS` evidence.
3. Verify source facts with `Test-Path` and `rg`:
   - `pyproject.toml` exists.
   - `src/research_core/cli.py` exists.
   - `src/research_core/__main__.py` is absent or present as observed.
   - no console script is declared unless current metadata differs.
4. Run bounded Python diagnostics with `python -B`, such as package visibility and module-resolution checks.
5. Optionally re-run the known CLI blocker probes as read-only help diagnostics with bytecode disabled.
6. Create `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`.
7. Update `CURRENT_STATUS.md` and `SOURCE_INDEX.md` only as allowed by the later implementor prompt.
8. Create QA-T002 implementation reports.
9. Run required bounded checks and record results.

## Required Checks For Later Implementor

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

Suggested read-only diagnostics for the later implementor, if included by the implementor prompt:

- `python -B -m pip show research-core`
- `python -B -c "import sys; print('executable=' + sys.executable); print('prefix=' + sys.prefix); print('base_prefix=' + sys.base_prefix); print('path0=' + (sys.path[0] if sys.path else ''))"`
- `python -B -c "import importlib.util; print('research_core=' + str(importlib.util.find_spec('research_core'))); print('research_core.cli=' + str(importlib.util.find_spec('research_core.cli')))"`
- `python -B -m research_core.cli --help`
- `python -B -m research_core --help`
- `research-core --help`

If any diagnostic writes unexpected files, the implementor must stop and report the side effect.

## Acceptance Criteria

- QA-T002 implementation remains docs-only and environment-readiness-only.
- The triage document records observed local environment/package/CLI resolution state.
- The triage document distinguishes source-tree facts from local environment observations.
- The triage document explains whether `python -m research_core`, `research-core`, and `python -m research_core.cli` are expected, unsupported, or blocked based on evidence.
- No environment repair, install, dependency change, source change, test creation, schema creation, fixture creation, CI change, generated-doc update, or downstream work occurs.
- Required reports are created and include command results, skipped commands, side-effect review, human gates, and readiness verdict.
- `No NullForge implementation code has started.` remains present in updated NullForge status/triage material.
- Any unresolved blocker is explicitly recorded as a human gate, not hidden as success.

## Human Gates And Stop Conditions

Stop and ask for human direction if:

- Any command would install, uninstall, repair, or mutate the Python environment.
- Any command would run full tests, docs generation, docs build, quickstart, or CI smoke.
- Any command would modify source, package metadata, dependencies, lockfiles, CI, generated docs, tests, schemas, or fixtures.
- A fix requires adding a console script, adding `__main__.py`, editing `pyproject.toml`, or changing CLI source.
- The working tree has unrelated changes outside QA-T002-approved paths.
- Diagnostics require deleting or cleaning side-effect files.
- The blocker expands into package design, CLI contract, generated-doc drift, or downstream M1 implementation.

## Rollback And Repair Route

Because QA-T002 implementation should be docs-only, rollback should be limited to reverting QA-T002 docs/report changes if audit finds scope drift.

If audit returns `HOLD`, create a bounded repair prompt focused on the exact missing evidence or documentation gap. If audit returns `REJECT`, stop for human direction before attempting repair.

Any real environment repair should be split into a later human-approved ticket.

## Planner Verdict

Ready for implementor handoff.

The later implementor may run bounded read-only diagnostics and create docs/reports only. Any environment-changing repair requires human direction outside this plan.
