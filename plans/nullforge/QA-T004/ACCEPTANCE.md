# QA-T004 Acceptance

Date: `2026-06-16`

Ticket: `QA-T004`

Role: Planner

Status: Ready for implementor

No NullForge implementation code has started.

## Acceptance Criteria

QA-T004 implementation passes only if all of the following are true:

- `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md` exists.
- QA-T004 reports exist under `reports/nullforge/QA-T004/`.
- The QA-T004 path doc includes ticket ID `QA-T004`, purpose, non-goals, prerequisite audit `PASS` evidence, QA-T003 decision packet summary, and the unresolved local environment blocker.
- The path doc records that `python -m research_core.cli --help` is the documented command shape that failed with `No module named research_core.cli`.
- The path doc records `<local-temp-editable-install>` as sanitized inherited evidence, not as a new raw local path.
- The path doc distinguishes source facts, recorded local environment observations, expected unsupported command shapes, unresolved blockers, candidate repair/readiness paths, and the recommended or selected path.
- The path doc states that no install, uninstall, editable install, dependency sync, package build, virtual-environment creation/activation, environment repair, full tests, docs generation, docs build, quickstart commands, or CI smoke commands were run.
- Human-gate requirements are explicit before any environment mutation or source/package change.
- Status and source index updates, if performed by the later implementor, preserve `No NullForge implementation code has started.` and `REPO_SOURCE_IMPORT_BASELINE`.
- No forbidden files or folders are created or modified.

## Required Outputs

Allowed implementation outputs for a later QA-T004 implementor:

- `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/QA-T004/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T004/CHANGED_FILES.md`
- `reports/nullforge/QA-T004/TEST_RESULTS.md`
- `reports/nullforge/QA-T004/AUDITOR_PROMPT.md`

The implementor must not create `audits/nullforge/QA-T004/`; that folder is reserved for the independent auditor.

## Required Checks

The later implementor must run and record:

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `Test-Path -LiteralPath docs\nullforge\qa\ENVIRONMENT_REPAIR_PATH.md`
- `Test-Path -LiteralPath reports\nullforge\QA-T004\IMPLEMENTATION_REPORT.md`
- `Test-Path -LiteralPath reports\nullforge\QA-T004\CHANGED_FILES.md`
- `Test-Path -LiteralPath reports\nullforge\QA-T004\TEST_RESULTS.md`
- `Test-Path -LiteralPath reports\nullforge\QA-T004\AUDITOR_PROMPT.md`
- `rg -n "Decision: PASS" audits\nullforge\QA-T001\AUDIT_REPORT.md audits\nullforge\HY-T001\AUDIT_REPORT.md audits\nullforge\QA-T002\AUDIT_REPORT.md audits\nullforge\QA-T003\AUDIT_REPORT.md`
- `rg -n "QA-T004|QA-T003|python -m research_core.cli|No module named research_core.cli|local-temp-editable-install|No NullForge implementation code has started" docs\nullforge\qa\ENVIRONMENT_REPAIR_PATH.md reports\nullforge\QA-T004\IMPLEMENTATION_REPORT.md reports\nullforge\QA-T004\TEST_RESULTS.md`
- `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools`
- `Test-Path -LiteralPath tickets`
- `Test-Path -LiteralPath milestones`
- `Test-Path -LiteralPath prompts`
- `Test-Path -LiteralPath audits\nullforge\QA-T004`

## Forbidden-Pass Conditions

QA-T004 must not pass if:

- any install, uninstall, editable install, dependency sync, package build, virtual-environment creation/activation, or environment repair command was run;
- any full test, docs generation, docs build, quickstart, CI smoke, or post-repair CLI validation command was run without explicit human authorization;
- `pyproject.toml`, source, tests, schemas, fixtures, dependencies, package files, CI, generated docs, README, docs/reference, or tools were modified;
- `[project.scripts]`, `console_scripts`, or `src/research_core/__main__.py` were added;
- the path doc claims local install correctness, CLI readiness, test pass status, docs build success, public release readiness, or implementation proof;
- the implementation starts `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, or downstream work;
- raw local absolute paths are introduced instead of sanitized placeholders;
- audit artifacts are created by the implementor.

## Source-Of-Truth Update Expectations

If the later implementor is allowed to update status/index docs:

- `docs/nullforge/CURRENT_STATUS.md` should name `QA-T004` as active/in-progress or ready-for-audit according to implementation state.
- `docs/nullforge/CURRENT_STATUS.md` must preserve `No NullForge implementation code has started.` and `REPO_SOURCE_IMPORT_BASELINE`.
- `docs/nullforge/SOURCE_INDEX.md` should link only repo-local files that exist, including the QA-T004 path doc and QA-T004 report artifacts after creation.

## Human Gates

Human approval is required before:

- choosing active-environment mutation over isolated environment preparation;
- running or authorizing any exact repair command;
- creating, selecting, activating, or deleting a virtual environment;
- changing editable install state;
- modifying source/package metadata or entrypoints;
- running tests, docs generation, docs build, quickstart commands, CI smoke commands, or CLI validation commands that rely on a repair;
- broadening scope into `ADR-T003`, desktop bridge/app work, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution.

## Done Definition

QA-T004 is ready for independent audit when the allowed docs and reports exist, the selected-path preparation is documented without execution, bounded checks are recorded, forbidden actions are avoided, and the next human decision is explicit.
