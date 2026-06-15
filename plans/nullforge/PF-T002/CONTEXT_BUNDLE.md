# PF-T002 Context Bundle

Pack name: NullForge M0 PF-T002 context bundle
Ticket: PF-T002 - Create NullForge current status and source index
Milestone: M0 - Repo Source Import + Canonical Baseline
Created by: Context Curator pass only

## Curator Boundary

This bundle is context only. It does not plan implementation, create status docs, create source indexes, edit ResearchCore Engine docs, modify code, install dependencies, or run ADR-T001 or downstream work.

## Repo State

- Repo root: `C:\Users\Filip\Desktop\Repos\research-core`
- Starting branch before this pass: `main`
- Starting status: clean, `## main...origin/main`
- Current branch created for this pass: `docs/PF-T002-nullforge-status-source-index`
- PF-T001 has been committed, pushed, merged to `main`, and pushed.
- PF-T001 audit decision: PASS.
- Current scoped output path: `plans/nullforge/PF-T002/`

Latest relevant commits before this curator pass:

```text
b319807 Merge branch 'docs/PF-T001-import-nullforge-volumes'
953a373 docs: import PF-T001 NullForge volumes
400674f Merge branch 'docs/PF-T000-nullforge-import-plan'
```

## Ticket Summary

PF-T002 is a docs/source-of-truth ticket. Its purpose is to create the active NullForge current status, source index, and source-of-truth navigation docs for the imported planning corpus.

The active incoming ticket source names these PF-T002 outputs:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/README.md`
- `docs/nullforge/ARCHIVE_POLICY.md or reference to Volume 1`
- `reports/nullforge/PF-T002/IMPLEMENTATION_REPORT.md`
- `audits/nullforge/PF-T002/AUDIT_REPORT.md`

Required role-loop artifacts from the incoming ticket:

- `plans/nullforge/PF-T002/CONTEXT_BUNDLE.md`
- `plans/nullforge/PF-T002/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/PF-T002/PLAN.md`
- `plans/nullforge/PF-T002/ACCEPTANCE.md`
- `plans/nullforge/PF-T002/IMPLEMENTOR_PROMPT.md`
- `reports/nullforge/PF-T002/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/PF-T002/CHANGED_FILES.md`
- `reports/nullforge/PF-T002/TEST_RESULTS.md`
- `reports/nullforge/PF-T002/AUDITOR_PROMPT.md`
- `audits/nullforge/PF-T002/AUDIT_REPORT.md`
- `audits/nullforge/PF-T002/FINDINGS.md`
- `audits/nullforge/PF-T002/REPAIR_PROMPT.md`

## Active Source Docs

Repo-local PF-T002 ticket and M0 milestone paths were checked and absent:

- `tickets/nullforge/PF-T002-create-nullforge-current-status-and-source-index.md`
- `milestones/nullforge/M0-repo-source-import/MILESTONE_BRIEF.md`
- `milestones/nullforge/M0-repo-source-import/TICKET_QUEUE.md`
- `milestones/nullforge/M0-repo-source-import/HUMAN_GATE_TRIGGERS.md`

Use the incoming package source until a scoped ticket imports these files into the repo:

- `C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\PF-T002-create-nullforge-current-status-and-source-index.md`
- `C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\MILESTONE_BRIEF.md`
- `C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\TICKET_QUEUE.md`
- `C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\HUMAN_GATE_TRIGGERS.md`

Repo-local dependency and imported-source docs inspected:

- `docs/nullforge/import/PF-T000_IMPORT_PLAN.md`
- `docs/nullforge/import/PF-T000_REPO_INVENTORY.md`
- `docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md`
- `audits/nullforge/PF-T001/AUDIT_REPORT.md`
- `reports/nullforge/PF-T001/TEST_RESULTS.md`
- `docs/nullforge/blueprint/volumes/README.md`
- `docs/nullforge/blueprint/volumes/VOLUME_IMPORT_MANIFEST.md`
- Imported Volume 00-07 files under `docs/nullforge/blueprint/volumes/`

Existing ResearchCore docs inspected for separation/context:

- `README.md`
- `docs/STATUS.md`
- `docs/index.md`
- `docs/contributing/docs_style_guide.md`

## Dependency Status

PF-T002 depends on PF-T001.

Dependency result:

- PF-T001 audit decision: PASS.
- PF-T001 closeout merged imported Volume 00-07 docs to `main`.
- Imported volumes are present under `docs/nullforge/blueprint/volumes/`.
- M0 remains serial:

```text
PF-T000 -> PF-T001 -> PF-T002 -> ADR-T001 -> ADR-T002 -> CX-T001 -> MB-T001
```

ADR-T001 must not start until PF-T002 has implementation outputs and an independent audit disposition.

## Target Path Status

PF-T002 candidate output paths were checked:

| Path | Exists now? | Notes |
|---|---:|---|
| `docs/nullforge/README.md` | No | Candidate PF-T002 output. |
| `docs/nullforge/CURRENT_STATUS.md` | No | Candidate PF-T002 output. |
| `docs/nullforge/SOURCE_INDEX.md` | No | Candidate PF-T002 output. |
| `docs/nullforge/DECISION_LEDGER.md` | No | Named by PF-T000 and Volume 7 as PF-T002/current-source baseline. |
| `docs/nullforge/ARCHIVE_POLICY.md` | No | Incoming PF-T002 ticket says create this or reference Volume 1. |
| `plans/nullforge/PF-T002/` | No before this curator pass | Created only to hold this context bundle. |
| `reports/nullforge/PF-T002/` | No | Future implementor output. |
| `audits/nullforge/PF-T002/` | No | Future auditor output. |

Existing nearby NullForge paths:

- `docs/nullforge/import/` from PF-T000.
- `docs/nullforge/blueprint/volumes/` from PF-T001.

Existing ResearchCore front-door/status docs:

- `README.md` exists.
- `docs/index.md` exists.
- `docs/STATUS.md` exists.

Do not overwrite or modify those existing ResearchCore docs in PF-T002 without an explicit human gate.

## Current ResearchCore Truth To Preserve

`README.md` frames ResearchCore as a validation-first research lab and evidence pipeline.

`docs/STATUS.md` says the repo contains a substantial implemented Python CLI and artifact pipeline under `src/research_core`, broad tests, and partial generated reference coverage. It also says ResearchCore is not a hosted service, web app, or networked control plane.

`docs/index.md` is the Research Core docs hub for quickstart, tutorials, generated references, how-to pages, troubleshooting, and contributing setup.

`docs/contributing/docs_style_guide.md` requires docs to use repo-truth sources, avoid guessed flags/paths/schema keys/behaviors, and mark unknown details with TODOs.

PF-T002 should keep NullForge status separate from `docs/STATUS.md` and avoid changing root README or docs navigation unless a human gate approves that scope.

## Imported Volume Status

PF-T001 imported these volume docs as repo-managed NullForge planning/workflow source after audit. They are not ResearchCore Engine implementation truth.

| Volume | Path | Context relevance for PF-T002 |
|---|---|---|
| 00 | `docs/nullforge/blueprint/volumes/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md` | Mission, naming boundary, MVP proof loop, claims, anti-goals, source-of-truth rules, archive/quarantine, decision/reversal conditions. |
| 01 | `docs/nullforge/blueprint/volumes/NullForge_Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine_System_v0_4.md` | Repo/workspace/source-of-truth hierarchy, archive/quarantine policy, current status template, decision ledger/ADR policy. |
| 02 | `docs/nullforge/blueprint/volumes/NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md` | Role-loop, ticket artifact expectations, PASS/HOLD/REJECT gates, docs-only compression policy. |
| 03 | `docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md` | Future desktop/bridge context only; do not implement in PF-T002. |
| 04 | `docs/nullforge/blueprint/volumes/NullForge_Volume_04_Dataset_Studio_ES_Intake_Fixture_Policy_DatasetCapabilityMap_Timeframe_Chart_Rules_v0_4.md` | Future data capability and ES boundary context only; no fixtures or raw data in PF-T002. |
| 05 | `docs/nullforge/blueprint/volumes/NullForge_Volume_05_Logic_Factory_LogicCard_Lifecycle_Compiler_Contract_Generator_Null_Ablation_TestPlan_Bridge_v0_4.md` | Future Logic Factory/compiler context only; no implementation in PF-T002. |
| 06 | `docs/nullforge/blueprint/volumes/NullForge_Volume_06_Visual_Replay_Evidence_Cards_Audit_Decision_UX_Result_Interpretation_Boundaries_v0_4.md` | Future replay/evidence/decision UX context only; no implementation in PF-T002. |
| 07 | `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` | Roadmap, M0 sequence, PF-T002 placement, active docs to create, next ticket ADR-T001. |

## Relevant Volume Context

### Volume 00

Volume 00 states that NullForge is a Windows-first local desktop research workbench for importing market datasets, mapping lawful dataset capabilities, compiling/generating candidate logic into auditable test specs, running the local ResearchCore Engine, inspecting visual trade replays, and deciding whether evidence should be promoted, repaired, archived, or quarantined.

It explicitly says Volume 00 does not implement the desktop app and does not authorize a broad build prompt.

Naming boundary:

- `NullForge` is the active working product name.
- `research-core` remains the existing repo name.
- `ResearchCore Engine` is the active internal engine label.
- Do not rename the existing GitHub repo yet.
- Public release, domains, company identity, or distribution under NullForge require later review.

Status/risk signals relevant to PF-T002:

- Current status is missing/to create.
- Decision ledger is needed.
- Archive means memory without authority.
- Quarantine means unresolved/conflicting/risky material without governance power.
- No implementation until Volume 1-2 and bridge contracts exist.
- Claims such as user/product/technical claims remain untested unless later evidence says otherwise.

### Volume 01

Volume 01 gives the core source hierarchy:

```text
Repo = executable truth + current docs.
Workspace = local user data, generated artifacts, private datasets, and runtime state.
Archive = memory without authority.
Quarantine = unresolved/conflicting/risky material without governance power.
Chat = scratch unless promoted.
```

It says promoted repo docs, passing audits, source code/tests, current status docs, and decision ledger/ADRs can govern implementation. Vault notes, Graphify, chat, archive, and quarantine cannot govern implementation directly.

Relevant PF-T002 signals:

- Current status doc points to the active ticket/state.
- Decision ledger and ADRs must include reversal conditions.
- Old prompts are provenance, not source truth.
- Prior chat is design memory unless explicitly promoted.
- Archive material may be cited as history but not used as active context unless an Archive Review Pack is created.
- Quarantine has no governance power.
- Required ADRs before implementation include name, platform, stack, engine boundary, local-first/no-cloud MVP, and ES.zip outside repo.

### Volume 02

Volume 02 defines the role-separated execution system:

```text
Human / ChatGPT Architect
-> Context Curator
-> Planner
-> Implementor / Codex
-> Auditor
-> Repair if needed
-> Human gate
-> Next ticket
```

It forbids broad "build the app" execution and says tickets must produce artifacts, acceptance criteria, and audit dispositions.

### Volume 03-06

Volumes 03-06 are relevant as source-index entries and future context, but PF-T002 should not implement their concepts.

Important boundary signals:

- Volume 03: desktop bridge/Tauri/sidecar concepts are future architecture context, not PF-T002 implementation authority.
- Volume 04: Dataset Studio, ES.zip, fixture, and DatasetCapabilityMap concepts are future data context; raw/full data and ES-derived fixtures remain gated.
- Volume 05: LogicCard/compiler/generator concepts are future logic context; generated ideas remain untrusted without compiler/evidence gates.
- Volume 06: Visual Replay is explanatory, Evidence Cards summarize evidence, and no result screen may imply financial advice, guaranteed edge, or live-trading readiness.

### Volume 07

Volume 07 states that after promoted volumes, the next sequence is repo-source import, current status/claim/decision/roadmap docs, milestone batching, and then one ticket at a time through curator/planner/implementor/auditor.

It says M0 blocks all implementation and that M1 is the later desktop shell plus ResearchCore Engine bridge proof.

PF-T002-specific signals from Volume 07:

- Current status: `docs/nullforge/CURRENT_STATUS.md`
- Decision ledger: `docs/nullforge/DECISION_LEDGER.md`
- Volume index: `docs/nullforge/blueprint/README.md`
- Roadmap and source docs are future docs, but the incoming PF-T002 ticket is narrower than all docs listed in Volume 07.
- PF-T002 is ticket 3 in M0, depends on PF-T001, and points next to ADR-T001.

Volume 07 M0 non-goals:

- No Tauri app.
- No engine changes.
- No dataset parser.
- No fixture creation.
- No desktop bridge implementation.
- No public release.
- No repo rename.

## PF-T002 Acceptance Signals From Active Ticket

The incoming ticket says acceptance requires:

- `CURRENT_STATUS` names the active phase as `PROJECT_FACTORY_SETUP` / `REPO_SOURCE_IMPORT` or the next precise state.
- `SOURCE_INDEX` links imported volumes, M0 milestone docs, ADRs, and ticket queue.
- Status explicitly says no implementation code has started unless that changes later through audited tickets.
- Source index separates active docs, design memory, archive, quarantine, and prompts.
- Next action points to `ADR-T001`.

Required checks:

- links/paths in source index resolve within repo;
- current status has updated date, active ticket, blockers, and next action;
- manual drift check: one active mission and roadmap.

## Human Gate Triggers

Human review is required before:

- overwriting existing ResearchCore Engine docs;
- changing root README beyond a clearly scoped link/summary;
- renaming repo, package, CLI, app, public project, or product identity;
- adding dependencies, code, scripts, parsers, sidecar binaries, packaging configs, tests, schemas, generated docs tooling, CI behavior, or release/build config;
- committing full `ES.zip`, raw/private/local data, or ES-derived fixtures;
- marking unreviewed materials canonical;
- treating old chat or prompts as active source truth;
- broadening into public release, legal/trademark claims, AI strategy activation, broker/live-trading integration, financial advice wording, auth, billing, cloud sync, marketplace, or mobile scope;
- starting ADR-T001 before PF-T002 audit disposition.

Human gates triggered in this curator pass: NONE.

## Context Risks

- The incoming PF-T002 ticket asks `SOURCE_INDEX` to link M0 milestone docs and ticket queue, but those files are not yet present under `milestones/nullforge/` or `tickets/nullforge/` in the repo. The active versions are still in the incoming package.
- The incoming PF-T002 ticket says `ARCHIVE_POLICY.md or reference to Volume 1`; PF-T000 and Volume 7 also identify `DECISION_LEDGER.md` as a PF-T002/source-baseline file.
- Volume 7 lists many possible future source docs, but PF-T002 should not expand into all of them unless the planner scopes that explicitly from ticket/source requirements.
- ADR-T001 and ADR-T002 are downstream and do not exist yet; PF-T002 can identify them as pending/next but must not create ADRs.
- Existing ResearchCore docs remain the engine truth. PF-T002 should not update root README, docs index, or `docs/STATUS.md` unless a human gate approves it.

## Open Questions For Planner

- Should PF-T002 create `docs/nullforge/DECISION_LEDGER.md`? PF-T000 and Volume 7 name it, but the incoming PF-T002 ticket output list omits it while asking for current status/source index and active decisions.
- Should PF-T002 create `docs/nullforge/ARCHIVE_POLICY.md`, or should it reference Volume 1's archive/quarantine policy instead?
- How should `SOURCE_INDEX.md` satisfy the requirement to link M0 milestone docs and ticket queue when the repo-local milestone/ticket files are absent? Options include listing incoming package sources as external active inputs, marking repo-local paths pending, or having the planner explicitly scope small repo-local source-index entries without importing the full milestone package.
- Should PF-T002 create `docs/nullforge/blueprint/README.md` as the "volume index" mentioned in Volume 7, or should `docs/nullforge/SOURCE_INDEX.md` cover that in PF-T002?
- What exact active phase label should `CURRENT_STATUS.md` use after PF-T001 PASS and before ADR-T001: `PROJECT_FACTORY_SETUP`, `REPO_SOURCE_IMPORT`, `REPO_SOURCE_IMPORT_BASELINE`, or another precise state?

## Ready For Planner

YES, subject to the planner resolving the PF-T002 output-scope questions above and keeping PF-T002 docs-only.
