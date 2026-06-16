# QA-T001 Acceptance Criteria

Date: `2026-06-16`

Ticket: `QA-T001`

Role: Planner

Acceptance verdict: `READY_FOR_IMPLEMENTOR`

## Required Outputs For Later Implementor

- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/CURRENT_STATUS.md`, only if needed for QA-T001 status/link updates.
- `docs/nullforge/SOURCE_INDEX.md`, only if needed for QA-T001 links.
- `reports/nullforge/QA-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T001/CHANGED_FILES.md`
- `reports/nullforge/QA-T001/TEST_RESULTS.md`
- `reports/nullforge/QA-T001/AUDITOR_PROMPT.md`

No NullForge implementation code has started.

## Required Discovery Content

`COMMAND_DISCOVERY.md` must record:

- QA-T001 scope and non-goals.
- M0 prerequisite audit `PASS` evidence.
- Current project metadata source, including `pyproject.toml`.
- Absence of root `package.json`, `pnpm-workspace.yaml`, and `pnpm-lock.yaml`.
- Python version expectation from CI and any bounded local runtime query.
- Package manager / environment expectation from source docs and bounded command output.
- Existing test command candidates from CI and docs.
- Existing docs-generation and docs-build command candidates from CI and docs.
- Existing CLI invocation evidence, including `python -m research_core.cli`.
- Existing smoke command evidence from `.github/workflows/research-ci.yml`.
- Existing fixture/sample locations.
- Commands run, commands skipped, command failures, and exact reasons.
- Side-effect review for `.pytest_cache/`, `exec_outputs/`, docs build output, and generated docs.
- Human gates, blockers, and next recommended action.

## Required Bounded Checks

The later implementor must run and record:

```text
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
git diff --check
Test-Path -LiteralPath docs\nullforge\qa\COMMAND_DISCOVERY.md
Test-Path -LiteralPath reports\nullforge\QA-T001\IMPLEMENTATION_REPORT.md
Test-Path -LiteralPath reports\nullforge\QA-T001\CHANGED_FILES.md
Test-Path -LiteralPath reports\nullforge\QA-T001\TEST_RESULTS.md
Test-Path -LiteralPath reports\nullforge\QA-T001\AUDITOR_PROMPT.md
rg -n "Decision: PASS" audits\nullforge\PF-T000\AUDIT_REPORT.md audits\nullforge\PF-T001\AUDIT_REPORT.md audits\nullforge\PF-T002\AUDIT_REPORT.md audits\nullforge\ADR-T001\AUDIT_REPORT.md audits\nullforge\ADR-T002\AUDIT_REPORT.md audits\nullforge\CX-T001\AUDIT_REPORT.md audits\nullforge\MB-T001\AUDIT_REPORT.md
rg -n "QA-T001|command|test|pyproject|package.json|pnpm-workspace|pnpm-lock|python -m pytest|python -m research_core.cli|No NullForge implementation code has started" docs\nullforge\qa\COMMAND_DISCOVERY.md reports\nullforge\QA-T001\IMPLEMENTATION_REPORT.md reports\nullforge\QA-T001\TEST_RESULTS.md
git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github tools docs\reference README.md
Test-Path -LiteralPath tickets
Test-Path -LiteralPath milestones
Test-Path -LiteralPath prompts
Test-Path -LiteralPath audits\nullforge\QA-T001
```

Allowed bounded command discovery may include:

```text
python --version
python -m pip --version
python -m pip show research-core
python -m pip show pyarrow
python -m pip show pytest
python -m pytest --version
python -m research_core.cli --help
python -m research_core --help
research-core --help
```

The implementor must not run `python -m pytest`, `python -m pytest -q`, docs generation, docs build, install commands, quickstart commands, or CI smoke commands unless a human explicitly approves that expansion.

## Source-Of-Truth Update Expectations

- `docs/nullforge/CURRENT_STATUS.md` may be updated only to show QA-T001 in-progress/discovery state and preserve the no-code sentence.
- `docs/nullforge/SOURCE_INDEX.md` may be updated only to link files that exist after QA-T001 implementation.
- `docs/nullforge/DECISION_LEDGER.md`, ADRs, archive policy, M0 handoff, role-loop docs, imported volumes, and existing ResearchCore Engine docs must remain unchanged.

## Forbidden-Pass Conditions

QA-T001 must not pass if:

- implementation code was created or modified;
- tests, schemas, fixtures, goldens, generated docs, package files, CI, raw data, or ResearchCore Engine docs/code were created or modified;
- install, full test, docs generation, docs build, quickstart, or CI smoke commands were run without human approval;
- `package.json`, `pnpm-workspace.yaml`, `pnpm-lock.yaml`, or other package files were created;
- command failures were hidden or described as passing;
- command candidates were invented without source evidence or bounded command evidence;
- `.pytest_cache/`, `exec_outputs/`, docs build output, or generated docs were created and ignored;
- `No NullForge implementation code has started.` was removed or contradicted;
- `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, or downstream M1 work was started.

## Done Definition

QA-T001 implementation is done when:

- all required outputs exist;
- all acceptance criteria above are satisfied;
- required checks are run or explicitly skipped with reason;
- human gates and blockers are recorded;
- changed files are limited to allowed QA-T001 docs/reports/status/index paths;
- an independent auditor can review the ticket and return `PASS`, `HOLD`, or `REJECT`.
