# ADR-T002 Plan

Ticket: `ADR-T002` - Local-first/no-cloud MVP ADR
Milestone: M0 - Repo Source Import + Canonical Baseline
Role: Planner
Date: `2026-06-16`

## Purpose

Produce a bounded, docs-only implementation plan for recording NullForge's local-first / no-cloud MVP boundary after ADR-T001 closed out with audit `PASS`.

ADR-T002 must decide what local-first means for the MVP and what remains out of scope. It must not create application code, Tauri scaffolds, bridge/sidecar implementation, schemas, tests, dependencies, fixtures, package changes, CI changes, generated docs, raw data, milestone/ticket/prompt imports, CX-T001, MB-T001, or any downstream work.

## Source Context Used

Repo-local context:

- `plans/nullforge/ADR-T002/CONTEXT_BUNDLE.md`
- `plans/nullforge/ADR-T002/CONTEXT_BUNDLE_MANIFEST.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/DECISION_LEDGER.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`
- `audits/nullforge/ADR-T001/AUDIT_REPORT.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md`

No external package files, prompts, old chats, raw data, or incoming ticket/milestone files were promoted or imported.

## Dependencies And Current Status

- ADR-T002 depends on ADR-T001 closeout.
- ADR-T001 closeout commit: `0853dbc docs: close out nullforge ADR-T001`.
- ADR-T001 audit decision: `PASS`.
- Current phase: `REPO_SOURCE_IMPORT_BASELINE`.
- Current status points next action to ADR-T002 after ADR-T001 closeout.
- No `docs/nullforge/adr/ADR-T002*` file existed before planner work.
- M0 remains serial:

```text
PF-T000 -> PF-T001 -> PF-T002 -> ADR-T001 -> ADR-T002 -> CX-T001 -> MB-T001
```

CX-T001 and MB-T001 must remain pending until ADR-T002 has implementation outputs and independent audit disposition.

## Planner Scope Resolutions

### Decision Ledger Update

ADR-T002 should update `docs/nullforge/DECISION_LEDGER.md` in place by changing `NF-D0005` from pending to accepted/reference status for ADR-T002.

Do not append a duplicate row for the same local-first/no-cloud MVP boundary decision. The active ledger should keep one row for `NF-D0005`.

The updated row should:

- reference `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`;
- reference the ADR-T002 audit after audit exists only in later closeout, not during initial implementation;
- keep CX-T001 / MB-T001 pending;
- avoid saying local-first implementation is complete.

### Current Status Update

ADR-T002 should update `docs/nullforge/CURRENT_STATUS.md`.

Reason: ADR-T001 closeout points next action to ADR-T002. During ADR-T002 implementation, current status should identify ADR-T002 as active and CX-T001 as next after ADR-T002 independent audit disposition.

Keep the active phase label:

```text
REPO_SOURCE_IMPORT_BASELINE
```

The status must continue to say:

```text
No NullForge implementation code has started.
```

The status must also keep existing ResearchCore Engine implementation separate and authoritative for current engine behavior.

### Source Index Update

ADR-T002 should update `docs/nullforge/SOURCE_INDEX.md`.

Reason: ADR-T002 creates a new repo-local ADR and should make that source discoverable. The update should link only to the new repo-local ADR file and ADR-T002 reports after creation. Keep incoming package sources as external plain-text inputs if mentioned. Do not create missing ticket, milestone, prompt, generic ADR, or downstream ADR/CX/MB paths.

### ADR Path

Create one ADR file:

```text
docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
```

Do not split the decision across multiple generic ADR files. Do not create ADR-T003 or downstream ADR files.

## Exact Scope

ADR-T002 planner may create:

```text
plans/nullforge/ADR-T002/CONTEXT_BUNDLE.md
plans/nullforge/ADR-T002/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/ADR-T002/PLAN.md
plans/nullforge/ADR-T002/ACCEPTANCE.md
plans/nullforge/ADR-T002/IMPLEMENTOR_PROMPT.md
```

ADR-T002 implementor may create or modify only:

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

The later auditor may create only:

```text
audits/nullforge/ADR-T002/AUDIT_REPORT.md
audits/nullforge/ADR-T002/FINDINGS.md
audits/nullforge/ADR-T002/REPAIR_PROMPT.md
```

No other files should change.

## Required ADR Content

`docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md` should include:

- title identifying ADR-T002 and the local-first/no-cloud MVP boundary;
- date `2026-06-16`;
- status such as `Accepted for M0 planning and source-of-truth purposes; not implementation proof`;
- context section citing ADR-T001 PASS, current status, decision ledger, Volume 00, Volume 03, and Volume 07;
- decision summary table;
- chosen decisions;
- options considered;
- consequences;
- risks and unknowns;
- human gates;
- reversal conditions;
- non-decisions;
- next action: `CX-T001` after ADR-T002 audit disposition.

Decision content:

- NullForge MVP is local-first by default.
- Runtime state is centered on one selected local workspace.
- Local workspace files, local manifests, local logs, local run/artifact metadata, local evidence placeholders, and local ResearchCore Engine execution are in the MVP boundary as planning assumptions.
- Local engine execution remains through future scoped sidecar/command bridge work; ADR-T002 does not implement or prove the bridge.
- Tiny/small fixtures may be used only through a later approved fixture policy; full ES.zip, raw/private data, and ES-derived fixtures remain gated and must not be committed by default.
- No cloud storage, cloud sync, hosted backend, account/auth, billing, telemetry/analytics, mobile, marketplace, broker-live integration, live order execution, or public distribution is in MVP scope.
- No network behavior is required for MVP; any future network access requires scoped ADR/ticket and human review.
- No legal/trademark clearance, public brand approval, financial advice safety, trading validity, product validation, user validation, market validation, Tauri feasibility, bridge reliability, packaging feasibility, data licensing safety, or public distribution safety is proven by ADR-T002.
- No NullForge implementation code has started.

Options to capture:

- Local-only MVP with no cloud/auth/billing.
- Local-first MVP with optional later cloud hooks.
- Hosted/cloud-first MVP.
- Hybrid desktop with remote services.
- Defer local/cloud decision.

Recommended choice:

```text
Local-only MVP with no cloud/auth/billing, while preserving later reversal through scoped ADRs if evidence proves a local-only MVP cannot support the first proof loop.
```

## Required Source Maintenance

### `docs/nullforge/DECISION_LEDGER.md`

Update `NF-D0005` in place from pending ADR to accepted/reference status for ADR-T002.

The row must reference:

```text
docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
```

Do not add a duplicate local-first/no-cloud decision row. Keep downstream items pending.

### `docs/nullforge/CURRENT_STATUS.md`

Update current status to:

- keep active phase `REPO_SOURCE_IMPORT_BASELINE`;
- set active ticket to `ADR-T002`;
- set next action to `CX-T001` after ADR-T002 independent audit disposition;
- keep PF-T000/PF-T001/PF-T002/ADR-T001 complete/PASS;
- show ADR-T002 as in progress until independent audit disposition;
- keep exact sentence `No NullForge implementation code has started.`;
- state ADR-T002 is docs/source-of-truth only and does not implement local workspace, cloud absence enforcement, bridge, sidecar, fixtures, schemas, tests, app scaffold, telemetry blocking, or release behavior.

### `docs/nullforge/SOURCE_INDEX.md`

Add the ADR-T002 ADR and implementor report artifacts after they exist:

```text
docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
reports/nullforge/ADR-T002/IMPLEMENTATION_REPORT.md
reports/nullforge/ADR-T002/CHANGED_FILES.md
reports/nullforge/ADR-T002/TEST_RESULTS.md
reports/nullforge/ADR-T002/AUDITOR_PROMPT.md
```

Keep CX-T001 and MB-T001 pending downstream. Do not create broken links to missing tickets, milestones, prompts, or downstream docs.

## Reports

Create:

```text
reports/nullforge/ADR-T002/IMPLEMENTATION_REPORT.md
reports/nullforge/ADR-T002/CHANGED_FILES.md
reports/nullforge/ADR-T002/TEST_RESULTS.md
reports/nullforge/ADR-T002/AUDITOR_PROMPT.md
```

`IMPLEMENTATION_REPORT.md` should summarize actions, source decisions, gates, and remaining audit work.

`CHANGED_FILES.md` should list every created or modified file and why.

`TEST_RESULTS.md` should record exact checks and results.

`AUDITOR_PROMPT.md` should be a bounded ADR-T002-only prompt for an independent auditor.

## Forbidden Actions

- Do not modify existing ResearchCore Engine docs:
  - `README.md`
  - `docs/index.md`
  - `docs/STATUS.md`
  - `docs/ARCHITECTURE.md`
  - `docs/reference/`
  - `docs/contributing/`
- Do not modify `src/`, `tests/`, `schemas/`, `configs/`, `tools/`, `pyproject.toml`, `mkdocs.yml`, `.github/`, package files, generated references, or CI files.
- Do not create implementation code, tests, schemas, scripts, Tauri scaffolds, sidecar binaries, bridge code, parsers, packaging configs, telemetry blockers, auth stubs, cloud stubs, or dependencies.
- Do not install dependencies.
- Do not import raw/full `ES.zip`, raw/private/local data, generated data, or ES-derived fixtures.
- Do not create or modify `tickets/nullforge/`, `milestones/nullforge/`, or `prompts/nullforge/`.
- Do not import old chat logs or prompt files as active source truth.
- Do not create CX-T001, MB-T001, ADR-T003, or downstream docs.
- Do not change repo/package/CLI/app/product/public identity.
- Do not perform legal/trademark clearance or claim public release readiness.
- Do not mark technical, product, user, market, trading, financial-advice, legal, data-licensing, or validation claims as proven.

## Step-By-Step Docs/Source Update Plan

1. Preflight
   - Run `git status --short --branch`.
   - Confirm ADR-T001 audit `PASS` exists.
   - Confirm `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md` does not already exist unless updating an existing in-progress implementor pass.
   - Confirm expected report paths do not already exist.
   - Confirm no downstream CX-T001 or MB-T001 files exist because of this ticket.

2. Create ADR and source docs updates
   - Create `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`.
   - Update `docs/nullforge/DECISION_LEDGER.md`.
   - Update `docs/nullforge/CURRENT_STATUS.md`.
   - Update `docs/nullforge/SOURCE_INDEX.md`.

3. Create ADR-T002 implementation reports
   - `IMPLEMENTATION_REPORT.md`: actions, decisions, gates, and remaining audit work.
   - `CHANGED_FILES.md`: every created/modified file and why.
   - `TEST_RESULTS.md`: exact checks and results.
   - `AUDITOR_PROMPT.md`: bounded ADR-T002-only audit prompt.

4. Verify docs/source boundaries
   - Check all required ADR-T002 output files exist.
   - Check ADR includes context, options considered, chosen decisions, consequences, risks, human gates, reversal conditions, non-decisions, and next action.
   - Check ADR includes required local-first/no-cloud decisions and avoids implementation, proof, public-release, legal, trading, financial advice, validation, and data-licensing claims.
   - Check decision ledger references ADR-T002 and keeps downstream items pending.
   - Check source index links only to existing repo-local files.
   - Check forbidden files/folders were not changed.

5. Final verification
   - Run required checks listed in `ACCEPTANCE.md`.
   - Record exact outputs in `reports/nullforge/ADR-T002/TEST_RESULTS.md`.

## Tests And Checks Required

Required:

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
- External or incoming package paths, if mentioned, remain plain text and are not broken repo-local links.
- Changed files are limited to:
  - `plans/nullforge/ADR-T002/`
  - `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`
  - `docs/nullforge/DECISION_LEDGER.md`
  - `docs/nullforge/CURRENT_STATUS.md`
  - `docs/nullforge/SOURCE_INDEX.md`
  - `reports/nullforge/ADR-T002/`
- No ResearchCore Engine docs, code, tests, schemas, configs, tools, package files, CI, milestones, tickets, prompts, raw data, fixtures, generated docs, ADR-T003, CX-T001, or MB-T001 files changed.
- ADR-T002 does not start implementation or assert proof/validation/legal/trading/data-safety claims.

Optional checks:

- `python -m mkdocs build` only if docs navigation or mkdocs-visible configuration is changed.
- `python tools/docs/verify_generated_docs_clean.py` only if generated docs tooling or generated reference files are changed.

ADR-T002 should not change docs navigation, mkdocs config, generated docs tooling, generated references, package files, or code, so these optional checks should normally be skipped with explanation. Do not install dependencies.

## Human Gate Triggers

Human review is required before:

- overwriting, moving, renaming, or materially editing existing ResearchCore Engine docs;
- changing root README, docs index, docs status, docs architecture, or docs navigation;
- changing repo, package, CLI, app, product, or public identity;
- adding dependencies, code, scripts, parsers, sidecar binaries, Tauri scaffolds, packaging configs, tests, schemas, generated docs tooling, or CI behavior;
- importing raw/full `ES.zip`, raw/private/local data, generated data, or ES-derived fixtures;
- enabling or claiming cloud storage, cloud sync, account/auth, billing, telemetry/analytics, mobile, marketplace, broker/live trading, live execution, network upload, updater, signing, AI/model calls, public release, financial advice, legal/trademark clearance, or data-licensing safety;
- marking unreviewed materials canonical;
- treating old chats or prompts as active source truth;
- creating CX-T001, MB-T001, ADR-T003, or any downstream artifacts.

Planner-detected human gates: none.

## Source-Of-Truth Risks

- "Local-first" could be read as implementation complete. Mitigate with explicit planning/source-of-truth status and no implementation proof language.
- "No cloud" could be read as technical enforcement. Mitigate by saying ADR-T002 decides MVP scope only and does not implement enforcement.
- Fixture language could accidentally authorize ES-derived data. Mitigate by keeping fixtures later, scoped, license-safe, and human-gated.
- "Telemetry absent" could imply audit of code that does not exist. Mitigate by saying telemetry/analytics are out of MVP scope and future network/telemetry changes require human gate.
- Status/source-index updates could overreach. Mitigate by changing only NullForge docs needed to point to ADR-T002 and next pending CX-T001.

## Done Definition

ADR-T002 implementation is ready for auditor when:

- ADR file exists under `docs/nullforge/adr/`.
- Decision ledger, current status, and source index reflect ADR-T002 without broken links.
- Required reports exist.
- Required checks are recorded in `reports/nullforge/ADR-T002/TEST_RESULTS.md`.
- Human gate status is explicitly reported.
- Changed files are scoped to ADR-T002 plans, allowed NullForge docs, and reports.
- `reports/nullforge/ADR-T002/AUDITOR_PROMPT.md` is ready for an independent auditor.

ADR-T002 itself is not complete until an independent auditor returns PASS, HOLD, or REJECT and a later closeout records the result.
