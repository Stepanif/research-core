# WB-T001 Context Bundle Manifest

Ticket: `WB-T001 - Artifact metadata read-only viewer`

Role: Context Curator

Date: `2026-06-18`

## Included Sources

| Source | Reason |
|---|---|
| `docs/nullforge/CURRENT_STATUS.md` | Current DA-T004 closeout state and next action. |
| `docs/nullforge/SOURCE_INDEX.md` | Active source navigation and DA-T004 audit links. |
| `docs/nullforge/codex/CODEX_ROLE_LOOP.md` | Required role-loop artifacts and stop conditions. |
| `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md` | Bridge response shape and artifact metadata boundary. |
| `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md` | Scaffold and excluded-scope boundaries. |
| `audits/nullforge/DA-T004/AUDIT_REPORT.md` | DA-T004 audit authority and evidence limits. |
| `audits/nullforge/DA-T004/FINDINGS.md` | DA-T004 non-blocking observation and no blocking findings. |
| `reports/nullforge/DA-T004/IMPLEMENTATION_REPORT.md` | DA-T004 implemented response shape and app files. |
| `reports/nullforge/DA-T004/TEST_RESULTS.md` | DA-T004 checks and cleanup evidence. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` | Backlog sequence: WB-T001 after DA-T004, before MB-T002. |

## Excluded Sources

| Source | Reason |
|---|---|
| Raw/full ES.zip and private/local data | Forbidden; not needed. |
| Incoming package ticket/milestone/prompt files | Not active truth for WB-T001. |
| M2+ detailed docs | Not required for the read-only DA-T004 artifact field display. |
| ResearchCore Engine internals | WB-T001 must not change engine behavior. |

## Relevant Implementation Files

| Path | Reason |
|---|---|
| `apps/nullforge-desktop/src/App.tsx` | Existing DA-T004 bridge-smoke UI and response type. |
| `apps/nullforge-desktop/src/styles.css` | Existing DA-T004 UI styling. |
| `apps/nullforge-desktop/src-tauri/src/main.rs` | Source of bridge response fields; should not change unless planner authorizes. |
| `apps/nullforge-desktop/src-tauri/capabilities/default.json` | Permission boundary; should remain empty. |
| `apps/nullforge-desktop/package.json` | App-local scripts and dependencies; no new dependency expected. |
| `apps/nullforge-desktop/src-tauri/Cargo.toml` | App-local Rust dependencies; no new dependency expected. |

## Context Risks

- DA-T004 returns `artifacts: []`; WB-T001 must not invent artifact metadata.
- A "viewer" could drift into workspace scanning; this is forbidden.
- UI text must not imply artifact production, workspace support, or engine readiness.

## Refresh Rule

Refresh this context if DA-T004 audit disposition changes, if app response shape changes, or if a human authorizes a different WB-T001 goal.

## Curator Verdict

The context is sufficient for a bounded WB-T001 planner.
