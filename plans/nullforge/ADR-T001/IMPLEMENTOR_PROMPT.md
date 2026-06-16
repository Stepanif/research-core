# Implementor Prompt: ADR-T001 - Name/platform/stack/engine ADR

You are the Implementor for NullForge M0 ticket `ADR-T001`.

You implement only the bounded docs/source-of-truth ADR baseline for ADR-T001. Do not write implementation code. Do not modify existing ResearchCore Engine docs. Do not create ADR-T002 or run any downstream ticket.

## Read First

Read these repo-local files:

```text
plans/nullforge/ADR-T001/CONTEXT_BUNDLE.md
plans/nullforge/ADR-T001/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/ADR-T001/PLAN.md
plans/nullforge/ADR-T001/ACCEPTANCE.md
```

The planner prompt referenced this in-repo ticket path:

```text
tickets/nullforge/ADR-T001-name-platform-stack-engine-adr.md
```

At planner time that path was absent. Use this incoming package ticket source unless the in-repo path now exists:

```text
C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\ADR-T001-name-platform-stack-engine-adr.md
```

If both paths exist, compare enough to identify the active source used and record that in the implementation report.

## Planner Decisions You Must Follow

- Update `docs/nullforge/CURRENT_STATUS.md`.
- Update `docs/nullforge/SOURCE_INDEX.md`.
- Phrase Tauri + React/TypeScript as an accepted default desktop stack direction pending bridge/packaging spikes with reversal conditions.
- Update `docs/nullforge/DECISION_LEDGER.md` in place by changing `NF-D0004` from pending to accepted/reference status for ADR-T001.
- Do not append a duplicate decision row for the same name/platform/stack/engine decision.
- Consolidate the name/platform/stack/engine boundary into the single active-ticket ADR path:

```text
docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md
```

## Allowed Files And Folders

You may create or modify only:

```text
docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md
docs/nullforge/DECISION_LEDGER.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
reports/nullforge/ADR-T001/IMPLEMENTATION_REPORT.md
reports/nullforge/ADR-T001/CHANGED_FILES.md
reports/nullforge/ADR-T001/TEST_RESULTS.md
reports/nullforge/ADR-T001/AUDITOR_PROMPT.md
```

Treat these files as read-only:

```text
plans/nullforge/ADR-T001/CONTEXT_BUNDLE.md
plans/nullforge/ADR-T001/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/ADR-T001/PLAN.md
plans/nullforge/ADR-T001/ACCEPTANCE.md
plans/nullforge/ADR-T001/IMPLEMENTOR_PROMPT.md
docs/nullforge/README.md
docs/nullforge/ARCHIVE_POLICY.md
docs/nullforge/import/PF-T000_IMPORT_PLAN.md
docs/nullforge/import/PF-T000_REPO_INVENTORY.md
docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md
audits/nullforge/PF-T002/AUDIT_REPORT.md
reports/nullforge/PF-T002/TEST_RESULTS.md
docs/nullforge/blueprint/volumes/README.md
docs/nullforge/blueprint/volumes/VOLUME_IMPORT_MANIFEST.md
docs/nullforge/blueprint/volumes/*.md
README.md
docs/STATUS.md
docs/index.md
docs/ARCHITECTURE.md
docs/contributing/docs_style_guide.md
```

## Required ADR Content

Create `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`.

It must include:

- title identifying ADR-T001 and the name/platform/stack/engine boundary;
- date `2026-06-15`;
- status that makes clear the decision is accepted for M0 planning/source-of-truth purposes and is not implementation proof;
- context section citing PF-T002 PASS and imported Volume 00/01/03/07 as main sources;
- options considered;
- chosen decisions;
- consequences;
- risks and unknowns;
- human gates;
- reversal conditions;
- next action: `ADR-T002` after ADR-T001 audit disposition.

It must record:

- `NullForge` is the working product name only.
- `NullForge` is not legally/trademark cleared and not safe/approved for public distribution.
- The repo remains `research-core`.
- Package names, CLI names, root README, existing ResearchCore docs, and public identity are unchanged.
- The internal engine label remains `ResearchCore Engine`.
- Existing ResearchCore Engine remains separate current engine truth.
- Windows 11 x64 is the first platform for future desktop proof work.
- Tauri + React/TypeScript is the accepted default desktop stack direction pending bridge/packaging spikes.
- The intended engine boundary is Python ResearchCore Engine sidecar / scoped command bridge.
- The bridge direction is narrow, allowlisted, and structured, not arbitrary shell execution.
- No NullForge implementation code has started.
- ADR-T001 does not prove Tauri feasibility, packaging feasibility, bridge reliability, product validation, user validation, market claims, trading validity, financial advice safety, legal clearance, or public distribution safety.

Options to consider:

- Name: `NullForge` as working name; keep `ResearchCore` only; defer naming.
- Platform: Windows 11 x64 first; cross-platform from start; defer platform.
- Stack: Tauri + React/TypeScript; Electron; native Python UI; defer stack.
- Engine boundary: command bridge/dev sidecar; packaged sidecar; embedded Python; local service/API; rewrite engine.

Reversal conditions must include:

- name conflict, legal/brand risk, or public release decision invalidates `NullForge` as working/public name;
- Windows 11 x64 blocks first-user proof or a later audited decision changes platform priority;
- Tauri cannot support required filesystem/process/permission/packaging/dev velocity needs;
- sidecar/command bridge repeatedly fails, requires arbitrary shell execution, or packaged sidecar is worse than an alternative engine API;
- app/engine split becomes impossible to communicate or maintain;
- human gate requires deferral or repair.

## Required Source Maintenance

### `docs/nullforge/DECISION_LEDGER.md`

Update `NF-D0004` in place from `Pending ADR` to accepted/reference status for ADR-T001.

The row must reference:

```text
docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md
```

Keep ADR-T002 pending. Do not append a duplicate name/platform/stack/engine decision row.

### `docs/nullforge/CURRENT_STATUS.md`

Update the active ticket from `PF-T002` to `ADR-T001`.

Keep active phase:

```text
REPO_SOURCE_IMPORT_BASELINE
```

Record:

- PF-T000, PF-T001, and PF-T002 are complete/PASS.
- ADR-T001 is in progress until independent audit disposition.
- ADR-T002 is next after ADR-T001 audit disposition.
- exact sentence: `No NullForge implementation code has started.`
- existing ResearchCore Engine implementation remains separate engine truth.
- public release, repo/package/CLI/app/product identity changes, desktop scaffold, bridge implementation, sidecar implementation, dependencies, code, tests, schemas, fixtures, raw data, broker/live trading, cloud/auth/billing/mobile scope remain out of scope/gated.

### `docs/nullforge/SOURCE_INDEX.md`

Add the new ADR as a repo-local Markdown link after the ADR file exists:

```text
docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md
```

Mark ADR-T002 as pending/not present. Keep incoming package sources as external plain-text inputs only.

## Reports

Create:

```text
reports/nullforge/ADR-T001/IMPLEMENTATION_REPORT.md
reports/nullforge/ADR-T001/CHANGED_FILES.md
reports/nullforge/ADR-T001/TEST_RESULTS.md
reports/nullforge/ADR-T001/AUDITOR_PROMPT.md
```

`IMPLEMENTATION_REPORT.md` should summarize actions, planner decisions followed, gates, and remaining audit work.

`CHANGED_FILES.md` should list every created or modified file and why.

`TEST_RESULTS.md` should record exact checks and results.

`AUDITOR_PROMPT.md` should be a bounded ADR-T001-only prompt for an independent auditor.

## Forbidden Files, Folders, And Actions

Do not modify or create:

```text
README.md
docs/index.md
docs/STATUS.md
docs/ARCHITECTURE.md
docs/reference/
docs/contributing/
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
docs/adr/
docs/architecture/
docs/nullforge/adr/ADR-T002*
```

Do not:

- create implementation code;
- add scripts, tests, schemas, package config, CI config, generated reference docs, or dependencies;
- install dependencies;
- run ADR-T002 or downstream work;
- create a Tauri scaffold;
- create sidecar binaries, bridge code, parsers, packaging configs, desktop app files, cloud/auth/billing/mobile/broker artifacts, or dataset fixtures;
- import prompt files as active source truth;
- import old chat logs;
- import raw/full `ES.zip`, private data, local data, or ES-derived fixtures;
- change repo/package/CLI/app/product/public identity;
- perform trademark/legal clearance;
- claim NullForge is safe for public distribution;
- overwrite, move, rename, or materially edit existing ResearchCore Engine docs;
- mark technical, product, user, market, trading, legal, public-release, or validation claims as proven.

## Implementation Tasks

1. Preflight
   - Run `git status --short --branch`.
   - Confirm branch is `docs/ADR-T001-nullforge-name-platform-stack-engine`.
   - Check whether the in-repo ADR-T001 ticket path exists.
   - Check expected output paths do not already exist except existing NullForge source docs to update.
   - Check PF-T002 audit PASS exists.

2. Create ADR and source maintenance docs
   - Create `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`.
   - Update `docs/nullforge/DECISION_LEDGER.md`.
   - Update `docs/nullforge/CURRENT_STATUS.md`.
   - Update `docs/nullforge/SOURCE_INDEX.md`.

3. Create report artifacts
   - Create `reports/nullforge/ADR-T001/IMPLEMENTATION_REPORT.md`.
   - Create `reports/nullforge/ADR-T001/CHANGED_FILES.md`.
   - Create `reports/nullforge/ADR-T001/TEST_RESULTS.md`.
   - Create `reports/nullforge/ADR-T001/AUDITOR_PROMPT.md`.

4. Final checks
   - Run and record:

```powershell
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
Test-Path -LiteralPath docs\nullforge\adr\ADR-T001-name-platform-stack-engine.md
Test-Path -LiteralPath reports\nullforge\ADR-T001\IMPLEMENTATION_REPORT.md
Test-Path -LiteralPath reports\nullforge\ADR-T001\CHANGED_FILES.md
Test-Path -LiteralPath reports\nullforge\ADR-T001\TEST_RESULTS.md
Test-Path -LiteralPath reports\nullforge\ADR-T001\AUDITOR_PROMPT.md
rg -n "Decision: PASS" audits\nullforge\PF-T002\AUDIT_REPORT.md
rg -n "NullForge|working product name|research-core|ResearchCore Engine|Windows 11 x64|Tauri|React|TypeScript|sidecar|command bridge|reversal|human gate" docs\nullforge\adr\ADR-T001-name-platform-stack-engine.md
rg -n "ADR-T001|NF-D0004|ADR-T002" docs\nullforge\DECISION_LEDGER.md
rg -n "ADR-T001|ADR-T002|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\CURRENT_STATUS.md
rg -n "ADR-T001|ADR-T002|ADR-T001-name-platform-stack-engine" docs\nullforge\SOURCE_INDEX.md
```

Manual checks:

- All repo-local Markdown links in `docs/nullforge/SOURCE_INDEX.md` resolve to existing files.
- External incoming package paths are not broken repo-local Markdown links.
- Changed files are limited to ADR-T001 plans, allowed NullForge docs, and reports.
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

Do not report ADR-T001 as complete. ADR-T001 is complete only after the independent auditor returns PASS, HOLD, or REJECT.
