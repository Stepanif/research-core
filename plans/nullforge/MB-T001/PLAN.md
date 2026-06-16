# MB-T001 Plan

Ticket: `MB-T001`

Role: Planner

Date: `2026-06-16`

Planner verdict: READY_FOR_IMPLEMENTOR

## Goal

Create a bounded NullForge M0 milestone handoff package that summarizes M0 repo source import readiness, records completed dependency audit evidence, preserves the current no-implementation boundary, and prepares the next human-scoped decision point after M0.

`MB-T001` is docs-only. It does not start M1, `QA-T001`, `ADR-T003`, implementation work, or downstream work.

## Source Context Used

- `plans/nullforge/MB-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/MB-T001/CONTEXT_BUNDLE_MANIFEST.md`
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

## Assumptions

- The worktree begins with only MB-T001 planner artifacts uncommitted.
- The six prerequisite tickets are complete with audit `PASS`: `PF-T000`, `PF-T001`, `PF-T002`, `ADR-T001`, `ADR-T002`, and `CX-T001`.
- `MB-T001` may create a repo-local M0 handoff doc under `docs/nullforge/` without creating `milestones/nullforge/`.
- `MB-T001` may update `CURRENT_STATUS.md` and `SOURCE_INDEX.md` to reflect MB-T001 in-progress implementation state and link the MB-T001 artifacts it creates.
- `No NullForge implementation code has started.` must remain present and true.
- `QA-T001` may be named only as the likely next scoped ticket after M0 handoff audit/closeout; it must not be started.

## Implementation Scope For Later Implementor

The implementor should:

1. Verify all six prerequisite audit reports contain `Decision: PASS`.
2. Create a concise M0 handoff document summarizing:
   - M0 goal and result;
   - completed M0 ticket list and audit dispositions;
   - produced docs, plans, reports, and audits;
   - accepted decisions and pending/deferred items;
   - scope drift check;
   - claim/risk status;
   - human decisions needed after audit;
   - M1 readiness limits and the next scoped-ticket recommendation.
3. Update `CURRENT_STATUS.md` to make `MB-T001` the active ticket during implementation and preserve `REPO_SOURCE_IMPORT_BASELINE`.
4. Update `SOURCE_INDEX.md` to link the MB-T001 handoff doc, planner artifacts, and implementation report artifacts after creation.
5. Create standard MB-T001 implementation report artifacts.
6. Record bounded checks and prepare the auditor prompt.

## Proposed Allowed Files For Later Implementor

- `docs/nullforge/M0_HANDOFF.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/MB-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/MB-T001/CHANGED_FILES.md`
- `reports/nullforge/MB-T001/TEST_RESULTS.md`
- `reports/nullforge/MB-T001/AUDITOR_PROMPT.md`

Read-only during implementation:

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
- prior `plans/nullforge/`, `reports/nullforge/`, and existing M0 artifacts.
- ResearchCore Engine docs/code.

## Explicitly Out Of Scope

- Creating `tickets/nullforge/`.
- Creating `milestones/nullforge/`.
- Creating `prompts/`.
- Creating QA docs.
- Creating audits for MB-T001.
- Starting M1, `QA-T001`, `ADR-T003`, or downstream tickets.
- Creating app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, ES-derived fixtures, or release artifacts.
- Modifying ResearchCore Engine docs/code, package metadata, schemas, tests, generated references, or implementation behavior.
- Importing incoming package milestone docs, ticket queues, human-gate docs, prompt files, old chat logs, or full ES.zip contents into canonical repo paths.
- Making claims of legal/trademark clearance, public distribution safety, product validation, user validation, market validation, trading validity, financial advice safety, data licensing safety, Tauri feasibility, bridge reliability, packaging feasibility, cloud absence enforcement, or telemetry enforcement.

## Acceptance Criteria

- `docs/nullforge/M0_HANDOFF.md` exists and is docs-only.
- `M0_HANDOFF.md` identifies `M0` as `Repo Source Import + Canonical Baseline`.
- `M0_HANDOFF.md` includes the completed M0 dependency table for `PF-T000`, `PF-T001`, `PF-T002`, `ADR-T001`, `ADR-T002`, and `CX-T001`, each with audit `PASS` evidence.
- `M0_HANDOFF.md` states `MB-T001` is the active handoff ticket and does not give itself audit `PASS` before independent audit.
- `M0_HANDOFF.md` records that no NullForge implementation code has started.
- `M0_HANDOFF.md` records M0 non-goals and out-of-scope boundaries.
- `M0_HANDOFF.md` records accepted ADR boundaries from ADR-T001 and ADR-T002 without broadening them.
- `M0_HANDOFF.md` records `NF-D0006` or equivalent pending milestone/ticket/prompt import as unresolved/deferred, not promoted.
- `M0_HANDOFF.md` names `QA-T001` only as a recommended next scoped ticket after MB-T001 audit/closeout, not as started work.
- `CURRENT_STATUS.md` keeps `REPO_SOURCE_IMPORT_BASELINE`, keeps `No NullForge implementation code has started.`, names `MB-T001` as active/in progress, and keeps M1/`QA-T001` downstream.
- `SOURCE_INDEX.md` links the M0 handoff doc, MB-T001 planner artifacts, and MB-T001 implementation reports after creation.
- No `tickets/`, `milestones/`, `prompts/`, QA docs, audits for MB-T001, code, tests, schemas, fixtures, package files, CI, generated docs, raw/private data, ES-derived fixtures, or downstream artifacts are created.
- ResearchCore Engine docs/code remain unchanged.
- Required checks are run and recorded in `reports/nullforge/MB-T001/TEST_RESULTS.md`.
- `reports/nullforge/MB-T001/AUDITOR_PROMPT.md` is ready for an independent audit.

## Required Checks For Later Implementor

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

The implementor should also validate that repo-local Markdown links added to `SOURCE_INDEX.md` resolve.

## Human Gates And Stop Conditions

Human gate triggers:

- Creating or importing `tickets/`, `milestones/`, or `prompts/`.
- Promoting incoming package milestone docs, ticket queues, prompt files, old chats, raw/private data, or full ES.zip contents into active repo-local truth.
- Updating `DECISION_LEDGER.md` beyond existing accepted/pending decisions.
- Changing ResearchCore Engine docs/code or repo/package/CLI identity.
- Starting M1, `QA-T001`, `ADR-T003`, app/code implementation, tests, schemas, fixtures, dependencies, package files, CI, generated docs, release work, network/cloud/telemetry/auth/billing/broker/live scope, or public distribution.
- Making product, legal, financial, market, trading, release, data licensing, Tauri feasibility, bridge reliability, packaging feasibility, cloud enforcement, or telemetry enforcement claims.

Stop conditions:

- Any prerequisite audit is missing or not `PASS`.
- Required MB-T001 allowed paths are insufficient.
- `No NullForge implementation code has started.` cannot be preserved truthfully.
- A required change would modify read-only files or forbidden areas.
- A human gate triggers and is unresolved.

## Rollback Or Repair Route

If implementation finds a bounded documentation issue, repair only the allowed MB-T001 implementation files and record the change in `reports/nullforge/MB-T001/CHANGED_FILES.md`.

If implementation discovers a missing prerequisite, source mismatch, forbidden file need, or human-gated decision, stop and write the needed decision in the implementation report instead of broadening scope.

If audit later returns `HOLD`, repair only findings listed by the MB-T001 auditor. If audit returns `REJECT`, stop and request human direction.

## Ready For Implementor Verdict

YES.

The context is bounded and sufficient for a docs-only MB-T001 implementation pass.
