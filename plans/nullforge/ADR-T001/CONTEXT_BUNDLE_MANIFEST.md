# ADR-T001 Context Bundle Manifest

Pack name: NullForge M0 ADR-T001 context bundle
Ticket: ADR-T001 - Name/platform/stack/engine ADR
Purpose: Provide the smallest sufficient active context for the ADR-T001 Planner without creating the ADR, reports, acceptance criteria, implementation docs, or audit docs.

## Included Files

| File | Truth status | Why included |
|---|---|---|
| `C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\ADR-T001-name-platform-stack-engine-adr.md` | Active ADR-T001 ticket source | Defines purpose, scope, outputs, acceptance criteria, checks, human gates, forbidden actions, and closeout requirement. |
| `C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\MILESTONE_BRIEF.md` | Active milestone source | Defines M0 goal, non-goals, target baseline, source doctrine, mission slice, and no-implementation boundary. |
| `C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\TICKET_QUEUE.md` | Active milestone queue | Confirms serial order: PF-T002 -> ADR-T001 -> ADR-T002. |
| `C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\HUMAN_GATE_TRIGGERS.md` | Active gate policy | Defines source-of-truth, technical, data, and product/legal gate triggers. |
| `docs/nullforge/README.md` | Active NullForge docs entry point | Establishes NullForge docs authority boundary and no-implementation status. |
| `docs/nullforge/CURRENT_STATUS.md` | Active NullForge current status | Confirms current phase, PF-T000/PF-T001/PF-T002 dependency state, next action ADR-T001, gates, and claim status. |
| `docs/nullforge/SOURCE_INDEX.md` | Active NullForge source index | Identifies active docs, imported volumes, external package inputs, and pending ADR-T001/ADR-T002. |
| `docs/nullforge/DECISION_LEDGER.md` | Active decision ledger | Contains pending ADR-T001 decision entry and existing source baseline decisions. |
| `docs/nullforge/ARCHIVE_POLICY.md` | Active archive/source policy | Defines active docs, design memory, archive, quarantine, prompts, and promotion rules. |
| `docs/nullforge/import/PF-T000_IMPORT_PLAN.md` | Accepted dependency output | Defines NullForge layout, ADR-T001 path, sequence, and identity-change gates. |
| `docs/nullforge/import/PF-T000_REPO_INVENTORY.md` | Accepted dependency output | Identifies existing ResearchCore truth and confirms separated NullForge path layout. |
| `docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md` | Accepted dependency output | Lists source-of-truth tensions, data/code/identity gates, and downstream sequence gates. |
| `audits/nullforge/PF-T002/AUDIT_REPORT.md` | Dependency audit disposition | Confirms PF-T002 PASS and readiness for ADR-T001 after closeout. |
| `reports/nullforge/PF-T002/TEST_RESULTS.md` | Dependency verification record | Confirms PF-T002 docs-only checks and absent forbidden folders. |
| `docs/nullforge/blueprint/volumes/README.md` | Imported volume index | Lists imported Volume 00-07 files and authority boundary. |
| `docs/nullforge/blueprint/volumes/VOLUME_IMPORT_MANIFEST.md` | Imported source manifest | Records imported volume paths, package hashes, selected entries, and prompt exclusions. |
| `README.md` | Existing ResearchCore front-door truth | Needed to preserve ResearchCore repo/product framing and avoid root README changes. |
| `docs/STATUS.md` | Existing ResearchCore status truth | Needed to keep ADR-T001 from changing ResearchCore Engine status. |
| `docs/index.md` | Existing ResearchCore docs hub | Needed to avoid unscoped docs navigation changes. |
| `docs/ARCHITECTURE.md` | Existing ResearchCore architecture truth | Needed to preserve engine architecture and implementation boundary. |

## Included Volume Context

The following imported volume files were inspected selectively with targeted searches and summarized in `CONTEXT_BUNDLE.md`:

| File | Included context |
|---|---|
| `docs/nullforge/blueprint/volumes/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md` | Working name, repo identity, engine label, first platform, desktop stack, sidecar/bridge strategy, untested claims, reversal conditions, public release/name gates. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine_System_v0_4.md` | ResearchCore repo boundary, ADR/decision-ledger authority, required ADRs, archive/quarantine/prompt source rules. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md` | Role loop, no direct implementation, human gates, Tauri/sidecar/dependency gate signals. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md` | Windows 11 x64 first, Tauri + React + TypeScript architecture, ResearchCore Engine ownership, sidecar/command bridge options, bridge contract, permissions, packaging spike gates. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_04_Dataset_Studio_ES_Intake_Fixture_Policy_DatasetCapabilityMap_Timeframe_Chart_Rules_v0_4.md` | Downstream data gates only: no full ES.zip, no cloud upload, no broker/live feed, no unproven benchmark claims. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_05_Logic_Factory_LogicCard_Lifecycle_Compiler_Contract_Generator_Null_Ablation_TestPlan_Bridge_v0_4.md` | Downstream validation and safety gates only: compile alone is not evidence, no broker/live trading, no financial advice. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_06_Visual_Replay_Evidence_Cards_Audit_Decision_UX_Result_Interpretation_Boundaries_v0_4.md` | Downstream interpretation gates only: one replay is not validation, no financial advice/live-trading readiness. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` | M0/M1 sequence, ADR-T001 placement, platform/stack/engine strategy summary, no implementation/public release/repo rename gates. |

## Path Checks

Repo-local ticket/milestone source paths checked and absent:

- `tickets/nullforge/ADR-T001-name-platform-stack-engine-adr.md`
- `milestones/nullforge/M0-repo-source-import/MILESTONE_BRIEF.md`
- `milestones/nullforge/M0-repo-source-import/TICKET_QUEUE.md`
- `milestones/nullforge/M0-repo-source-import/HUMAN_GATE_TRIGGERS.md`

ADR-T001 output path checks:

- `plans/nullforge/ADR-T001/` absent before this curator pass; created only for this context bundle.
- `docs/nullforge/adr/` absent.
- `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` absent.
- `reports/nullforge/ADR-T001/` absent.
- `audits/nullforge/ADR-T001/` absent.

Existing possible conflict paths:

- `docs/adr/` absent.
- `docs/architecture/` absent.
- `docs/ARCHITECTURE.md` present.
- `README.md` present.
- `docs/STATUS.md` present.
- `docs/index.md` present.

## Excluded Context

| Excluded source | Reason |
|---|---|
| Full copied text of all Volume 00-07 files | Planner needs bounded targeted context; repo-local volumes remain available for direct read. |
| External volume zip packages | PF-T001 already imported and audited selected volume files; ADR-T001 should use repo-local imported docs. |
| Prompt files inside volume packages | Prompt files were not imported as canonical content in PF-T001 and remain provenance only. |
| Full incoming M0 package dump | Only ADR-T001 ticket, milestone brief, ticket queue, and gate policy are needed for this context bundle. |
| `src/`, `tests/`, `schemas/`, `configs/`, `tools/`, package files, and CI files | ADR-T001 is docs/source-of-truth only and must not modify implementation surfaces. |
| Raw/full `ES.zip`, private data, local generated data, or ES-derived fixtures | Explicit data gate and out of ADR-T001 scope. |
| Old chat transcripts and stale prompts | Not source truth unless promoted through a scoped ticket. |
| ADR-T002 planning or ADR files | Downstream; ADR-T001 should only note ADR-T002 as next/pending. |

## Truth Status Summary

- Existing ResearchCore tracked docs/config/code remain authoritative for ResearchCore Engine truth.
- PF-T000, PF-T001, and PF-T002 outputs and PASS audits are authoritative dependency context for ADR-T001.
- Imported Volume 00-07 files are repo-managed NullForge planning/workflow source after PF-T001 audit, not ResearchCore Engine implementation truth.
- Incoming M0 ticket/milestone docs are active instructions until superseded by repo-governed M0 artifacts.
- This ADR-T001 context bundle is temporary planner context, not canonical project documentation.

## Expiry

This bundle expires if any of the following occur before the ADR-T001 Planner starts:

- current branch changes away from `docs/ADR-T001-nullforge-name-platform-stack-engine`;
- `main` changes and this branch is not refreshed;
- working tree changes outside `plans/nullforge/ADR-T001/`;
- in-repo ADR-T001 ticket or M0 milestone files appear;
- PF-T002 audit/status/source-index artifacts are amended;
- `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` appears or changes;
- a human gate is triggered.

## Refresh Rule

Refresh context before running the ADR-T001 Planner if:

- `git status --short --branch` is dirty beyond `plans/nullforge/ADR-T001/`;
- repo-local ticket/milestone paths now exist;
- ADR/report/audit target paths now exist;
- PF-T002 audit status changes;
- the planner needs exact line-level wording from full volume files not summarized here.

## Open Questions

- Should ADR-T001 update `docs/nullforge/CURRENT_STATUS.md`, even though the active ticket does not list it as an output?
- Should ADR-T001 update `docs/nullforge/SOURCE_INDEX.md` to link the new ADR after creation, even though the active ticket does not list it as an output?
- How should the ADR phrase Tauri + React/TypeScript: accepted default stack, or default stack pending bridge/packaging spikes with reversal conditions?
- Should `docs/nullforge/DECISION_LEDGER.md` update `NF-D0004` in place, append a new ADR-T001 entry, or both?
- Should the planner consolidate the name/platform/stack/engine boundary into the single active-ticket ADR path, despite older volume examples that split those decisions across multiple ADRs?

## Human Gate Triggers

Human review is required before overwriting ResearchCore Engine docs, changing root README/docs navigation, changing repo/package/CLI/public identity, adding dependencies/code/scripts/CI behavior, committing raw or ES-derived data without a safety decision, treating unreviewed prompts/chat as active truth, or broadening into public release/legal/financial/live trading/cloud/auth/billing/mobile scope.
