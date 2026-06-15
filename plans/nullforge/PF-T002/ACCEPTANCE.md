# PF-T002 Acceptance

Ticket: PF-T002 - Create NullForge current status and source index

## Testable Acceptance Criteria

- `docs/nullforge/README.md` exists.
- `docs/nullforge/CURRENT_STATUS.md` exists.
- `docs/nullforge/SOURCE_INDEX.md` exists.
- `docs/nullforge/DECISION_LEDGER.md` exists.
- `docs/nullforge/ARCHIVE_POLICY.md` exists.
- `reports/nullforge/PF-T002/IMPLEMENTATION_REPORT.md` exists.
- `reports/nullforge/PF-T002/CHANGED_FILES.md` exists.
- `reports/nullforge/PF-T002/TEST_RESULTS.md` exists.
- `reports/nullforge/PF-T002/AUDITOR_PROMPT.md` exists.
- `CURRENT_STATUS.md` names the active phase exactly as `REPO_SOURCE_IMPORT_BASELINE`.
- `CURRENT_STATUS.md` includes updated date `2026-06-15`, active ticket `PF-T002`, blockers/gates, and next action `ADR-T001`.
- `CURRENT_STATUS.md` explicitly states that no NullForge implementation code has started.
- `CURRENT_STATUS.md` distinguishes existing ResearchCore Engine implementation truth from NullForge product/workflow planning docs.
- `CURRENT_STATUS.md` does not mark technical, product, user, market, trading, or validation claims as proven.
- `SOURCE_INDEX.md` links imported Volume 00-07 docs and PF-T000/PF-T001 dependency artifacts that exist in the repo.
- `SOURCE_INDEX.md` lists incoming package M0/PF-T002 sources as external active inputs because repo-local milestone/ticket files are absent.
- `SOURCE_INDEX.md` does not contain broken Markdown links to absent repo-local milestone, ticket, or ADR files.
- `SOURCE_INDEX.md` separates active docs, design memory, archive, quarantine, prompts, incoming package inputs, and pending downstream docs.
- `DECISION_LEDGER.md` seeds source/import/status decisions without replacing ADR-T001 or ADR-T002.
- `DECISION_LEDGER.md` marks name/platform/stack/engine and local-first/no-cloud decisions as pending downstream ADR work.
- `ARCHIVE_POLICY.md` summarizes archive/quarantine/prompt treatment and references Volume 1 as deeper source.
- `README.md` serves as a NullForge docs entry point and does not replace root `README.md`.
- No existing ResearchCore Engine docs are modified.
- No root README, docs index, docs status, docs navigation, generated reference docs, package files, CI files, code, tests, schemas, tools, milestones, tickets, prompts, raw data, ES-derived fixtures, or ADR files are created or modified.
- No ADR-T001 or downstream ticket work is started.

## Required Checks And Commands

Run and record:

```powershell
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
```

Run and record `Test-Path -LiteralPath` checks for:

```text
docs\nullforge\README.md
docs\nullforge\CURRENT_STATUS.md
docs\nullforge\SOURCE_INDEX.md
docs\nullforge\DECISION_LEDGER.md
docs\nullforge\ARCHIVE_POLICY.md
reports\nullforge\PF-T002\IMPLEMENTATION_REPORT.md
reports\nullforge\PF-T002\CHANGED_FILES.md
reports\nullforge\PF-T002\TEST_RESULTS.md
reports\nullforge\PF-T002\AUDITOR_PROMPT.md
```

Run and record:

```powershell
rg -n "REPO_SOURCE_IMPORT_BASELINE|PF-T002|ADR-T001|No NullForge implementation code has started" docs\nullforge\CURRENT_STATUS.md
rg -n "Active docs|Design memory|Archive|Quarantine|Prompts|Incoming package inputs|Pending downstream docs" docs\nullforge\SOURCE_INDEX.md
rg -n "Decision: PASS" audits\nullforge\PF-T001\AUDIT_REPORT.md
```

Manual review required:

- Confirm all repo-local Markdown links in `SOURCE_INDEX.md` resolve to existing repo files.
- Confirm external incoming package sources are recorded as plain text/external inputs and not broken repo-local links.
- Confirm changed files are limited to:
  - `plans/nullforge/PF-T002/`
  - `docs/nullforge/README.md`
  - `docs/nullforge/CURRENT_STATUS.md`
  - `docs/nullforge/SOURCE_INDEX.md`
  - `docs/nullforge/DECISION_LEDGER.md`
  - `docs/nullforge/ARCHIVE_POLICY.md`
  - `reports/nullforge/PF-T002/`
- Confirm no `README.md`, `docs/index.md`, `docs/STATUS.md`, `docs/ARCHITECTURE.md`, `docs/reference/`, `docs/contributing/`, `src/`, `tests/`, `schemas/`, `configs/`, `tools/`, package files, `mkdocs.yml`, `.github/`, milestone files, ticket files, prompt files, or ADR files changed.
- Confirm current status has one active mission and one active next action.
- Confirm no NullForge implementation or validation claim is marked proven.

Optional checks:

- `python -m mkdocs build` only if docs navigation or mkdocs-visible configuration is changed.
- `python tools/docs/verify_generated_docs_clean.py` only if generated docs tooling or generated reference files are changed.

Do not install dependencies. If optional checks are skipped, record why in `TEST_RESULTS.md`.

## Scope Question Resolutions To Verify

- `docs/nullforge/DECISION_LEDGER.md` is created.
- `docs/nullforge/ARCHIVE_POLICY.md` is created.
- Incoming package M0 milestone/ticket sources are listed as external active inputs; repo-local milestone/ticket imports are not created.
- `docs/nullforge/blueprint/README.md` is not created in PF-T002.
- `CURRENT_STATUS.md` uses `REPO_SOURCE_IMPORT_BASELINE`.

## Conditions That Force HOLD Or REJECT

Return HOLD or REJECT if any of these occur:

- Existing ResearchCore Engine docs are overwritten, moved, renamed, or materially edited.
- Root README, docs index, docs status, docs navigation, generated reference docs, package files, CI, code, tests, schemas, tools, milestones, tickets, prompts, raw data, ES-derived fixtures, or ADR files are changed.
- NullForge implementation code is created or implementation is claimed to have started.
- Technical, product, user, market, trading, or validation claims are marked proven without audited evidence.
- `SOURCE_INDEX.md` contains broken repo-local Markdown links.
- Incoming-only M0 milestone/ticket sources are treated as repo-local files that already exist.
- Prompt files or old chats are treated as active source truth.
- ADR-T001 or downstream M0 work starts.
- Checks are skipped without explanation.
- Changed files cannot be bounded to PF-T002 docs/plans/reports.
- A human gate is triggered and work continues without approval.

## Done Definition

PF-T002 implementation is ready for auditor when all required docs/reports exist, checks are recorded, human gate status is reported, and `reports/nullforge/PF-T002/AUDITOR_PROMPT.md` is ready for an independent auditor.

PF-T002 itself is not complete until an auditor returns PASS, HOLD, or REJECT.
