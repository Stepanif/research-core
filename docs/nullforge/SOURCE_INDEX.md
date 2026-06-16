# NullForge Source Index

Date: `2026-06-16`

Active phase: `M1_READINESS_COMMAND_DISCOVERY`

This index links only to repo-local files that exist. Incoming package sources that are not repo-local are listed in plain text and are not linked as repo paths.

Completed M0 baseline context: `REPO_SOURCE_IMPORT_BASELINE`.

## Active docs

| Source | Purpose | Truth status |
|---|---|---|
| [NullForge README](README.md) | Entry point for NullForge docs. | Active NullForge planning navigation. |
| [Current Status](CURRENT_STATUS.md) | Current NullForge state, gates, blockers, next action. | Active NullForge status baseline after QA-T001 audit `PASS`. |
| [Source Index](SOURCE_INDEX.md) | Index of repo-local NullForge sources and external active inputs. | Active NullForge source navigation after PF-T002 audit disposition. |
| [Decision Ledger](DECISION_LEDGER.md) | Seed decision and pending ADR ledger. | Active NullForge decision tracking after PF-T002 audit disposition. |
| [Archive Policy](ARCHIVE_POLICY.md) | Source authority, archive, quarantine, and prompt policy. | Active NullForge governance baseline after PF-T002 audit disposition. |
| [M0 Handoff](M0_HANDOFF.md) | M0 repo source import and canonical baseline handoff summary. | Active MB-T001 handoff source after MB-T001 audit `PASS`; not implementation proof. |
| [Codex Role Loop](codex/CODEX_ROLE_LOOP.md) | NullForge-specific context curator, planner, implementor, auditor, repair, and human-gate workflow. | Active CX-T001 workflow source after CX-T001 audit `PASS`; not implementation proof. |
| [QA Command Discovery](qa/COMMAND_DISCOVERY.md) | QA-T001 existing repo command and test discovery record. | Active QA-T001 discovery source after QA-T001 audit `PASS`; not implementation proof. |
| [ADR-T001 - Name/platform/stack/engine](adr/ADR-T001-name-platform-stack-engine.md) | Records working product name, first platform, default desktop stack direction, and ResearchCore Engine boundary. | Active NullForge decision record after ADR-T001 audit `PASS`; not implementation proof. |
| [ADR-T002 - Local-first/no-cloud MVP](adr/ADR-T002-local-first-no-cloud-mvp.md) | Records local-first/no-cloud MVP boundary. | Active NullForge decision record after ADR-T002 audit `PASS`; not implementation proof. |
| [PF-T000 Import Plan](import/PF-T000_IMPORT_PLAN.md) | Bounded import and source-of-truth plan. | Active PF-T000 source after audit `PASS`. |
| [PF-T000 Repo Inventory](import/PF-T000_REPO_INVENTORY.md) | Repo inventory and ResearchCore boundary context. | Active PF-T000 source after audit `PASS`. |
| [PF-T000 Conflicts And Gates](import/PF-T000_CONFLICTS_AND_GATES.md) | Conflict and gate register. | Active PF-T000 source after audit `PASS`. |
| [Blueprint Volume README](blueprint/volumes/README.md) | Volume folder authority and volume list. | Active PF-T001 source after audit `PASS`. |
| [Volume Import Manifest](blueprint/volumes/VOLUME_IMPORT_MANIFEST.md) | Imported volume records, hashes, selected entries, and prompt exclusions. | Active PF-T001 source after audit `PASS`. |

## Imported volumes

| Volume | Repo-local file | Purpose | Truth status |
|---|---|---|---|
| 00 | [North Star, Doctrine, Naming, Claims, MVP Cutline, Anti-Goals](blueprint/volumes/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md) | North Star, naming, claim posture, MVP cutline, anti-goals. | NullForge planning/workflow source; not engine implementation truth. |
| 01 | [Workspace, Repo, Context, Source-of-Truth, Archive, Quarantine System](blueprint/volumes/NullForge_Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine_System_v0_4.md) | Workspace, source-of-truth, archive, and quarantine model. | NullForge planning/workflow source; not engine implementation truth. |
| 02 | [Planner, Implementor, Auditor Loop, QA Gates, Human Gates, Codex Execution System](blueprint/volumes/NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md) | Role loop, gates, QA, Codex execution model. | NullForge planning/workflow source; not engine implementation truth. |
| 03 | [Windows Tauri Desktop Architecture, ResearchCore Engine Bridge, Sidecar Contract, Packaging Spike](blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md) | Proposed desktop architecture and engine bridge context. | Proposed planning source only until later ADR or implementation audit. |
| 04 | [Dataset Studio, ES Intake, Fixture Policy, DatasetCapabilityMap, Timeframe and Chart Rules](blueprint/volumes/NullForge_Volume_04_Dataset_Studio_ES_Intake_Fixture_Policy_DatasetCapabilityMap_Timeframe_Chart_Rules_v0_4.md) | Dataset studio and fixture policy context. | Proposed planning source only; raw/private data and ES fixtures remain gated. |
| 05 | [Logic Factory, LogicCard Lifecycle, Compiler Contract, Generator/Null/Ablation Boundary, Test-Plan Bridge](blueprint/volumes/NullForge_Volume_05_Logic_Factory_LogicCard_Lifecycle_Compiler_Contract_Generator_Null_Ablation_TestPlan_Bridge_v0_4.md) | Logic Factory and test-plan bridge context. | Proposed planning source only until later audited work. |
| 06 | [Visual Replay, Evidence Cards, Audit Decision UX, Result Interpretation Boundaries](blueprint/volumes/NullForge_Volume_06_Visual_Replay_Evidence_Cards_Audit_Decision_UX_Result_Interpretation_Boundaries_v0_4.md) | Evidence, audit, visual replay, and interpretation boundaries. | Proposed planning source only until later audited work. |
| 07 | [Roadmap, Milestones, Ticket Backlog, Codex Prompt Packs, First Execution Batch](blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md) | Roadmap, ticket sequence, and prompt pack context. | Planning source for sequence context; downstream tickets still require scoped role-loop execution. |

## Current ticket artifacts

| Source | Purpose | Status |
|---|---|---|
| [ADR-T001 Context Bundle](../../plans/nullforge/ADR-T001/CONTEXT_BUNDLE.md) | Curated active context for ADR-T001. | Repo-local plan artifact. |
| [ADR-T001 Context Bundle Manifest](../../plans/nullforge/ADR-T001/CONTEXT_BUNDLE_MANIFEST.md) | Context source list and exclusions. | Repo-local plan artifact. |
| [ADR-T001 Plan](../../plans/nullforge/ADR-T001/PLAN.md) | Bounded implementation plan. | Repo-local plan artifact. |
| [ADR-T001 Acceptance](../../plans/nullforge/ADR-T001/ACCEPTANCE.md) | Acceptance criteria and checks. | Repo-local plan artifact. |
| [ADR-T001 Implementor Prompt](../../plans/nullforge/ADR-T001/IMPLEMENTOR_PROMPT.md) | Implementor instructions. | Repo-local plan artifact. |
| [ADR-T001 Implementation Report](../../reports/nullforge/ADR-T001/IMPLEMENTATION_REPORT.md) | Implementor report. | Created by ADR-T001 implementor. |
| [ADR-T001 Changed Files](../../reports/nullforge/ADR-T001/CHANGED_FILES.md) | Changed-file inventory. | Created by ADR-T001 implementor. |
| [ADR-T001 Test Results](../../reports/nullforge/ADR-T001/TEST_RESULTS.md) | Required check results. | Created by ADR-T001 implementor. |
| [ADR-T001 Auditor Prompt](../../reports/nullforge/ADR-T001/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by ADR-T001 implementor. |
| [ADR-T001 Audit Report](../../audits/nullforge/ADR-T001/AUDIT_REPORT.md) | Independent audit report and disposition. | ADR-T001 audit decision `PASS`. |
| [ADR-T001 Findings](../../audits/nullforge/ADR-T001/FINDINGS.md) | Independent audit findings summary. | No findings. |
| [ADR-T001 Repair Prompt](../../audits/nullforge/ADR-T001/REPAIR_PROMPT.md) | Bounded repair prompt if later drift is found. | No repair required for ADR-T001 audit `PASS`. |
| [ADR-T002 Context Bundle](../../plans/nullforge/ADR-T002/CONTEXT_BUNDLE.md) | Curated active context for ADR-T002. | Repo-local plan artifact. |
| [ADR-T002 Context Bundle Manifest](../../plans/nullforge/ADR-T002/CONTEXT_BUNDLE_MANIFEST.md) | Context source list and exclusions. | Repo-local plan artifact. |
| [ADR-T002 Plan](../../plans/nullforge/ADR-T002/PLAN.md) | Bounded implementation plan. | Repo-local plan artifact. |
| [ADR-T002 Acceptance](../../plans/nullforge/ADR-T002/ACCEPTANCE.md) | Acceptance criteria and checks. | Repo-local plan artifact. |
| [ADR-T002 Implementor Prompt](../../plans/nullforge/ADR-T002/IMPLEMENTOR_PROMPT.md) | Implementor instructions. | Repo-local plan artifact. |
| [ADR-T002 Implementation Report](../../reports/nullforge/ADR-T002/IMPLEMENTATION_REPORT.md) | Implementor report. | Created by ADR-T002 implementor. |
| [ADR-T002 Changed Files](../../reports/nullforge/ADR-T002/CHANGED_FILES.md) | Changed-file inventory. | Created by ADR-T002 implementor. |
| [ADR-T002 Test Results](../../reports/nullforge/ADR-T002/TEST_RESULTS.md) | Required check results. | Created by ADR-T002 implementor. |
| [ADR-T002 Auditor Prompt](../../reports/nullforge/ADR-T002/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by ADR-T002 implementor. |
| [ADR-T002 Audit Report](../../audits/nullforge/ADR-T002/AUDIT_REPORT.md) | Independent audit report and disposition. | ADR-T002 audit decision `PASS`. |
| [ADR-T002 Findings](../../audits/nullforge/ADR-T002/FINDINGS.md) | Independent audit findings summary. | No findings. |
| [ADR-T002 Repair Prompt](../../audits/nullforge/ADR-T002/REPAIR_PROMPT.md) | Bounded repair prompt if later drift is found. | No repair required for ADR-T002 audit `PASS`. |
| [CX-T001 Context Bundle](../../plans/nullforge/CX-T001/CONTEXT_BUNDLE.md) | Curated active context for CX-T001. | Repo-local plan artifact. |
| [CX-T001 Context Bundle Manifest](../../plans/nullforge/CX-T001/CONTEXT_BUNDLE_MANIFEST.md) | Context source list and exclusions. | Repo-local plan artifact. |
| [CX-T001 Plan](../../plans/nullforge/CX-T001/PLAN.md) | Bounded implementation plan. | Repo-local plan artifact. |
| [CX-T001 Acceptance](../../plans/nullforge/CX-T001/ACCEPTANCE.md) | Acceptance criteria and checks. | Repo-local plan artifact. |
| [CX-T001 Implementor Prompt](../../plans/nullforge/CX-T001/IMPLEMENTOR_PROMPT.md) | Implementor instructions. | Repo-local plan artifact. |
| [CX-T001 Implementation Report](../../reports/nullforge/CX-T001/IMPLEMENTATION_REPORT.md) | Implementor report. | Created by CX-T001 implementor. |
| [CX-T001 Changed Files](../../reports/nullforge/CX-T001/CHANGED_FILES.md) | Changed-file inventory. | Created by CX-T001 implementor. |
| [CX-T001 Test Results](../../reports/nullforge/CX-T001/TEST_RESULTS.md) | Required check results. | Created by CX-T001 implementor. |
| [CX-T001 Auditor Prompt](../../reports/nullforge/CX-T001/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by CX-T001 implementor. |
| [CX-T001 Audit Report](../../audits/nullforge/CX-T001/AUDIT_REPORT.md) | Independent audit report and disposition. | CX-T001 audit decision `PASS`. |
| [CX-T001 Findings](../../audits/nullforge/CX-T001/FINDINGS.md) | Independent audit findings summary. | No findings. |
| [CX-T001 Repair Prompt](../../audits/nullforge/CX-T001/REPAIR_PROMPT.md) | Bounded repair prompt if later drift is found. | No repair required for CX-T001 audit `PASS`. |
| [MB-T001 Context Bundle](../../plans/nullforge/MB-T001/CONTEXT_BUNDLE.md) | Curated active context for MB-T001. | Repo-local plan artifact. |
| [MB-T001 Context Bundle Manifest](../../plans/nullforge/MB-T001/CONTEXT_BUNDLE_MANIFEST.md) | Context source list and exclusions. | Repo-local plan artifact. |
| [MB-T001 Plan](../../plans/nullforge/MB-T001/PLAN.md) | Bounded implementation plan. | Repo-local plan artifact. |
| [MB-T001 Acceptance](../../plans/nullforge/MB-T001/ACCEPTANCE.md) | Acceptance criteria and checks. | Repo-local plan artifact. |
| [MB-T001 Implementor Prompt](../../plans/nullforge/MB-T001/IMPLEMENTOR_PROMPT.md) | Implementor instructions. | Repo-local plan artifact. |
| [MB-T001 Implementation Report](../../reports/nullforge/MB-T001/IMPLEMENTATION_REPORT.md) | Implementor report. | Created by MB-T001 implementor. |
| [MB-T001 Changed Files](../../reports/nullforge/MB-T001/CHANGED_FILES.md) | Changed-file inventory. | Created by MB-T001 implementor. |
| [MB-T001 Test Results](../../reports/nullforge/MB-T001/TEST_RESULTS.md) | Required check results. | Created by MB-T001 implementor. |
| [MB-T001 Auditor Prompt](../../reports/nullforge/MB-T001/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by MB-T001 implementor. |
| [MB-T001 Audit Report](../../audits/nullforge/MB-T001/AUDIT_REPORT.md) | Independent audit report and disposition. | MB-T001 audit decision `PASS`. |
| [MB-T001 Findings](../../audits/nullforge/MB-T001/FINDINGS.md) | Independent audit findings summary. | No findings. |
| [MB-T001 Repair Prompt](../../audits/nullforge/MB-T001/REPAIR_PROMPT.md) | Bounded repair prompt if later drift is found. | No repair required for MB-T001 audit `PASS`. |
| [QA-T001 Context Bundle](../../plans/nullforge/QA-T001/CONTEXT_BUNDLE.md) | Curated active context for QA-T001. | Repo-local context artifact. |
| [QA-T001 Context Bundle Manifest](../../plans/nullforge/QA-T001/CONTEXT_BUNDLE_MANIFEST.md) | Context source list and exclusions. | Repo-local context artifact. |
| [QA-T001 Plan](../../plans/nullforge/QA-T001/PLAN.md) | Bounded implementation plan. | Repo-local plan artifact. |
| [QA-T001 Acceptance](../../plans/nullforge/QA-T001/ACCEPTANCE.md) | Acceptance criteria and checks. | Repo-local plan artifact. |
| [QA-T001 Implementor Prompt](../../plans/nullforge/QA-T001/IMPLEMENTOR_PROMPT.md) | Implementor instructions. | Repo-local plan artifact. |
| [QA-T001 Implementation Report](../../reports/nullforge/QA-T001/IMPLEMENTATION_REPORT.md) | Implementor report. | Created by QA-T001 implementor. |
| [QA-T001 Changed Files](../../reports/nullforge/QA-T001/CHANGED_FILES.md) | Changed-file inventory. | Created by QA-T001 implementor. |
| [QA-T001 Test Results](../../reports/nullforge/QA-T001/TEST_RESULTS.md) | Required check and discovery command results. | Created by QA-T001 implementor. |
| [QA-T001 Auditor Prompt](../../reports/nullforge/QA-T001/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by QA-T001 implementor. |
| [QA-T001 Audit Report](../../audits/nullforge/QA-T001/AUDIT_REPORT.md) | Independent audit report and disposition. | QA-T001 audit decision `PASS`. |
| [QA-T001 Findings](../../audits/nullforge/QA-T001/FINDINGS.md) | Independent audit findings summary. | No blocking findings; non-blocking local environment blocker recorded. |
| [QA-T001 Repair Prompt](../../audits/nullforge/QA-T001/REPAIR_PROMPT.md) | Bounded repair prompt if later drift is found. | No repair required for QA-T001 audit `PASS`. |

## Incoming package inputs

These active inputs are external package sources, not repo-local canonical docs in current M0 status. They are listed in plain text and must not be treated as resolved repo links.

```text
C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\ADR-T001-name-platform-stack-engine-adr.md
C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\MILESTONE_BRIEF.md
C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\TICKET_QUEUE.md
C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\HUMAN_GATE_TRIGGERS.md
```

Repo-local paths below are pending or absent in PF-T002 and are intentionally not linked:

```text
tickets/nullforge/ADR-T001-name-platform-stack-engine-adr.md
milestones/nullforge/M0-repo-source-import/MILESTONE_BRIEF.md
milestones/nullforge/M0-repo-source-import/TICKET_QUEUE.md
milestones/nullforge/M0-repo-source-import/HUMAN_GATE_TRIGGERS.md
```

## Design memory

Imported Volume 00-07 files preserve generated planning context and may be used as design memory for later scoped tickets. Design memory does not override current ResearchCore Engine truth and does not authorize implementation by itself.

## Archive

Archive material is memory without authority. PF-T002 does not import an archive folder. Older source packages, old chat logs, superseded prompts, and prior drafts remain outside active repo-local truth unless a later audited ticket explicitly promotes them.

## Quarantine

Quarantine is for unresolved, conflicting, risky, private, or unreviewed material. Quarantined material has no governance power. Raw/full ES.zip contents, private/local data, ES-derived fixtures, broker-live materials, and unresolved identity/platform claims remain gated.

## Prompts

Prompt files are not canonical volume content. PF-T001 did not import package prompt files as standalone source docs, and PF-T002 does not import M0 prompt files into repo paths. Prompt text may describe workflow intent, but it is not active truth unless promoted by a later audited doc.

## Pending downstream docs

| Item | Expected role | Status |
|---|---|---|
| `ADR-T003` | Future scoped decision if later required. | Pending downstream; not created or started in QA-T001. |
| M1 desktop/bridge/product implementation tickets | Future scoped M1 implementation work after QA readiness and human direction. | Pending downstream; not created or started in QA-T001. |
| M0 milestone and ticket queue repo import | Potential future source import or handoff task. | Incoming-package-only; not created or started in QA-T001. |
