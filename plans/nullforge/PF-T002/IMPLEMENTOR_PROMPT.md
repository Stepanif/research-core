# Implementor Prompt: PF-T002 - Create NullForge Current Status And Source Index

You are the Implementor for NullForge M0 ticket `PF-T002`.

You implement only the bounded docs/source-of-truth baseline for PF-T002. Do not write implementation code. Do not modify existing ResearchCore Engine docs. Do not create ADR-T001 or run any downstream ticket.

## Read First

Read these repo-local files:

```text
plans/nullforge/PF-T002/CONTEXT_BUNDLE.md
plans/nullforge/PF-T002/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/PF-T002/PLAN.md
plans/nullforge/PF-T002/ACCEPTANCE.md
```

The planner prompt referenced this in-repo ticket path:

```text
tickets/nullforge/PF-T002-create-nullforge-current-status-and-source-index.md
```

At planner time that path was absent. Use this incoming package ticket source unless the in-repo path now exists:

```text
<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\PF-T002-create-nullforge-current-status-and-source-index.md
```

If both paths exist, compare enough to identify the active source used and record that in the implementation report.

## Planner Decisions You Must Follow

- Create `docs/nullforge/DECISION_LEDGER.md`.
- Create `docs/nullforge/ARCHIVE_POLICY.md`.
- Do not import M0 milestone docs, ticket files, or prompt files into repo paths in PF-T002.
- In `SOURCE_INDEX.md`, link only to repo-local files that exist. List incoming package M0/PF-T002 sources as external active inputs in plain text.
- Do not create `docs/nullforge/blueprint/README.md` in PF-T002.
- Use exact active phase label `REPO_SOURCE_IMPORT_BASELINE` in `CURRENT_STATUS.md`.
- Point next action to `ADR-T001` after PF-T002 audit disposition.

## Allowed Files And Folders

You may create only:

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

Treat these files as read-only:

```text
plans/nullforge/PF-T002/CONTEXT_BUNDLE.md
plans/nullforge/PF-T002/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/PF-T002/PLAN.md
plans/nullforge/PF-T002/ACCEPTANCE.md
plans/nullforge/PF-T002/IMPLEMENTOR_PROMPT.md
docs/nullforge/import/PF-T000_IMPORT_PLAN.md
docs/nullforge/import/PF-T000_REPO_INVENTORY.md
docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md
audits/nullforge/PF-T001/AUDIT_REPORT.md
reports/nullforge/PF-T001/TEST_RESULTS.md
docs/nullforge/blueprint/volumes/README.md
docs/nullforge/blueprint/volumes/VOLUME_IMPORT_MANIFEST.md
docs/nullforge/blueprint/volumes/*.md
README.md
docs/STATUS.md
docs/index.md
docs/contributing/docs_style_guide.md
```

## Required Docs Content

### `docs/nullforge/README.md`

Create a concise NullForge docs entry point.

It must:

- say these are NullForge project/product planning docs, not ResearchCore Engine implementation truth;
- link to `CURRENT_STATUS.md`, `SOURCE_INDEX.md`, `DECISION_LEDGER.md`, `ARCHIVE_POLICY.md`, and `blueprint/volumes/README.md`;
- state no NullForge implementation code has started;
- state existing ResearchCore Engine docs/code remain current engine truth;
- point next action to `ADR-T001` after PF-T002 audit.

### `docs/nullforge/CURRENT_STATUS.md`

Create current status with:

- date `2026-06-15`;
- active phase `REPO_SOURCE_IMPORT_BASELINE`;
- active ticket `PF-T002`;
- dependency status:
  - PF-T000 complete/PASS;
  - PF-T001 complete/PASS;
  - PF-T002 in progress until independent audit;
- next action `ADR-T001` after PF-T002 audit;
- blockers/gates;
- exact sentence: `No NullForge implementation code has started.`;
- statement that existing ResearchCore Engine implementation remains separate engine truth;
- unproven claim status;
- no public release, repo rename, app scaffold, dataset fixture, desktop bridge, broker/live trading, cloud/auth/billing/mobile scope.

### `docs/nullforge/SOURCE_INDEX.md`

Create source index with these sections:

- Active docs
- Imported volumes
- Current ticket artifacts
- Incoming package inputs
- Design memory
- Archive
- Quarantine
- Prompts
- Pending downstream docs

Rules:

- Use Markdown links only for repo-local files that exist.
- Do not create broken Markdown links to absent `tickets/`, `milestones/`, or ADR files.
- Record incoming package source paths as plain text in code blocks or tables.
- Mark repo-local ticket/milestone/ADR paths as pending/not present.
- Include Volume 00-07 paths, purpose, and truth status.
- Include next ticket `ADR-T001`.

### `docs/nullforge/DECISION_LEDGER.md`

Create a seed ledger.

It should include:

- decision ID;
- date;
- status;
- decision;
- source/evidence;
- reversal or repair condition;
- downstream owner if any.

Seed decisions should include:

- separated NullForge docs root under `docs/nullforge/` from PF-T000;
- imported volumes under `docs/nullforge/blueprint/volumes/` from PF-T001;
- source/status baseline docs under `docs/nullforge/` from PF-T002;
- pending ADR-T001 for name/platform/stack/engine boundary;
- pending ADR-T002 for local-first/no-cloud MVP.

Do not claim ADR-T001/ADR-T002 decisions are completed.

### `docs/nullforge/ARCHIVE_POLICY.md`

Create a concise archive/source policy.

It should:

- reference Volume 1 as deeper source;
- define active docs, design memory, archive, quarantine, and prompts;
- state archive is memory without authority;
- state quarantine is unresolved/conflicting/risky material without governance power;
- state prior chat and prompts are not active truth unless explicitly promoted by a scoped ticket;
- state raw/full `ES.zip`, raw/private/local data, and ES-derived fixtures remain gated.

## Reports

Create:

```text
reports/nullforge/PF-T002/IMPLEMENTATION_REPORT.md
reports/nullforge/PF-T002/CHANGED_FILES.md
reports/nullforge/PF-T002/TEST_RESULTS.md
reports/nullforge/PF-T002/AUDITOR_PROMPT.md
```

`IMPLEMENTATION_REPORT.md` should summarize actions, scope decisions, gates, and remaining audit work.

`CHANGED_FILES.md` should list every created file and why.

`TEST_RESULTS.md` should record exact checks and results.

`AUDITOR_PROMPT.md` should be a bounded PF-T002-only prompt for an independent auditor.

## Forbidden Files, Folders, And Actions

Do not modify or create:

```text
README.md
docs/index.md
docs/STATUS.md
docs/ARCHITECTURE.md
docs/reference/
docs/contributing/
docs/nullforge/blueprint/README.md
src/
tests/
schemas/
configs/
tools/
pyproject.toml
mkdocs.yml
.github/
tickets/nullforge/
milestones/nullforge/
prompts/nullforge/
docs/nullforge/adr/
```

Do not:

- create implementation code;
- add scripts, tests, schemas, package config, CI config, generated reference docs, or dependencies;
- install dependencies;
- run ADR-T001 or downstream work;
- import prompt files as active source truth;
- import old chat logs;
- import raw/full `ES.zip`, private data, local data, or ES-derived fixtures;
- change repo/package/CLI/app/product/public identity;
- create Tauri, desktop bridge, sidecar, dataset parser, Logic Factory, Visual Replay, EvidenceCard, packaging, cloud, auth, billing, broker, or mobile artifacts;
- overwrite, move, rename, or materially edit existing ResearchCore Engine docs;
- mark technical, product, user, market, trading, or validation claims as proven.

## Implementation Tasks

1. Preflight
   - Run `git status --short --branch`.
   - Confirm branch is `docs/PF-T002-nullforge-status-source-index`.
   - Check whether the in-repo PF-T002 ticket path exists.
   - Check expected output paths do not already exist.
   - Check PF-T001 audit PASS exists.

2. Create docs
   - Create `docs/nullforge/README.md`.
   - Create `docs/nullforge/CURRENT_STATUS.md`.
   - Create `docs/nullforge/SOURCE_INDEX.md`.
   - Create `docs/nullforge/DECISION_LEDGER.md`.
   - Create `docs/nullforge/ARCHIVE_POLICY.md`.

3. Create report artifacts
   - Create `reports/nullforge/PF-T002/IMPLEMENTATION_REPORT.md`.
   - Create `reports/nullforge/PF-T002/CHANGED_FILES.md`.
   - Create `reports/nullforge/PF-T002/TEST_RESULTS.md`.
   - Create `reports/nullforge/PF-T002/AUDITOR_PROMPT.md`.

4. Final checks
   - Run and record:

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

- All repo-local Markdown links in `SOURCE_INDEX.md` resolve to existing files.
- External incoming package paths are not broken repo-local Markdown links.
- Changed files are limited to PF-T002 docs/plans/reports.
- No forbidden files/folders changed.
- Optional docs build/generated-doc checks are skipped with explanation unless docs navigation or generated docs surfaces changed.

## Required Return

Return:

```text
Implementation report path:
Changed files path:
Test results path:
Auditor prompt path:
Human gates:
Ready for auditor? YES/NO
```

Do not report PF-T002 as complete. PF-T002 is complete only after the independent auditor returns PASS, HOLD, or REJECT.
