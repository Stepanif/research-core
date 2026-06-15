# PF-T002 Plan

Ticket: PF-T002 - Create NullForge current status and source index
Milestone: M0 - Repo Source Import + Canonical Baseline
Role: Planner

## Purpose

Produce a bounded, docs-only implementation plan for creating the active NullForge status and source-index baseline after PF-T001 imported and audited the Volume 00-07 planning corpus.

PF-T002 must keep NullForge project/source docs separate from existing ResearchCore Engine docs. It must not claim NullForge implementation has started, must not mark technical/product/user claims as proven, and must not start ADR-T001 or any downstream ticket.

## Source Context Used

Repo-local context:

- `plans/nullforge/PF-T002/CONTEXT_BUNDLE.md`
- `plans/nullforge/PF-T002/CONTEXT_BUNDLE_MANIFEST.md`
- `docs/nullforge/import/PF-T000_IMPORT_PLAN.md`
- `docs/nullforge/import/PF-T000_REPO_INVENTORY.md`
- `docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md`
- `audits/nullforge/PF-T001/AUDIT_REPORT.md`
- `reports/nullforge/PF-T001/TEST_RESULTS.md`
- `docs/nullforge/blueprint/volumes/README.md`
- `docs/nullforge/blueprint/volumes/VOLUME_IMPORT_MANIFEST.md`
- Imported Volume 00-07 docs under `docs/nullforge/blueprint/volumes/`

Active incoming ticket source:

- `C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\PF-T002-create-nullforge-current-status-and-source-index.md`

The in-repo PF-T002 ticket path is absent at planner time:

- `tickets/nullforge/PF-T002-create-nullforge-current-status-and-source-index.md`

Existing ResearchCore docs used for boundary context:

- `README.md`
- `docs/STATUS.md`
- `docs/index.md`
- `docs/contributing/docs_style_guide.md`

## Dependencies And Current Status

- PF-T002 depends on PF-T001.
- PF-T001 audit decision: PASS.
- PF-T001 was committed, pushed, merged to `main`, and pushed.
- Imported Volume 00-07 docs are present on `main`.
- Current branch: `docs/PF-T002-nullforge-status-source-index`.
- Current working tree contains only PF-T002 context bundle files under `plans/nullforge/PF-T002/`.
- M0 remains serial:

```text
PF-T000 -> PF-T001 -> PF-T002 -> ADR-T001 -> ADR-T002 -> CX-T001 -> MB-T001
```

ADR-T001 must remain blocked until PF-T002 has implementation outputs and an independent audit disposition.

## Planner Scope Decisions

### `docs/nullforge/DECISION_LEDGER.md`

PF-T002 should create `docs/nullforge/DECISION_LEDGER.md`.

Reason: PF-T000 names it as a PF-T002-owned source-of-truth file, Volume 7 lists it as a source baseline doc, and the PF-T002 ticket requires the status/source index to point to active decisions. The file should be a lightweight seed ledger only. It must not replace ADR-T001/ADR-T002 and must mark those downstream ADRs as pending.

### `docs/nullforge/ARCHIVE_POLICY.md`

PF-T002 should create `docs/nullforge/ARCHIVE_POLICY.md`.

Reason: the incoming ticket permits either creating this file or referencing Volume 1. A short repo-local policy improves source-index clarity and satisfies the requirement to separate active docs, design memory, archive, quarantine, and prompts. It should cite Volume 1 as the deeper source and avoid importing prompts or old chat.

### Incoming-Only M0 Milestone And Ticket Sources

PF-T002 should not import M0 milestone docs or ticket files into `milestones/nullforge/` or `tickets/nullforge/`.

`SOURCE_INDEX.md` should:

- link only to repo-local files that actually exist;
- list incoming package PF-T002/M0 milestone/ticket/gate sources as active external inputs in plain text;
- mark repo-local milestone/ticket paths as pending/not present;
- avoid broken Markdown links to absent repo-local milestone, ticket, or ADR files.

This satisfies the source-index requirement without broadening PF-T002 into milestone/ticket import work.

### Volume Index

PF-T002 should not create `docs/nullforge/blueprint/README.md`.

Reason: PF-T001 already created `docs/nullforge/blueprint/volumes/README.md`, and PF-T002 can use `docs/nullforge/SOURCE_INDEX.md` as the top-level volume/source index for now. A separate `docs/nullforge/blueprint/README.md` can be created later by a scoped docs-navigation ticket if needed.

### Active Phase Label

`CURRENT_STATUS.md` should use this exact active phase label:

```text
REPO_SOURCE_IMPORT_BASELINE
```

Meaning: PF-T001 imported and audited the planning corpus, PF-T002 is creating the source/status baseline, and ADR-T001 is next. The status must explicitly say:

- no NullForge implementation code has started;
- the existing ResearchCore Engine implementation already exists and remains separate engine truth;
- M0 is still active and implementation tickets remain blocked.

## Exact Scope

PF-T002 planner may create:

```text
plans/nullforge/PF-T002/PLAN.md
plans/nullforge/PF-T002/ACCEPTANCE.md
plans/nullforge/PF-T002/IMPLEMENTOR_PROMPT.md
```

PF-T002 implementor may create only:

```text
docs/nullforge/README.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
docs/nullforge/DECISION_LEDGER.md
docs/nullforge/ARCHIVE_POLICY.md
reports/nullforge/PF-T002/IMPLEMENTATION_REPORT.md
reports/nullforge/PF-T002/CHANGED_FILES.md
reports/nullforge/PF-T002/TEST_RESULTS.md
reports/nullforge/PF-T002/AUDITOR_PROMPT.md
```

The later auditor may create only:

```text
audits/nullforge/PF-T002/AUDIT_REPORT.md
audits/nullforge/PF-T002/FINDINGS.md
audits/nullforge/PF-T002/REPAIR_PROMPT.md
```

PF-T002 may also leave existing PF-T002 context/planner files under:

```text
plans/nullforge/PF-T002/
```

No other files should change.

## Required Content Expectations

### `docs/nullforge/README.md`

Should be a NullForge docs entry point that:

- states NullForge docs are project/product planning docs, not ResearchCore Engine implementation truth;
- links to `CURRENT_STATUS.md`, `SOURCE_INDEX.md`, `DECISION_LEDGER.md`, `ARCHIVE_POLICY.md`, and the imported volume folder;
- states no NullForge implementation code has started;
- points next action to ADR-T001 after PF-T002 audit;
- does not change root README or `docs/index.md`.

### `docs/nullforge/CURRENT_STATUS.md`

Should include:

- updated date `2026-06-15`;
- active phase `REPO_SOURCE_IMPORT_BASELINE`;
- active ticket `PF-T002`;
- dependency status: PF-T000 complete/PASS; PF-T001 complete/PASS; PF-T002 in progress until audit;
- next action: `ADR-T001` after PF-T002 audit PASS/HOLD/REJECT as appropriate;
- blockers/gates: no current blocker, but implementation remains blocked until M0 docs/ADRs/role-loop are complete;
- explicit statement that no NullForge implementation code has started;
- explicit statement that existing ResearchCore Engine implementation remains current engine truth;
- status of active claims as untested/unproven unless later audited evidence says otherwise;
- no public release, repo rename, app scaffold, dataset fixture, desktop bridge, broker/live trading, cloud/auth/billing/mobile scope.

### `docs/nullforge/SOURCE_INDEX.md`

Should include:

- repo-local active NullForge docs:
  - PF-T000 import docs;
  - PF-T001 imported volume folder/manifest/README;
  - PF-T002 docs created in this ticket;
  - PF-T000/PF-T001 plans, reports, and audits where useful;
- imported Volume 00-07 paths and each volume's purpose/truth status;
- active incoming package sources for PF-T002/M0 milestone docs as plain text paths, not broken repo links;
- pending repo-local milestone/ticket/ADR paths as pending text only;
- separated categories for active docs, design memory, archive, quarantine, prompts, incoming package inputs, and pending downstream docs;
- no broken Markdown links to absent files;
- next ticket `ADR-T001`.

### `docs/nullforge/DECISION_LEDGER.md`

Should include seed decision records only, such as:

- separated NullForge docs root under `docs/nullforge/` from PF-T000;
- imported Volume 00-07 planning docs under `docs/nullforge/blueprint/volumes/` from PF-T001;
- PF-T002 source/status baseline created under `docs/nullforge/`;
- pending ADR decisions for name/platform/stack/engine boundary and local-first/no-cloud.

The ledger should include status, source, date, and reversal/repair note fields. It must not claim ADR-level decisions are fully made if ADR-T001/ADR-T002 are pending.

### `docs/nullforge/ARCHIVE_POLICY.md`

Should summarize:

- active docs vs design memory vs archive vs quarantine vs prompts;
- archive means memory without authority;
- quarantine means unresolved/conflicting/risky material without governance power;
- prior chat and prompt files are not active truth unless explicitly promoted by a scoped ticket;
- raw/full data and ES-derived fixtures remain gated;
- Volume 1 is the deeper source for archive/quarantine doctrine.

## Forbidden Actions

- Do not modify existing ResearchCore Engine docs:
  - `README.md`
  - `docs/index.md`
  - `docs/STATUS.md`
  - `docs/ARCHITECTURE.md`
  - `docs/reference/`
  - `docs/contributing/`
- Do not modify `src/`, `tests/`, `schemas/`, `configs/`, `tools/`, `pyproject.toml`, `mkdocs.yml`, `.github/`, package files, or CI files.
- Do not create implementation code, tests, schemas, scripts, Tauri scaffolds, sidecar binaries, parsers, packaging configs, or dependencies.
- Do not install dependencies.
- Do not import raw/full `ES.zip`, raw/private/local data, or ES-derived fixtures.
- Do not import old chat logs.
- Do not import prompt files as active source truth.
- Do not create `tickets/nullforge/`, `milestones/nullforge/`, or `prompts/nullforge/` content in PF-T002.
- Do not create ADR files or run ADR-T001.
- Do not change repo/package/CLI/product/public identity.
- Do not broaden into public release, legal/trademark, financial advice, broker/live trading, auth, billing, cloud sync, marketplace, or mobile scope.

## Step-By-Step Docs/Source Update Plan

1. Preflight
   - Run `git status --short --branch`.
   - Confirm branch is `docs/PF-T002-nullforge-status-source-index`.
   - Confirm in-repo PF-T002 ticket path status.
   - Confirm PF-T001 audit PASS is present.
   - Confirm candidate output paths do not already exist.

2. Create target docs
   - Create `docs/nullforge/README.md`.
   - Create `docs/nullforge/CURRENT_STATUS.md`.
   - Create `docs/nullforge/SOURCE_INDEX.md`.
   - Create `docs/nullforge/DECISION_LEDGER.md`.
   - Create `docs/nullforge/ARCHIVE_POLICY.md`.

3. Create PF-T002 implementation reports
   - `IMPLEMENTATION_REPORT.md`: actions, decisions, gates, and remaining audit work.
   - `CHANGED_FILES.md`: every created file and why.
   - `TEST_RESULTS.md`: exact checks and results.
   - `AUDITOR_PROMPT.md`: bounded PF-T002-only audit prompt.

4. Verify docs/source boundaries
   - Check all required PF-T002 output files exist.
   - Check `CURRENT_STATUS.md` includes `REPO_SOURCE_IMPORT_BASELINE`, `PF-T002`, `ADR-T001`, date, blockers/gates, and no-NullForge-implementation statement.
   - Check `SOURCE_INDEX.md` links only to existing repo-local files.
   - Check incoming package sources are recorded as external/plain-text active inputs, not repo-local links.
   - Check root README, `docs/index.md`, and `docs/STATUS.md` were not modified.

5. Final verification
   - Run `git status --short --branch`.
   - Run `git status --short --untracked-files=all`.
   - Run `git diff --name-only`.
   - Manually confirm changed paths are limited to:
     - `plans/nullforge/PF-T002/`
     - `docs/nullforge/README.md`
     - `docs/nullforge/CURRENT_STATUS.md`
     - `docs/nullforge/SOURCE_INDEX.md`
     - `docs/nullforge/DECISION_LEDGER.md`
     - `docs/nullforge/ARCHIVE_POLICY.md`
     - `reports/nullforge/PF-T002/`

## Tests And Checks Required

Required:

```powershell
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
Test-Path -LiteralPath docs\nullforge\README.md
Test-Path -LiteralPath docs\nullforge\CURRENT_STATUS.md
Test-Path -LiteralPath docs\nullforge\SOURCE_INDEX.md
Test-Path -LiteralPath docs\nullforge\DECISION_LEDGER.md
Test-Path -LiteralPath docs\nullforge\ARCHIVE_POLICY.md
Test-Path -LiteralPath reports\nullforge\PF-T002\IMPLEMENTATION_REPORT.md
Test-Path -LiteralPath reports\nullforge\PF-T002\CHANGED_FILES.md
Test-Path -LiteralPath reports\nullforge\PF-T002\TEST_RESULTS.md
Test-Path -LiteralPath reports\nullforge\PF-T002\AUDITOR_PROMPT.md
rg -n "REPO_SOURCE_IMPORT_BASELINE|PF-T002|ADR-T001|No NullForge implementation code has started" docs\nullforge\CURRENT_STATUS.md
rg -n "Active docs|Design memory|Archive|Quarantine|Prompts|Incoming package inputs|Pending downstream docs" docs\nullforge\SOURCE_INDEX.md
rg -n "Decision: PASS" audits\nullforge\PF-T001\AUDIT_REPORT.md
```

Manual checks:

- All Markdown links in `SOURCE_INDEX.md` that target repo-local files resolve to existing files.
- Incoming package paths in `SOURCE_INDEX.md` are plain text/external active inputs, not broken repo-local Markdown links.
- No existing ResearchCore Engine docs were changed.
- No code, tests, schemas, dependencies, raw data, generated references, package files, CI, milestones, tickets, prompts, or ADR files were created or modified.
- Current status has one active mission and one active roadmap direction.

Optional checks:

- `python -m mkdocs build` only if docs navigation or mkdocs-visible config is changed.
- `python tools/docs/verify_generated_docs_clean.py` only if generated docs tooling or generated reference files are changed.

PF-T002 should not change docs navigation, mkdocs config, generated docs tooling, or generated references, so these optional checks should normally be skipped with explanation. Do not install dependencies.

## Human Gate Triggers

Human review is required before:

- overwriting, moving, renaming, or materially editing existing ResearchCore Engine docs;
- changing root README, docs index, or docs navigation;
- changing repo, package, CLI, app, product, or public identity;
- adding dependencies, code, scripts, parsers, sidecar binaries, packaging configs, tests, schemas, or CI behavior;
- importing raw/full `ES.zip`, raw/private/local data, or ES-derived fixtures;
- marking unreviewed materials canonical;
- treating old chats or prompts as active source truth;
- creating ADR-T001 or any downstream artifacts;
- broadening into public release, legal/trademark naming, AI strategy activation, broker/live trading, financial advice, auth, billing, cloud sync, marketplace, or mobile scope.

Planner-detected human gates: NONE.

## Source-Of-Truth Risks

- Creating a status doc could imply implementation has started. Mitigate with explicit "no NullForge implementation code has started" language.
- Creating a decision ledger could accidentally preempt ADR-T001/ADR-T002. Mitigate by marking ADR topics as pending and not settled.
- Incoming M0 ticket/milestone docs are still outside the repo. Mitigate by listing them as external active inputs and marking repo-local milestone/ticket paths pending.
- Source index links could be broken if they point to absent ADR/milestone/ticket files. Mitigate by using Markdown links only for files that exist.
- Root docs could blur ResearchCore Engine truth and NullForge product truth. Do not edit root README, `docs/index.md`, or `docs/STATUS.md`.

## Done Definition

PF-T002 implementation is ready for auditor when:

- All planned PF-T002 docs and reports exist.
- Required checks are recorded in `reports/nullforge/PF-T002/TEST_RESULTS.md`.
- Human gate status is explicitly reported.
- Changed files are scoped to PF-T002 plans, docs, and reports.
- `reports/nullforge/PF-T002/AUDITOR_PROMPT.md` is ready for an independent auditor.

PF-T002 itself is not complete until an auditor returns PASS, HOLD, or REJECT and the result is recorded by the later M0 handoff workflow.
