# Implementor Prompt: CX-T001 - NullForge Codex role-loop docs

You are the Implementor for NullForge M0 ticket `CX-T001`.

You implement only the bounded docs/workflow baseline for CX-T001. Do not write implementation code. Do not modify existing ResearchCore Engine docs. Do not create MB-T001, ADR-T003, M1 work, or any downstream ticket.

## Preflight Gate

Before editing, run:

```powershell
git status --short --branch
```

Stop and report a blocker unless one of these is true:

- ADR-T002 branch closeout has been committed and the only pending changes are `plans/nullforge/CX-T001/`; or
- the human explicitly approved continuing CX-T001 implementation on the current dirty branch.

Reason: ADR-T002 audit `PASS` exists, but CX-T001 should not mix implementation with unclosed ADR-T002 work unless the human chooses that workflow.

## Read First

Read these repo-local files:

```text
plans/nullforge/CX-T001/CONTEXT_BUNDLE.md
plans/nullforge/CX-T001/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/CX-T001/PLAN.md
plans/nullforge/CX-T001/ACCEPTANCE.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
docs/nullforge/DECISION_LEDGER.md
docs/nullforge/ARCHIVE_POLICY.md
docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md
docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
audits/nullforge/ADR-T002/AUDIT_REPORT.md
docs/nullforge/blueprint/volumes/NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md
```

Do not create ticket, milestone, prompt, audit, app, code, schema, test, fixture, dependency, package, CI, generated-doc, MB-T001, ADR-T003, or M1 files.

## Planner Decisions You Must Follow

- Create one workflow doc:

```text
docs/nullforge/codex/CODEX_ROLE_LOOP.md
```

- Update `docs/nullforge/CURRENT_STATUS.md`.
- Update `docs/nullforge/SOURCE_INDEX.md`.
- Do not update `docs/nullforge/DECISION_LEDGER.md` unless a human-approved decision gate is triggered.
- Keep MB-T001, ADR-T003, M1, and downstream work pending only.
- Do not create `docs/nullforge/qa/HUMAN_GATES.md`; human gate rules belong in CODEX_ROLE_LOOP for this ticket.
- Do not implement app behavior, local workspace behavior, cloud absence enforcement, telemetry blocking, bridge code, sidecar code, fixtures, schemas, tests, data import, prompt archives, ticket files, or milestone files.

## Allowed Files And Folders

You may create or modify only:

```text
docs/nullforge/codex/CODEX_ROLE_LOOP.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
reports/nullforge/CX-T001/IMPLEMENTATION_REPORT.md
reports/nullforge/CX-T001/CHANGED_FILES.md
reports/nullforge/CX-T001/TEST_RESULTS.md
reports/nullforge/CX-T001/AUDITOR_PROMPT.md
```

Treat these files as read-only:

```text
plans/nullforge/CX-T001/CONTEXT_BUNDLE.md
plans/nullforge/CX-T001/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/CX-T001/PLAN.md
plans/nullforge/CX-T001/ACCEPTANCE.md
plans/nullforge/CX-T001/IMPLEMENTOR_PROMPT.md
docs/nullforge/DECISION_LEDGER.md
docs/nullforge/ARCHIVE_POLICY.md
docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md
docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
audits/nullforge/ADR-T002/AUDIT_REPORT.md
docs/nullforge/blueprint/volumes/*.md
README.md
docs/STATUS.md
docs/index.md
docs/ARCHITECTURE.md
docs/contributing/docs_style_guide.md
```

## Required CODEX_ROLE_LOOP Content

Create `docs/nullforge/codex/CODEX_ROLE_LOOP.md`.

It must include:

- title identifying NullForge Codex role-loop docs;
- date `2026-06-16`;
- status making clear this is workflow/source documentation and not implementation proof;
- context section citing current status, source index, archive policy, ADR-T001, ADR-T002, ADR-T002 audit `PASS`, Volume 02, and Volume 07;
- exact sentence `No NullForge implementation code has started.`;
- role-loop overview:

```text
Human / ChatGPT Architect -> Context Curator -> Planner -> Implementor / Codex -> Auditor -> Repair if needed -> Human gate -> Next ticket
```

- role responsibilities and forbidden actions for:
  - Human / ChatGPT Architect;
  - Context Curator;
  - Planner;
  - Implementor / Codex;
  - Auditor;
  - Repair Implementor.
- artifact tree and required sections for:
  - `plans/nullforge/[TICKET_ID]/CONTEXT_BUNDLE.md`;
  - `plans/nullforge/[TICKET_ID]/CONTEXT_BUNDLE_MANIFEST.md`;
  - `plans/nullforge/[TICKET_ID]/PLAN.md`;
  - `plans/nullforge/[TICKET_ID]/ACCEPTANCE.md`;
  - `plans/nullforge/[TICKET_ID]/IMPLEMENTOR_PROMPT.md`;
  - `reports/nullforge/[TICKET_ID]/IMPLEMENTATION_REPORT.md`;
  - `reports/nullforge/[TICKET_ID]/CHANGED_FILES.md`;
  - `reports/nullforge/[TICKET_ID]/TEST_RESULTS.md`;
  - `reports/nullforge/[TICKET_ID]/AUDITOR_PROMPT.md`;
  - `audits/nullforge/[TICKET_ID]/AUDIT_REPORT.md`;
  - `audits/nullforge/[TICKET_ID]/FINDINGS.md`;
  - `audits/nullforge/[TICKET_ID]/REPAIR_PROMPT.md`.
- PASS / HOLD / REJECT rules;
- human gate triggers;
- stop conditions;
- docs-only ticket handling rules;
- branch and ticket hygiene rules;
- source-of-truth, design memory, archive, quarantine, and prompt handling rules;
- CX-T001 boundaries and non-decisions;
- next action: `MB-T001` after CX-T001 audit disposition.

It must preserve:

- ADR-T001 working name/platform/stack/engine boundaries;
- ADR-T002 local-first/no-cloud MVP boundaries;
- ResearchCore Engine as separate engine truth;
- prompt files as workflow instructions, not active source truth unless scoped and audited;
- no cloud/auth/billing/mobile/marketplace/telemetry/broker/live/public release scope;
- no raw/full ES.zip, private/local data, generated datasets, or ES-derived fixtures;
- no app code, Tauri scaffold, sidecar, bridge, schemas, tests, dependencies, package changes, CI changes, generated docs, data imports, or fixtures.

It must not claim:

- Tauri feasibility;
- packaging feasibility;
- bridge reliability;
- workspace safety;
- telemetry enforcement;
- cloud-security proof;
- legal/trademark clearance;
- public distribution safety;
- financial advice safety;
- trading validity;
- product validation;
- user validation;
- market validation;
- data licensing safety;
- implementation proof.

## Required Source Maintenance

### `docs/nullforge/CURRENT_STATUS.md`

Update current status to:

- keep active phase `REPO_SOURCE_IMPORT_BASELINE`;
- name active ticket `CX-T001`;
- point next action to `MB-T001` after CX-T001 independent audit disposition;
- keep PF-T000, PF-T001, PF-T002, ADR-T001, and ADR-T002 complete/PASS;
- record CX-T001 as in progress until independent audit disposition;
- keep exact sentence `No NullForge implementation code has started.`;
- state existing ResearchCore Engine implementation remains separate engine truth;
- state CX-T001 is docs/workflow source only and does not implement app code, local workspace behavior, cloud absence enforcement, telemetry blocking, bridge, sidecar, fixtures, schemas, tests, app scaffold, prompt archives, ticket/milestone imports, MB-T001, ADR-T003, M1, or release behavior.

### `docs/nullforge/SOURCE_INDEX.md`

Add the new workflow doc as a repo-local Markdown link after it exists:

```text
docs/nullforge/codex/CODEX_ROLE_LOOP.md
```

Add CX-T001 plan/report links only after files exist:

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

Keep MB-T001 pending. Keep incoming package sources as external plain-text inputs if mentioned.

## Reports

Create:

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
docs/nullforge/qa/HUMAN_GATES.md
docs/nullforge/adr/ADR-T003*
reports/nullforge/MB-T001/
reports/nullforge/ADR-T003/
audits/nullforge/CX-T001/
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
- mark technical, product, user, market, trading, legal, financial-advice, public-release, data-licensing, cloud-security, telemetry-enforcement, or validation claims as proven.

## Implementation Tasks

1. Preflight
   - Run `git status --short --branch`.
   - Confirm ADR-T002 audit PASS exists.
   - Confirm ADR-T002 closeout is complete or human explicitly approved continuing with a dirty branch.
   - Confirm `docs/nullforge/codex/CODEX_ROLE_LOOP.md` does not already exist unless updating an interrupted implementation pass.
   - Check expected report paths do not already exist.
   - Check no MB-T001, ADR-T003, M1, ticket, milestone, prompt, audit, app, data, or implementation paths are created by this ticket.

2. Create workflow doc and source maintenance docs
   - Create `docs/nullforge/codex/CODEX_ROLE_LOOP.md`.
   - Update `docs/nullforge/CURRENT_STATUS.md`.
   - Update `docs/nullforge/SOURCE_INDEX.md`.
   - Do not update `docs/nullforge/DECISION_LEDGER.md` unless a human-approved decision gate is triggered.

3. Create report artifacts
   - Create `reports/nullforge/CX-T001/IMPLEMENTATION_REPORT.md`.
   - Create `reports/nullforge/CX-T001/CHANGED_FILES.md`.
   - Create `reports/nullforge/CX-T001/TEST_RESULTS.md`.
   - Create `reports/nullforge/CX-T001/AUDITOR_PROMPT.md`.

4. Final checks
   - Run and record:

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
- External incoming package paths are not broken repo-local Markdown links.
- Changed files are limited to CX-T001 plans, allowed NullForge docs, and reports.
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

Do not report CX-T001 as complete. CX-T001 is complete only after the independent auditor returns PASS, HOLD, or REJECT.
