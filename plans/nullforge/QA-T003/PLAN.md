# QA-T003 Plan

Date: `2026-06-16`

Ticket: `QA-T003`

Status: Ready for implementor

No NullForge implementation code has started.

## Goal

Create a docs-only decisioning artifact for the local Python environment and CLI/runtime blocker confirmed by `QA-T002`.

`QA-T003` should help the human decide whether to authorize a separate environment repair/readiness ticket, keep CLI execution blocked, or choose another bounded path. It must not run repair commands or mutate the Python environment.

## Non-Goals

`QA-T003` does not:

- install, uninstall, editable install, dependency sync, package build, create/select a virtual environment, activate a virtual environment, or repair the Python environment;
- modify `pyproject.toml`, dependencies, package metadata, source, tests, schemas, fixtures, CI, generated docs, README, docs/reference files, or tools;
- add `[project.scripts]`, `console_scripts`, or `src/research_core/__main__.py`;
- run full tests, docs generation, docs build, quickstart commands, or CI smoke commands;
- prove local install correctness, CLI smoke success, test pass status, docs build success, or package release readiness;
- start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

## Source Context Used

- `plans/nullforge/QA-T003/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T003/CONTEXT_BUNDLE_MANIFEST.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`
- `audits/nullforge/HY-T001/AUDIT_REPORT.md`
- `audits/nullforge/QA-T002/AUDIT_REPORT.md`
- `reports/nullforge/QA-T002/TEST_RESULTS.md`
- `pyproject.toml`
- `docs/how-to/run_ci_locally.md`
- `docs/reference/cli/overview.md`
- `src/research_core/cli.py`

## Assumptions

- `QA-T001`, `HY-T001`, and `QA-T002` audit decisions are `PASS`.
- `main` was clean and aligned with `origin/main` before `QA-T003` context artifacts were created.
- The active local Python environment may have changed since `QA-T002`; `QA-T003` should treat `QA-T002` diagnostics as the latest recorded evidence, not as current live proof.
- Human direction is required before any environment mutation, package/source change, or executable readiness proof.
- The immediate decision target is local Python/CLI readiness, not product/app implementation.

## Implementation Scope For Later Implementor

The later `QA-T003` implementor should create a docs-only decision packet that:

- restates the `QA-T002` blocker and relevant package/CLI facts;
- presents candidate repair/readiness paths with tradeoffs and risks;
- identifies which paths require human approval;
- recommends a next human decision without executing repair;
- records skipped command classes and why they remain forbidden;
- updates status/source index only if needed to link `QA-T003` artifacts and preserve no-code/baseline wording;
- creates standard implementation reports.

## Explicit Decision Policy

The later `QA-T003` implementor may only document repair options and prepare a human gate packet.

The implementor must not run exact environment repair commands inside `QA-T003`. If repair appears necessary, the implementor must stop at a human decision request and provide a follow-up prompt for a separate scoped repair/readiness ticket.

Candidate commands may be listed as examples only if clearly marked `not run` and attached to a future human approval path. No command that mutates Python environment state may be executed by `QA-T003`.

## Candidate Repair / Readiness Paths

These paths are planning inputs only. The later implementor must not execute them.

| Path | Decision value | Risks / gates |
|---|---|---|
| Isolated project-local virtual environment | Avoids mutating global Python state and can make local readiness reproducible. | Requires human approval for venv creation/selection, install commands, dependency sync, activation model, and cleanup policy. |
| Active-environment editable reinstall from current workspace | Could quickly align `research-core` visibility with this repo. | Mutates active Python environment and may affect other work; requires explicit human approval and rollback plan. |
| Diagnostics-only deferral | Keeps current environment untouched and records that local CLI execution remains blocked. | Future executable work remains blocked until a later repair ticket. |
| Package/source entrypoint ticket | Could add `research-core --help` or `python -m research_core --help` support if needed. | This is source/package implementation, not environment repair; requires a separate scoped code/package ticket. |
| Defer until M1 implementation planning | Avoids premature environment work. | Any ticket needing CLI execution must treat the blocker as unresolved. |

## Side-Effect Policy

| Area | Policy |
|---|---|
| Python environment | No install, uninstall, editable install, dependency sync, package build, venv creation/activation, or repair commands. |
| Bytecode/cache | Avoid Python commands unless read-only and explicitly approved by the implementor prompt; prefer status/search checks. Do not intentionally create `__pycache__/`. |
| Editable install state | Must remain unchanged. Do not alter active environment or installed package metadata. |
| Virtual environments | Do not create, select, activate, delete, or mutate virtual environments in QA-T003. |
| Generated docs | Do not run docs generation, generated-doc verification, or docs build commands. |
| Local absolute paths | Sanitize local absolute paths in QA-T003 docs/reports where diagnostic or option text would otherwise expose them; preserve placeholders such as `<local-temp-editable-install>`. |
| Source/package/test/CI files | Read-only unless a separate future ticket explicitly authorizes changes. |

## Explicitly Out Of Scope

- `src/` edits, including `src/research_core/cli.py` and future `src/research_core/__main__.py`
- `pyproject.toml` edits
- dependency, package metadata, lockfile, or console-script changes
- install, uninstall, editable install, dependency sync, package build, venv work, or environment repair
- full tests, docs generation, docs build, quickstart commands, CI smoke commands
- generated docs and docs/reference updates
- `tests/`, `schemas/`, `fixtures/`, raw/private data, ES-derived fixtures
- `tickets/`, `milestones/`, `prompts/`
- audits for QA-T003
- `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, public distribution

## Proposed Allowed Files For Later Implementor

- `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/QA-T003/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T003/CHANGED_FILES.md`
- `reports/nullforge/QA-T003/TEST_RESULTS.md`
- `reports/nullforge/QA-T003/AUDITOR_PROMPT.md`

Treat as read-only:

- `plans/nullforge/QA-T003/*`
- all previous plans, reports, and audits
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`
- `pyproject.toml`
- `docs/how-to/run_ci_locally.md`
- `docs/reference/cli/overview.md`
- `src/`
- `tests/`
- `schemas/`
- `fixtures/`
- `.github/`
- package/dependency files
- generated docs

## Implementation Steps For Later Implementor

1. Verify working tree status and prerequisite audit `PASS` evidence.
2. Read all QA-T003 planner artifacts and QA-T002 source/report/audit context.
3. Create `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md`.
4. Present the candidate repair/readiness paths without executing them.
5. Record the decision policy that QA-T003 does not repair the environment.
6. Update `CURRENT_STATUS.md` and `SOURCE_INDEX.md` only if needed to link QA-T003 docs/reports and preserve `No NullForge implementation code has started.` and `REPO_SOURCE_IMPORT_BASELINE`.
7. Create QA-T003 implementation reports.
8. Run bounded checks only.

## Required Checks

The later implementor should run only bounded checks such as:

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

Do not run `python -m pip install`, `pip install`, `python -m pytest`, docs generation, docs build, quickstart, CI smoke, venv, package build, or environment repair commands.

## Human Gates

Human approval is required before:

- any install, uninstall, editable install, dependency sync, package build, venv creation/activation, or environment repair command;
- changing `pyproject.toml`, dependencies, package metadata, source, tests, schemas, fixtures, CI, README, generated docs, docs/reference, or tools;
- adding `[project.scripts]`, `console_scripts`, or `src/research_core/__main__.py`;
- running full tests, docs generation, docs build, quickstart commands, or CI smoke commands;
- starting `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

## Stop Conditions

Stop if:

- working tree changes appear outside allowed QA-T003 files;
- a prerequisite audit is missing or no longer `PASS`;
- implementing the decision packet requires live environment mutation;
- a repair path must be chosen without human direction;
- source/package/test/CI/generated-doc changes appear necessary;
- command output would require exposing unsanitized local/private paths;
- the scope drifts toward implementation, test creation, dependency changes, app work, or `ADR-T003`.

## Rollback / Repair Route

If the implementor creates an incorrect decision packet, repair should be docs-only and limited to:

- `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/QA-T003/*`

No environment state, package/source files, tests, schemas, fixtures, CI, or generated docs may be changed as repair for QA-T003.

## Ready-For-Implementor Verdict

Ready for implementor.

The implementor must produce a docs-only human gate packet and reports. QA-T003 must not repair the environment or run repair commands.
