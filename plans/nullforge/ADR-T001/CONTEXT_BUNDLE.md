# ADR-T001 Context Bundle

Pack name: NullForge M0 ADR-T001 context bundle
Ticket: ADR-T001 - Name/platform/stack/engine ADR
Milestone: M0 - Repo Source Import + Canonical Baseline
Created by: Context Curator pass only

## Curator Boundary

This bundle is context only. It does not plan implementation, create the ADR, update the decision ledger, write reports, edit ResearchCore Engine docs, modify code, install dependencies, or run ADR-T002 or downstream work.

## Repo State

- Repo root: `<repo-root>`
- Starting branch before this pass: `main`
- Starting status: clean, `## main...origin/main`
- Current branch created for this pass: `docs/ADR-T001-nullforge-name-platform-stack-engine`
- PF-T000 audit decision: PASS.
- PF-T001 audit decision: PASS.
- PF-T002 audit decision: PASS.
- PF-T000, PF-T001, and PF-T002 have been committed, pushed, merged to `main`, and pushed.
- Current scoped output path: `plans/nullforge/ADR-T001/`

Latest relevant commit before this curator pass:

```text
76848a6 Merge branch 'docs/PF-T002-nullforge-status-source-index'
```

## Ticket Summary

ADR-T001 is a docs/source-of-truth ticket. Its purpose is to record major working decisions:

- `NullForge` as working product name only;
- `research-core` remains the existing repo name;
- `ResearchCore Engine` remains the internal engine label;
- Windows 11 x64 is the first platform;
- Tauri + React/TypeScript is the default desktop stack, pending bridge/packaging spikes;
- the existing Python ResearchCore Engine is controlled through an intended sidecar / scoped command bridge boundary.

The active incoming ticket source names these outputs:

- `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`
- `docs/nullforge/DECISION_LEDGER.md update or creation`
- `reports/nullforge/ADR-T001/IMPLEMENTATION_REPORT.md`
- `audits/nullforge/ADR-T001/AUDIT_REPORT.md`

Required role-loop artifacts from the incoming ticket:

- `plans/nullforge/ADR-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/ADR-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/ADR-T001/PLAN.md`
- `plans/nullforge/ADR-T001/ACCEPTANCE.md`
- `plans/nullforge/ADR-T001/IMPLEMENTOR_PROMPT.md`
- `reports/nullforge/ADR-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/ADR-T001/CHANGED_FILES.md`
- `reports/nullforge/ADR-T001/TEST_RESULTS.md`
- `reports/nullforge/ADR-T001/AUDITOR_PROMPT.md`
- `audits/nullforge/ADR-T001/AUDIT_REPORT.md`
- `audits/nullforge/ADR-T001/FINDINGS.md`
- `audits/nullforge/ADR-T001/REPAIR_PROMPT.md`

## Active Source Docs

Repo-local ADR-T001 ticket and M0 milestone paths were checked and absent:

- `tickets/nullforge/ADR-T001-name-platform-stack-engine-adr.md`
- `milestones/nullforge/M0-repo-source-import/MILESTONE_BRIEF.md`
- `milestones/nullforge/M0-repo-source-import/TICKET_QUEUE.md`
- `milestones/nullforge/M0-repo-source-import/HUMAN_GATE_TRIGGERS.md`

Use the incoming package source until a scoped ticket imports these files into the repo:

- `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\ADR-T001-name-platform-stack-engine-adr.md`
- `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\MILESTONE_BRIEF.md`
- `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\TICKET_QUEUE.md`
- `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\HUMAN_GATE_TRIGGERS.md`

Repo-local dependency and baseline docs inspected:

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
- Imported Volume 00, 01, 02, 03, 04, 05, 06, and 07 files under `docs/nullforge/blueprint/volumes/`

Existing ResearchCore docs inspected for separation/context:

- `README.md`
- `docs/STATUS.md`
- `docs/index.md`
- `docs/ARCHITECTURE.md`

## Dependency Status

ADR-T001 depends on PF-T002.

Dependency result:

- PF-T000 audit decision: PASS.
- PF-T001 audit decision: PASS.
- PF-T002 audit decision: PASS.
- PF-T002 closeout merged the current status/source index baseline to `main`.
- `docs/nullforge/DECISION_LEDGER.md` marks ADR-T001 as pending and scoped to the name/platform/stack/engine boundary.
- M0 remains serial:

```text
PF-T000 -> PF-T001 -> PF-T002 -> ADR-T001 -> ADR-T002 -> CX-T001 -> MB-T001
```

ADR-T002 must not start until ADR-T001 has implementation outputs and an independent audit disposition.

## Target Path Status

ADR-T001 candidate output paths were checked:

| Path | Exists now? | Notes |
|---|---:|---|
| `docs/nullforge/adr/` | No | Expected ADR-T001 implementation target folder. |
| `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` | No | Expected ADR-T001 ADR output. |
| `docs/adr/` | No | Generic ADR folder absent; use NullForge-specific path unless planner decides otherwise from active ticket. |
| `docs/architecture/` | No | Generic architecture folder absent. |
| `docs/ARCHITECTURE.md` | Yes | Existing ResearchCore Engine architecture truth; do not modify in ADR-T001 without human gate. |
| `plans/nullforge/ADR-T001/` | No before this curator pass | Created only to hold this context bundle. |
| `reports/nullforge/ADR-T001/` | No | Future implementor output. |
| `audits/nullforge/ADR-T001/` | No | Future auditor output. |

Existing ResearchCore front-door/status docs:

- `README.md` exists.
- `docs/index.md` exists.
- `docs/STATUS.md` exists.
- `docs/ARCHITECTURE.md` exists.

Do not overwrite or materially edit these existing ResearchCore docs in ADR-T001 without an explicit human gate.

## Current ResearchCore Truth To Preserve

`README.md` frames ResearchCore as a validation-first research lab and evidence pipeline for candidate logic, canonical data, artifacts, validation, analysis, comparison, extraction, harness, and optimization.

`docs/STATUS.md` says the repo contains a substantial implemented Python CLI and artifact pipeline under `src/research_core`, broad tests, schemas, reference docs, and CI/docs workflows. It also says ResearchCore is not a hosted service, web application, or networked control plane.

`docs/index.md` is the Research Core docs hub for quickstart, tutorials, generated references, how-to pages, troubleshooting, and contributing setup.

`docs/ARCHITECTURE.md` says Research Core is a local deterministic artifact pipeline implemented in Python under `src/research_core` and exposed through a Typer CLI in `src/research_core/cli.py`. It describes local filesystem boundaries, implemented modules, partial docs/reference coverage, and future extension points.

ADR-T001 should keep NullForge product/platform/stack decisions separate from these ResearchCore Engine docs and should not imply the engine implementation is renamed, replaced, or rewritten.

## Current NullForge Baseline To Preserve

`docs/nullforge/README.md` states:

- NullForge docs under `docs/nullforge/` are planning/workflow source for audited NullForge tickets.
- These docs are not ResearchCore Engine implementation truth.
- Existing ResearchCore Engine docs, code, package metadata, schemas, tests, and generated references remain current engine truth.
- No NullForge implementation code has started.
- Technical, product, user, market, trading, validation, and release claims remain unproven until later audited evidence promotes them.

`docs/nullforge/CURRENT_STATUS.md` states:

- date: `2026-06-15`;
- active phase: `REPO_SOURCE_IMPORT_BASELINE`;
- PF-T000/PF-T001/PF-T002 are PASS/complete by audit state;
- next action is `ADR-T001` after PF-T002 audit disposition;
- no NullForge implementation code has started;
- public release, repo/package/CLI/app/product identity changes, desktop bridge, sidecar, broker-live integration, cloud/auth/billing/mobile scope, schemas, datasets, tests, implementation code, and fixtures are out of current scope.

`docs/nullforge/SOURCE_INDEX.md` states:

- incoming package M0/PF-T002 sources are external plain-text active inputs;
- `docs/nullforge/adr/ADR-T001.md` and `docs/nullforge/adr/ADR-T002.md` are pending/not present;
- `ADR-T001` should decide name/platform/stack/engine boundary after PF-T002 audit disposition.

`docs/nullforge/DECISION_LEDGER.md` records:

- `NF-D0001`: accepted separated NullForge repo-local planning docs under `docs/nullforge/`;
- `NF-D0002`: accepted selected Volume 00-07 imports under `docs/nullforge/blueprint/volumes/`;
- `NF-D0003`: PF-T002 source/status baseline in progress until audit;
- `NF-D0004`: pending ADR to decide NullForge name, platform, stack, and ResearchCore Engine boundary, downstream owner `ADR-T001`;
- `NF-D0005`: pending ADR for local-first/no-cloud MVP, downstream owner `ADR-T002`.

`docs/nullforge/ARCHIVE_POLICY.md` states archive is memory without authority, quarantine is unresolved/conflicting/risky material without governance power, prompts/prior chat are not active truth unless promoted, and raw/full ES.zip/private/local/ES-derived data remains gated.

## Imported Volume Status

PF-T001 imported these volume docs as repo-managed NullForge planning/workflow source after audit. They are not ResearchCore Engine implementation truth.

| Volume | Path | Relevance for ADR-T001 |
|---|---|---|
| 00 | `docs/nullforge/blueprint/volumes/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md` | Main source for working name, existing repo identity, engine label, first platform, stack direction, bridge strategy, claim/reversal conditions. |
| 01 | `docs/nullforge/blueprint/volumes/NullForge_Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine_System_v0_4.md` | Source hierarchy, ADR/decision ledger policy, ResearchCore repo boundary, required ADRs before implementation. |
| 02 | `docs/nullforge/blueprint/volumes/NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md` | Role loop, human gates, no direct implementation, dependencies/sidecar/Tauri permission gates. |
| 03 | `docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md` | Primary source for Windows 11 x64 first, Tauri + React + TypeScript, ResearchCore Engine boundary, sidecar/command bridge options, bridge reversal/gates. |
| 04 | `docs/nullforge/blueprint/volumes/NullForge_Volume_04_Dataset_Studio_ES_Intake_Fixture_Policy_DatasetCapabilityMap_Timeframe_Chart_Rules_v0_4.md` | Downstream data gates: no full ES.zip, no cloud upload, no broker/live feed, no unproven benchmark claims. |
| 05 | `docs/nullforge/blueprint/volumes/NullForge_Volume_05_Logic_Factory_LogicCard_Lifecycle_Compiler_Contract_Generator_Null_Ablation_TestPlan_Bridge_v0_4.md` | Downstream validation boundary: compile alone is not evidence, no broker/live trading, no financial advice. |
| 06 | `docs/nullforge/blueprint/volumes/NullForge_Volume_06_Visual_Replay_Evidence_Cards_Audit_Decision_UX_Result_Interpretation_Boundaries_v0_4.md` | Result interpretation gates: no financial advice, no live-trading readiness, one replay is not validation. |
| 07 | `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` | Roadmap, M0 ticket order, ADR-T001/ADR-T002 placement, M1 bridge proof context. |

## Relevant Volume Context

### Volume 00

Volume 00 states:

- Project: `NullForge`.
- Existing repo / engine: `research-core`.
- Internal engine label: `ResearchCore Engine`.
- `NullForge` is the working user-facing product name for the desktop app.
- The product name is promoted for planning, but not for public release.
- `research-core` remains the existing repo and engine identity.
- Do not rename the existing GitHub repo yet.
- Do not publish, package publicly, buy domains, create company identity, or distribute under NullForge until a name availability/conflict check is completed.
- NullForge is a local-first desktop research workbench and governed shell around the existing ResearchCore Engine.
- The MVP proof loop starts on a Windows 11 x64 desktop app and includes one ResearchCore Engine smoke command through the desktop bridge.
- Technical claims `NF-C005` and `NF-C006` are untested: Tauri + React/TypeScript shell feasibility and ResearchCore Engine Python sidecar / command bridge reliability.
- Reversal conditions include: Tauri cannot support the workflow, the Tauri + Python sidecar strategy is repeatedly blocked, Python sidecar packaging blocks MVP beyond reasonable repair, or Windows 11 x64 cannot support the first user.

Decision/reversal rows in Volume 00 relevant to ADR-T001:

| Decision area | Proposed stance | Reversal condition |
|---|---|---|
| Product name | NullForge as working name | Reverse before public release if name conflict/legal/brand risk is meaningful. |
| Existing repo identity | Keep `research-core` as repo/engine | Reverse only if app/engine split becomes impossible to communicate or maintain. |
| First platform | Windows 11 x64 | Add/switch platform only after Windows MVP proof or if Windows blocks first user. |
| Desktop stack | Tauri + React/TypeScript | Reverse if Tauri cannot support file access, sidecar bridge, packaging, or dev velocity. |
| Engine strategy | ResearchCore Engine as Python sidecar / command bridge | Reverse if sidecar bridge repeatedly fails or is worse than an engine API alternative. |

### Volume 01

Volume 01 states:

- `research-core` is the current engine repo, not a blank slate.
- Existing Python package/CLI and tracked docs are engine implementation truth.
- ResearchCore Engine remains the internal artifact/validation engine.
- `ResearchCore Engine` is the internal Python engine label.
- `research-core` is the existing repo name until separate ADR approves rename.
- ADRs and decision ledgers are high-authority repo docs and must include reversal conditions.
- Required ADRs before implementation include working name, Windows 11 x64 first, Tauri + React + TypeScript, ResearchCore Engine sidecar/bridge boundary, local-first/no-cloud, and full ES.zip outside repo.

Volume 01 contains older generic ADR path examples under `docs/adr/`, but the active ticket and PF-T000 plan use the scoped NullForge path `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`.

### Volume 02

Volume 02 states:

- Direct implementation is forbidden.
- No implementation starts from a broad app-building prompt.
- Human gates include dependency approval, public release gates, Tauri permission broadening, Python sidecar execution model changes, public release/distribution, and any gate-triggering merge/release work.
- Future implementation must allowlist bridge commands and avoid silent architecture reversal.

### Volume 03

Volume 03 is the primary technical context for ADR-T001. It states:

- NullForge should become a Windows 11 x64 desktop app.
- The desktop shell direction is Tauri + React + TypeScript.
- The existing `research-core` repo / engine is treated as a real prior asset.
- The ResearchCore Engine owns existing Python CLI, canonicalization, validation, artifact production, schemas/report patterns, and engine truth.
- Do not rewrite the ResearchCore Engine just to make the UI easier.
- React/TypeScript owns screens, interactions, status display, and user confirmation flows.
- Tauri/Rust owns desktop permissions, filesystem boundary, process spawning, and command adapter.
- The bridge contract is a structured command protocol, not a raw shell interface.
- The desktop app invokes only allowlisted bridge commands.
- Recommended MVP bridge starts with a strict command bridge against a local Python environment, then proves a packaged sidecar path in a dedicated packaging spike.
- The bridge must not mutate the repo unless a scoped dev ticket says so.
- Tauri permissions must be treated as architecture surface, expanded only through ADR/ticket/audit.
- Full ES.zip remains outside repo.
- Human gates include adding Tauri plugins, changing sidecar packaging method, changing Python version, changing ResearchCore Engine command behavior, and installer signing/public release.

Volume 03 bridge options:

| Option | Summary | Risk/context |
|---|---|---|
| A | Tauri external binary sidecar wrapping ResearchCore Engine | Useful target, but Python dependency packaging may be difficult. |
| B | Development bridge to local Python environment | Fastest early proof, but can mask packaging failures. |
| C | Embedded Python distribution | More controlled, but more custom packaging complexity. |
| Local ResearchCore service | Clear API boundary, but too much for MVP bridge proof. |

### Volumes 04-06

Volumes 04-06 are downstream context only for ADR-T001. They reinforce gates:

- no cloud upload/sync;
- no broker/live feed or broker/live trading behavior;
- no full ES.zip in repo;
- no benchmark/validation claims without manifest/provenance/evidence;
- compile alone is not validation;
- one replay example is not validation;
- no financial advice, guaranteed edge, or live-trading readiness wording.

### Volume 07

Volume 07 states:

- Internal engine label: ResearchCore Engine.
- Platform: Windows 11 x64 first.
- Desktop stack: Tauri + React + TypeScript.
- Engine strategy: Python ResearchCore Engine sidecar / scoped command bridge.
- M0 blocks all implementation.
- M1 later proves a Windows/Tauri shell can call a safe ResearchCore Engine command and show read-only artifact metadata.
- M0 non-goals include no Tauri app, no public release, and no repo rename.
- ADR-T001 records NullForge, Windows 11 x64, Tauri, and ResearchCore Engine boundary.

Volume 07's ticket table shows ADR-T001 depends on PF-T001, but the active incoming M0 ticket queue and ADR-T001 ticket say ADR-T001 depends on PF-T002. PF-T002 is now PASS and merged.

## PF-T002 Acceptance Signals For ADR-T001

PF-T002 audit PASS confirms:

- PF-T002 stayed docs-only.
- `SOURCE_INDEX.md` links only to repo-local files that exist.
- `DECISION_LEDGER.md` records pending ADR-T001/ADR-T002 without claiming ADR completion.
- No M0 milestone docs, ticket files, prompt files, raw/full ES.zip contents, private/local data, ES-derived fixtures, implementation code, tests, schemas, dependencies, package files, CI files, generated reference docs, or downstream artifacts were created.
- After PF-T002 closeout, ADR-T001 is ready to start.

## ADR-T001 Acceptance Signals From Active Ticket

The incoming ADR-T001 ticket says acceptance requires:

- ADR records `NullForge` as working product name only.
- ADR records repo remains `research-core` and engine remains `ResearchCore Engine`.
- ADR records Windows 11 x64 as first platform.
- ADR records Tauri + React/TypeScript as default stack pending bridge/packaging spikes.
- ADR records Python sidecar/command bridge as intended boundary.
- Reversal conditions and human gates are explicit.

Required checks:

- ADR has date, context, options considered, chosen option, risks, reversal conditions.
- Decision ledger references ADR-T001.

## Human Gate Triggers

Human review is required before:

- overwriting existing ResearchCore Engine docs;
- changing root README, docs index, docs status, docs architecture, or docs navigation;
- renaming repo, package, CLI, app, public project, or product identity;
- adding dependencies, code, scripts, Tauri scaffolds, sidecar binaries, parsers, packaging configs, tests, schemas, CI behavior, or release/build config;
- committing raw/full ES.zip, raw/private/local data, or ES-derived fixtures;
- treating unreviewed prompts/chat/archive/quarantine material as active source truth;
- broadening into public release, legal/trademark claims, AI strategy activation, broker/live trading, financial advice, auth, billing, cloud sync, marketplace, or mobile scope;
- performing trademark/legal clearance or claiming NullForge is legally/publicly safe.

Human gates triggered in this curator pass: NONE.

## Context Risks

- ADR-T001 is allowed to record working name/platform/stack/engine decisions, but must not actually rename repo/package/CLI/app/product identity.
- The ADR should avoid wording that implies public naming/legal clearance or public distribution safety.
- Tauri + React/TypeScript and sidecar/command bridge are planning decisions with explicit spike/reversal conditions; the imported volumes still mark bridge feasibility and packaging as untested.
- The existing ResearchCore Engine docs already define engine architecture and implementation truth; ADR-T001 must not overwrite them or imply they are superseded.
- The active incoming ticket requires a decision-ledger reference/update, but the decision ledger already exists from PF-T002. The planner should scope whether ADR-T001 implementor updates only `docs/nullforge/DECISION_LEDGER.md` or also updates current status/source index.
- Volume 07's older ticket table lists ADR-T001 dependency as PF-T001, while the active incoming ticket queue and ADR-T001 ticket list PF-T002. Current execution should follow the active queue/ticket because PF-T002 is PASS and merged.
- Volume 01 contains older generic ADR path examples under `docs/adr/`; active M0/PF-T000/ADR-T001 sources point to `docs/nullforge/adr/`.

## Open Questions For Planner

- Should ADR-T001 update `docs/nullforge/CURRENT_STATUS.md` from PF-T002 to ADR-T001 status, or should that wait for a later status-maintenance ticket? The active ADR-T001 ticket does not list `CURRENT_STATUS.md` as an output.
- Should ADR-T001 update `docs/nullforge/SOURCE_INDEX.md` to link the new ADR after creation, or should the source index remain unchanged until a later source-index maintenance pass? The active ADR-T001 ticket does not list `SOURCE_INDEX.md` as an output.
- How should the ADR phrase the Tauri + React/TypeScript decision: accepted default stack, or default stack pending bridge/packaging spikes with reversal conditions? The active ticket acceptance includes "default stack pending bridge/packaging spikes."
- Should the decision ledger entry `NF-D0004` be updated in place from `Pending ADR` to accepted/reference status, or should ADR-T001 append a new ledger entry while preserving history?
- Should the ADR consolidate all name/platform/stack/engine boundary decisions into one ADR file per active ticket, despite Volume 01/03 examples suggesting separate ADRs for name, platform, stack, and sidecar?

## Ready For Planner

YES, subject to the planner resolving the ADR-T001 output-scope questions above and keeping ADR-T001 docs-only.
