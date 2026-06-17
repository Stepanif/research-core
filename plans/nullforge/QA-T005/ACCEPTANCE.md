# QA-T005 Acceptance

Date: `2026-06-16`

Ticket: `QA-T005`

Role: Planner

Status: Ready for conditional implementor handoff

No NullForge implementation code has started.

## Required Outputs

The planner must create only:

- `plans/nullforge/QA-T005/PLAN.md`
- `plans/nullforge/QA-T005/ACCEPTANCE.md`
- `plans/nullforge/QA-T005/IMPLEMENTOR_PROMPT.md`

No reports, audits, QA docs, tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, or downstream artifacts may be created by planning.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| `QA-T005-AC-001` | Planner artifacts identify QA-T005 as a human-approved local Python environment repair/readiness execution path planning ticket. |
| `QA-T005-AC-002` | Planner artifacts preserve `No NullForge implementation code has started.` |
| `QA-T005-AC-003` | Planner artifacts cite prerequisite audit `PASS` evidence for QA-T001, HY-T001, QA-T002, QA-T003, and QA-T004. |
| `QA-T005-AC-004` | Planner artifacts describe the unresolved blocker: `<local-temp-editable-install>`, invisible `research_core.cli`, `python -m research_core.cli --help` failing with `No module named research_core.cli`, unsupported `python -m research_core --help`, and unsupported `research-core --help`. |
| `QA-T005-AC-005` | Planner artifacts include the QA-T004 recommended isolated project-local virtual environment path as the default candidate path, without executing it. |
| `QA-T005-AC-006` | Candidate command packet entries are labeled `not run` and require explicit human authorization. |
| `QA-T005-AC-007` | Human-gate policy requires explicit approval before any environment mutation or validation command. |
| `QA-T005-AC-008` | Side-effect policy covers Python environment, venv artifacts, bytecode/cache, editable install state, `.pytest_cache/`, `exec_outputs/`, generated docs, local paths, and source/package/test/CI files. |
| `QA-T005-AC-009` | Proposed later implementor allowed files are bounded to NullForge QA execution docs, status/source index docs, and QA-T005 reports. |
| `QA-T005-AC-010` | Planner artifacts forbid source/package/dependency/test/schema/fixture/CI/generated-doc/README/docs/reference/tool changes. |
| `QA-T005-AC-011` | Planner artifacts forbid `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, public distribution, or downstream work. |
| `QA-T005-AC-012` | Required bounded checks pass. |

## Required Checks

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `Test-Path -LiteralPath plans\nullforge\QA-T005\PLAN.md`
- `Test-Path -LiteralPath plans\nullforge\QA-T005\ACCEPTANCE.md`
- `Test-Path -LiteralPath plans\nullforge\QA-T005\IMPLEMENTOR_PROMPT.md`
- `rg -n "Decision: PASS" audits\nullforge\QA-T001\AUDIT_REPORT.md audits\nullforge\HY-T001\AUDIT_REPORT.md audits\nullforge\QA-T002\AUDIT_REPORT.md audits\nullforge\QA-T003\AUDIT_REPORT.md audits\nullforge\QA-T004\AUDIT_REPORT.md`
- `rg -n "QA-T005|QA-T004|python -m research_core.cli|No module named research_core.cli|local-temp-editable-install|No NullForge implementation code has started" plans\nullforge\QA-T005\PLAN.md plans\nullforge\QA-T005\ACCEPTANCE.md plans\nullforge\QA-T005\IMPLEMENTOR_PROMPT.md`

## Forbidden-Pass Conditions

QA-T005 planning must not pass if:

- any environment-changing command was run;
- any CLI validation command was run;
- any install, uninstall, editable install, dependency sync, package build, virtual-environment creation/activation, full test, docs generation, docs build, quickstart, or CI smoke command was run;
- existing files outside `plans/nullforge/QA-T005/` were modified;
- reports, audits, QA docs, tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, or downstream artifacts were created;
- candidate commands are presented as approved or already run;
- human gates are missing or weakened;
- the plan permits source/package changes or downstream work without separate scoped approval;
- required checks fail.

## Source-Of-Truth Updates

No source-of-truth updates are required during planning.

A later implementor may update `docs/nullforge/CURRENT_STATUS.md` and `docs/nullforge/SOURCE_INDEX.md` only if explicitly allowed by the implementor prompt and only within QA-T005 scope.

## Done Definition

QA-T005 planning is done when:

- the three planner artifacts exist;
- required checks pass;
- human gates and stop conditions are explicit;
- the plan is ready for conditional implementor handoff;
- no environment, source, package, dependency, test, schema, fixture, CI, generated-doc, raw/private data, or downstream work was performed.
