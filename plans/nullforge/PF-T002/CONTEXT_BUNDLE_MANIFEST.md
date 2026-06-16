# PF-T002 Context Bundle Manifest

Pack name: NullForge M0 PF-T002 context bundle
Ticket: PF-T002 - Create NullForge current status and source index
Purpose: Provide the smallest sufficient active context for the PF-T002 Planner without creating status/source-index docs or planning implementation.

## Included Files

| File | Truth status | Why included |
|---|---|---|
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\PF-T002-create-nullforge-current-status-and-source-index.md` | Active PF-T002 ticket source | Defines purpose, scope, outputs, acceptance criteria, checks, human gates, and closeout requirement. |
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\MILESTONE_BRIEF.md` | Active milestone source | Defines M0 goal, non-goals, target baseline, success definition, and no-implementation boundary. |
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\TICKET_QUEUE.md` | Active milestone queue | Defines serial order and confirms PF-T002 depends on PF-T001 and precedes ADR-T001. |
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\HUMAN_GATE_TRIGGERS.md` | Active gate policy | Defines source-of-truth, technical, data, and product/legal gate triggers. |
| `docs/nullforge/import/PF-T000_IMPORT_PLAN.md` | Accepted dependency output | Defines separated `docs/nullforge/` target layout and PF-T002 ownership of README/status/source index/decision ledger. |
| `docs/nullforge/import/PF-T000_REPO_INVENTORY.md` | Accepted dependency output | Identifies existing ResearchCore docs and confirms separated NullForge paths avoid collisions. |
| `docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md` | Accepted dependency output | Lists source-of-truth tensions, path non-conflicts, and human gates. |
| `audits/nullforge/PF-T001/AUDIT_REPORT.md` | Dependency audit disposition | Confirms PF-T001 PASS and imported volume scope. |
| `reports/nullforge/PF-T001/TEST_RESULTS.md` | Dependency verification record | Shows PF-T001 volume files/checks and no implementation/source changes. |
| `docs/nullforge/blueprint/volumes/README.md` | Imported NullForge planning source index | Lists imported Volume 00-07 files and authority boundary. |
| `docs/nullforge/blueprint/volumes/VOLUME_IMPORT_MANIFEST.md` | Imported source manifest | Records package hashes, selected entries, prompt exclusion, authority status, and Volume 00 human decision. |
| `README.md` | Existing ResearchCore front-door truth | Needed to preserve ResearchCore repo/product framing and avoid root README changes. |
| `docs/STATUS.md` | Existing ResearchCore status truth | Needed to keep NullForge current status separate from ResearchCore Engine status. |
| `docs/index.md` | Existing ResearchCore docs hub | Needed to avoid unscoped docs navigation changes. |
| `docs/contributing/docs_style_guide.md` | Repo docs governance | Needed for repo-truth-only and no-guessed-details docs expectations. |

## Included Volume Context

The following imported volume files were inspected selectively, not copied in full into this context bundle:

| File | Included context |
|---|---|
| `docs/nullforge/blueprint/volumes/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md` | Mission, naming boundary, no-implementation status, current-status/decision-ledger need, archive/quarantine rules, claim status risks. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine_System_v0_4.md` | Repo/workspace/source hierarchy, archive/quarantine policy, current status template, decision ledger/ADR policy, prompt/archive rules. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md` | Role-loop and ticket artifact context for PF-T002 planning. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md` | Future desktop/bridge source-index context only. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_04_Dataset_Studio_ES_Intake_Fixture_Policy_DatasetCapabilityMap_Timeframe_Chart_Rules_v0_4.md` | Future data and DatasetCapabilityMap source-index context only. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_05_Logic_Factory_LogicCard_Lifecycle_Compiler_Contract_Generator_Null_Ablation_TestPlan_Bridge_v0_4.md` | Future Logic Factory/source-index context only. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_06_Visual_Replay_Evidence_Cards_Audit_Decision_UX_Result_Interpretation_Boundaries_v0_4.md` | Future replay/evidence/source-index context only. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` | Roadmap, active source-doc list, M0 ticket order, PF-T002 placement, next action ADR-T001. |

## Path Checks

Repo-local ticket/milestone source paths checked and absent:

- `tickets/nullforge/PF-T002-create-nullforge-current-status-and-source-index.md`
- `milestones/nullforge/M0-repo-source-import/MILESTONE_BRIEF.md`
- `milestones/nullforge/M0-repo-source-import/TICKET_QUEUE.md`
- `milestones/nullforge/M0-repo-source-import/HUMAN_GATE_TRIGGERS.md`

PF-T002 output path checks:

- `docs/nullforge/README.md` absent.
- `docs/nullforge/CURRENT_STATUS.md` absent.
- `docs/nullforge/SOURCE_INDEX.md` absent.
- `docs/nullforge/DECISION_LEDGER.md` absent.
- `docs/nullforge/ARCHIVE_POLICY.md` absent.
- `reports/nullforge/PF-T002/` absent.
- `audits/nullforge/PF-T002/` absent.

Existing ResearchCore paths checked present:

- `README.md`
- `docs/STATUS.md`
- `docs/index.md`

## Excluded Context

| Excluded source | Reason |
|---|---|
| Full text of all Volume 00-07 files | Planner needs targeted context and can read repo-local volumes directly if needed; full copy would bloat the bundle. |
| External volume zip packages | PF-T001 already imported and audited the selected volume files; PF-T002 should use repo-local imported docs. |
| Prompt files inside volume packages | Prompt files were not imported as canonical content in PF-T001 and remain provenance only. |
| Full incoming M0 package dump | Only ticket, milestone brief, ticket queue, and gate policy are needed for PF-T002 context. |
| `src/`, `tests/`, `schemas/`, `configs/`, `tools/`, package files, and CI files | PF-T002 is docs/source-of-truth only and must not modify implementation surfaces. |
| Raw/full `ES.zip`, private data, local generated data, or ES-derived fixtures | Explicit data gate and out of PF-T002 scope. |
| Old chat transcripts and stale prompts | Not source truth unless promoted through a scoped ticket. |
| ADR-T001 planning or ADR files | Downstream; PF-T002 should only point next action to ADR-T001. |

## Truth Status Summary

- Existing ResearchCore tracked docs/config/code remain authoritative for ResearchCore Engine truth.
- PF-T000 outputs and PF-T001 PASS audit are authoritative dependency context for PF-T002.
- Imported Volume 00-07 files are repo-managed NullForge planning/workflow source after PF-T001 audit, not ResearchCore Engine implementation truth.
- Incoming M0 ticket/milestone docs are active instructions until superseded by repo-governed M0 artifacts.
- This PF-T002 context bundle is temporary planner context, not canonical project documentation.

## Expiry

This bundle expires if any of the following occur before the PF-T002 Planner starts:

- current branch changes away from `docs/PF-T002-nullforge-status-source-index`;
- `main` changes and this branch is not refreshed;
- working tree changes outside `plans/nullforge/PF-T002/`;
- in-repo PF-T002 ticket or M0 milestone files appear;
- PF-T001 audit/volume import artifacts are amended;
- `docs/nullforge/README.md`, `CURRENT_STATUS.md`, `SOURCE_INDEX.md`, `DECISION_LEDGER.md`, or `ARCHIVE_POLICY.md` appear or change;
- a human gate is triggered.

## Refresh Rule

Refresh context before running the PF-T002 Planner if:

- `git status --short --branch` is dirty beyond `plans/nullforge/PF-T002/`;
- repo-local ticket/milestone paths now exist;
- target output paths now exist;
- PF-T001 audit status changes;
- the planner needs exact line-level wording from full volume files not summarized here.

## Open Questions

- Should PF-T002 create `docs/nullforge/DECISION_LEDGER.md`, given PF-T000 and Volume 7 name it but the incoming PF-T002 ticket output list omits it?
- Should PF-T002 create `docs/nullforge/ARCHIVE_POLICY.md`, or reference Volume 1's archive/quarantine policy?
- How should `SOURCE_INDEX.md` handle M0 milestone docs and ticket queue while those files are incoming-package-only and not repo-local?
- Should PF-T002 create `docs/nullforge/blueprint/README.md`, or should `docs/nullforge/SOURCE_INDEX.md` serve as the volume index for this ticket?
- What exact active phase label should PF-T002 use now that PF-T001 is merged and ADR-T001 is next?

## Human Gate Triggers

Human review is required before overwriting ResearchCore Engine docs, changing root README/docs navigation, changing repo/package/CLI/public identity, adding dependencies/code/scripts/CI behavior, committing raw or ES-derived data without a safety decision, treating unreviewed prompts/chat as active truth, or broadening into public release/legal/financial/live trading/cloud/auth/billing/mobile scope.
