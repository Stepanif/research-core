# NullForge Source Index

Date: `2026-06-18`

Active phase: `M1_WB_T001_AUDIT_PASS`

This index links only to repo-local files that exist. Incoming package sources that are not repo-local are listed in plain text and are not linked as repo paths.

Completed M0 baseline context: `REPO_SOURCE_IMPORT_BASELINE`.

## Active docs

| Source | Purpose | Truth status |
|---|---|---|
| [NullForge README](README.md) | Entry point for NullForge docs. | Active NullForge planning navigation. |
| [Current Status](CURRENT_STATUS.md) | Current NullForge state, gates, blockers, next action. | Active NullForge status baseline after WB-T001 repo-local audit `PASS`; MB-T002 and downstream work are not started. |
| [Source Index](SOURCE_INDEX.md) | Index of repo-local NullForge sources and external active inputs. | Active NullForge source navigation after WB-T001 repo-local audit `PASS`; DA-T004 audit `PASS` remains the bridge-smoke authority, and WB-T001 adds only read-only display of returned artifact metadata. |
| [Decision Ledger](DECISION_LEDGER.md) | Seed decision and pending ADR ledger. | Active NullForge decision tracking after PF-T002 audit disposition. |
| [Archive Policy](ARCHIVE_POLICY.md) | Source authority, archive, quarantine, and prompt policy. | Active NullForge governance baseline after PF-T002 audit disposition. |
| [M0 Handoff](M0_HANDOFF.md) | M0 repo source import and canonical baseline handoff summary. | Active MB-T001 handoff source after MB-T001 audit `PASS`; not implementation proof. |
| [Codex Role Loop](codex/CODEX_ROLE_LOOP.md) | NullForge-specific context curator, planner, implementor, auditor, repair, and human-gate workflow. | Active CX-T001 workflow source after CX-T001 audit `PASS`; not implementation proof. |
| [QA Command Discovery](qa/COMMAND_DISCOVERY.md) | QA-T001 existing repo command and test discovery record. | Active QA-T001 discovery source after QA-T001 audit `PASS`; not implementation proof. |
| [QA Environment Triage](qa/ENVIRONMENT_TRIAGE.md) | QA-T002 local Python environment and CLI/runtime blocker triage record. | Active QA-T002 triage source after audit `PASS`; not environment repair or implementation proof. |
| [QA Environment Repair Decision](qa/ENVIRONMENT_REPAIR_DECISION.md) | QA-T003 human-gated local Python environment repair/readiness decision packet. | Active QA-T003 implementation source after audit `PASS`; not environment repair or CLI readiness proof. |
| [QA Environment Repair Path](qa/ENVIRONMENT_REPAIR_PATH.md) | QA-T004 human-gated local Python environment repair/readiness path preparation packet. | Active QA-T004 implementation source after audit `PASS`; not environment repair or CLI readiness proof. |
| [QA Environment Repair Execution](qa/ENVIRONMENT_REPAIR_EXECUTION.md) | QA-T005 human-approved isolated project-local virtual environment repair/readiness execution record. | Active QA-T005 execution source after audit `PASS`; readiness proof is limited to `.venv-qa-t005`. |
| [Rust/Cargo Toolchain Decision](qa/RUST_CARGO_TOOLCHAIN_DECISION.md) | DA-T003R human-gated Rust/Cargo availability decision path for DA-T003 HOLD. | Active DA-T003R source after audit `PASS`; docs-only and not Rust/Cargo installation, PATH repair, environment repair, toolchain proof, app scaffold, package/dependency work, or runtime proof. |
| [Human Rust/Cargo Availability Gate](qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md) | DA-T003H human-only Rust/Cargo availability gate with DA-T003V human evidence entry. | Active DA-T003H source after audit `PASS`, updated by DA-T003V evidence recording after audit `PASS`; docs-only and not Rust/Cargo installation, PATH repair, environment repair, toolchain proof, app scaffold, package/dependency work, or runtime proof. |
| [Rust/Cargo Setup Path](qa/RUST_CARGO_SETUP_PATH.md) | DA-T003S human-approved Rust/Cargo setup path and setup evidence. | Active DA-T003S source after audit `PASS`; setup evidence only and not DA-T003 resume, app scaffold, package/dependency readiness, Tauri runtime, bridge behavior, sidecar behavior, or runtime proof. |
| [Engine Bridge Contract](architecture/ENGINE_BRIDGE_CONTRACT.md) | DA-T001 planned desktop bridge command contract. | Active DA-T001 source after audit `PASS`; docs-only and not bridge/app implementation proof. |
| [Tauri Scaffold Plan](architecture/TAURI_SCAFFOLD_PLAN.md) | DA-T002 planned Tauri app scaffold source document. | Active DA-T002 source after audit `PASS`; docs-only and not app/scaffold/runtime implementation proof. |
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
| [HY-T001 Context Bundle](../../plans/nullforge/HY-T001/CONTEXT_BUNDLE.md) | Curated context for local-path hygiene cleanup. | Repo-local context artifact. |
| [HY-T001 Context Bundle Manifest](../../plans/nullforge/HY-T001/CONTEXT_BUNDLE_MANIFEST.md) | HY-T001 source list, discovery commands, and candidate files. | Repo-local context artifact. |
| [HY-T001 Plan](../../plans/nullforge/HY-T001/PLAN.md) | Bounded implementation plan for local-path hygiene cleanup. | Repo-local plan artifact. |
| [HY-T001 Acceptance](../../plans/nullforge/HY-T001/ACCEPTANCE.md) | HY-T001 acceptance criteria and required checks. | Repo-local plan artifact. |
| [HY-T001 Implementor Prompt](../../plans/nullforge/HY-T001/IMPLEMENTOR_PROMPT.md) | HY-T001 implementor instructions. | Repo-local plan artifact. |
| [HY-T001 Implementation Report](../../reports/nullforge/HY-T001/IMPLEMENTATION_REPORT.md) | Implementor report. | Created by HY-T001 implementor. |
| [HY-T001 Changed Files](../../reports/nullforge/HY-T001/CHANGED_FILES.md) | Changed-file inventory. | Created by HY-T001 implementor. |
| [HY-T001 Test Results](../../reports/nullforge/HY-T001/TEST_RESULTS.md) | Required check results. | Created by HY-T001 implementor. |
| [HY-T001 Auditor Prompt](../../reports/nullforge/HY-T001/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by HY-T001 implementor. |
| [HY-T001 Audit Report](../../audits/nullforge/HY-T001/AUDIT_REPORT.md) | Independent audit report and disposition. | HY-T001 audit decision `PASS`. |
| [HY-T001 Findings](../../audits/nullforge/HY-T001/FINDINGS.md) | Independent audit findings summary. | No blocking findings; no repair required. |
| [HY-T001 Repair Prompt](../../audits/nullforge/HY-T001/REPAIR_PROMPT.md) | Bounded repair prompt if later drift is found. | No repair required for HY-T001 audit `PASS`. |
| [QA-T002 Context Bundle](../../plans/nullforge/QA-T002/CONTEXT_BUNDLE.md) | Curated context for local Python environment and CLI/runtime blocker triage. | Repo-local context artifact. |
| [QA-T002 Context Bundle Manifest](../../plans/nullforge/QA-T002/CONTEXT_BUNDLE_MANIFEST.md) | QA-T002 context source list and exclusions. | Repo-local context artifact. |
| [QA-T002 Plan](../../plans/nullforge/QA-T002/PLAN.md) | Bounded implementation plan for environment and CLI/runtime blocker triage. | Repo-local plan artifact. |
| [QA-T002 Acceptance](../../plans/nullforge/QA-T002/ACCEPTANCE.md) | QA-T002 acceptance criteria and required checks. | Repo-local plan artifact. |
| [QA-T002 Implementor Prompt](../../plans/nullforge/QA-T002/IMPLEMENTOR_PROMPT.md) | QA-T002 implementor instructions. | Repo-local plan artifact. |
| [QA-T002 Implementation Report](../../reports/nullforge/QA-T002/IMPLEMENTATION_REPORT.md) | Implementor report. | Created by QA-T002 implementor. |
| [QA-T002 Changed Files](../../reports/nullforge/QA-T002/CHANGED_FILES.md) | Changed-file inventory. | Created by QA-T002 implementor. |
| [QA-T002 Test Results](../../reports/nullforge/QA-T002/TEST_RESULTS.md) | Required check and diagnostic command results. | Created by QA-T002 implementor. |
| [QA-T002 Auditor Prompt](../../reports/nullforge/QA-T002/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by QA-T002 implementor. |
| [QA-T002 Audit Report](../../audits/nullforge/QA-T002/AUDIT_REPORT.md) | Independent audit report and disposition. | QA-T002 audit decision `PASS`. |
| [QA-T002 Findings](../../audits/nullforge/QA-T002/FINDINGS.md) | Independent audit findings summary. | No blocking findings; local environment blocker remains gated by design. |
| [QA-T002 Repair Prompt](../../audits/nullforge/QA-T002/REPAIR_PROMPT.md) | Bounded repair prompt if later drift is found. | No repair required for QA-T002 audit `PASS`. |
| [QA-T003 Context Bundle](../../plans/nullforge/QA-T003/CONTEXT_BUNDLE.md) | Curated context for local Python environment repair decisioning. | Repo-local context artifact. |
| [QA-T003 Context Bundle Manifest](../../plans/nullforge/QA-T003/CONTEXT_BUNDLE_MANIFEST.md) | QA-T003 context source list and exclusions. | Repo-local context artifact. |
| [QA-T003 Plan](../../plans/nullforge/QA-T003/PLAN.md) | Bounded implementation plan for repair decisioning. | Repo-local plan artifact. |
| [QA-T003 Acceptance](../../plans/nullforge/QA-T003/ACCEPTANCE.md) | QA-T003 acceptance criteria and required checks. | Repo-local plan artifact. |
| [QA-T003 Implementor Prompt](../../plans/nullforge/QA-T003/IMPLEMENTOR_PROMPT.md) | QA-T003 implementor instructions. | Repo-local plan artifact. |
| [QA-T003 Implementation Report](../../reports/nullforge/QA-T003/IMPLEMENTATION_REPORT.md) | Implementor report. | Created by QA-T003 implementor. |
| [QA-T003 Changed Files](../../reports/nullforge/QA-T003/CHANGED_FILES.md) | Changed-file inventory. | Created by QA-T003 implementor. |
| [QA-T003 Test Results](../../reports/nullforge/QA-T003/TEST_RESULTS.md) | Required check results. | Created by QA-T003 implementor. |
| [QA-T003 Auditor Prompt](../../reports/nullforge/QA-T003/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by QA-T003 implementor. |
| [QA-T003 Audit Report](../../audits/nullforge/QA-T003/AUDIT_REPORT.md) | Independent audit report and disposition. | QA-T003 audit decision `PASS`. |
| [QA-T003 Findings](../../audits/nullforge/QA-T003/FINDINGS.md) | Independent audit findings summary. | No blocking findings; local environment repair remains human-gated by design. |
| [QA-T003 Repair Prompt](../../audits/nullforge/QA-T003/REPAIR_PROMPT.md) | Bounded repair prompt if later drift is found. | No repair required for QA-T003 audit `PASS`. |
| [QA-T004 Context Bundle](../../plans/nullforge/QA-T004/CONTEXT_BUNDLE.md) | Curated context for local Python environment repair path preparation. | Repo-local context artifact. |
| [QA-T004 Context Bundle Manifest](../../plans/nullforge/QA-T004/CONTEXT_BUNDLE_MANIFEST.md) | QA-T004 context source list and exclusions. | Repo-local context artifact. |
| [QA-T004 Plan](../../plans/nullforge/QA-T004/PLAN.md) | Bounded implementation plan for repair path preparation. | Repo-local plan artifact. |
| [QA-T004 Acceptance](../../plans/nullforge/QA-T004/ACCEPTANCE.md) | QA-T004 acceptance criteria and required checks. | Repo-local plan artifact. |
| [QA-T004 Implementor Prompt](../../plans/nullforge/QA-T004/IMPLEMENTOR_PROMPT.md) | QA-T004 implementor instructions. | Repo-local plan artifact. |
| [QA-T004 Implementation Report](../../reports/nullforge/QA-T004/IMPLEMENTATION_REPORT.md) | Implementor report. | Created by QA-T004 implementor. |
| [QA-T004 Changed Files](../../reports/nullforge/QA-T004/CHANGED_FILES.md) | Changed-file inventory. | Created by QA-T004 implementor. |
| [QA-T004 Test Results](../../reports/nullforge/QA-T004/TEST_RESULTS.md) | Required check results. | Created by QA-T004 implementor. |
| [QA-T004 Auditor Prompt](../../reports/nullforge/QA-T004/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by QA-T004 implementor. |
| [QA-T004 Audit Report](../../audits/nullforge/QA-T004/AUDIT_REPORT.md) | Independent audit report and disposition. | QA-T004 audit decision `PASS`. |
| [QA-T004 Findings](../../audits/nullforge/QA-T004/FINDINGS.md) | Independent audit findings summary. | No blocking findings; local environment repair remains human-gated by design. |
| [QA-T004 Repair Prompt](../../audits/nullforge/QA-T004/REPAIR_PROMPT.md) | Bounded repair prompt if later drift is found. | No repair required for QA-T004 audit `PASS`. |
| [QA-T005 Context Bundle](../../plans/nullforge/QA-T005/CONTEXT_BUNDLE.md) | Curated context for human-approved local Python environment repair/readiness execution. | Repo-local context artifact. |
| [QA-T005 Context Bundle Manifest](../../plans/nullforge/QA-T005/CONTEXT_BUNDLE_MANIFEST.md) | QA-T005 context source list and exclusions. | Repo-local context artifact. |
| [QA-T005 Plan](../../plans/nullforge/QA-T005/PLAN.md) | Bounded implementation plan for environment repair/readiness execution. | Repo-local plan artifact. |
| [QA-T005 Acceptance](../../plans/nullforge/QA-T005/ACCEPTANCE.md) | QA-T005 acceptance criteria and required checks. | Repo-local plan artifact. |
| [QA-T005 Implementor Prompt](../../plans/nullforge/QA-T005/IMPLEMENTOR_PROMPT.md) | QA-T005 implementor instructions. | Repo-local plan artifact. |
| [QA-T005 Implementation Report](../../reports/nullforge/QA-T005/IMPLEMENTATION_REPORT.md) | Implementor report. | Created by QA-T005 implementor. |
| [QA-T005 Changed Files](../../reports/nullforge/QA-T005/CHANGED_FILES.md) | Changed-file inventory. | Created by QA-T005 implementor. |
| [QA-T005 Test Results](../../reports/nullforge/QA-T005/TEST_RESULTS.md) | Required check and approved command results. | Created by QA-T005 implementor. |
| [QA-T005 Auditor Prompt](../../reports/nullforge/QA-T005/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by QA-T005 implementor. |
| [QA-T005 Audit Report](../../audits/nullforge/QA-T005/AUDIT_REPORT.md) | Independent audit report and disposition. | QA-T005 audit decision `PASS`. |
| [QA-T005 Findings](../../audits/nullforge/QA-T005/FINDINGS.md) | Independent audit findings summary. | No blocking findings; QA-T005 readiness proof remains scoped to `.venv-qa-t005`. |
| [QA-T005 Repair Prompt](../../audits/nullforge/QA-T005/REPAIR_PROMPT.md) | Bounded repair prompt if later drift is found. | No repair required for QA-T005 audit `PASS`. |
| [DA-T001 Context Bundle](../../plans/nullforge/DA-T001/CONTEXT_BUNDLE.md) | Curated context for desktop bridge contract finalization. | Repo-local context artifact. |
| [DA-T001 Context Bundle Manifest](../../plans/nullforge/DA-T001/CONTEXT_BUNDLE_MANIFEST.md) | DA-T001 context source list and exclusions. | Repo-local context artifact. |
| [DA-T001 Plan](../../plans/nullforge/DA-T001/PLAN.md) | Bounded implementation plan for desktop bridge contract finalization. | Repo-local plan artifact. |
| [DA-T001 Acceptance](../../plans/nullforge/DA-T001/ACCEPTANCE.md) | DA-T001 acceptance criteria and required checks. | Repo-local plan artifact. |
| [DA-T001 Implementor Prompt](../../plans/nullforge/DA-T001/IMPLEMENTOR_PROMPT.md) | DA-T001 implementor instructions. | Repo-local plan artifact. |
| [DA-T001 Implementation Report](../../reports/nullforge/DA-T001/IMPLEMENTATION_REPORT.md) | Implementor report. | Created by DA-T001 implementor. |
| [DA-T001 Changed Files](../../reports/nullforge/DA-T001/CHANGED_FILES.md) | Changed-file inventory. | Created by DA-T001 implementor. |
| [DA-T001 Test Results](../../reports/nullforge/DA-T001/TEST_RESULTS.md) | Required check results. | Created by DA-T001 implementor. |
| [DA-T001 Auditor Prompt](../../reports/nullforge/DA-T001/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by DA-T001 implementor. |
| [DA-T001 Audit Report](../../audits/nullforge/DA-T001/AUDIT_REPORT.md) | Independent audit report and disposition. | DA-T001 audit decision `PASS`. |
| [DA-T001 Findings](../../audits/nullforge/DA-T001/FINDINGS.md) | Independent audit findings summary. | No blocking findings; DA-T001 remains docs-only bridge contract source work. |
| [DA-T001 Repair Prompt](../../audits/nullforge/DA-T001/REPAIR_PROMPT.md) | Bounded repair prompt if later drift is found. | No repair required for DA-T001 audit `PASS`. |
| [DA-T002 Context Bundle](../../plans/nullforge/DA-T002/CONTEXT_BUNDLE.md) | Curated context for Tauri scaffold plan finalization. | Repo-local context artifact. |
| [DA-T002 Context Bundle Manifest](../../plans/nullforge/DA-T002/CONTEXT_BUNDLE_MANIFEST.md) | DA-T002 context source list and exclusions. | Repo-local context artifact. |
| [DA-T002 Plan](../../plans/nullforge/DA-T002/PLAN.md) | Bounded implementation plan for Tauri scaffold plan finalization. | Repo-local plan artifact. |
| [DA-T002 Acceptance](../../plans/nullforge/DA-T002/ACCEPTANCE.md) | DA-T002 acceptance criteria and required checks. | Repo-local plan artifact. |
| [DA-T002 Implementor Prompt](../../plans/nullforge/DA-T002/IMPLEMENTOR_PROMPT.md) | DA-T002 implementor instructions. | Repo-local plan artifact. |
| [DA-T002 Implementation Report](../../reports/nullforge/DA-T002/IMPLEMENTATION_REPORT.md) | Implementor report. | Created by DA-T002 implementor. |
| [DA-T002 Changed Files](../../reports/nullforge/DA-T002/CHANGED_FILES.md) | Changed-file inventory. | Created by DA-T002 implementor. |
| [DA-T002 Test Results](../../reports/nullforge/DA-T002/TEST_RESULTS.md) | Required check results. | Created by DA-T002 implementor. |
| [DA-T002 Auditor Prompt](../../reports/nullforge/DA-T002/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by DA-T002 implementor. |
| [DA-T002 Audit Report](../../audits/nullforge/DA-T002/AUDIT_REPORT.md) | Independent audit report and disposition. | DA-T002 audit decision `PASS`. |
| [DA-T002 Findings](../../audits/nullforge/DA-T002/FINDINGS.md) | Independent audit findings summary. | No blocking findings; DA-T002 remains docs-only scaffold plan source work. |
| [DA-T002 Repair Prompt](../../audits/nullforge/DA-T002/REPAIR_PROMPT.md) | Bounded repair prompt if later drift is found. | No repair required for DA-T002 audit `PASS`. |
| [DA-T003 Context Bundle](../../plans/nullforge/DA-T003/CONTEXT_BUNDLE.md) | Curated context for minimal Tauri shell scaffold implementation. | Repo-local context artifact; DA-T003 audit `HOLD` due missing Rust/Cargo before scaffold creation. |
| [DA-T003 Context Bundle Manifest](../../plans/nullforge/DA-T003/CONTEXT_BUNDLE_MANIFEST.md) | DA-T003 context source list and exclusions. | Repo-local context artifact; DA-T003 audit `HOLD` due missing Rust/Cargo before scaffold creation. |
| [DA-T003 Plan](../../plans/nullforge/DA-T003/PLAN.md) | Bounded implementation plan for minimal launch-only Tauri shell scaffold. | Repo-local plan artifact; DA-T003 audit `HOLD` due missing Rust/Cargo before scaffold creation. |
| [DA-T003 Acceptance](../../plans/nullforge/DA-T003/ACCEPTANCE.md) | DA-T003 acceptance criteria and required checks. | Repo-local plan artifact; DA-T003 audit `HOLD` due missing Rust/Cargo before scaffold creation. |
| [DA-T003 Implementor Prompt](../../plans/nullforge/DA-T003/IMPLEMENTOR_PROMPT.md) | DA-T003 implementor instructions. | Repo-local plan artifact; DA-T003 audit `HOLD` due missing Rust/Cargo before scaffold creation. |
| [DA-T003 Implementation Report](../../reports/nullforge/DA-T003/IMPLEMENTATION_REPORT.md) | Blocked implementor report. | DA-T003 stopped before scaffold creation; no `apps/`, app package, lockfile, Tauri, Rust, React, TypeScript, JavaScript, CSS, or HTML files were created. |
| [DA-T003 Changed Files](../../reports/nullforge/DA-T003/CHANGED_FILES.md) | Changed-file inventory for blocked attempt. | Records DA-T003 report-only implementation attempt and no scaffold files. |
| [DA-T003 Test Results](../../reports/nullforge/DA-T003/TEST_RESULTS.md) | Required probe and skipped-check results. | Records `node`/`pnpm` available, `rustc`/`cargo` unavailable, and DA-T003 stopped before scaffold creation. |
| [DA-T003 Auditor Prompt](../../reports/nullforge/DA-T003/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by DA-T003 blocked implementor attempt. |
| [DA-T003 Audit Report](../../audits/nullforge/DA-T003/AUDIT_REPORT.md) | Independent audit report and disposition. | DA-T003 audit decision `HOLD`; toolchain blocker confirmed. |
| [DA-T003 Findings](../../audits/nullforge/DA-T003/FINDINGS.md) | Independent audit findings summary. | Blocking finding: `rustc` and `cargo` unavailable on PATH. |
| [DA-T003 Repair Prompt](../../audits/nullforge/DA-T003/REPAIR_PROMPT.md) | Bounded resume prompt after human-approved toolchain availability or plan change. | Repair prompt only; no environment repair or implementation performed. |
| [DA-T003R Context Bundle](../../plans/nullforge/DA-T003R/CONTEXT_BUNDLE.md) | Curated context for Rust/Cargo toolchain availability decisioning. | Repo-local context artifact. |
| [DA-T003R Context Bundle Manifest](../../plans/nullforge/DA-T003R/CONTEXT_BUNDLE_MANIFEST.md) | DA-T003R context source list and exclusions. | Repo-local context artifact. |
| [DA-T003R Plan](../../plans/nullforge/DA-T003R/PLAN.md) | Bounded implementation plan for docs-only Rust/Cargo decision source. | Repo-local plan artifact. |
| [DA-T003R Acceptance](../../plans/nullforge/DA-T003R/ACCEPTANCE.md) | DA-T003R acceptance criteria and required checks. | Repo-local plan artifact. |
| [DA-T003R Implementor Prompt](../../plans/nullforge/DA-T003R/IMPLEMENTOR_PROMPT.md) | DA-T003R implementor instructions. | Repo-local plan artifact. |
| [DA-T003R Decision Source](qa/RUST_CARGO_TOOLCHAIN_DECISION.md) | Human-gated Rust/Cargo availability decision path. | DA-T003R source after audit `PASS`; not toolchain proof or environment repair. |
| [DA-T003R Implementation Report](../../reports/nullforge/DA-T003R/IMPLEMENTATION_REPORT.md) | Implementor report. | Created by DA-T003R implementor. |
| [DA-T003R Changed Files](../../reports/nullforge/DA-T003R/CHANGED_FILES.md) | Changed-file inventory. | Created by DA-T003R implementor. |
| [DA-T003R Test Results](../../reports/nullforge/DA-T003R/TEST_RESULTS.md) | Required check results. | Created by DA-T003R implementor. |
| [DA-T003R Auditor Prompt](../../reports/nullforge/DA-T003R/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by DA-T003R implementor. |
| [DA-T003R Audit Report](../../audits/nullforge/DA-T003R/AUDIT_REPORT.md) | Independent audit report and disposition. | DA-T003R audit decision `PASS`. |
| [DA-T003R Findings](../../audits/nullforge/DA-T003R/FINDINGS.md) | Independent audit findings summary. | No blocking findings; DA-T003R remains docs-only toolchain availability decision work. |
| [DA-T003R Repair Prompt](../../audits/nullforge/DA-T003R/REPAIR_PROMPT.md) | Bounded repair prompt if later drift is found. | No repair required for DA-T003R audit `PASS`. |
| [DA-T003H Context Bundle](../../plans/nullforge/DA-T003H/CONTEXT_BUNDLE.md) | Curated context for human Rust/Cargo availability gate. | Repo-local context artifact. |
| [DA-T003H Context Bundle Manifest](../../plans/nullforge/DA-T003H/CONTEXT_BUNDLE_MANIFEST.md) | DA-T003H context source list and exclusions. | Repo-local context artifact. |
| [DA-T003H Plan](../../plans/nullforge/DA-T003H/PLAN.md) | Bounded implementation plan for docs-only human Rust/Cargo availability gate. | Repo-local plan artifact. |
| [DA-T003H Acceptance](../../plans/nullforge/DA-T003H/ACCEPTANCE.md) | DA-T003H acceptance criteria and required checks. | Repo-local plan artifact. |
| [DA-T003H Implementor Prompt](../../plans/nullforge/DA-T003H/IMPLEMENTOR_PROMPT.md) | DA-T003H implementor instructions. | Repo-local plan artifact. |
| [DA-T003H Gate Source](qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md) | Human-only Rust/Cargo availability checklist and gate. | DA-T003H source after audit `PASS`; not toolchain proof or environment repair. |
| [DA-T003H Implementation Report](../../reports/nullforge/DA-T003H/IMPLEMENTATION_REPORT.md) | Implementor report. | Created by DA-T003H implementor. |
| [DA-T003H Changed Files](../../reports/nullforge/DA-T003H/CHANGED_FILES.md) | Changed-file inventory. | Created by DA-T003H implementor. |
| [DA-T003H Test Results](../../reports/nullforge/DA-T003H/TEST_RESULTS.md) | Required check results. | Created by DA-T003H implementor. |
| [DA-T003H Auditor Prompt](../../reports/nullforge/DA-T003H/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by DA-T003H implementor. |
| [DA-T003H Audit Report](../../audits/nullforge/DA-T003H/AUDIT_REPORT.md) | Independent audit report and disposition. | DA-T003H audit decision `PASS`. |
| [DA-T003H Findings](../../audits/nullforge/DA-T003H/FINDINGS.md) | Independent audit findings summary. | No blocking findings; DA-T003H remains docs-only human Rust/Cargo availability gate work. |
| [DA-T003H Repair Prompt](../../audits/nullforge/DA-T003H/REPAIR_PROMPT.md) | Bounded repair prompt if later drift is found. | No repair required for DA-T003H audit `PASS`. |
| [DA-T003V Evidence Record](../../reports/nullforge/DA-T003V/EVIDENCE_RECORD.md) | Human-provided Rust/Cargo evidence record. | DA-T003V negative evidence recorded after audit `PASS`; not Codex verification or toolchain proof. |
| [DA-T003V Changed Files](../../reports/nullforge/DA-T003V/CHANGED_FILES.md) | Changed-file inventory. | Created by DA-T003V evidence recorder. |
| [DA-T003V Test Results](../../reports/nullforge/DA-T003V/TEST_RESULTS.md) | Required check results. | Created by DA-T003V evidence recorder. |
| [DA-T003V Auditor Prompt](../../reports/nullforge/DA-T003V/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by DA-T003V evidence recorder. |
| [DA-T003V Audit Report](../../audits/nullforge/DA-T003V/AUDIT_REPORT.md) | Independent audit report and disposition. | DA-T003V audit decision `PASS`. |
| [DA-T003V Findings](../../audits/nullforge/DA-T003V/FINDINGS.md) | Independent audit findings summary. | No blocking findings; DA-T003V remains historical negative human evidence only. |
| [DA-T003V Repair Prompt](../../audits/nullforge/DA-T003V/REPAIR_PROMPT.md) | Bounded repair prompt if later drift is found. | No repair required for DA-T003V audit `PASS`. |
| [DA-T003S Context Bundle](../../plans/nullforge/DA-T003S/CONTEXT_BUNDLE.md) | Curated context for human-gated Rust/Cargo setup path. | Repo-local plan artifact. |
| [DA-T003S Context Bundle Manifest](../../plans/nullforge/DA-T003S/CONTEXT_BUNDLE_MANIFEST.md) | DA-T003S context source list and exclusions. | Repo-local plan artifact. |
| [DA-T003S Plan](../../plans/nullforge/DA-T003S/PLAN.md) | Bounded plan for Rust/Cargo setup path. | Repo-local plan artifact; latest implementor prompt explicitly authorized setup execution. |
| [DA-T003S Acceptance](../../plans/nullforge/DA-T003S/ACCEPTANCE.md) | DA-T003S planning acceptance criteria and checks. | Repo-local plan artifact; superseded only where the latest implementor prompt explicitly authorized setup/probe execution. |
| [DA-T003S Implementor Prompt](../../plans/nullforge/DA-T003S/IMPLEMENTOR_PROMPT.md) | DA-T003S implementor instructions from planner handoff. | Repo-local plan artifact; latest user prompt expanded scope to minimum approved setup/probes. |
| [DA-T003S Setup Path](qa/RUST_CARGO_SETUP_PATH.md) | Human-approved Rust/Cargo setup path and setup evidence. | DA-T003S source after audit `PASS`; setup evidence only and not DA-T003 resume proof. |
| [DA-T003S Implementation Report](../../reports/nullforge/DA-T003S/IMPLEMENTATION_REPORT.md) | Implementor report. | Created by DA-T003S implementor. |
| [DA-T003S Changed Files](../../reports/nullforge/DA-T003S/CHANGED_FILES.md) | Changed-file inventory. | Created by DA-T003S implementor. |
| [DA-T003S Test Results](../../reports/nullforge/DA-T003S/TEST_RESULTS.md) | Required check and setup/probe results. | Created by DA-T003S implementor. |
| [DA-T003S Auditor Prompt](../../reports/nullforge/DA-T003S/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by DA-T003S implementor. |
| [DA-T003S Audit Report](../../audits/nullforge/DA-T003S/AUDIT_REPORT.md) | Independent audit report and disposition. | DA-T003S audit decision `PASS`. |
| [DA-T003S Findings](../../audits/nullforge/DA-T003S/FINDINGS.md) | Independent audit findings summary. | No blocking findings; DA-T003S remains setup-evidence-only work. |
| [DA-T003S Repair Prompt](../../audits/nullforge/DA-T003S/REPAIR_PROMPT.md) | Bounded repair prompt if later drift is found. | No repair required for DA-T003S audit `PASS`. |
| [DA-T003 Resume Context Bundle](../../plans/nullforge/DA-T003-RESUME/CONTEXT_BUNDLE.md) | Curated context for DA-T003 resume after DA-T003S setup evidence. | Repo-local plan artifact; not scaffold implementation proof. |
| [DA-T003 Resume Context Bundle Manifest](../../plans/nullforge/DA-T003-RESUME/CONTEXT_BUNDLE_MANIFEST.md) | DA-T003 resume context source list and exclusions. | Repo-local plan artifact; not scaffold implementation proof. |
| [DA-T003 Resume Plan](../../plans/nullforge/DA-T003-RESUME/PLAN.md) | Bounded plan for DA-T003 resume. | Repo-local plan artifact; requires fresh resume probes before scaffold creation. |
| [DA-T003 Resume Acceptance](../../plans/nullforge/DA-T003-RESUME/ACCEPTANCE.md) | DA-T003 resume acceptance criteria and required checks. | Repo-local plan artifact. |
| [DA-T003 Resume Implementor Prompt](../../plans/nullforge/DA-T003-RESUME/IMPLEMENTOR_PROMPT.md) | DA-T003 resume implementor instructions. | Repo-local plan artifact. |
| [DA-T003 Resume Implementation Report](../../reports/nullforge/DA-T003-RESUME/IMPLEMENTATION_REPORT.md) | DA-T003-RESUME implementor report. | Created by DA-T003-RESUME; records fresh tool gate pass, bounded scaffold creation, app-local pnpm/icon repair, exact app-local install/build pass, process-level `tauri dev` launch evidence, and generated-output cleanup. |
| [DA-T003 Resume Changed Files](../../reports/nullforge/DA-T003-RESUME/CHANGED_FILES.md) | Changed-file inventory for DA-T003-RESUME. | Records app-local scaffold files, app-local lockfiles, status/source updates, and DA-T003-RESUME reports only. |
| [DA-T003 Resume Test Results](../../reports/nullforge/DA-T003-RESUME/TEST_RESULTS.md) | Required probe, install/build, launch-smoke, and boundary-check results. | Records `rustc`/`cargo`/`node`/`pnpm` available, app-local install/build pass, historical pre-repair Vite watcher and icon blockers, human-authorized app-local repairs, final process-level launch evidence, and no screenshot-level UI proof. |
| [DA-T003 Resume Auditor Prompt](../../reports/nullforge/DA-T003-RESUME/AUDITOR_PROMPT.md) | Independent auditor prompt for DA-T003-RESUME. | Created by DA-T003-RESUME implementor; asks auditor to review bounded scaffold, app-local pnpm/icon repair, install/build proof, process-level launch evidence, and proof boundaries. |
| [DA-T003 Resume Audit Report](../../audits/nullforge/DA-T003-RESUME/AUDIT_REPORT.md) | Independent audit report and disposition for DA-T003-RESUME. | DA-T003-RESUME audit decision `PASS`; process-level `nullforge-desktop.exe` launch evidence accepted for the launch-only scaffold, with no screenshot-level UI proof. |
| [DA-T003 Resume Findings](../../audits/nullforge/DA-T003-RESUME/FINDINGS.md) | Independent audit findings and cleanup status for DA-T003-RESUME. | No blocking findings; non-blocking stale icon-blocker wording finding cleaned up by documentation-only follow-up. |
| [DA-T003 Resume Repair Prompt](../../audits/nullforge/DA-T003-RESUME/REPAIR_PROMPT.md) | Bounded repair/cleanup prompt for DA-T003-RESUME drift. | No blocking repair required; cleanup prompt is retained only for future wording drift. |
| [DA-T004 Context Bundle](../../plans/nullforge/DA-T004/CONTEXT_BUNDLE.md) | Curated context for the first desktop bridge smoke. | Repo-local plan artifact. |
| [DA-T004 Context Bundle Manifest](../../plans/nullforge/DA-T004/CONTEXT_BUNDLE_MANIFEST.md) | DA-T004 context source list and exclusions. | Repo-local plan artifact. |
| [DA-T004 Plan](../../plans/nullforge/DA-T004/PLAN.md) | Bounded plan for exactly one temporary dev-only bridge smoke command. | Repo-local plan artifact. |
| [DA-T004 Acceptance](../../plans/nullforge/DA-T004/ACCEPTANCE.md) | DA-T004 acceptance criteria and required checks. | Repo-local plan artifact. |
| [DA-T004 Implementor Prompt](../../plans/nullforge/DA-T004/IMPLEMENTOR_PROMPT.md) | DA-T004 implementor instructions. | Repo-local plan artifact; latest human prompt explicitly authorized `engine.cli_help_smoke` as the temporary dev-only first bridge proof. |
| [DA-T004 Implementation Report](../../reports/nullforge/DA-T004/IMPLEMENTATION_REPORT.md) | DA-T004 implementor report. | Created by DA-T004 implementor; records one app-local `engine.cli_help_smoke` bridge command, fixed `.venv-qa-t005` help-smoke target, app-local dependency updates, build/check evidence, launch evidence, and boundaries. |
| [DA-T004 Changed Files](../../reports/nullforge/DA-T004/CHANGED_FILES.md) | Changed-file inventory for DA-T004. | Records app-local bridge/UI/dependency files, status/source updates, and DA-T004 reports only. |
| [DA-T004 Test Results](../../reports/nullforge/DA-T004/TEST_RESULTS.md) | Required DA-T004 check results. | Records app-local install/build/check results, fixed CLI help-smoke result, Tauri process-level launch evidence, cleanup state, skipped `rustfmt` reason, and no screenshot-level visual UI or button-click proof. |
| [DA-T004 Auditor Prompt](../../reports/nullforge/DA-T004/AUDITOR_PROMPT.md) | Independent auditor prompt for DA-T004. | Created by DA-T004 implementor; asks auditor to verify the single-command bridge smoke and forbidden-scope boundaries. |
| [DA-T004 Audit Report](../../audits/nullforge/DA-T004/AUDIT_REPORT.md) | Independent audit report and disposition for DA-T004. | DA-T004 audit decision `PASS`; accepts the bounded single-command bridge smoke with explicit evidence limits and no screenshot/button-click proof. |
| [DA-T004 Findings](../../audits/nullforge/DA-T004/FINDINGS.md) | Independent audit findings and observations for DA-T004. | No blocking findings; records non-blocking observation that audit-time process-query reruns were sandbox-blocked while implementation test results recorded cleanup success. |
| [DA-T004 Repair Prompt](../../audits/nullforge/DA-T004/REPAIR_PROMPT.md) | Bounded repair prompt if later DA-T004 drift is found. | No blocking repair required for DA-T004 audit `PASS`. |
| [WB-T001 Context Bundle](../../plans/nullforge/WB-T001/CONTEXT_BUNDLE.md) | Curated context for artifact metadata read-only viewer. | Repo-local plan artifact; scopes WB-T001 to displaying DA-T004 bridge-returned `artifacts` only. |
| [WB-T001 Context Bundle Manifest](../../plans/nullforge/WB-T001/CONTEXT_BUNDLE_MANIFEST.md) | WB-T001 context source list and exclusions. | Repo-local plan artifact. |
| [WB-T001 Plan](../../plans/nullforge/WB-T001/PLAN.md) | Bounded plan for read-only artifact metadata display. | Repo-local plan artifact. |
| [WB-T001 Acceptance](../../plans/nullforge/WB-T001/ACCEPTANCE.md) | WB-T001 acceptance criteria and required checks. | Repo-local plan artifact. |
| [WB-T001 Implementor Prompt](../../plans/nullforge/WB-T001/IMPLEMENTOR_PROMPT.md) | WB-T001 implementor instructions. | Repo-local plan artifact. |
| [WB-T001 Implementation Report](../../reports/nullforge/WB-T001/IMPLEMENTATION_REPORT.md) | WB-T001 implementor report. | Created by WB-T001 implementor; records frontend-only read-only artifact metadata display and evidence boundaries. |
| [WB-T001 Changed Files](../../reports/nullforge/WB-T001/CHANGED_FILES.md) | Changed-file inventory for WB-T001. | Records `App.tsx`, `styles.css`, status/source updates, and WB-T001 reports only. |
| [WB-T001 Test Results](../../reports/nullforge/WB-T001/TEST_RESULTS.md) | Required WB-T001 check results. | Records app-local build pass, diff hygiene, forbidden-scope scans, and no screenshot/button-click proof. |
| [WB-T001 Auditor Prompt](../../reports/nullforge/WB-T001/AUDITOR_PROMPT.md) | Repo-local auditor prompt for WB-T001. | Used for repo-local closeout; WB-T001 audit decision is `PASS`. |
| [WB-T001 Audit Report](../../audits/nullforge/WB-T001/AUDIT_REPORT.md) | Repo-local audit report and disposition for WB-T001. | WB-T001 audit decision `PASS`; closes the read-only returned-artifact metadata viewer with explicit evidence limits. |
| [WB-T001 Findings](../../audits/nullforge/WB-T001/FINDINGS.md) | Repo-local audit findings and observations for WB-T001. | No blocking or reject-level findings; records accepted evidence limits for no screenshot/button-click/Tauri dev/non-empty runtime artifact proof. |
| [WB-T001 Repair Prompt](../../audits/nullforge/WB-T001/REPAIR_PROMPT.md) | Bounded repair prompt if later WB-T001 drift is found. | No blocking repair required for WB-T001 audit `PASS`. |
| [NullForge Desktop Gitignore](../../apps/nullforge-desktop/.gitignore) | App-local ignore rules for dependency/build outputs. | DA-T003-RESUME scaffold file; ignores `node_modules/`, `dist/`, `src-tauri/target/`, and `src-tauri/gen/`. |
| [NullForge Desktop HTML](../../apps/nullforge-desktop/index.html) | Static app entry HTML. | DA-T003-RESUME launch-only scaffold file. |
| [NullForge Desktop Package Manifest](../../apps/nullforge-desktop/package.json) | App-local pnpm package manifest and scripts. | DA-T004 adds only app-local `@tauri-apps/api` for the single bridge-smoke UI; no root package file exists. |
| [NullForge Desktop pnpm Lock](../../apps/nullforge-desktop/pnpm-lock.yaml) | App-local resolved Node package graph. | DA-T004 app-local dependency artifact; no root lockfile. |
| [NullForge Desktop pnpm Workspace Settings](../../apps/nullforge-desktop/pnpm-workspace.yaml) | App-local pnpm 11 build-script approval settings. | DA-T003-RESUME repair file; approves only `esbuild` for Vite dependency installation and does not create a root workspace. |
| [NullForge Desktop TypeScript Config](../../apps/nullforge-desktop/tsconfig.json) | App-local TypeScript config. | DA-T003-RESUME scaffold file. |
| [NullForge Desktop Vite Config](../../apps/nullforge-desktop/vite.config.ts) | App-local Vite config. | DA-T003-RESUME scaffold file; Vite dev server is loopback only and ignores Tauri generated/build outputs. |
| [NullForge Desktop React App](../../apps/nullforge-desktop/src/App.tsx) | DA-T004 bridge-smoke UI plus WB-T001 read-only artifact metadata display. | Adds exactly one user-triggered `engine.cli_help_smoke` invoke action and bounded result display; WB-T001 displays only `result.artifacts` from the bridge response and an empty state; no workspace, sidecar, artifact file access, dataset, network, telemetry, public release, broker/live, AI/model, or financial advice behavior. |
| [NullForge Desktop React Main](../../apps/nullforge-desktop/src/main.tsx) | React mount entrypoint. | DA-T003-RESUME scaffold file. |
| [NullForge Desktop Styles](../../apps/nullforge-desktop/src/styles.css) | DA-T004 bridge-smoke UI and WB-T001 artifact metadata styling. | Styles the single trigger/result surface and read-only artifact metadata empty/list state while preserving app-local bounded UI scope. |
| [NullForge Desktop Cargo Manifest](../../apps/nullforge-desktop/src-tauri/Cargo.toml) | App-local Rust/Tauri manifest. | DA-T004 adds only app-local `serde` for bounded bridge response serialization; no root Cargo manifest exists. |
| [NullForge Desktop Cargo Lock](../../apps/nullforge-desktop/src-tauri/Cargo.lock) | App-local resolved Rust package graph. | DA-T004 app-local dependency artifact; no root Cargo lockfile. |
| [NullForge Desktop Tauri Build Script](../../apps/nullforge-desktop/src-tauri/build.rs) | Tauri build script. | DA-T003-RESUME scaffold file; default Tauri build behavior requires a Windows ICO file for launch smoke. |
| [NullForge Desktop Icon](../../apps/nullforge-desktop/src-tauri/icons/icon.ico) | App-local Windows icon required by Tauri resource generation. | DA-T003-RESUME repair asset; minimal local icon only, not branding/legal/trademark proof. |
| [NullForge Desktop Tauri Config](../../apps/nullforge-desktop/src-tauri/tauri.conf.json) | Tauri app config. | DA-T003-RESUME scaffold file; bundle inactive, static window only. |
| [NullForge Desktop Default Capability](../../apps/nullforge-desktop/src-tauri/capabilities/default.json) | Minimal Tauri capability file. | DA-T003-RESUME scaffold file; empty permission list. |
| [NullForge Desktop Rust Main](../../apps/nullforge-desktop/src-tauri/src/main.rs) | DA-T004 app-local Tauri command entrypoint. | Implements exactly one Tauri command, `engine.cli_help_smoke`, using fixed `.venv-qa-t005` Python/help arguments, timeout, bounded output excerpts, and structured `OK`/`ERROR`/`TIMEOUT`/`BLOCKED` responses; no plugins, sidecar, workspace, network, telemetry, updater, signing, public release, broker/live, AI/model, or financial advice behavior. |

## Incoming package inputs

These active inputs are external package sources, not repo-local canonical docs in current M0 status. They are listed in plain text and must not be treated as resolved repo links.

```text
<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\ADR-T001-name-platform-stack-engine-adr.md
<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\MILESTONE_BRIEF.md
<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\TICKET_QUEUE.md
<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\HUMAN_GATE_TRIGGERS.md
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
| `ADR-T003` | Future scoped decision if later required. | Pending downstream; not created or started. |
| Rust/Cargo setup action or scoped plan change | Historical setup path for making `rustc` and `cargo` visible to a later resume shell. | DA-T003S setup evidence recorded with audit `PASS`; DA-T003-RESUME independently verified Rust/Cargo availability in the restarted PowerShell Codex shell. |
| `DA-T003` resume launch-smoke repair | Human-authorized repair for pnpm 11 build approval and Tauri Windows icon requirement. | Closed by DA-T003-RESUME audit `PASS`; repair files exist under `apps/nullforge-desktop/`; process-level `tauri dev` launch evidence was accepted; no screenshot-level UI proof was captured. |
| `MB-T002` or next scoped implementation | Human-selected next step after WB-T001 closeout. | WB-T001 is closed with audit `PASS`; `MB-T002` is not started. |
| M0 milestone and ticket queue repo import | Potential future source import or handoff task. | Incoming-package-only; not created or started in DA-T002. |
