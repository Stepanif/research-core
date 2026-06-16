# ADR-T001 Acceptance

Ticket: ADR-T001 - Name/platform/stack/engine ADR

## Testable Acceptance Criteria

- `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` exists.
- `docs/nullforge/DECISION_LEDGER.md` is updated.
- `docs/nullforge/CURRENT_STATUS.md` is updated.
- `docs/nullforge/SOURCE_INDEX.md` is updated.
- `reports/nullforge/ADR-T001/IMPLEMENTATION_REPORT.md` exists.
- `reports/nullforge/ADR-T001/CHANGED_FILES.md` exists.
- `reports/nullforge/ADR-T001/TEST_RESULTS.md` exists.
- `reports/nullforge/ADR-T001/AUDITOR_PROMPT.md` exists.
- ADR date is `2026-06-15`.
- ADR status makes clear the decision is accepted for M0 planning and source-of-truth purposes, not implementation proof.
- ADR records `NullForge` as working product name only.
- ADR explicitly states `NullForge` is not legally/trademark cleared and not safe/approved for public distribution.
- ADR records the repo remains `research-core`.
- ADR records package names, CLI names, root README, existing ResearchCore docs, and public identity are unchanged.
- ADR records internal engine label remains `ResearchCore Engine`.
- ADR records existing ResearchCore Engine remains separate current engine truth.
- ADR records Windows 11 x64 as first platform for future desktop proof work.
- ADR records Tauri + React/TypeScript as accepted default desktop stack direction pending bridge/packaging spikes.
- ADR records the intended engine boundary as Python ResearchCore Engine sidecar / scoped command bridge.
- ADR records the bridge as narrow, allowlisted, and structured, not arbitrary shell execution.
- ADR includes context, options considered, chosen decision, consequences, risks, unknowns, human gates, and reversal conditions.
- ADR states no NullForge implementation code has started.
- ADR does not claim Tauri feasibility, packaging feasibility, bridge reliability, product validation, user validation, market claims, trading validity, financial advice safety, legal clearance, or public distribution safety is proven.
- `docs/nullforge/DECISION_LEDGER.md` updates `NF-D0004` in place to reference ADR-T001 and does not add a duplicate row for the same decision.
- `docs/nullforge/DECISION_LEDGER.md` keeps ADR-T002 pending.
- `docs/nullforge/CURRENT_STATUS.md` keeps active phase `REPO_SOURCE_IMPORT_BASELINE`, names active ticket `ADR-T001`, and points next action to `ADR-T002` after ADR-T001 audit disposition.
- `docs/nullforge/CURRENT_STATUS.md` still contains the exact sentence `No NullForge implementation code has started.`
- `docs/nullforge/SOURCE_INDEX.md` links the new ADR-T001 file with a repo-local Markdown link that resolves.
- `docs/nullforge/SOURCE_INDEX.md` does not create broken links to missing ticket, milestone, prompt, or ADR-T002 files.
- No existing ResearchCore Engine docs are modified.
- No root README, docs index, docs status, docs architecture, docs navigation, generated reference docs, package files, CI files, code, tests, schemas, tools, milestones, tickets, prompts, raw data, ES-derived fixtures, or ADR-T002 files are created or modified.
- No ADR-T002 or downstream ticket work is started.

## Required Checks And Commands

Run and record:

```powershell
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
```

Run and record `Test-Path -LiteralPath` checks for:

```text
docs\nullforge\adr\ADR-T001-name-platform-stack-engine.md
reports\nullforge\ADR-T001\IMPLEMENTATION_REPORT.md
reports\nullforge\ADR-T001\CHANGED_FILES.md
reports\nullforge\ADR-T001\TEST_RESULTS.md
reports\nullforge\ADR-T001\AUDITOR_PROMPT.md
```

Run and record:

```powershell
rg -n "Decision: PASS" audits\nullforge\PF-T002\AUDIT_REPORT.md
rg -n "NullForge|working product name|research-core|ResearchCore Engine|Windows 11 x64|Tauri|React|TypeScript|sidecar|command bridge|reversal|human gate" docs\nullforge\adr\ADR-T001-name-platform-stack-engine.md
rg -n "ADR-T001|NF-D0004|ADR-T002" docs\nullforge\DECISION_LEDGER.md
rg -n "ADR-T001|ADR-T002|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\CURRENT_STATUS.md
rg -n "ADR-T001|ADR-T002|ADR-T001-name-platform-stack-engine" docs\nullforge\SOURCE_INDEX.md
```

Manual review required:

- Confirm all repo-local Markdown links in `docs/nullforge/SOURCE_INDEX.md` resolve to existing repo files.
- Confirm external incoming package sources are recorded as plain text/external inputs and not broken repo-local links.
- Confirm changed files are limited to:
  - `plans/nullforge/ADR-T001/`
  - `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`
  - `docs/nullforge/DECISION_LEDGER.md`
  - `docs/nullforge/CURRENT_STATUS.md`
  - `docs/nullforge/SOURCE_INDEX.md`
  - `reports/nullforge/ADR-T001/`
- Confirm no `README.md`, `docs/index.md`, `docs/STATUS.md`, `docs/ARCHITECTURE.md`, `docs/reference/`, `docs/contributing/`, `src/`, `tests/`, `schemas/`, `configs/`, `tools/`, package files, `mkdocs.yml`, `.github/`, milestone files, ticket files, prompt files, raw data, ES-derived fixtures, or ADR-T002 files changed.
- Confirm ADR-T001 does not start implementation or assert proof/validation/legal claims.

Optional checks:

- `python -m mkdocs build` only if docs navigation or mkdocs-visible configuration is changed.
- `python tools/docs/verify_generated_docs_clean.py` only if generated docs tooling or generated reference files are changed.

Do not install dependencies. If optional checks are skipped, record why in `TEST_RESULTS.md`.

## Scope Question Resolutions To Verify

- ADR-T001 updates `docs/nullforge/CURRENT_STATUS.md`.
- ADR-T001 updates `docs/nullforge/SOURCE_INDEX.md`.
- Tauri + React/TypeScript is phrased as accepted default stack direction pending bridge/packaging spikes with reversal conditions.
- `docs/nullforge/DECISION_LEDGER.md` updates `NF-D0004` in place and does not append a duplicate same-decision row.
- ADR-T001 consolidates the name/platform/stack/engine boundary into `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`.

## Conditions That Force HOLD Or REJECT

Return HOLD or REJECT if any of these occur:

- Existing ResearchCore Engine docs are overwritten, moved, renamed, or materially edited.
- Root README, docs index, docs status, docs architecture, docs navigation, generated reference docs, package files, CI, code, tests, schemas, tools, milestones, tickets, prompts, raw data, ES-derived fixtures, or ADR-T002 files are changed.
- NullForge implementation code is created or implementation is claimed to have started.
- Repo/package/CLI/app/product/public identity is actually changed.
- ADR claims legal/trademark clearance, public distribution safety, Tauri feasibility proof, packaging proof, bridge proof, product validation, user validation, market validation, live-trading readiness, or financial advice safety.
- ADR omits options considered, chosen decisions, risks, reversal conditions, or human gates.
- Decision ledger does not reference ADR-T001.
- `SOURCE_INDEX.md` contains broken repo-local Markdown links.
- Incoming-only ticket/milestone sources are treated as repo-local files that already exist.
- Prompt files or old chats are treated as active source truth.
- ADR-T002 or downstream M0 work starts.
- Checks are skipped without explanation.
- Changed files cannot be bounded to ADR-T001 plans, allowed NullForge docs, and reports.
- A human gate is triggered and work continues without approval.

## Done Definition

ADR-T001 implementation is ready for auditor when all required docs/reports exist, checks are recorded, human gate status is reported, and `reports/nullforge/ADR-T001/AUDITOR_PROMPT.md` is ready for an independent auditor.

ADR-T001 itself is not complete until an auditor returns PASS, HOLD, or REJECT.
