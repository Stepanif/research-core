# ADR-T002 Context Bundle Manifest

Pack name: NullForge M0 ADR-T002 context bundle
Ticket: `ADR-T002` - Local-first/no-cloud MVP ADR
Purpose: Provide bounded active context for the ADR-T002 Planner without creating the ADR, implementation reports, audit files, downstream docs, code, or data fixtures.
Date: `2026-06-16`

## Included Files

| File | Truth status | Why included |
|---|---|---|
| `docs/nullforge/CURRENT_STATUS.md` | Active NullForge status after ADR-T001 closeout | Confirms ADR-T001 PASS/closeout, no implementation code, ADR-T002 as next action, and gated cloud/auth/billing/mobile/broker/data/app scope. |
| `docs/nullforge/SOURCE_INDEX.md` | Active NullForge source index after ADR-T001 closeout | Identifies active docs, ADR-T001 artifacts, imported volumes, pending downstream ADR-T002/CX-T001/MB-T001, external input handling, prompt policy, archive, and quarantine posture. |
| `docs/nullforge/DECISION_LEDGER.md` | Active decision ledger | Contains accepted `NF-D0004` and pending `NF-D0005`, the local-first/no-cloud MVP boundary decision owned by ADR-T002. |
| `docs/nullforge/ARCHIVE_POLICY.md` | Active archive/source policy | Governs active docs, design memory, archive, quarantine, prompts, and source promotion rules. |
| `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` | Accepted ADR-T001 decision record | Establishes working name, first platform, desktop stack direction, ResearchCore Engine boundary, and explicitly leaves ADR-T002 undecided. |
| `audits/nullforge/ADR-T001/AUDIT_REPORT.md` | ADR-T001 audit disposition | Confirms `Decision: PASS` and that ADR-T002 is ready after ADR-T001 closeout. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md` | Repo-managed imported planning/workflow source | Provides local-first doctrine, MVP cutline, anti-goals, data posture, no-cloud/no-auth/no-billing/no-broker boundaries, claim and reversal language. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md` | Repo-managed imported planning/workflow source | Provides desktop/local workspace, filesystem, no network/cloud/broker/telemetry defaults, sidecar/bridge permission gates, ES.zip boundary, and Tauri permission context. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` | Repo-managed imported planning/workflow source | Confirms M0 sequence, ADR-T002 role, downstream CX-T001/MB-T001 ordering, and roadmap anti-patterns. |

## Source Excerpts Included In Bundle

The context bundle summarizes only the ADR-T002-relevant parts of the included files:

- local-first MVP stance;
- one selected local workspace;
- local data/artifacts/logs/evidence posture;
- full ES.zip/raw/private data exclusion;
- license-safe fixture gate;
- no cloud sync/storage/SaaS/auth/accounts/billing/mobile/marketplace/telemetry/broker/live/public release;
- no implementation code or downstream ticket start;
- human gate triggers.

## Excluded Context

| Excluded source | Reason |
|---|---|
| Full text of all Volume 00/03/07 files in the context bundle | The bundle should remain concise; the repo-local source files remain available for direct implementor/auditor reads. |
| Volume 01/02/04/05/06 full files | Useful for later tickets but not required to plan the local-first/no-cloud ADR beyond source/quarantine and downstream gates already captured in active docs. |
| External zip packages | PF-T001 imported selected repo-local volume files and PF-T001 audit accepted them. |
| Incoming milestone/ticket/prompt package files | Current repo-local source docs are sufficient for ADR-T002 planning; incoming package paths remain external inputs until a scoped import promotes them. |
| Old chats and prompt files | Not active truth unless promoted by a scoped audited ticket. |
| `README.md`, `docs/STATUS.md`, `docs/index.md`, `docs/ARCHITECTURE.md`, `src/`, `tests/`, `schemas/`, `configs/`, `tools/`, package files, CI files | ADR-T002 is docs/source-of-truth only and must not modify implementation or ResearchCore Engine surfaces. |
| Raw/full ES.zip, private/local data, generated datasets, ES-derived fixtures | Explicitly gated and out of ADR-T002 planner scope. |

## Path Checks Before Planner Work

Commands/checks run before planner files were created:

```text
git status --short --branch
git status --short --untracked-files=all
rg -n "Decision: PASS" audits\nullforge\ADR-T001\AUDIT_REPORT.md
Test-Path -Path docs\nullforge\adr\ADR-T002*
```

Results:

```text
git status --short --branch -> ## docs/ADR-T001-nullforge-name-platform-stack-engine
git status --short --untracked-files=all -> no output
rg -n "Decision: PASS" audits\nullforge\ADR-T001\AUDIT_REPORT.md -> 5:Decision: PASS
Test-Path -Path docs\nullforge\adr\ADR-T002* -> False
```

Note: the first sandboxed wildcard `Test-Path` run failed because the Windows sandbox helper could not launch. The same read-only check was rerun with escalation and returned `False`.

## Truth Status Summary

- Existing ResearchCore Engine docs/code remain authoritative for current engine behavior.
- PF-T000, PF-T001, PF-T002, and ADR-T001 outputs with PASS audits are dependency context for ADR-T002.
- Imported Volume 00/03/07 files are active NullForge planning/workflow source, not implementation truth.
- ADR-T002 planner files are temporary role-loop artifacts, not the ADR decision itself.
- ADR-T002 decision becomes active only after implementor output and independent audit disposition.

## Expiry

Refresh this context if any of the following occur before ADR-T002 implementation:

- current branch changes or this branch is rebased/merged;
- working tree changes outside `plans/nullforge/ADR-T002/`;
- `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md` appears;
- `docs/nullforge/CURRENT_STATUS.md`, `SOURCE_INDEX.md`, `DECISION_LEDGER.md`, or `ARCHIVE_POLICY.md` changes;
- ADR-T001 audit disposition changes;
- a human gate is triggered;
- incoming M0 ticket/milestone files are imported into repo-local canonical paths.

## Refresh Rule

Refresh context before implementor work if:

- `git status --short --branch` is dirty beyond `plans/nullforge/ADR-T002/`;
- repo-local ADR-T002 ticket/milestone/prompt paths appear;
- ADR-T002 output/report/audit paths already exist;
- required sources move or are edited;
- exact line-level wording from additional volumes becomes necessary.

## Human Gate Triggers

Human review is required before overwriting ResearchCore Engine docs, changing repo/package/CLI/public identity, creating code/dependencies/schemas/tests/CI/generated docs/data fixtures, importing raw/private/ES-derived data, enabling cloud/auth/billing/mobile/broker/live/telemetry/public release scope, or promoting old prompts/chats/external inputs as active truth.

Planner-detected human gates: none.
