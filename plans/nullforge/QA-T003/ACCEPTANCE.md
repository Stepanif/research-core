# QA-T003 Acceptance

Date: `2026-06-16`

Ticket: `QA-T003`

Status: Ready for implementor

No NullForge implementation code has started.

## Required Outputs

The later implementor must create:

- `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md`
- `reports/nullforge/QA-T003/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T003/CHANGED_FILES.md`
- `reports/nullforge/QA-T003/TEST_RESULTS.md`
- `reports/nullforge/QA-T003/AUDITOR_PROMPT.md`

The implementor may update only if needed:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`

## Acceptance Criteria

QA-T003 implementation passes if:

- it is docs-only and decisioning-only;
- it records `QA-T001`, `HY-T001`, and `QA-T002` audit `PASS` evidence;
- it summarizes the `QA-T002` local Python environment/CLI blocker;
- it distinguishes source facts, local environment observations, unsupported command shapes, and unresolved blockers;
- it presents candidate repair/readiness paths without executing any of them;
- it states that QA-T003 does not authorize environment repair;
- it records exact human gates before any future environment mutation or package/source change;
- it preserves `No NullForge implementation code has started.`;
- it preserves `REPO_SOURCE_IMPORT_BASELINE` if `CURRENT_STATUS.md` or `SOURCE_INDEX.md` is touched;
- it creates the standard implementation reports;
- all required bounded checks pass or any skip is explicitly justified by scope.

## Required Content In Decision Doc

`docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md` must include:

- ticket ID `QA-T003`;
- purpose and non-goals;
- prerequisite audit `PASS` evidence for `QA-T001`, `HY-T001`, and `QA-T002`;
- `QA-T002` blocker summary;
- relevant package/CLI facts from `pyproject.toml`, `docs/reference/cli/overview.md`, `docs/how-to/run_ci_locally.md`, and `src/research_core/cli.py`;
- explicit statement that no install, uninstall, editable install, dependency sync, package build, venv work, environment repair, full tests, docs generation, docs build, quickstart, or CI smoke commands were run;
- candidate repair/readiness paths with tradeoffs and gates;
- recommended human decision options;
- side-effect and rollback considerations;
- local-path sanitization policy;
- exact sentence `No NullForge implementation code has started.`

## Required Checks

The later implementor must run and record:

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `Test-Path -LiteralPath docs\nullforge\qa\ENVIRONMENT_REPAIR_DECISION.md`
- `Test-Path -LiteralPath reports\nullforge\QA-T003\IMPLEMENTATION_REPORT.md`
- `Test-Path -LiteralPath reports\nullforge\QA-T003\CHANGED_FILES.md`
- `Test-Path -LiteralPath reports\nullforge\QA-T003\TEST_RESULTS.md`
- `Test-Path -LiteralPath reports\nullforge\QA-T003\AUDITOR_PROMPT.md`
- `rg -n "Decision: PASS" audits\nullforge\QA-T001\AUDIT_REPORT.md audits\nullforge\HY-T001\AUDIT_REPORT.md audits\nullforge\QA-T002\AUDIT_REPORT.md`
- `rg -n "QA-T003|QA-T002|python -m research_core.cli|No module named research_core.cli|local-temp-editable-install|No NullForge implementation code has started" docs\nullforge\qa\ENVIRONMENT_REPAIR_DECISION.md reports\nullforge\QA-T003\IMPLEMENTATION_REPORT.md reports\nullforge\QA-T003\TEST_RESULTS.md`
- `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools`
- `Test-Path -LiteralPath tickets`
- `Test-Path -LiteralPath milestones`
- `Test-Path -LiteralPath prompts`
- `Test-Path -LiteralPath audits\nullforge\QA-T003`

## Forbidden-Pass Conditions

QA-T003 must not pass if:

- any install, uninstall, editable install, dependency sync, package build, venv creation/activation, or environment repair command was run;
- full tests, docs generation, docs build, quickstart, or CI smoke commands were run;
- source, tests, schemas, fixtures, package metadata, dependency files, CI, README, docs/reference, tools, or generated docs were modified;
- `tickets/`, `milestones/`, `prompts/`, or `audits/nullforge/QA-T003/` were created by the implementor;
- the decision doc claims local install correctness, CLI smoke success, test pass status, docs build success, or package release readiness;
- the decision doc chooses and executes a repair path instead of requesting human direction;
- `No NullForge implementation code has started.` is removed or contradicted.

## Source-Of-Truth Updates

If `CURRENT_STATUS.md` or `SOURCE_INDEX.md` is updated, it must:

- link only repo-local files that exist;
- preserve `REPO_SOURCE_IMPORT_BASELINE`;
- preserve `No NullForge implementation code has started.`;
- describe QA-T003 as decisioning/human-gate work, not environment repair proof.

## Done Definition

QA-T003 implementation is done when:

- the decision doc and reports exist;
- bounded checks pass;
- no forbidden files or commands were used;
- human decision options are clear;
- QA-T003 is ready for independent audit.
