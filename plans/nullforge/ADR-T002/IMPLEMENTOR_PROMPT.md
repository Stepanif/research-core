# Implementor Prompt: ADR-T002 - Local-first/no-cloud MVP ADR

You are the Implementor for NullForge M0 ticket `ADR-T002`.

You implement only the bounded docs/source-of-truth ADR baseline for ADR-T002. Do not write implementation code. Do not modify existing ResearchCore Engine docs. Do not create CX-T001, MB-T001, ADR-T003, M1 work, or any downstream ticket.

## Read First

Read these repo-local files:

```text
plans/nullforge/ADR-T002/CONTEXT_BUNDLE.md
plans/nullforge/ADR-T002/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/ADR-T002/PLAN.md
plans/nullforge/ADR-T002/ACCEPTANCE.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
docs/nullforge/DECISION_LEDGER.md
docs/nullforge/ARCHIVE_POLICY.md
docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md
audits/nullforge/ADR-T001/AUDIT_REPORT.md
docs/nullforge/blueprint/volumes/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md
```

If a repo-local ADR-T002 ticket file now exists, read it and record the source used in the implementation report. Do not create ticket, milestone, or prompt files.

## Planner Decisions You Must Follow

- Create one ADR file:

```text
docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
```

- Update `docs/nullforge/CURRENT_STATUS.md`.
- Update `docs/nullforge/SOURCE_INDEX.md`.
- Update `docs/nullforge/DECISION_LEDGER.md` in place by changing `NF-D0005` from pending to accepted/reference status for ADR-T002.
- Do not append a duplicate decision row for the local-first/no-cloud MVP boundary.
- Keep CX-T001, MB-T001, ADR-T003, and downstream M0/M1 work pending only.
- Do not implement local-first behavior, cloud absence enforcement, telemetry blocking, app code, bridge code, sidecar code, fixtures, schemas, tests, or data import.

## Allowed Files And Folders

You may create or modify only:

```text
docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
docs/nullforge/DECISION_LEDGER.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
reports/nullforge/ADR-T002/IMPLEMENTATION_REPORT.md
reports/nullforge/ADR-T002/CHANGED_FILES.md
reports/nullforge/ADR-T002/TEST_RESULTS.md
reports/nullforge/ADR-T002/AUDITOR_PROMPT.md
```

Treat these files as read-only:

```text
plans/nullforge/ADR-T002/CONTEXT_BUNDLE.md
plans/nullforge/ADR-T002/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/ADR-T002/PLAN.md
plans/nullforge/ADR-T002/ACCEPTANCE.md
plans/nullforge/ADR-T002/IMPLEMENTOR_PROMPT.md
docs/nullforge/ARCHIVE_POLICY.md
docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md
audits/nullforge/ADR-T001/AUDIT_REPORT.md
docs/nullforge/blueprint/volumes/*.md
README.md
docs/STATUS.md
docs/index.md
docs/ARCHITECTURE.md
docs/contributing/docs_style_guide.md
```

## Required ADR Content

Create `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`.

It must include:

- title identifying ADR-T002 and the local-first/no-cloud MVP boundary;
- date `2026-06-16`;
- status that makes clear the decision is accepted for M0 planning/source-of-truth purposes and is not implementation proof;
- context section citing ADR-T001 audit `PASS`, current status, decision ledger, Volume 00, Volume 03, and Volume 07;
- decision summary table;
- options considered;
- chosen decisions;
- consequences;
- risks and unknowns;
- human gates;
- reversal conditions;
- non-decisions;
- next action: `CX-T001` after ADR-T002 audit disposition.

It must record:

- NullForge MVP is local-first by default.
- One selected local workspace is the MVP runtime boundary.
- Local files, local manifests, local logs, local run/artifact metadata, local evidence placeholders, and local ResearchCore Engine execution are in the MVP boundary as planning assumptions.
- Local engine execution remains future scoped sidecar/command bridge work and is not implemented or proven by ADR-T002.
- Tiny/small fixtures may be used only through a later approved fixture policy.
- Full ES.zip, raw/private data, generated datasets, and ES-derived fixtures remain gated and must not be committed by default.
- Cloud storage, cloud sync, hosted backend, account/auth, billing, telemetry/analytics, mobile, marketplace, broker-live integration, live order execution, and public distribution are outside MVP scope.
- No network behavior is required for MVP; future network access requires scoped ADR/ticket and human review.
- No NullForge implementation code has started.
- ADR-T002 does not prove legal/trademark clearance, public brand approval, public distribution safety, financial advice safety, trading validity, product validation, user validation, market validation, Tauri feasibility, bridge reliability, packaging feasibility, data licensing safety, cloud-security proof, or no-cloud technical enforcement.

Options to consider:

- Local-only MVP with no cloud/auth/billing.
- Local-first MVP with optional later cloud hooks.
- Hosted/cloud-first MVP.
- Hybrid desktop with remote services.
- Defer local/cloud decision.

Reversal conditions must include:

- first proof loop cannot work locally;
- local workspace model is unsafe, confusing, or cannot protect user files;
- future validated user need requires multi-device collaboration or cloud sync;
- local engine execution becomes infeasible and a remote service is explicitly approved by later ADR/human gate;
- data licensing/privacy review changes fixture or storage rules;
- public release, telemetry, auth, billing, broker/live, or network scope is intentionally promoted by later scoped ADR and human review;
- human gate requires deferral or repair.

## Required Source Maintenance

### `docs/nullforge/DECISION_LEDGER.md`

Update `NF-D0005` in place from `Pending ADR` to accepted/reference status for ADR-T002.

The row must reference:

```text
docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
```

Keep downstream work pending. Do not append a duplicate local-first/no-cloud decision row.

### `docs/nullforge/CURRENT_STATUS.md`

Update current status to:

- keep active phase `REPO_SOURCE_IMPORT_BASELINE`;
- name active ticket `ADR-T002`;
- point next action to `CX-T001` after ADR-T002 independent audit disposition;
- keep PF-T000, PF-T001, PF-T002, and ADR-T001 complete/PASS;
- record ADR-T002 as in progress until independent audit disposition;
- keep exact sentence `No NullForge implementation code has started.`;
- state existing ResearchCore Engine implementation remains separate engine truth;
- state ADR-T002 is docs/source-of-truth only and does not implement local workspace behavior, cloud absence enforcement, telemetry blocking, bridge, sidecar, fixtures, schemas, tests, app scaffold, or release behavior;
- keep public release, repo/package/CLI/app/product identity changes, dependencies, code, tests, schemas, fixtures, raw data, cloud/auth/billing/mobile, telemetry/analytics, broker/live trading, and downstream work out of scope/gated.

### `docs/nullforge/SOURCE_INDEX.md`

Add the new ADR as a repo-local Markdown link after the ADR file exists:

```text
docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
```

Add ADR-T002 report links only after report files exist:

```text
reports/nullforge/ADR-T002/IMPLEMENTATION_REPORT.md
reports/nullforge/ADR-T002/CHANGED_FILES.md
reports/nullforge/ADR-T002/TEST_RESULTS.md
reports/nullforge/ADR-T002/AUDITOR_PROMPT.md
```

Keep CX-T001 and MB-T001 pending. Keep incoming package sources as external plain-text inputs if mentioned.

## Reports

Create:

```text
reports/nullforge/ADR-T002/IMPLEMENTATION_REPORT.md
reports/nullforge/ADR-T002/CHANGED_FILES.md
reports/nullforge/ADR-T002/TEST_RESULTS.md
reports/nullforge/ADR-T002/AUDITOR_PROMPT.md
```

`IMPLEMENTATION_REPORT.md` should summarize actions, planner decisions followed, gates, and remaining audit work.

`CHANGED_FILES.md` should list every created or modified file and why.

`TEST_RESULTS.md` should record exact checks and results.

`AUDITOR_PROMPT.md` should be a bounded ADR-T002-only prompt for an independent auditor.

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
docs/nullforge/adr/ADR-T003*
docs/nullforge/codex/
reports/nullforge/CX-T001/
reports/nullforge/MB-T001/
```

Do not:

- create implementation code;
- add scripts, tests, schemas, package config, CI config, generated reference docs, or dependencies;
- install dependencies;
- create a Tauri scaffold;
- create sidecar binaries, bridge code, parsers, packaging configs, desktop app files, cloud/auth/billing/mobile/broker artifacts, telemetry artifacts, network code, or dataset fixtures;
- import prompt files as active source truth;
- import old chat logs;
- import raw/full `ES.zip`, private data, local data, generated data, or ES-derived fixtures;
- change repo/package/CLI/app/product/public identity;
- perform trademark/legal clearance;
- claim NullForge is safe for public distribution;
- overwrite, move, rename, or materially edit existing ResearchCore Engine docs;
- mark technical, product, user, market, trading, legal, financial-advice, public-release, data-licensing, cloud-security, or validation claims as proven.

## Implementation Tasks

1. Preflight
   - Run `git status --short --branch`.
   - Confirm ADR-T001 audit PASS exists.
   - Confirm `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md` does not already exist unless updating an interrupted implementation pass.
   - Check expected report paths do not already exist.
   - Check no CX-T001 or MB-T001 paths are created by this ticket.

2. Create ADR and source maintenance docs
   - Create `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`.
   - Update `docs/nullforge/DECISION_LEDGER.md`.
   - Update `docs/nullforge/CURRENT_STATUS.md`.
   - Update `docs/nullforge/SOURCE_INDEX.md`.

3. Create report artifacts
   - Create `reports/nullforge/ADR-T002/IMPLEMENTATION_REPORT.md`.
   - Create `reports/nullforge/ADR-T002/CHANGED_FILES.md`.
   - Create `reports/nullforge/ADR-T002/TEST_RESULTS.md`.
   - Create `reports/nullforge/ADR-T002/AUDITOR_PROMPT.md`.

4. Final checks
   - Run and record:

```powershell
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
Test-Path -LiteralPath docs\nullforge\adr\ADR-T002-local-first-no-cloud-mvp.md
Test-Path -LiteralPath reports\nullforge\ADR-T002\IMPLEMENTATION_REPORT.md
Test-Path -LiteralPath reports\nullforge\ADR-T002\CHANGED_FILES.md
Test-Path -LiteralPath reports\nullforge\ADR-T002\TEST_RESULTS.md
Test-Path -LiteralPath reports\nullforge\ADR-T002\AUDITOR_PROMPT.md
rg -n "Decision: PASS" audits\nullforge\ADR-T001\AUDIT_REPORT.md
rg -n "local-first|no-cloud|cloud sync|auth|billing|telemetry|broker|live trading|public distribution|ES.zip|workspace|ResearchCore Engine|human gate|reversal" docs\nullforge\adr\ADR-T002-local-first-no-cloud-mvp.md
rg -n "ADR-T002|NF-D0005|CX-T001|MB-T001" docs\nullforge\DECISION_LEDGER.md
rg -n "ADR-T002|CX-T001|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\CURRENT_STATUS.md
rg -n "ADR-T002|CX-T001|MB-T001|ADR-T002-local-first-no-cloud-mvp" docs\nullforge\SOURCE_INDEX.md
```

Manual checks:

- All repo-local Markdown links in `docs/nullforge/SOURCE_INDEX.md` resolve to existing files.
- External incoming package paths are not broken repo-local Markdown links.
- Changed files are limited to ADR-T002 plans, allowed NullForge docs, and reports.
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

Do not report ADR-T002 as complete. ADR-T002 is complete only after the independent auditor returns PASS, HOLD, or REJECT.
