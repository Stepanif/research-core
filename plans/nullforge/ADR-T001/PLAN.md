# ADR-T001 Plan

Ticket: ADR-T001 - Name/platform/stack/engine ADR
Milestone: M0 - Repo Source Import + Canonical Baseline
Role: Planner

## Purpose

Produce a bounded, docs-only implementation plan for recording the NullForge working name, first platform, default desktop stack direction, and ResearchCore Engine boundary after PF-T002 created the current source/status baseline.

ADR-T001 must not rename the repo, change package names, create a Tauri scaffold, add dependencies, perform legal/trademark clearance, claim public-distribution safety, modify ResearchCore Engine docs, or start ADR-T002 or downstream work.

## Source Context Used

Repo-local context:

- `plans/nullforge/ADR-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/ADR-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `docs/nullforge/README.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/DECISION_LEDGER.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/import/PF-T000_IMPORT_PLAN.md`
- `docs/nullforge/import/PF-T000_REPO_INVENTORY.md`
- `docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md`
- `audits/nullforge/PF-T002/AUDIT_REPORT.md`
- `reports/nullforge/PF-T002/TEST_RESULTS.md`
- `docs/nullforge/blueprint/volumes/README.md`
- `docs/nullforge/blueprint/volumes/VOLUME_IMPORT_MANIFEST.md`
- Imported Volume 00-07 docs under `docs/nullforge/blueprint/volumes/`

Active incoming ticket source:

- `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\ADR-T001-name-platform-stack-engine-adr.md`

The in-repo ADR-T001 ticket path is absent at planner time:

- `tickets/nullforge/ADR-T001-name-platform-stack-engine-adr.md`

Existing ResearchCore docs used for boundary context:

- `README.md`
- `docs/STATUS.md`
- `docs/index.md`
- `docs/ARCHITECTURE.md`

## Dependencies And Current Status

- ADR-T001 depends on PF-T002.
- PF-T000 audit decision: PASS.
- PF-T001 audit decision: PASS.
- PF-T002 audit decision: PASS.
- PF-T002 was committed, pushed, merged to `main`, and pushed.
- Current branch: `docs/ADR-T001-nullforge-name-platform-stack-engine`.
- Current working tree contains only ADR-T001 context bundle files under `plans/nullforge/ADR-T001/`.
- M0 remains serial:

```text
PF-T000 -> PF-T001 -> PF-T002 -> ADR-T001 -> ADR-T002 -> CX-T001 -> MB-T001
```

ADR-T002 must remain blocked until ADR-T001 has implementation outputs and an independent audit disposition.

## Planner Scope Decisions

### Current Status Update

ADR-T001 should update `docs/nullforge/CURRENT_STATUS.md`.

Reason: PF-T002 intentionally created the active status file and pointed the next action to ADR-T001. After ADR-T001 implementation starts, the status should identify ADR-T001 as the active ticket and point next action to ADR-T002 after ADR-T001 audit disposition. This is bounded source-of-truth maintenance and does not touch ResearchCore Engine docs.

Keep the active phase label:

```text
REPO_SOURCE_IMPORT_BASELINE
```

The status must continue to say no NullForge implementation code has started and that existing ResearchCore Engine implementation remains separate engine truth.

### Source Index Update

ADR-T001 should update `docs/nullforge/SOURCE_INDEX.md`.

Reason: ADR-T001 creates the first NullForge ADR and should make that repo-local source discoverable. The update should link only to the new repo-local ADR file and leave incoming package ticket/milestone sources as external plain text. It should not create `tickets/nullforge/`, `milestones/nullforge/`, `prompts/nullforge/`, or generic `docs/adr/` paths.

### Tauri + React/TypeScript Wording

The ADR should phrase Tauri + React/TypeScript as an accepted default stack direction pending bridge and packaging spikes, with explicit reversal conditions.

Do not claim Tauri feasibility, packaging feasibility, bridge reliability, or public distribution safety is proven.

### Decision Ledger Update

ADR-T001 should update `docs/nullforge/DECISION_LEDGER.md` in place by changing `NF-D0004` from pending to accepted/reference status for ADR-T001.

Do not append a second duplicate decision row for the same name/platform/stack/engine decision. Git history preserves the transition from pending to accepted; the active ledger should avoid conflicting duplicate rows.

The updated row should:

- reference `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`;
- record status as accepted by ADR-T001 or equivalent clear wording;
- keep reversal/repair conditions tied to name conflict, Windows proof failure, Tauri/packaging/bridge failure, or future scoped ADR.

### Single ADR Path

ADR-T001 should consolidate the name/platform/stack/engine boundary into the single active-ticket ADR path:

```text
docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md
```

Reason: the active incoming ticket and PF-T000 plan name one ADR-T001 file. Older volume examples split the decisions across multiple generic ADR files, but those examples are superseded for M0 execution by the active ticket path. The ADR can contain separate sections for name, platform, stack, and engine boundary without creating multiple ADR files.

## Exact Scope

ADR-T001 planner may create:

```text
plans/nullforge/ADR-T001/PLAN.md
plans/nullforge/ADR-T001/ACCEPTANCE.md
plans/nullforge/ADR-T001/IMPLEMENTOR_PROMPT.md
```

ADR-T001 implementor may create or modify only:

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

The later auditor may create only:

```text
audits/nullforge/ADR-T001/AUDIT_REPORT.md
audits/nullforge/ADR-T001/FINDINGS.md
audits/nullforge/ADR-T001/REPAIR_PROMPT.md
```

ADR-T001 may also leave existing ADR-T001 context/planner files under:

```text
plans/nullforge/ADR-T001/
```

No other files should change.

## Required ADR Content

`docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` should include:

- title identifying ADR-T001 and the name/platform/stack/engine boundary;
- date `2026-06-15`;
- status such as `Accepted for M0 planning; not implementation proof`;
- context section citing PF-T002 PASS and imported Volume 00/01/03/07 as main sources;
- decision summary table;
- options considered;
- chosen decisions;
- consequences, risks, unknowns, human gates, and reversal conditions;
- explicit next action: ADR-T002 after ADR-T001 audit disposition.

Decision content:

- `NullForge` is the working product name only.
- `NullForge` is not cleared for public distribution, trademark/domain use, legal claims, company identity, or public release.
- Repo remains `research-core`.
- Package names, CLI names, and existing ResearchCore Engine docs remain unchanged.
- Internal engine label remains `ResearchCore Engine`.
- Existing ResearchCore Engine is the current Python CLI/artifact/validation engine and remains separate engine truth.
- Windows 11 x64 is the first platform for future desktop proof work.
- Tauri + React/TypeScript is the accepted default desktop stack direction pending bridge/packaging spikes.
- The intended engine boundary is a Python ResearchCore Engine sidecar / scoped command bridge.
- The bridge direction is a narrow, allowlisted, structured command protocol, not arbitrary shell execution.
- No NullForge implementation code has started.
- ADR-T001 does not prove bridge feasibility, Tauri feasibility, packaging feasibility, product validation, user validation, market claims, live trading readiness, financial advice safety, or public distribution safety.

Options to capture:

- name options: use `NullForge` as working name, keep `ResearchCore` only, defer naming;
- platform options: Windows 11 x64 first, cross-platform from start, defer platform;
- stack options: Tauri + React/TypeScript, Electron, native Python UI, defer stack;
- engine boundary options: command bridge/dev sidecar, packaged sidecar, embedded Python, local service/API, rewrite engine.

Reversal conditions:

- name conflict, legal/brand risk, or public release decision invalidates `NullForge` as working/public name;
- Windows 11 x64 blocks first-user proof or a later audited decision changes platform priority;
- Tauri cannot support required filesystem/process/permission/packaging/dev velocity needs;
- sidecar/command bridge repeatedly fails, requires arbitrary shell execution, or packaged sidecar is worse than an alternative engine API;
- app/engine split becomes impossible to communicate or maintain;
- human gate requires deferral or repair.

## Required Source Maintenance

### `docs/nullforge/DECISION_LEDGER.md`

Update `NF-D0004` in place from pending ADR to accepted/reference status for ADR-T001.

The row must reference:

```text
docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md
```

Keep ADR-T002 pending.

### `docs/nullforge/CURRENT_STATUS.md`

Update the active ticket from `PF-T002` to `ADR-T001`.

Keep active phase:

```text
REPO_SOURCE_IMPORT_BASELINE
```

Record:

- PF-T000, PF-T001, and PF-T002 are complete/PASS.
- ADR-T001 is in progress until independent audit disposition.
- ADR-T002 is next after ADR-T001 audit.
- No NullForge implementation code has started.
- Existing ResearchCore Engine implementation remains separate engine truth.
- Public release, repo/package/CLI/app/product identity changes, desktop scaffold, bridge implementation, sidecar implementation, dependencies, code, tests, schemas, fixtures, raw data, broker/live trading, cloud/auth/billing/mobile scope remain out of scope/gated.

### `docs/nullforge/SOURCE_INDEX.md`

Add the new ADR as a repo-local active/pending ticket artifact once created:

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

`IMPLEMENTATION_REPORT.md` should summarize actions, scope decisions, gates, and remaining audit work.

`CHANGED_FILES.md` should list every created or modified file and why.

`TEST_RESULTS.md` should record exact checks and results.

`AUDITOR_PROMPT.md` should be a bounded ADR-T001-only prompt for an independent auditor.

## Forbidden Actions

- Do not modify existing ResearchCore Engine docs:
  - `README.md`
  - `docs/index.md`
  - `docs/STATUS.md`
  - `docs/ARCHITECTURE.md`
  - `docs/reference/`
  - `docs/contributing/`
- Do not modify `src/`, `tests/`, `schemas/`, `configs/`, `tools/`, `pyproject.toml`, `mkdocs.yml`, `.github/`, package files, generated references, or CI files.
- Do not create implementation code, tests, schemas, scripts, Tauri scaffolds, sidecar binaries, parsers, packaging configs, or dependencies.
- Do not install dependencies.
- Do not import raw/full `ES.zip`, raw/private/local data, or ES-derived fixtures.
- Do not import old chat logs.
- Do not import prompt files as active source truth.
- Do not create `tickets/nullforge/`, `milestones/nullforge/`, or `prompts/nullforge/` content in ADR-T001.
- Do not create ADR-T002 or downstream docs.
- Do not change repo/package/CLI/app/product/public identity.
- Do not perform trademark/legal clearance or claim NullForge is safe for public release.
- Do not mark technical, product, user, market, trading, or validation claims as proven.

## Step-By-Step Docs/Source Update Plan

1. Preflight
   - Run `git status --short --branch`.
   - Confirm branch is `docs/ADR-T001-nullforge-name-platform-stack-engine`.
   - Check whether the in-repo ADR-T001 ticket path exists.
   - Confirm active incoming ADR-T001 ticket source if in-repo path is absent.
   - Confirm PF-T002 audit PASS is present.
   - Confirm expected output paths do not already exist unless explicitly updating existing NullForge source docs.

2. Create ADR and source docs updates
   - Create `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`.
   - Update `docs/nullforge/DECISION_LEDGER.md`.
   - Update `docs/nullforge/CURRENT_STATUS.md`.
   - Update `docs/nullforge/SOURCE_INDEX.md`.

3. Create ADR-T001 implementation reports
   - `IMPLEMENTATION_REPORT.md`: actions, decisions, gates, and remaining audit work.
   - `CHANGED_FILES.md`: every created/modified file and why.
   - `TEST_RESULTS.md`: exact checks and results.
   - `AUDITOR_PROMPT.md`: bounded ADR-T001-only audit prompt.

4. Verify docs/source boundaries
   - Check all required ADR-T001 output files exist.
   - Check ADR includes date, context, options considered, chosen option, risks, reversal conditions, and human gates.
   - Check ADR includes required decisions and does not imply implementation proof or public/legal clearance.
   - Check decision ledger references ADR-T001 and keeps ADR-T002 pending.
   - Check source index links only to existing repo-local files.
   - Check root README, `docs/index.md`, `docs/STATUS.md`, and `docs/ARCHITECTURE.md` were not modified.

5. Final verification
   - Run `git status --short --branch`.
   - Run `git status --short --untracked-files=all`.
   - Run `git diff --name-only`.
   - Manually confirm changed paths are limited to:
     - `plans/nullforge/ADR-T001/`
     - `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`
     - `docs/nullforge/DECISION_LEDGER.md`
     - `docs/nullforge/CURRENT_STATUS.md`
     - `docs/nullforge/SOURCE_INDEX.md`
     - `reports/nullforge/ADR-T001/`

## Tests And Checks Required

Required:

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

- All Markdown links in `docs/nullforge/SOURCE_INDEX.md` that target repo-local files resolve to existing files.
- Incoming package paths remain plain text/external active inputs, not broken repo-local links.
- No existing ResearchCore Engine docs were changed.
- No code, tests, schemas, dependencies, raw data, generated references, package files, CI, milestones, tickets, prompts, or ADR-T002 files were created or modified.
- ADR-T001 does not claim legal clearance, public release safety, Tauri feasibility proof, packaging proof, bridge proof, product validation, user validation, market claims, trading validity, or implementation start.

Optional checks:

- `python -m mkdocs build` only if docs navigation or mkdocs-visible configuration is changed.
- `python tools/docs/verify_generated_docs_clean.py` only if generated docs tooling or generated reference files are changed.

ADR-T001 should not change docs navigation, mkdocs config, generated docs tooling, generated references, package files, or code, so these optional checks should normally be skipped with explanation. Do not install dependencies.

## Human Gate Triggers

Human review is required before:

- overwriting, moving, renaming, or materially editing existing ResearchCore Engine docs;
- changing root README, docs index, docs status, docs architecture, or docs navigation;
- changing repo, package, CLI, app, product, or public identity;
- adding dependencies, code, scripts, parsers, sidecar binaries, Tauri scaffolds, packaging configs, tests, schemas, generated docs tooling, or CI behavior;
- importing raw/full `ES.zip`, raw/private/local data, or ES-derived fixtures;
- marking unreviewed materials canonical;
- treating old chats or prompts as active source truth;
- creating ADR-T002 or any downstream artifacts;
- broadening into public release, legal/trademark naming, AI strategy activation, broker/live trading, financial advice, auth, billing, cloud sync, marketplace, or mobile scope.

Planner-detected human gates: NONE.

## Source-Of-Truth Risks

- ADR wording could accidentally imply a public brand decision. Mitigate with "working product name only" and explicit no-legal-clearance/no-public-release language.
- Stack wording could imply implementation feasibility is proven. Mitigate with "default stack direction pending bridge/packaging spikes" and reversal conditions.
- Engine boundary wording could imply ResearchCore Engine is being renamed or rewritten. Mitigate by preserving `research-core` and `ResearchCore Engine` identity and describing a future scoped bridge only.
- Updating current status/source index broadens beyond the active ticket output list. Mitigate by treating those edits as directly related source-of-truth maintenance and limiting them to NullForge docs only.
- Decision ledger update could duplicate the same decision. Mitigate by updating `NF-D0004` in place and not appending a duplicate row.

## Done Definition

ADR-T001 implementation is ready for auditor when:

- ADR file exists under `docs/nullforge/adr/`.
- Decision ledger, current status, and source index reflect ADR-T001 without broken links.
- Required reports exist.
- Required checks are recorded in `reports/nullforge/ADR-T001/TEST_RESULTS.md`.
- Human gate status is explicitly reported.
- Changed files are scoped to ADR-T001 plans, NullForge docs, and reports.
- `reports/nullforge/ADR-T001/AUDITOR_PROMPT.md` is ready for an independent auditor.

ADR-T001 itself is not complete until an auditor returns PASS, HOLD, or REJECT and the result is recorded by the later M0 handoff workflow.
