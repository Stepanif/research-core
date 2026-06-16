# CX-T001 Context Bundle Manifest

Pack name: NullForge M0 CX-T001 context bundle
Ticket: `CX-T001` - NullForge Codex role-loop docs
Purpose: Provide bounded active context for the CX-T001 Planner without creating implementation docs, reports, audits, code, data, tickets, milestones, or prompt archives.
Date: `2026-06-16`

## Included Files

| File | Truth status | Why included |
|---|---|---|
| `docs/nullforge/CURRENT_STATUS.md` | Active NullForge status after ADR-T002 audit `PASS` closeout wording | Confirms phase, no-code sentence, ADR-T002 PASS, CX-T001 as next scoped ticket, MB-T001 pending, and gated implementation/data/cloud/broker/release scope. |
| `docs/nullforge/SOURCE_INDEX.md` | Active NullForge source index after ADR-T002 audit `PASS` closeout wording | Identifies active docs, ADR-T001/ADR-T002 artifacts, incoming input boundaries, prompt policy, and CX-T001/MB-T001 downstream status. |
| `docs/nullforge/DECISION_LEDGER.md` | Active decision ledger | Confirms accepted ADR-T001 and ADR-T002 decisions, pending source import, and the rule that accepted decisions do not authorize implementation code. |
| `docs/nullforge/ARCHIVE_POLICY.md` | Active archive/source policy | Governs active docs, design memory, archive, quarantine, prompts, and source promotion rules. |
| `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` | Accepted ADR-T001 decision record | Establishes working name, first platform, desktop stack direction, and ResearchCore Engine boundary that CX-T001 must preserve. |
| `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md` | Accepted ADR-T002 decision record | Establishes local-first/no-cloud MVP boundary and the scope gates CX-T001 must preserve. |
| `audits/nullforge/ADR-T002/AUDIT_REPORT.md` | ADR-T002 audit disposition | Confirms `Decision: PASS`, no CX-T001 work was started during ADR-T002, and CX-T001 is ready after ADR-T002 closeout. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md` | Repo-managed imported planning/workflow source | Primary source for role-loop responsibilities, artifact tree, templates, PASS/HOLD/REJECT rules, human gates, and stop conditions. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` | Repo-managed imported planning/workflow source | Confirms M0 sequence, CX-T001 purpose, M0 non-goals, milestone batching policy, and later QA/M1 ordering. |

## Source Excerpts Included In Bundle

The context bundle summarizes only the CX-T001-relevant parts of the included files:

- current status and dependency state;
- active source/truth boundaries;
- ADR-T001 working name/platform/stack/engine boundary;
- ADR-T002 local-first/no-cloud boundary;
- Volume 02 role-loop requirements;
- Volume 07 M0 ordering and CX-T001 purpose;
- human gate and stop-condition triggers;
- forbidden implementation, data, cloud, broker/live, AI, release, and downstream work.

## Excluded Sources

| Excluded source | Why excluded |
|---|---|
| Full text of Volume 00/01/03/04/05/06 | Useful design memory, but not required to plan the Codex role-loop docs beyond boundaries already captured by active status docs, ADRs, Volume 02, and Volume 07. |
| Existing ResearchCore Engine source files and implementation docs | CX-T001 is docs-only workflow planning and must not modify engine behavior or engine truth. |
| `README.md`, `docs/STATUS.md`, `docs/index.md`, `docs/ARCHITECTURE.md`, `docs/reference/`, `src/`, `tests/`, `schemas/`, `configs/`, `tools/`, package files, CI files | Forbidden implementation/engine surfaces for this ticket. |
| External zip packages | PF-T001 imported selected volume files and PF-T001 audit accepted them as repo-local planning/workflow source. |
| Incoming package milestone, ticket, and prompt files | Current active docs keep these as external inputs until a later scoped import promotes them. |
| Old chats and prompt files | Not active truth unless promoted by a scoped audited ticket. |
| `docs/nullforge/codex/` | Implementation output directory for CX-T001, not a planner input. |
| `reports/nullforge/CX-T001/` and `audits/nullforge/CX-T001/` | Reports/audits must not be created during planner-only work. |
| `tickets/nullforge/`, `milestones/nullforge/`, `prompts/nullforge/` | Explicitly out of planner scope and out of CX-T001 implementation scope unless a later scoped ticket imports them. |
| Raw/full ES.zip, private/local data, generated datasets, ES-derived fixtures | Explicitly gated and out of CX-T001 scope. |

## Path Checks Before Planner Work

Commands/checks run before planner files were created:

```text
git status --short --branch
```

Result:

```text
## docs/ADR-T001-nullforge-name-platform-stack-engine
 M docs/nullforge/CURRENT_STATUS.md
 M docs/nullforge/DECISION_LEDGER.md
 M docs/nullforge/SOURCE_INDEX.md
?? audits/nullforge/ADR-T002/
?? docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
?? plans/nullforge/ADR-T002/
?? reports/nullforge/ADR-T002/
```

Interpretation: ADR-T002 audit `PASS` exists, but ADR-T002 closeout is not yet committed. CX-T001 planner-only work is allowed by the human prompt. CX-T001 implementation should not start until ADR-T002 branch closeout or explicit human approval.

## Truth Status Summary

- Existing ResearchCore Engine docs/code remain authoritative for current engine behavior.
- PF-T000, PF-T001, PF-T002, ADR-T001, and ADR-T002 are dependency context with audit `PASS`.
- Imported Volume 02 and Volume 07 are active NullForge planning/workflow source, not implementation truth.
- CX-T001 planner artifacts are role-loop planning artifacts, not implementation docs.
- CX-T001 docs become active only after implementor output and independent audit disposition.

## Expiry

Refresh this context if any of the following occur before CX-T001 implementation:

- ADR-T002 closeout changes, is repaired, or is not committed as expected;
- current branch changes, is rebased, or is merged;
- working tree changes outside ADR-T002 closeout files and `plans/nullforge/CX-T001/`;
- `docs/nullforge/CURRENT_STATUS.md`, `SOURCE_INDEX.md`, `DECISION_LEDGER.md`, or `ARCHIVE_POLICY.md` changes;
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md` appears before implementation;
- `reports/nullforge/CX-T001/`, `audits/nullforge/CX-T001/`, `tickets/nullforge/`, `milestones/nullforge/`, or `prompts/nullforge/` appear;
- a human gate is triggered;
- incoming M0 ticket/milestone/prompt files are imported into repo-local canonical paths.

## Refresh Rule

Refresh context before implementor work if:

- `git status --short --branch` is dirty beyond expected CX-T001 planner artifacts;
- ADR-T002 audit `PASS` is missing or changed;
- required source files move or are edited;
- human approval changes the scope;
- exact line-level wording from additional volumes becomes necessary.

## Context Risks

- Current dirty tree can blur ADR-T002 closeout and CX-T001 implementation. Mitigation: planner files may exist, but implementor should wait for ADR-T002 branch closeout or explicit human approval.
- Role-loop docs can accidentally become a broad permission slip. Mitigation: require explicit forbidden actions, human gates, audit rules, and no implementation proof language.
- Prompt material can be mistaken for active truth. Mitigation: preserve archive policy and state prompts are workflow instructions unless promoted by audited docs.
- CX-T001 can drift into milestone/ticket/prompt import. Mitigation: keep tickets, milestones, and prompts out of scope.

## Human Gate Triggers

Human review is required before overwriting ResearchCore Engine docs, changing repo/package/CLI/public identity, creating code/dependencies/schemas/tests/CI/generated docs/data fixtures, importing raw/private/ES-derived data, enabling cloud/auth/billing/mobile/broker/live/telemetry/AI/public release scope, creating downstream milestone/ticket/prompt artifacts, or promoting old prompts/chats/external inputs as active truth.

Planner-detected human gates: none.

## Curator Verdict

READY_FOR_PLANNER.

Immediate implementation verdict: BLOCKED_UNTIL_ADR_T002_BRANCH_CLOSEOUT_OR_HUMAN_APPROVAL.
