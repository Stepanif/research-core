# CX-T001 Plan

Ticket: `CX-T001` - NullForge Codex role-loop docs
Milestone: M0 - Repo Source Import + Canonical Baseline
Role: Planner
Date: `2026-06-16`

## Purpose

Produce a bounded, docs-only implementation plan for creating NullForge Codex role-loop documentation after ADR-T002 audit `PASS`.

CX-T001 should turn the imported Volume 02 workflow into one repo-local, NullForge-specific active doc that future tickets can follow. It must not start implementation work, create app scaffolds, import data, create prompt archives, create milestone/ticket files, or start MB-T001, ADR-T003, M1, or downstream work.

## Source Context Used

Repo-local context:

- `plans/nullforge/CX-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/CX-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/DECISION_LEDGER.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`
- `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`
- `audits/nullforge/ADR-T002/AUDIT_REPORT.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md`

No external package files, prompts, old chats, raw data, incoming ticket/milestone files, or implementation source files were promoted or imported by this planner.

## Dependencies And Current Status

- CX-T001 depends on ADR-T002 audit disposition.
- ADR-T002 audit decision: `PASS`.
- Current phase: `REPO_SOURCE_IMPORT_BASELINE`.
- Current status points next action to CX-T001 planner after ADR-T002 branch closeout.
- No NullForge implementation code has started.
- Current working tree still contains uncommitted ADR-T002 closeout artifacts. CX-T001 implementation should not start until ADR-T002 branch closeout or explicit human approval.
- M0 remains serial:

```text
PF-T000 -> PF-T001 -> PF-T002 -> ADR-T001 -> ADR-T002 -> CX-T001 -> MB-T001
```

MB-T001, ADR-T003, M1, and downstream work must remain pending until CX-T001 has implementation outputs and independent audit disposition.

## Planner Scope Resolutions

### Number Of Workflow Docs

CX-T001 should create one repo-local workflow doc:

```text
docs/nullforge/codex/CODEX_ROLE_LOOP.md
```

Reason: CX-T001 is scoped to "Codex role-loop docs." One doc is enough to adapt Volume 02 to the repo without creating a larger docs tree. Separate QA/human gate docs, ticket files, milestone packs, or prompt archives require later scoped tickets.

### Decision Ledger Update

CX-T001 should not update `docs/nullforge/DECISION_LEDGER.md` by default.

Reason: the role-loop decision is already imported as Volume 02 planning/workflow source, and CX-T001 creates operational workflow documentation rather than a new product or architecture decision. If the implementor discovers a new decision is needed, stop and request human review instead of silently adding a ledger row.

### Current Status Update

CX-T001 should update `docs/nullforge/CURRENT_STATUS.md` during implementation.

Reason: after CX-T001 implementation starts, current status should identify CX-T001 as the active ticket and MB-T001 as the next ticket after CX-T001 independent audit disposition.

Keep the active phase label:

```text
REPO_SOURCE_IMPORT_BASELINE
```

The status must continue to say:

```text
No NullForge implementation code has started.
```

### Source Index Update

CX-T001 should update `docs/nullforge/SOURCE_INDEX.md`.

Reason: CX-T001 creates a new repo-local workflow doc and implementation reports that should be discoverable. The source index should link only to repo-local files that exist after creation.

### Implementor Handoff Readiness

This plan is ready for implementor handoff only after ADR-T002 branch closeout or explicit human approval to continue on the dirty branch.

If the implementor sees uncommitted changes outside `plans/nullforge/CX-T001/` and the allowed CX-T001 implementation files, it should stop and report the blocker.

## Exact Scope

CX-T001 planner may create only:

```text
plans/nullforge/CX-T001/CONTEXT_BUNDLE.md
plans/nullforge/CX-T001/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/CX-T001/PLAN.md
plans/nullforge/CX-T001/ACCEPTANCE.md
plans/nullforge/CX-T001/IMPLEMENTOR_PROMPT.md
```

CX-T001 implementor may create or modify only:

```text
docs/nullforge/codex/CODEX_ROLE_LOOP.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
reports/nullforge/CX-T001/IMPLEMENTATION_REPORT.md
reports/nullforge/CX-T001/CHANGED_FILES.md
reports/nullforge/CX-T001/TEST_RESULTS.md
reports/nullforge/CX-T001/AUDITOR_PROMPT.md
```

The later auditor may create only:

```text
audits/nullforge/CX-T001/AUDIT_REPORT.md
audits/nullforge/CX-T001/FINDINGS.md
audits/nullforge/CX-T001/REPAIR_PROMPT.md
```

No other files should change.

## Required CODEX_ROLE_LOOP Content

`docs/nullforge/codex/CODEX_ROLE_LOOP.md` should include:

- title identifying NullForge Codex role-loop docs;
- date `2026-06-16`;
- status such as `Accepted for CX-T001 implementation review; not implementation proof` until audit disposition exists;
- context citing active status, source index, archive policy, ADR-T001, ADR-T002, ADR-T002 audit `PASS`, Volume 02, and Volume 07;
- explicit statement that NullForge is still planning/docs only and no implementation code has started;
- role-loop overview:

```text
Human / ChatGPT Architect -> Context Curator -> Planner -> Implementor -> Auditor -> Repair if needed -> Human gate -> Next ticket
```

- role responsibilities for Human / ChatGPT Architect, Context Curator, Planner, Implementor, Auditor, and Repair Implementor;
- per-ticket artifact tree for `plans/`, `reports/`, and `audits/`;
- expected sections for context bundle, manifest, plan, acceptance, implementor prompt, implementation report, changed files report, test results, auditor prompt, audit report, findings, and repair prompt;
- PASS / HOLD / REJECT rules;
- human gate triggers;
- stop conditions;
- docs-only ticket handling rules;
- branch/ticket hygiene rules;
- source-of-truth, archive, quarantine, and prompt handling rules;
- CX-T001 boundaries and non-decisions;
- next action: `MB-T001` after CX-T001 independent audit disposition.

The doc must preserve ADR-T001 and ADR-T002 boundaries:

- working product name only, no public/legal/trademark clearance;
- Windows 11 x64 first, Tauri + React/TypeScript direction only, no implementation proof;
- ResearchCore Engine remains separate engine truth;
- local-first/no-cloud MVP boundary;
- no cloud/auth/billing/mobile/marketplace/telemetry/broker/live/public release scope;
- no raw/full ES.zip, private/local data, generated datasets, or ES-derived fixtures;
- no app code, Tauri scaffold, sidecar, bridge, schemas, tests, dependencies, package changes, CI changes, generated docs, data imports, or fixtures.

## Required Source Maintenance

### `docs/nullforge/CURRENT_STATUS.md`

Update current status to:

- keep active phase `REPO_SOURCE_IMPORT_BASELINE`;
- name active ticket `CX-T001`;
- point next action to `MB-T001` after CX-T001 independent audit disposition;
- keep PF-T000, PF-T001, PF-T002, ADR-T001, and ADR-T002 complete/PASS;
- show CX-T001 as in progress until independent audit disposition;
- keep exact sentence `No NullForge implementation code has started.`;
- state CX-T001 is docs/workflow source only and does not create app code, implementation code, dependencies, schemas, tests, fixtures, data imports, Tauri scaffolds, bridge/sidecar work, prompt archives, ticket/milestone imports, MB-T001, ADR-T003, M1, or downstream work.

### `docs/nullforge/SOURCE_INDEX.md`

Add the new workflow doc after it exists:

```text
docs/nullforge/codex/CODEX_ROLE_LOOP.md
```

Add CX-T001 planner and report links only after files exist:

```text
plans/nullforge/CX-T001/CONTEXT_BUNDLE.md
plans/nullforge/CX-T001/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/CX-T001/PLAN.md
plans/nullforge/CX-T001/ACCEPTANCE.md
plans/nullforge/CX-T001/IMPLEMENTOR_PROMPT.md
reports/nullforge/CX-T001/IMPLEMENTATION_REPORT.md
reports/nullforge/CX-T001/CHANGED_FILES.md
reports/nullforge/CX-T001/TEST_RESULTS.md
reports/nullforge/CX-T001/AUDITOR_PROMPT.md
```

Keep MB-T001 pending. Do not create broken links to tickets, milestones, prompt archives, CX-T001 audit files before audit exists, ADR-T003, M1, or downstream docs.

## Reports

The implementor should create:

```text
reports/nullforge/CX-T001/IMPLEMENTATION_REPORT.md
reports/nullforge/CX-T001/CHANGED_FILES.md
reports/nullforge/CX-T001/TEST_RESULTS.md
reports/nullforge/CX-T001/AUDITOR_PROMPT.md
```

`IMPLEMENTATION_REPORT.md` should summarize actions, planner decisions followed, gates, and remaining audit work.

`CHANGED_FILES.md` should list every created or modified file and why.

`TEST_RESULTS.md` should record exact checks and results.

`AUDITOR_PROMPT.md` should be a bounded CX-T001-only prompt for an independent auditor.

## Forbidden Actions

- Do not modify existing ResearchCore Engine docs:
  - `README.md`
  - `docs/index.md`
  - `docs/STATUS.md`
  - `docs/ARCHITECTURE.md`
  - `docs/reference/`
  - `docs/contributing/`
- Do not modify `src/`, `tests/`, `schemas/`, `configs/`, `tools/`, `pyproject.toml`, `mkdocs.yml`, `.github/`, package files, generated references, or CI files.
- Do not create implementation code, tests, schemas, scripts, Tauri scaffolds, sidecar binaries, bridge code, parsers, packaging configs, telemetry blockers, auth stubs, cloud stubs, dependencies, app files, or generated docs.
- Do not install dependencies.
- Do not create `docs/nullforge/qa/HUMAN_GATES.md`.
- Do not create or modify `tickets/nullforge/`, `milestones/nullforge/`, or `prompts/nullforge/`.
- Do not create `reports/nullforge/MB-T001/`, `reports/nullforge/ADR-T003/`, `reports/nullforge/M1/`, or downstream artifacts.
- Do not create CX-T001 audit files during implementation.
- Do not import old chat logs or prompt files as active source truth.
- Do not import raw/full `ES.zip`, raw/private/local data, generated data, or ES-derived fixtures.
- Do not change repo/package/CLI/app/product/public identity.
- Do not perform legal/trademark clearance or claim public release readiness.
- Do not mark technical, product, user, market, trading, financial-advice, legal, data-licensing, privacy, security, or validation claims as proven.

## Step-By-Step Docs/Source Update Plan

1. Preflight
   - Run `git status --short --branch`.
   - Confirm ADR-T002 audit `PASS` exists.
   - Confirm ADR-T002 branch closeout is complete or human explicitly approved continuing with a dirty tree.
   - Confirm `docs/nullforge/codex/CODEX_ROLE_LOOP.md` does not already exist unless updating an interrupted CX-T001 implementation pass.
   - Confirm expected CX-T001 report paths do not already exist.
   - Confirm no MB-T001, ADR-T003, M1, ticket, milestone, prompt, app, data, or implementation paths are created by this ticket.

2. Create workflow doc and source maintenance updates
   - Create `docs/nullforge/codex/CODEX_ROLE_LOOP.md`.
   - Update `docs/nullforge/CURRENT_STATUS.md`.
   - Update `docs/nullforge/SOURCE_INDEX.md`.
   - Do not update `docs/nullforge/DECISION_LEDGER.md` unless a new decision is discovered; if that happens, stop and request human review.

3. Create CX-T001 implementation reports
   - `IMPLEMENTATION_REPORT.md`: actions, decisions followed, gates, and remaining audit work.
   - `CHANGED_FILES.md`: every created/modified file and why.
   - `TEST_RESULTS.md`: exact checks and results.
   - `AUDITOR_PROMPT.md`: bounded CX-T001-only audit prompt.

4. Verify docs/source boundaries
   - Check all required CX-T001 output files exist.
   - Check CODEX_ROLE_LOOP includes role-loop responsibilities, artifact tree, PASS/HOLD/REJECT, human gates, stop conditions, source/truth rules, and next action.
   - Check CODEX_ROLE_LOOP avoids implementation proof, product validation, legal/trademark, trading, financial-advice, public-release, data-safety, cloud-security, and telemetry-enforcement claims.
   - Check source index links only to repo-local files that exist.
   - Check forbidden files/folders were not changed.

5. Final verification
   - Run required checks listed in `ACCEPTANCE.md`.
   - Record exact outputs in `reports/nullforge/CX-T001/TEST_RESULTS.md`.

## Tests And Checks Required

Required:

```powershell
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
git diff --check
Test-Path -LiteralPath docs\nullforge\codex\CODEX_ROLE_LOOP.md
Test-Path -LiteralPath reports\nullforge\CX-T001\IMPLEMENTATION_REPORT.md
Test-Path -LiteralPath reports\nullforge\CX-T001\CHANGED_FILES.md
Test-Path -LiteralPath reports\nullforge\CX-T001\TEST_RESULTS.md
Test-Path -LiteralPath reports\nullforge\CX-T001\AUDITOR_PROMPT.md
rg -n "Decision: PASS" audits\nullforge\ADR-T002\AUDIT_REPORT.md
rg -n "Context Curator|Planner|Implementor|Auditor|PASS|HOLD|REJECT|human gate|stop condition|No NullForge implementation code has started|CX-T001|MB-T001" docs\nullforge\codex\CODEX_ROLE_LOOP.md
rg -n "CX-T001|CODEX_ROLE_LOOP|MB-T001|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md
```

Manual checks:

- All repo-local Markdown links in `docs/nullforge/SOURCE_INDEX.md` resolve to existing files.
- External or incoming package paths, if mentioned, remain plain text and are not broken repo-local links.
- Changed files are limited to:
  - `plans/nullforge/CX-T001/`
  - `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
  - `docs/nullforge/CURRENT_STATUS.md`
  - `docs/nullforge/SOURCE_INDEX.md`
  - `reports/nullforge/CX-T001/`
- No ResearchCore Engine docs, code, tests, schemas, configs, tools, package files, CI, generated docs, tickets, milestones, prompts, raw data, fixtures, CX-T001 audit files, MB-T001, ADR-T003, or M1 files changed.
- CX-T001 does not start implementation or assert proof/validation/legal/trading/data-safety claims.

Optional checks:

- Docs build checks should be skipped unless docs navigation, mkdocs config, generated docs tooling, package files, or generated reference files are changed.
- Do not install dependencies.

## Human Gate Triggers

Human review is required before:

- overwriting, moving, renaming, or materially editing existing ResearchCore Engine docs;
- changing root README, docs index, docs status, docs architecture, or docs navigation outside NullForge source docs;
- changing repo, package, CLI, app, product, or public identity;
- adding dependencies, code, scripts, parsers, sidecar binaries, Tauri scaffolds, packaging configs, tests, schemas, generated docs tooling, or CI behavior;
- importing raw/full `ES.zip`, raw/private/local data, generated data, or ES-derived fixtures;
- creating `tickets/nullforge/`, `milestones/nullforge/`, `prompts/nullforge/`, `docs/nullforge/qa/HUMAN_GATES.md`, MB-T001, ADR-T003, M1, or downstream artifacts;
- enabling or claiming cloud storage, cloud sync, account/auth, billing, telemetry/analytics, mobile, marketplace, broker/live trading, live execution, network upload, updater, signing, AI/model calls, public release, financial advice, legal/trademark clearance, or data-licensing safety;
- treating old chats, prompt files, or incoming package files as active source truth.

Planner-detected human gates: none.

## Source-Of-Truth Risks

- Role-loop docs could be read as completed governance before audit. Mitigate with CX-T001 status and independent audit requirement.
- Role-loop docs could authorize broad future implementation. Mitigate with explicit role separation, acceptance criteria, forbidden actions, human gates, and stop conditions.
- Human gate language could become disconnected from ADR-T002 local-first/no-cloud scope. Mitigate by repeating ADR-T002 boundaries.
- Prompt archive language could accidentally promote prompts. Mitigate by preserving archive policy and saying prompts are not active truth unless scoped and audited.
- Current dirty tree could mix ADR-T002 and CX-T001 work. Mitigate by gating implementation until ADR-T002 branch closeout or explicit human approval.

## Done Definition

CX-T001 implementation is ready for auditor when:

- `docs/nullforge/codex/CODEX_ROLE_LOOP.md` exists.
- Current status and source index reflect CX-T001 without broken links.
- Required reports exist.
- Required checks are recorded in `reports/nullforge/CX-T001/TEST_RESULTS.md`.
- Human gate status is explicitly reported.
- Changed files are scoped to CX-T001 plans, allowed NullForge docs, and reports.
- `reports/nullforge/CX-T001/AUDITOR_PROMPT.md` is ready for an independent auditor.

CX-T001 itself is not complete until an independent auditor returns PASS, HOLD, or REJECT and a later closeout records the result.

## Planner Verdict

Planner artifacts are ready.

Implementor handoff is blocked until ADR-T002 branch closeout is complete or the human explicitly approves continuing on the current dirty branch.
