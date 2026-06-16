# MB-T001 Acceptance

Ticket: `MB-T001`

Role: Planner

Date: `2026-06-16`

## Required Outcome

The later MB-T001 implementor must create a docs-only M0 handoff package that summarizes completed M0 readiness without starting M1, `QA-T001`, `ADR-T003`, implementation work, or downstream work.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| `MB-A001` | `docs/nullforge/M0_HANDOFF.md` exists and is the only new active NullForge handoff doc. |
| `MB-A002` | The handoff identifies M0 as `Repo Source Import + Canonical Baseline`. |
| `MB-A003` | The handoff lists `PF-T000`, `PF-T001`, `PF-T002`, `ADR-T001`, `ADR-T002`, and `CX-T001` with audit `PASS` evidence. |
| `MB-A004` | The handoff records `MB-T001` as in progress or pending audit, not as independently audited `PASS`. |
| `MB-A005` | The handoff preserves `No NullForge implementation code has started.` |
| `MB-A006` | The handoff records M0 non-goals: no Tauri app, no engine changes, no dataset parser, no fixture creation, no desktop bridge implementation, no public release, and no repo rename. |
| `MB-A007` | ADR-T001 boundaries remain intact: `NullForge` is a working product name only, Windows 11 x64 is first proof target, Tauri + React/TypeScript is a default direction only, and ResearchCore Engine remains separate engine truth. |
| `MB-A008` | ADR-T002 boundaries remain intact: local-first/no-cloud is a planning boundary only, and cloud/auth/billing/telemetry/mobile/marketplace/broker-live/live execution/public distribution remain out of MVP scope. |
| `MB-A009` | `NF-D0006` or equivalent milestone/ticket/prompt import status remains pending/deferred unless a human prompt explicitly authorizes promotion. |
| `MB-A010` | `QA-T001` is mentioned only as a recommended next scoped ticket after MB-T001 audit/closeout, not as started work. |
| `MB-A011` | `CURRENT_STATUS.md` keeps `REPO_SOURCE_IMPORT_BASELINE`, keeps the exact no-code sentence, marks `MB-T001` as the active/in-progress ticket, and keeps M1/`QA-T001` downstream. |
| `MB-A012` | `SOURCE_INDEX.md` links the M0 handoff doc, MB-T001 context/planner artifacts, and MB-T001 implementation report artifacts after creation. |
| `MB-A013` | MB-T001 reports exist under `reports/nullforge/MB-T001/`: `IMPLEMENTATION_REPORT.md`, `CHANGED_FILES.md`, `TEST_RESULTS.md`, and `AUDITOR_PROMPT.md`. |
| `MB-A014` | No MB-T001 audit artifacts are created by the implementor. |
| `MB-A015` | No `tickets/`, `milestones/`, `prompts/`, QA docs, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw/private data, ES-derived fixtures, or downstream artifacts are created. |
| `MB-A016` | ResearchCore Engine docs/code and existing M0 source artifacts are not modified except for explicitly allowed status/source index updates. |
| `MB-A017` | Required checks are run and recorded in `reports/nullforge/MB-T001/TEST_RESULTS.md`. |
| `MB-A018` | The auditor prompt is bounded to MB-T001 only and asks for PASS/HOLD/REJECT. |

## Required Checks

The later implementor must run and record:

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

The later implementor should also run a repo-local Markdown link validation for any links added to `SOURCE_INDEX.md`.

## Failure Conditions

Any of the following should block readiness for audit:

- A prerequisite audit report is missing or lacks `Decision: PASS`.
- `No NullForge implementation code has started.` is removed or contradicted.
- `QA-T001`, `ADR-T003`, M1, app/code/test/schema/fixture/package/CI/generated-doc work, or downstream artifacts are started.
- ResearchCore Engine docs/code are modified.
- `tickets/`, `milestones/`, or `prompts/` are created without explicit human authorization.
- Incoming package milestone docs, ticket queues, prompt files, raw/private data, old chats, or full ES.zip contents are promoted without explicit human authorization.
- MB-T001 audit files are created by the implementor.

## Human Gates

Human decision is required before:

- creating `tickets/`, `milestones/`, or `prompts/`;
- modifying `DECISION_LEDGER.md`;
- promoting pending milestone/ticket/prompt imports;
- changing ResearchCore Engine truth;
- starting M1, `QA-T001`, `ADR-T003`, or downstream work;
- making public release, legal, financial, market, trading, data licensing, Tauri feasibility, bridge reliability, packaging feasibility, cloud enforcement, telemetry enforcement, or product validation claims.

## Ready For Implementor Verdict

YES.

The acceptance surface is bounded to M0 handoff documentation and reports.
