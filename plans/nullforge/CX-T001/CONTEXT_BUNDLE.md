# CX-T001 Context Bundle

Ticket: `CX-T001` - NullForge Codex role-loop docs
Role: Planner context bundle
Date: `2026-06-16`

## Purpose

Provide the smallest sufficient active context for planning CX-T001. CX-T001 should adapt the NullForge context curator -> planner -> implementor -> auditor workflow into repo-local docs after ADR-T002 audit `PASS`.

This bundle does not create implementation docs, reports, audits, code, schemas, fixtures, tickets, milestones, prompt archives, app scaffolds, or downstream work.

## Prerequisite State

- ADR-T002 audit report contains `Decision: PASS`.
- ADR-T002 findings report says no findings.
- `docs/nullforge/CURRENT_STATUS.md` says CX-T001 is the next scoped ticket after ADR-T002 branch closeout.
- No NullForge implementation code has started.
- Existing ResearchCore Engine docs, code, package metadata, schemas, tests, and generated references remain separate engine truth.
- Current working tree is not clean because ADR-T002 closeout artifacts are still pending in this branch. CX-T001 planner artifacts may be created now, but CX-T001 implementation should wait until ADR-T002 branch closeout or explicit human approval to continue on the dirty branch.

## Mission Slice For CX-T001

CX-T001 should make the NullForge role loop explicit in repo-local documentation so future tickets do not begin from broad "build the app" prompts.

The role-loop doc should describe:

- context curator, planner, implementor, auditor, and repair responsibilities;
- per-ticket artifact paths under `plans/`, `reports/`, and `audits/`;
- PASS / HOLD / REJECT closeout rules;
- human gate and stop-condition handling;
- source-of-truth boundaries for active docs, design memory, archive, quarantine, and prompts;
- NullForge-specific forbidden actions for code, data, cloud, broker/live, AI, release, and identity changes;
- serial ticket execution and audit requirements before MB-T001 or M1 work.

CX-T001 should remain docs-only. It should not start M1, create app files, create Tauri scaffolds, write ResearchCore Engine code, import data, or create downstream milestone/ticket artifacts.

## Active Source Context

### Current status

`docs/nullforge/CURRENT_STATUS.md` states:

- active phase remains `REPO_SOURCE_IMPORT_BASELINE`;
- active ticket is ADR-T002 closeout;
- next action is `CX-T001` planner after ADR-T002 branch closeout;
- `No NullForge implementation code has started.`;
- ADR-T002 has audit decision `PASS`;
- CX-T001 is pending next scoped ticket;
- MB-T001 remains pending downstream;
- implementation code, dependencies, schemas, tests, generated references, raw data, fixtures, cloud/auth/billing/mobile, telemetry, broker/live, public release, legal/trademark claims, and app scaffolding remain gated or out of scope.

### Source index

`docs/nullforge/SOURCE_INDEX.md` identifies:

- active NullForge planning docs;
- ADR-T001 and ADR-T002 as active decision records after audit `PASS`;
- ADR-T002 plan, report, and audit artifacts;
- CX-T001 as the pending next scoped ticket after ADR-T002 branch closeout;
- MB-T001 as pending downstream;
- incoming package sources as external plain-text inputs, not repo-local canonical docs;
- prompt files as workflow instructions, not active truth unless promoted by a later audited doc.

### Decision ledger

`docs/nullforge/DECISION_LEDGER.md` contains:

- `NF-D0004`: accepted by ADR-T001 for working name, first platform, desktop stack direction, and ResearchCore Engine boundary.
- `NF-D0005`: accepted by ADR-T002 for the local-first/no-cloud MVP boundary.
- `NF-D0006`: pending source import for incoming M0 milestone docs and ticket queue.
- accepted entries do not authorize implementation code unless later scoped ticket work does that.

CX-T001 does not need a new decision ledger row unless the implementor discovers a source-of-truth decision not already covered by Volume 2, ADR-T001, or ADR-T002. Planner-detected decision ledger update need: none.

### Archive policy

`docs/nullforge/ARCHIVE_POLICY.md` says:

- active docs are repo-local files created or imported by scoped role-loop tickets and accepted by audit disposition;
- design memory may inform later work but does not authorize implementation or prove claims;
- archive material has no governance power;
- quarantine is for unresolved, risky, private, local-only, or unreviewed material;
- prompt files are workflow instructions, not canonical product or architecture source by default;
- promotion into active truth requires a bounded ticket, changed-file inventory, recorded checks, human gate handling, and independent audit disposition.

### ADR-T001

`docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` establishes:

- `NullForge` is a working product name only;
- repo remains `research-core`;
- internal engine label remains `ResearchCore Engine`;
- first platform is Windows 11 x64;
- Tauri + React/TypeScript is the accepted default desktop stack direction pending bridge and packaging spikes;
- intended future engine boundary is a Python ResearchCore Engine sidecar / scoped command bridge;
- ADR-T001 does not implement code or prove Tauri, packaging, bridge, product, user, market, legal, trading, financial-advice, or public-distribution claims.

### ADR-T002

`docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md` establishes:

- NullForge MVP is local-first by default;
- one selected local workspace is the MVP runtime boundary as a planning assumption;
- local ResearchCore Engine execution is future scoped sidecar / command bridge work, not implemented or proven;
- tiny/small fixtures require later approved fixture policy;
- full ES.zip, raw/private data, generated datasets, and ES-derived fixtures remain gated;
- cloud storage, cloud sync, hosted backend, account/auth, billing, telemetry/analytics, mobile, marketplace, broker-live integration, live execution, public distribution, updater/signing/release channel, and financial advice scope are outside MVP;
- any future network, telemetry, cloud, auth, billing, broker/live, updater, signing, or public release work requires scoped ADR or ticket and human review.

### ADR-T002 audit

`audits/nullforge/ADR-T002/AUDIT_REPORT.md` records:

- `Decision: PASS`;
- ADR-T002 stayed docs-only;
- no CX-T001, MB-T001, ADR-T003, M1, implementation, data, cloud/auth/billing, telemetry, broker/live, or downstream artifact was created;
- after ADR-T002 closeout, `CX-T001` is ready to start.

## Imported Volume Context

### Volume 02

`docs/nullforge/blueprint/volumes/NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md` is the primary workflow source for CX-T001.

Relevant decisions and constraints:

- direct-to-Codex implementation is forbidden;
- every implementation ticket must move through context, plan, implementation report, audit, and gate handling;
- no ticket starts without acceptance criteria;
- no role grades its own work;
- no generated output becomes truth without audit;
- every ticket needs scoped artifacts under `plans/`, `reports/`, and `audits/`;
- planner output requires `PLAN.md`, `ACCEPTANCE.md`, and `IMPLEMENTOR_PROMPT.md`;
- implementor output requires `IMPLEMENTATION_REPORT.md`, `CHANGED_FILES.md`, `TEST_RESULTS.md`, and `AUDITOR_PROMPT.md`;
- auditor output requires `AUDIT_REPORT.md`, `FINDINGS.md`, and `REPAIR_PROMPT.md`;
- PASS, HOLD, and REJECT rules are explicit;
- human gates apply to dependencies, Tauri permissions, file access, data, security/privacy, packaging, AI, broker/live, and release changes;
- stop conditions include dirty repo before ticket start, missing dependencies, source conflicts, unclear tests, scope expansion, dependency needs, raw/private data changes, AI strategy generation, broker/live behavior, public release, and repeated audit failure.

### Volume 07

`docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` places CX-T001 in M0.

Relevant roadmap context:

- M0 order is PF-T000 -> PF-T001 -> PF-T002 -> ADR-T001 -> ADR-T002 -> CX-T001 -> MB-T001.
- CX-T001 title is `NullForge Codex role-loop docs`.
- CX-T001 purpose is to adapt the context curator -> planner -> implementor -> auditor workflow to the repo.
- M0 explicit non-goals include no Tauri app, no engine changes, no dataset parser, no fixture creation, no desktop bridge implementation, no public release, and no repo rename.
- M0 acceptance expects Codex role-loop docs to exist or be mapped to existing project docs.
- Before implementation tickets, NullForge must create role-loop docs, discover actual repo test/run commands later, confirm active ticket queue and human gates, and start M1 only after M0 PASS or human-approved deferral.

## Expected CX-T001 Implementor Scope

The later CX-T001 implementor should create the repo-local Codex workflow doc and reports only.

Expected allowed implementor files:

```text
docs/nullforge/codex/CODEX_ROLE_LOOP.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
reports/nullforge/CX-T001/IMPLEMENTATION_REPORT.md
reports/nullforge/CX-T001/CHANGED_FILES.md
reports/nullforge/CX-T001/TEST_RESULTS.md
reports/nullforge/CX-T001/AUDITOR_PROMPT.md
```

Expected read-only planner files:

```text
plans/nullforge/CX-T001/CONTEXT_BUNDLE.md
plans/nullforge/CX-T001/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/CX-T001/PLAN.md
plans/nullforge/CX-T001/ACCEPTANCE.md
plans/nullforge/CX-T001/IMPLEMENTOR_PROMPT.md
```

The implementor should not create `docs/nullforge/qa/HUMAN_GATES.md`, `tickets/nullforge/`, `milestones/nullforge/`, `prompts/nullforge/`, CX-T001 audit files, MB-T001 files, ADR-T003 files, M1 files, code, tests, schemas, dependencies, app scaffolds, or data fixtures.

## Required Checks For Implementor

The later implementor should run and record:

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

- Changed files are limited to CX-T001 plans, allowed NullForge docs, and CX-T001 reports.
- No ResearchCore Engine docs/code are changed.
- No implementation code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, tickets, milestones, prompts, audits, MB-T001, ADR-T003, or M1 artifacts are created.
- Source index links only to repo-local files that exist.

## Human Gate Triggers

Human review is required before:

- changing ResearchCore Engine docs, code, package metadata, schemas, tests, CLI names, package names, or generated references;
- changing repo, package, CLI, app, product, or public identity;
- creating code, dependencies, schemas, tests, generated docs tooling, CI, app files, bridge implementation, sidecar implementation, Tauri scaffolds, or release config;
- importing raw/full ES.zip, private/local data, generated data, ES-derived fixtures, or license/privacy-sensitive datasets;
- enabling cloud storage, cloud sync, hosted backend, network upload, telemetry/analytics, account/auth, billing, mobile, marketplace, broker/live trading, live execution, AI/model calls, updater, signing, public release, legal/trademark claims, or financial advice claims;
- creating or promoting prompt archives, incoming package prompt files, old chats, ticket files, milestone files, MB-T001, ADR-T003, M1, or downstream work;
- treating CX-T001 docs as proof that implementation governance has been audited before the independent audit returns PASS.

Planner-detected human gates: none.

## Excluded Context

- Full repo source tree: not needed for a docs-only workflow plan.
- Existing ResearchCore Engine docs beyond active NullForge status/source docs: read-only and authoritative for engine behavior.
- Volume 00/01/03/04/05/06 full files: useful for later tickets, but CX-T001 is governed mainly by active status/source docs, ADR-T001, ADR-T002, Volume 02, and Volume 07.
- Incoming package ticket, milestone, and prompt files: not repo-local active truth.
- Old chats and prompt files: not active truth unless promoted by a later scoped and audited ticket.
- Raw/full ES.zip, private/local data, generated datasets, ES-derived fixtures: gated and out of scope.

## Open Questions For Planner

- Should CX-T001 create one workflow doc or multiple docs?
- Should CX-T001 update the decision ledger?
- Should CX-T001 update current status and source index during implementation?
- Should CX-T001 be considered ready for implementor while ADR-T002 artifacts remain uncommitted?

Planner resolution should answer these in `PLAN.md`.

## Ready For Planner

YES.
