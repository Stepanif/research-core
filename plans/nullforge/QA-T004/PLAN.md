# QA-T004 Plan

Date: `2026-06-16`

Ticket: `QA-T004`

Role: Planner

Status: Ready for implementor

No NullForge implementation code has started.

## Goal

Plan a bounded docs-only implementation for `QA-T004`, the NullForge M1 readiness ticket for choosing and preparing a local Python environment repair/readiness path after `QA-T003`.

`QA-T004` should turn the `QA-T003` decision packet into a concrete human-gated readiness path proposal. It must not repair the environment, run install commands, run tests, mutate package metadata, or start downstream M1 implementation.

## Non-Goals

`QA-T004` does not:

- install, uninstall, editable install, dependency sync, package build, create/select/activate a virtual environment, or repair the Python environment;
- run `python -m research_core.cli --help`, `python -m research_core --help`, `research-core --help`, full tests, docs generation, docs build, quickstart commands, or CI smoke commands;
- modify `pyproject.toml`, dependencies, package metadata, source, tests, schemas, fixtures, CI, generated docs, README, docs/reference, or tools;
- add `[project.scripts]`, `console_scripts`, or `src/research_core/__main__.py`;
- prove local install correctness, CLI smoke success, test pass status, docs build success, or package release readiness;
- create tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, generated docs, raw data, private data, or downstream artifacts;
- start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

## Source Context Used

- `plans/nullforge/QA-T004/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T004/CONTEXT_BUNDLE_MANIFEST.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md`
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`
- `audits/nullforge/HY-T001/AUDIT_REPORT.md`
- `audits/nullforge/QA-T002/AUDIT_REPORT.md`
- `audits/nullforge/QA-T003/AUDIT_REPORT.md`
- `reports/nullforge/QA-T003/TEST_RESULTS.md`
- `pyproject.toml`
- `docs/how-to/run_ci_locally.md`
- `docs/reference/cli/overview.md`
- `src/research_core/cli.py`

## Assumptions

- `QA-T001`, `HY-T001`, `QA-T002`, and `QA-T003` have audit decision `PASS`.
- The unresolved blocker remains: `research_core.cli` is not visible to the active Python environment, and `python -m research_core.cli --help` failed with `No module named research_core.cli`.
- The editable install visibility still points outside this workspace as `<local-temp-editable-install>` in recorded evidence.
- `python -m research_core --help` and `research-core --help` are separate unsupported command shapes because `src/research_core/__main__.py` is absent and no console script is declared.
- The implementor will not receive authorization to mutate the Python environment unless a future prompt explicitly grants exact commands and side-effect boundaries.
- The safest default recommendation to document is an isolated project-local virtual environment path, but `QA-T004` itself may only prepare the human gate and command packet; it must not execute it.

## Implementation Scope For Later Implementor

The later implementor should create a docs-only QA-T004 repair/readiness path preparation document that:

- records the selected recommended path as a proposal, not an executed repair;
- compares the candidate paths from `QA-T003`;
- recommends a default isolated project-local virtual environment path unless the human prompt gives another explicit choice;
- lists exact command classes that would need later human approval before execution;
- defines success criteria for a later repair ticket, such as proving package visibility and `python -m research_core.cli --help` only after authorized environment work;
- distinguishes expected unsupported command shapes from the immediate environment blocker;
- records risks, side effects, rollback considerations, and local-path sanitization policy;
- updates status and source index only if the implementor prompt explicitly allows those files;
- creates implementation reports for QA-T004 only.

The implementor must not run repair commands or live CLI validation. It may use only bounded status, diff, path, and text-search checks.

## Human-Gate Decision Policy

Human approval is required before any environment mutation, including:

- `pip install`, `python -m pip install`, uninstall, editable install, dependency sync, or package build;
- virtual-environment creation, deletion, selection, activation, or dependency installation;
- changing editable install state in the active Python environment;
- running `python -m research_core.cli --help` as a post-repair proof if that command would depend on an environment change not yet authorized;
- running full tests, docs generation, docs build, quickstart commands, or CI smoke commands;
- modifying package metadata, source files, tests, schemas, fixtures, CI, generated docs, README, docs/reference, or tools.

If the implementor receives no explicit human-selected repair path, it should document a recommended path and stop at a human gate. It must not infer approval to execute repair.

## Candidate Repair / Readiness Paths From QA-T003

| Candidate | QA-T004 planning posture | Required human gate |
|---|---|---|
| Isolated project-local virtual environment | Recommended default proposal because it avoids mutating the active global Python environment. | Approve venv location, creation command, install command, activation model, validation commands, output sanitization, and cleanup policy. |
| Active-environment editable reinstall | Document as faster but riskier because it mutates active Python state and may affect unrelated work. | Approve exact reinstall command, rollback, active-environment risk, and validation commands. |
| Diagnostics-only deferral | Document as valid if the human wants to avoid environment mutation. | Accept that CLI readiness remains blocked for executable work. |
| Source/package entrypoint ticket | Document as separate from environment repair because it would change package/source behavior. | Open a separate scoped ticket if `python -m research_core --help` or `research-core --help` support is desired. |
| Defer to later M1 implementation | Document as possible but risky for later executable tasks. | Accept that downstream tickets may stop when CLI execution is required. |

## Recommended Selected-Path Preparation Inputs

The later QA-T004 implementation should prepare, but not execute, a path packet containing:

- selected or recommended path name;
- goal of the later repair/readiness ticket;
- exact commands that would need approval in the later repair ticket;
- commands that remain forbidden;
- target success proof;
- expected side effects;
- rollback and cleanup plan;
- local path redaction policy;
- when to stop and request human input;
- evidence needed before moving from readiness planning to repair execution.

## Side-Effect Policy

| Area | Policy |
|---|---|
| Python environment | Must not change. No install, uninstall, repair, venv creation/activation, package build, or dependency sync. |
| Bytecode/cache | Avoid Python execution. If a read-only Python command becomes necessary in a later prompt, require `-B` and record cache checks. |
| Editable install state | Must not change. Treat `<local-temp-editable-install>` as recorded evidence only. |
| Virtual environments | Must not create, select, activate, delete, or modify. |
| Generated docs | Must not generate, build, or verify generated docs. |
| Local paths | Use placeholders such as `<repo-root>`, `<local-temp-editable-install>`, and `<python-313-install>` in new docs/reports. |
| Source/package/test/CI files | Must remain unchanged. |

## Explicitly Out Of Scope

- Environment repair execution.
- Source/package entrypoint implementation.
- Package/dependency metadata changes.
- Test creation or test execution.
- Docs generation or docs build.
- CI smoke execution.
- ResearchCore Engine behavior changes.
- New tickets, milestones, prompts, reports outside QA-T004, audits during implementation, app files, code, schemas, fixtures, raw/private data, or downstream M1 artifacts.

## Proposed Allowed Files For Later Implementor

If the human proceeds with QA-T004 implementation, allow only:

- `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/QA-T004/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T004/CHANGED_FILES.md`
- `reports/nullforge/QA-T004/TEST_RESULTS.md`
- `reports/nullforge/QA-T004/AUDITOR_PROMPT.md`

Treat as read-only:

- `plans/nullforge/QA-T004/*`
- prior NullForge docs, plans, reports, and audits not listed above
- `pyproject.toml`
- `requirements-docs.txt`
- `.github/`
- `README.md`
- `docs/` except allowed NullForge status/source-index/QA path files
- `tools/`
- `src/`
- `tests/`
- `schemas/`
- `fixtures/`
- package files and generated docs

## Planned Steps For Later Implementor

1. Verify working tree status and prerequisite audit `PASS` dispositions.
2. Read the QA-T004 planner artifacts and the QA-T001 through QA-T003 QA docs.
3. Create `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md`.
4. Document the recommended repair/readiness path and alternatives without executing any command from those paths.
5. Update `docs/nullforge/CURRENT_STATUS.md` only if explicitly allowed, preserving `No NullForge implementation code has started.` and `REPO_SOURCE_IMPORT_BASELINE`.
6. Update `docs/nullforge/SOURCE_INDEX.md` only if explicitly allowed, linking the QA-T004 path doc and report artifacts after creation.
7. Create QA-T004 implementation reports.
8. Run bounded status, diff, existence, and text-search checks only.

## Acceptance Criteria

The later implementation should pass if:

- all allowed QA-T004 outputs exist;
- the path doc identifies `QA-T004`, purpose, non-goals, prerequisite `PASS` evidence, QA-T003 decision packet summary, and the unresolved blocker;
- the path doc recommends or records a selected repair/readiness path while making clear no repair was executed;
- candidate paths and tradeoffs from QA-T003 are preserved;
- human approval requirements before environment mutation are explicit;
- no install, repair, virtual-environment, package build, test, docs generation, docs build, quickstart, CI smoke, source, package, dependency, or downstream work occurred;
- status/source index updates, if allowed, link only existing repo-local files and preserve the no-code sentence;
- bounded checks pass or are validly recorded as skipped with exact reasons;
- changed files remain within the allowed QA-T004 scope.

## Required Checks

Use bounded checks only:

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

Do not run Python, pip, pytest, docs-generation, docs-build, quickstart, CI smoke, venv, or repair commands unless a later human prompt explicitly changes the scope.

## Human Gates And Stop Conditions

Stop and request human direction if:

- a repair path must be executed rather than documented;
- the human-selected path is unclear;
- any command would install, uninstall, sync dependencies, build packages, create/activate a virtual environment, mutate editable install state, run tests, generate docs, build docs, run quickstart, run CI smoke, or execute CLI validation after repair;
- package/source/test/CI/generated-doc changes appear necessary;
- `ADR-T003`, desktop bridge/app work, M1 implementation, or downstream work is requested;
- changed files appear outside the allowed QA-T004 scope;
- prerequisite audit `PASS` evidence is missing.

## Rollback / Repair Route

If QA-T004 implementation needs repair, keep repair bounded to:

- `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/QA-T004/*`

Do not repair by changing environment state, source code, package metadata, tests, dependencies, CI, generated docs, raw/private data, tickets, milestones, prompts, or downstream artifacts.

## Ready-For-Implementor Verdict

Ready for implementor.

The implementor may prepare QA-T004 documentation and reports only. Any actual local Python environment repair/readiness execution requires a later explicit human-approved ticket with exact command scope.
