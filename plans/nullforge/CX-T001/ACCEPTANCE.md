# CX-T001 Acceptance

Ticket: `CX-T001` - NullForge Codex role-loop docs
Date: `2026-06-16`

## Testable Acceptance Criteria

- `docs/nullforge/codex/CODEX_ROLE_LOOP.md` exists.
- `docs/nullforge/CURRENT_STATUS.md` is updated.
- `docs/nullforge/SOURCE_INDEX.md` is updated.
- `reports/nullforge/CX-T001/IMPLEMENTATION_REPORT.md` exists.
- `reports/nullforge/CX-T001/CHANGED_FILES.md` exists.
- `reports/nullforge/CX-T001/TEST_RESULTS.md` exists.
- `reports/nullforge/CX-T001/AUDITOR_PROMPT.md` exists.
- CODEX_ROLE_LOOP date is `2026-06-16`.
- CODEX_ROLE_LOOP status makes clear the doc is CX-T001 workflow/source documentation and is not implementation proof.
- CODEX_ROLE_LOOP confirms ADR-T002 audit `PASS` as prerequisite evidence.
- CODEX_ROLE_LOOP states `No NullForge implementation code has started.`
- CODEX_ROLE_LOOP describes the role loop:
  - Human / ChatGPT Architect;
  - Context Curator;
  - Planner;
  - Implementor / Codex;
  - Auditor;
  - Repair Implementor if needed;
  - Human gate;
  - next ticket.
- CODEX_ROLE_LOOP defines required artifact paths under `plans/nullforge/[TICKET_ID]/`, `reports/nullforge/[TICKET_ID]/`, and `audits/nullforge/[TICKET_ID]/`.
- CODEX_ROLE_LOOP defines required contents for context bundle, context bundle manifest, plan, acceptance, implementor prompt, implementation report, changed files, test results, auditor prompt, audit report, findings, and repair prompt.
- CODEX_ROLE_LOOP defines PASS, HOLD, and REJECT conditions.
- CODEX_ROLE_LOOP records human gate triggers and stop conditions.
- CODEX_ROLE_LOOP records source-of-truth, archive, quarantine, and prompt handling rules.
- CODEX_ROLE_LOOP preserves ADR-T001 working name/platform/stack/engine boundaries.
- CODEX_ROLE_LOOP preserves ADR-T002 local-first/no-cloud MVP boundaries.
- CODEX_ROLE_LOOP does not claim Tauri feasibility, packaging feasibility, bridge reliability, workspace safety, telemetry enforcement, cloud-security proof, legal/trademark clearance, public distribution safety, financial advice safety, trading validity, product validation, user validation, market validation, data licensing safety, or implementation proof.
- `docs/nullforge/CURRENT_STATUS.md` keeps active phase `REPO_SOURCE_IMPORT_BASELINE`, names active ticket `CX-T001`, and points next action to `MB-T001` after CX-T001 audit disposition.
- `docs/nullforge/CURRENT_STATUS.md` still contains the exact sentence `No NullForge implementation code has started.`
- `docs/nullforge/SOURCE_INDEX.md` links `docs/nullforge/codex/CODEX_ROLE_LOOP.md` with a repo-local Markdown link that resolves.
- `docs/nullforge/SOURCE_INDEX.md` links only to existing CX-T001 plan and report files after they are created.
- `docs/nullforge/SOURCE_INDEX.md` does not create broken links to missing ticket, milestone, prompt, CX-T001 audit, MB-T001, ADR-T003, M1, or downstream files.
- `docs/nullforge/DECISION_LEDGER.md` is not changed unless a human-approved decision gate is triggered.
- No existing ResearchCore Engine docs are modified.
- No root README, docs index, docs status, docs architecture, docs navigation, generated reference docs, package files, CI files, code, tests, schemas, tools, milestones, tickets, prompts, raw data, generated data, ES-derived fixtures, CX-T001 audit files, MB-T001, ADR-T003, or M1 files are created or modified.
- No implementation, data import, fixture creation, Tauri scaffold, bridge/sidecar work, telemetry implementation, cloud/auth/billing work, broker/live work, public release work, or downstream ticket work is started.

## Required Outputs

Implementation outputs:

```text
docs/nullforge/codex/CODEX_ROLE_LOOP.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
reports/nullforge/CX-T001/IMPLEMENTATION_REPORT.md
reports/nullforge/CX-T001/CHANGED_FILES.md
reports/nullforge/CX-T001/TEST_RESULTS.md
reports/nullforge/CX-T001/AUDITOR_PROMPT.md
```

Planner outputs already created by this planner pass:

```text
plans/nullforge/CX-T001/CONTEXT_BUNDLE.md
plans/nullforge/CX-T001/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/CX-T001/PLAN.md
plans/nullforge/CX-T001/ACCEPTANCE.md
plans/nullforge/CX-T001/IMPLEMENTOR_PROMPT.md
```

## Required Checks And Commands

Run and record:

```powershell
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
git diff --check
```

Run and record `Test-Path -LiteralPath` checks for:

```text
docs\nullforge\codex\CODEX_ROLE_LOOP.md
reports\nullforge\CX-T001\IMPLEMENTATION_REPORT.md
reports\nullforge\CX-T001\CHANGED_FILES.md
reports\nullforge\CX-T001\TEST_RESULTS.md
reports\nullforge\CX-T001\AUDITOR_PROMPT.md
```

Run and record:

```powershell
rg -n "Decision: PASS" audits\nullforge\ADR-T002\AUDIT_REPORT.md
rg -n "Context Curator|Planner|Implementor|Auditor|PASS|HOLD|REJECT|human gate|stop condition|No NullForge implementation code has started|CX-T001|MB-T001" docs\nullforge\codex\CODEX_ROLE_LOOP.md
rg -n "CX-T001|CODEX_ROLE_LOOP|MB-T001|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md
```

Manual review required:

- Confirm all repo-local Markdown links in `docs/nullforge/SOURCE_INDEX.md` resolve to existing repo files.
- Confirm external incoming package sources, if mentioned, are recorded as plain text/external inputs and not broken repo-local links.
- Confirm changed files are limited to:
  - `plans/nullforge/CX-T001/`
  - `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
  - `docs/nullforge/CURRENT_STATUS.md`
  - `docs/nullforge/SOURCE_INDEX.md`
  - `reports/nullforge/CX-T001/`
- Confirm no `README.md`, `docs/index.md`, `docs/STATUS.md`, `docs/ARCHITECTURE.md`, `docs/reference/`, `docs/contributing/`, `src/`, `tests/`, `schemas/`, `configs/`, `tools/`, package files, `mkdocs.yml`, `.github/`, milestone files, ticket files, prompt files, raw data, generated data, ES-derived fixtures, CX-T001 audit files, MB-T001, ADR-T003, or M1 files changed.
- Confirm CX-T001 does not start implementation or assert proof/validation/legal/trading/data-safety claims.

Optional checks:

- Docs build checks are skipped unless docs navigation, mkdocs-visible configuration, generated docs tooling, package files, or generated reference files are changed.
- Do not install dependencies. If optional checks are skipped, record why in `TEST_RESULTS.md`.

## Scope Question Resolutions To Verify

- CX-T001 creates one workflow doc: `docs/nullforge/codex/CODEX_ROLE_LOOP.md`.
- CX-T001 updates `docs/nullforge/CURRENT_STATUS.md`.
- CX-T001 updates `docs/nullforge/SOURCE_INDEX.md`.
- CX-T001 does not update `docs/nullforge/DECISION_LEDGER.md` unless a human-approved decision gate is triggered.
- CX-T001 keeps MB-T001 pending only and does not start it.
- CX-T001 does not create ticket files, milestone files, prompt archives, QA docs, audit files, app files, code, schemas, tests, fixtures, or dependencies.

## Conditions That Force HOLD Or REJECT

Return HOLD or REJECT if any of these occur:

- Existing ResearchCore Engine docs are overwritten, moved, renamed, or materially edited.
- Root README, docs index, docs status, docs architecture, docs navigation, generated reference docs, package files, CI, code, tests, schemas, tools, milestones, tickets, prompts, raw data, generated data, ES-derived fixtures, CX-T001 audit files, MB-T001, ADR-T003, M1, or downstream files are changed.
- NullForge implementation code is created or implementation is claimed to have started.
- Tauri scaffold, bridge implementation, sidecar implementation, schemas, tests, package/dependency changes, CI changes, telemetry implementation, cloud/auth/billing/mobile code, broker/live code, network code, fixtures, or dataset imports are created.
- Repo/package/CLI/app/product/public identity is actually changed.
- CODEX_ROLE_LOOP claims legal/trademark clearance, public distribution safety, Tauri feasibility proof, packaging proof, bridge proof, product validation, user validation, market validation, live-trading readiness, financial advice safety, data-licensing safety, cloud-security proof, telemetry enforcement, or no-cloud technical enforcement.
- CODEX_ROLE_LOOP omits role responsibilities, artifact tree, PASS/HOLD/REJECT rules, human gates, stop conditions, or source/truth rules.
- `SOURCE_INDEX.md` contains broken repo-local Markdown links.
- Incoming-only ticket/milestone/prompt sources are treated as repo-local files that already exist.
- Prompt files or old chats are treated as active source truth.
- MB-T001, ADR-T003, M1, or downstream work starts.
- Checks are skipped without explanation.
- Changed files cannot be bounded to CX-T001 plans, allowed NullForge docs, and reports.
- A human gate is triggered and work continues without approval.

## Done Definition

CX-T001 implementation is ready for auditor when all required docs/reports exist, checks are recorded, human gate status is reported, and `reports/nullforge/CX-T001/AUDITOR_PROMPT.md` is ready for an independent auditor.

CX-T001 itself is not complete until an auditor returns PASS, HOLD, or REJECT.
