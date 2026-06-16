# ADR-T002 Acceptance

Ticket: `ADR-T002` - Local-first/no-cloud MVP ADR
Date: `2026-06-16`

## Testable Acceptance Criteria

- `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md` exists.
- `docs/nullforge/DECISION_LEDGER.md` is updated.
- `docs/nullforge/CURRENT_STATUS.md` is updated.
- `docs/nullforge/SOURCE_INDEX.md` is updated.
- `reports/nullforge/ADR-T002/IMPLEMENTATION_REPORT.md` exists.
- `reports/nullforge/ADR-T002/CHANGED_FILES.md` exists.
- `reports/nullforge/ADR-T002/TEST_RESULTS.md` exists.
- `reports/nullforge/ADR-T002/AUDITOR_PROMPT.md` exists.
- ADR date is `2026-06-16`.
- ADR status makes clear the decision is accepted for M0 planning/source-of-truth purposes, not implementation proof.
- ADR confirms ADR-T001 audit `PASS` as prerequisite evidence.
- ADR records NullForge MVP as local-first by default.
- ADR records one selected local workspace as the MVP runtime boundary.
- ADR records local files, local manifests, local logs, local run/artifact metadata, local evidence placeholders, and local ResearchCore Engine execution as MVP planning assumptions.
- ADR records local engine execution as future scoped sidecar/command bridge work and does not claim the bridge is implemented or proven.
- ADR records tiny/small fixtures are allowed only through a later approved fixture policy.
- ADR records full ES.zip, raw/private data, generated datasets, and ES-derived fixtures remain gated and must not be committed by default.
- ADR records cloud storage, cloud sync, hosted backend, account/auth, billing, telemetry/analytics, mobile, marketplace, broker-live integration, live order execution, and public distribution are outside MVP scope.
- ADR records no network behavior is required for MVP and future network access requires scoped ADR/ticket and human review.
- ADR states no NullForge implementation code has started.
- ADR does not claim legal/trademark clearance, public brand approval, public distribution safety, financial advice safety, trading validity, product validation, user validation, market validation, Tauri feasibility, bridge reliability, packaging feasibility, data licensing safety, or cloud-security proof.
- ADR includes context, options considered, chosen decisions, consequences, risks and unknowns, human gates, reversal conditions, non-decisions, and next action.
- ADR next action is `CX-T001` after ADR-T002 independent audit disposition.
- `docs/nullforge/DECISION_LEDGER.md` updates `NF-D0005` in place to reference ADR-T002 and does not add a duplicate row for the same local-first/no-cloud decision.
- `docs/nullforge/DECISION_LEDGER.md` keeps CX-T001, MB-T001, ADR-T003, or other downstream work pending/not started if mentioned.
- `docs/nullforge/CURRENT_STATUS.md` keeps active phase `REPO_SOURCE_IMPORT_BASELINE`, names active ticket `ADR-T002`, and points next action to `CX-T001` after ADR-T002 audit disposition.
- `docs/nullforge/CURRENT_STATUS.md` still contains the exact sentence `No NullForge implementation code has started.`
- `docs/nullforge/SOURCE_INDEX.md` links the new ADR-T002 file with a repo-local Markdown link that resolves.
- `docs/nullforge/SOURCE_INDEX.md` links only to existing ADR-T002 report files after they are created.
- `docs/nullforge/SOURCE_INDEX.md` does not create broken links to missing ticket, milestone, prompt, CX-T001, MB-T001, ADR-T003, or downstream files.
- No existing ResearchCore Engine docs are modified.
- No root README, docs index, docs status, docs architecture, docs navigation, generated reference docs, package files, CI files, code, tests, schemas, tools, milestones, tickets, prompts, raw data, generated data, ES-derived fixtures, ADR-T003, CX-T001, or MB-T001 files are created or modified.
- No implementation, data import, fixture creation, Tauri scaffold, bridge/sidecar work, telemetry implementation, cloud/auth/billing work, broker/live work, public release work, or downstream ticket work is started.

## Required Checks And Commands

Run and record:

```powershell
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
```

Run and record `Test-Path -LiteralPath` checks for:

```text
docs\nullforge\adr\ADR-T002-local-first-no-cloud-mvp.md
reports\nullforge\ADR-T002\IMPLEMENTATION_REPORT.md
reports\nullforge\ADR-T002\CHANGED_FILES.md
reports\nullforge\ADR-T002\TEST_RESULTS.md
reports\nullforge\ADR-T002\AUDITOR_PROMPT.md
```

Run and record:

```powershell
rg -n "Decision: PASS" audits\nullforge\ADR-T001\AUDIT_REPORT.md
rg -n "local-first|no-cloud|cloud sync|auth|billing|telemetry|broker|live trading|public distribution|ES.zip|workspace|ResearchCore Engine|human gate|reversal" docs\nullforge\adr\ADR-T002-local-first-no-cloud-mvp.md
rg -n "ADR-T002|NF-D0005|CX-T001|MB-T001" docs\nullforge\DECISION_LEDGER.md
rg -n "ADR-T002|CX-T001|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\CURRENT_STATUS.md
rg -n "ADR-T002|CX-T001|MB-T001|ADR-T002-local-first-no-cloud-mvp" docs\nullforge\SOURCE_INDEX.md
```

Manual review required:

- Confirm all repo-local Markdown links in `docs/nullforge/SOURCE_INDEX.md` resolve to existing repo files.
- Confirm external incoming package sources, if mentioned, are recorded as plain text/external inputs and not broken repo-local links.
- Confirm changed files are limited to:
  - `plans/nullforge/ADR-T002/`
  - `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`
  - `docs/nullforge/DECISION_LEDGER.md`
  - `docs/nullforge/CURRENT_STATUS.md`
  - `docs/nullforge/SOURCE_INDEX.md`
  - `reports/nullforge/ADR-T002/`
- Confirm no `README.md`, `docs/index.md`, `docs/STATUS.md`, `docs/ARCHITECTURE.md`, `docs/reference/`, `docs/contributing/`, `src/`, `tests/`, `schemas/`, `configs/`, `tools/`, package files, `mkdocs.yml`, `.github/`, milestone files, ticket files, prompt files, raw data, generated data, ES-derived fixtures, ADR-T003, CX-T001, or MB-T001 files changed.
- Confirm ADR-T002 does not start implementation or assert proof/validation/legal/trading/data-safety claims.

Optional checks:

- `python -m mkdocs build` only if docs navigation or mkdocs-visible configuration is changed.
- `python tools/docs/verify_generated_docs_clean.py` only if generated docs tooling or generated reference files are changed.

Do not install dependencies. If optional checks are skipped, record why in `TEST_RESULTS.md`.

## Scope Question Resolutions To Verify

- ADR-T002 updates `docs/nullforge/CURRENT_STATUS.md`.
- ADR-T002 updates `docs/nullforge/SOURCE_INDEX.md`.
- ADR-T002 updates `docs/nullforge/DECISION_LEDGER.md` by changing `NF-D0005` in place and does not append a duplicate same-decision row.
- ADR-T002 consolidates the local-first/no-cloud MVP boundary into `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`.
- ADR-T002 keeps CX-T001 and MB-T001 pending only and does not start either.

## Conditions That Force HOLD Or REJECT

Return HOLD or REJECT if any of these occur:

- Existing ResearchCore Engine docs are overwritten, moved, renamed, or materially edited.
- Root README, docs index, docs status, docs architecture, docs navigation, generated reference docs, package files, CI, code, tests, schemas, tools, milestones, tickets, prompts, raw data, generated data, ES-derived fixtures, ADR-T003, CX-T001, MB-T001, or downstream files are changed.
- NullForge implementation code is created or implementation is claimed to have started.
- Tauri scaffold, bridge implementation, sidecar implementation, schemas, tests, package/dependency changes, CI changes, telemetry implementation, cloud/auth/billing/mobile code, broker/live code, network code, fixtures, or dataset imports are created.
- Repo/package/CLI/app/product/public identity is actually changed.
- ADR claims legal/trademark clearance, public distribution safety, Tauri feasibility proof, packaging proof, bridge proof, product validation, user validation, market validation, live-trading readiness, financial advice safety, data-licensing safety, cloud-security proof, telemetry enforcement, or no-cloud technical enforcement.
- ADR omits options considered, chosen decisions, risks, reversal conditions, non-decisions, or human gates.
- Decision ledger does not reference ADR-T002.
- Decision ledger duplicates the local-first/no-cloud decision row instead of updating `NF-D0005`.
- `SOURCE_INDEX.md` contains broken repo-local Markdown links.
- Incoming-only ticket/milestone/prompt sources are treated as repo-local files that already exist.
- Prompt files or old chats are treated as active source truth.
- CX-T001, MB-T001, ADR-T003, or downstream M0/M1 work starts.
- Checks are skipped without explanation.
- Changed files cannot be bounded to ADR-T002 plans, allowed NullForge docs, and reports.
- A human gate is triggered and work continues without approval.

## Done Definition

ADR-T002 implementation is ready for auditor when all required docs/reports exist, checks are recorded, human gate status is reported, and `reports/nullforge/ADR-T002/AUDITOR_PROMPT.md` is ready for an independent auditor.

ADR-T002 itself is not complete until an auditor returns PASS, HOLD, or REJECT.
