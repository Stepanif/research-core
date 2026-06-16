# MB-T001 Implementor Prompt

You are Codex working in `C:\Users\Filip\Desktop\Repos\research-core`.

Task: implement `MB-T001` only. Do not commit.

## Context

- `MB-T001` planner artifacts exist under `plans/nullforge/MB-T001/`.
- Completed M0 dependencies have audit `PASS`: `PF-T000`, `PF-T001`, `PF-T002`, `ADR-T001`, `ADR-T002`, and `CX-T001`.
- `MB-T001` is the NullForge M0 milestone handoff ticket.
- `MB-T001` must summarize M0 readiness and prepare handoff only.
- No NullForge implementation code has started.
- Do not start M1, `QA-T001`, `ADR-T003`, implementation work, or downstream work.

## Read First

- `plans/nullforge/MB-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/MB-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/MB-T001/PLAN.md`
- `plans/nullforge/MB-T001/ACCEPTANCE.md`
- `plans/nullforge/MB-T001/IMPLEMENTOR_PROMPT.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/DECISION_LEDGER.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `audits/nullforge/PF-T000/AUDIT_REPORT.md`
- `audits/nullforge/PF-T001/AUDIT_REPORT.md`
- `audits/nullforge/PF-T002/AUDIT_REPORT.md`
- `audits/nullforge/ADR-T001/AUDIT_REPORT.md`
- `audits/nullforge/ADR-T002/AUDIT_REPORT.md`
- `audits/nullforge/CX-T001/AUDIT_REPORT.md`
- `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`
- `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md`

## Allowed Files

- `docs/nullforge/M0_HANDOFF.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/MB-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/MB-T001/CHANGED_FILES.md`
- `reports/nullforge/MB-T001/TEST_RESULTS.md`
- `reports/nullforge/MB-T001/AUDITOR_PROMPT.md`

## Treat As Read-Only

- `plans/nullforge/MB-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/MB-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/MB-T001/PLAN.md`
- `plans/nullforge/MB-T001/ACCEPTANCE.md`
- `plans/nullforge/MB-T001/IMPLEMENTOR_PROMPT.md`
- `docs/nullforge/DECISION_LEDGER.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/adr/`
- `docs/nullforge/blueprint/volumes/`
- `audits/nullforge/`
- existing plans and reports outside `reports/nullforge/MB-T001/`
- ResearchCore Engine docs/code

## Forbidden

- Do not create audits for MB-T001.
- Do not create `tickets/`, `milestones/`, `prompts/`, QA docs, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, ES-derived fixtures, or downstream artifacts.
- Do not modify ResearchCore Engine docs/code.
- Do not modify `docs/nullforge/DECISION_LEDGER.md` unless you stop and ask for human approval first.
- Do not import incoming package milestone docs, ticket queues, prompt files, old chat logs, raw/private data, or full ES.zip contents into repo-local canonical paths.
- Do not start M1, `QA-T001`, `ADR-T003`, desktop shell, bridge, sidecar, dataset, parser, fixture, packaging, release, cloud, telemetry, auth, billing, broker/live, mobile, marketplace, or public distribution work.
- Do not claim legal/trademark clearance, product validation, user validation, market validation, trading validity, financial advice safety, data licensing safety, public distribution safety, Tauri feasibility, bridge reliability, packaging feasibility, cloud absence enforcement, or telemetry enforcement.

## Required Work

1. Verify current status and all six prerequisite audit `PASS` dispositions.
2. Create `docs/nullforge/M0_HANDOFF.md`.
3. Update `docs/nullforge/CURRENT_STATUS.md` for `MB-T001` in-progress handoff state while preserving:
   - `REPO_SOURCE_IMPORT_BASELINE`
   - `No NullForge implementation code has started.`
   - M1, `QA-T001`, `ADR-T003`, and downstream work as not started.
4. Update `docs/nullforge/SOURCE_INDEX.md` to link:
   - `docs/nullforge/M0_HANDOFF.md`
   - MB-T001 context/planner artifacts
   - MB-T001 report artifacts after creation.
5. Create MB-T001 implementation reports:
   - `reports/nullforge/MB-T001/IMPLEMENTATION_REPORT.md`
   - `reports/nullforge/MB-T001/CHANGED_FILES.md`
   - `reports/nullforge/MB-T001/TEST_RESULTS.md`
   - `reports/nullforge/MB-T001/AUDITOR_PROMPT.md`
6. Run and record the bounded checks listed below.

## M0 Handoff Doc Requirements

`docs/nullforge/M0_HANDOFF.md` must include:

- M0 title: `Repo Source Import + Canonical Baseline`.
- M0 goal and result.
- Overall status for MB-T001 implementation, such as ready for independent audit, not audit `PASS`.
- Completed ticket table for `PF-T000`, `PF-T001`, `PF-T002`, `ADR-T001`, `ADR-T002`, and `CX-T001` with audit `PASS` evidence.
- MB-T001 row/status as in progress or pending independent audit.
- Artifacts produced by M0: active docs, imported volumes, ADRs, role-loop doc, plans, reports, and audits.
- Accepted decisions from `NF-D0001` through `NF-D0005`.
- Pending/deferred status for `NF-D0006` or equivalent milestone/ticket/prompt import.
- Tests/checks summary.
- Scope drift section.
- Human decisions needed after audit.
- Claims, risks, and non-proofs.
- M1 readiness statement that names `QA-T001` only as the next recommended scoped ticket after MB-T001 audit/closeout.
- Exact sentence: `No NullForge implementation code has started.`

## Checks To Run

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `Test-Path -LiteralPath docs\nullforge\M0_HANDOFF.md`
- `Test-Path -LiteralPath reports\nullforge\MB-T001\IMPLEMENTATION_REPORT.md`
- `Test-Path -LiteralPath reports\nullforge\MB-T001\CHANGED_FILES.md`
- `Test-Path -LiteralPath reports\nullforge\MB-T001\TEST_RESULTS.md`
- `Test-Path -LiteralPath reports\nullforge\MB-T001\AUDITOR_PROMPT.md`
- `rg -n "Decision: PASS" audits\nullforge\PF-T000\AUDIT_REPORT.md audits\nullforge\PF-T001\AUDIT_REPORT.md audits\nullforge\PF-T002\AUDIT_REPORT.md audits\nullforge\ADR-T001\AUDIT_REPORT.md audits\nullforge\ADR-T002\AUDIT_REPORT.md audits\nullforge\CX-T001\AUDIT_REPORT.md`
- `rg -n "M0|MB-T001|PF-T000|PF-T001|PF-T002|ADR-T001|ADR-T002|CX-T001|PASS|QA-T001|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\M0_HANDOFF.md docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md`
- `git diff --name-only -- src tests schemas fixtures package.json pnpm-lock.yaml pnpm-workspace.yaml .github docs\backend docs\kernel docs\qa docs\security docs\setup docs\codex docs\workflows README.md`
- `Test-Path -LiteralPath tickets`
- `Test-Path -LiteralPath milestones`
- `Test-Path -LiteralPath prompts`
- `Test-Path -LiteralPath docs\nullforge\qa`
- `Test-Path -LiteralPath audits\nullforge\MB-T001`
- Validate that repo-local Markdown links added to `SOURCE_INDEX.md` resolve.

## Report

Report:

- changed files;
- checks run;
- human gates;
- whether MB-T001 is ready for independent audit.

Do not commit.
