# DA-T001 Acceptance

Date: `2026-06-17`

Ticket: `DA-T001`

Title: Desktop bridge contract finalization

Role: Planner

Status: Ready for implementor handoff

No NullForge implementation code has started.

## Required Planner Outputs

This planner pass must create only:

- `plans/nullforge/DA-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/DA-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/DA-T001/PLAN.md`
- `plans/nullforge/DA-T001/ACCEPTANCE.md`
- `plans/nullforge/DA-T001/IMPLEMENTOR_PROMPT.md`

No DA-T001 implementation docs, reports, audits, architecture docs, status/source-index updates, code, tests, schemas, fixtures, package files, dependencies, CI, generated docs, tickets, milestones, prompts, raw/private data, app files, bridge files, or sidecar files may be created by this planner pass.

## Required Later Implementor Outputs

A later DA-T001 implementor should create or update only:

- `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T001/CHANGED_FILES.md`
- `reports/nullforge/DA-T001/TEST_RESULTS.md`
- `reports/nullforge/DA-T001/AUDITOR_PROMPT.md`

## Acceptance Criteria

| ID | Criterion |
|---|---|
| `DA-T001-AC-001` | Planner artifacts identify DA-T001 as desktop bridge contract finalization. |
| `DA-T001-AC-002` | Planner artifacts preserve `No NullForge implementation code has started.` |
| `DA-T001-AC-003` | Planner artifacts cite current status/source docs and prior audit `PASS` evidence through QA-T005. |
| `DA-T001-AC-004` | Planner artifacts cite Volume 3 as the primary bridge contract draft and Volume 7 as the M1/DA-T001 roadmap source. |
| `DA-T001-AC-005` | Planner artifacts cite ADR-T001 and ADR-T002 as active decisions governing platform, stack direction, engine boundary, local-first, and no-cloud scope. |
| `DA-T001-AC-006` | Planned implementation target is `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`. |
| `DA-T001-AC-007` | Planned bridge contract scope requires allowlisted structured command IDs and forbids arbitrary shell execution. |
| `DA-T001-AC-008` | Planned bridge contract scope distinguishes planned candidate bridge commands from currently proven ResearchCore Engine behavior. |
| `DA-T001-AC-009` | Planned bridge contract scope preserves QA-T005 limitations: readiness proof is scoped to `.venv-qa-t005` and `python -m research_core.cli --help`. |
| `DA-T001-AC-010` | Planner artifacts forbid Tauri/Rust/React/Python bridge/sidecar/app scaffolding and implementation. |
| `DA-T001-AC-011` | Planner artifacts forbid source/package/dependency/test/schema/fixture/generated-doc/CI/README/docs-reference/tool changes. |
| `DA-T001-AC-012` | Planner artifacts forbid cloud, network, telemetry, auth, billing, broker/live, AI/model, updater, signing, public release, and financial advice scope. |
| `DA-T001-AC-013` | Required checks pass or any skipped checks are recorded with exact reason. |

## Required Planner Checks

- `git status --short --untracked-files=all`
- `git diff --check`
- `Test-Path -LiteralPath plans\nullforge\DA-T001\CONTEXT_BUNDLE.md`
- `Test-Path -LiteralPath plans\nullforge\DA-T001\CONTEXT_BUNDLE_MANIFEST.md`
- `Test-Path -LiteralPath plans\nullforge\DA-T001\PLAN.md`
- `Test-Path -LiteralPath plans\nullforge\DA-T001\ACCEPTANCE.md`
- `Test-Path -LiteralPath plans\nullforge\DA-T001\IMPLEMENTOR_PROMPT.md`
- `rg -n "Decision: PASS" audits\nullforge\PF-T000\AUDIT_REPORT.md audits\nullforge\PF-T001\AUDIT_REPORT.md audits\nullforge\PF-T002\AUDIT_REPORT.md audits\nullforge\ADR-T001\AUDIT_REPORT.md audits\nullforge\ADR-T002\AUDIT_REPORT.md audits\nullforge\CX-T001\AUDIT_REPORT.md audits\nullforge\MB-T001\AUDIT_REPORT.md audits\nullforge\QA-T001\AUDIT_REPORT.md audits\nullforge\HY-T001\AUDIT_REPORT.md audits\nullforge\QA-T002\AUDIT_REPORT.md audits\nullforge\QA-T003\AUDIT_REPORT.md audits\nullforge\QA-T004\AUDIT_REPORT.md audits\nullforge\QA-T005\AUDIT_REPORT.md`
- `rg -n "DA-T001|ENGINE_BRIDGE_CONTRACT|No NullForge implementation code has started|allowlist|arbitrary shell|\\.venv-qa-t005|python -m research_core.cli --help|network|broker|live" plans\nullforge\DA-T001`

## Later Implementor Required Checks

The implementor should run:

- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- path existence checks for the bridge contract and DA-T001 reports
- prerequisite audit `Decision: PASS` checks through QA-T005
- content checks for contract target, no-code sentence, allowlist boundary, arbitrary shell prohibition, QA-T005 limitation, and excluded network/broker/live scope
- forbidden-path diff checks for source, package, dependency, test, schema, fixture, generated-doc, CI, README, docs/reference, and tools
- absence checks for `tickets`, `milestones`, and `prompts`

## Source-Of-Truth Updates Expected Later

DA-T001 implementation should:

- create `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md` as an active docs-only source after audit disposition;
- update `docs/nullforge/SOURCE_INDEX.md` to link the contract and DA-T001 artifacts that exist;
- update `docs/nullforge/CURRENT_STATUS.md` only within DA-T001 scope;
- preserve `No NullForge implementation code has started.`

## Forbidden-Pass Conditions

DA-T001 planning or implementation must not pass if:

- Tauri, Rust, React, TypeScript, JavaScript, Python bridge, sidecar, app, package, dependency, schema, test, fixture, generated-doc, CI, or source code is created or modified;
- ResearchCore Engine behavior, CLI entrypoints, package metadata, or docs/reference files are changed;
- install, environment repair, full test, docs build, CI smoke, quickstart, Tauri, Node, Rust, bridge, sidecar, app, or runtime validation commands are run;
- the contract claims bridge implementation, Tauri feasibility, packaging feasibility, telemetry enforcement, no-cloud technical enforcement, product validation, user validation, market validation, legal/trademark clearance, trading validity, financial advice safety, or public distribution safety;
- bridge command IDs are described as implemented without evidence;
- arbitrary shell execution is permitted;
- broad filesystem scan, network/cloud/telemetry/auth/billing/broker/live/AI/updater/public release behavior is permitted;
- raw/full ES.zip, private/local data, generated datasets, or ES-derived fixtures are introduced;
- required checks fail without a documented blocker.

## Done Definition

This planner pass is done when:

- the five DA-T001 planner artifacts exist;
- required planner checks pass;
- the later implementor scope is bounded to docs/status/source-index/reports only;
- human gates are explicit;
- no implementation, environment, dependency, runtime, app, bridge, sidecar, data, test, schema, fixture, generated-doc, CI, or downstream work was performed.

Later DA-T001 implementation is done only after its docs-only artifacts exist, required checks are recorded, reports are created, and an independent audit is ready to run.
