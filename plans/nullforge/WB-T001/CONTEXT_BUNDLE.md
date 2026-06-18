# WB-T001 Context Bundle

Ticket: `WB-T001 - Artifact metadata read-only viewer`

Role: Context Curator

Date: `2026-06-18`

## Ticket Summary

WB-T001 is the next scoped M1 work after DA-T004 audit `PASS`. Its purpose is to add a read-only artifact metadata display surface to the existing NullForge desktop bridge-smoke UI without creating artifacts, scanning a workspace, adding bridge commands, or changing ResearchCore Engine behavior.

DA-T004 currently returns a structured bridge response with an `artifacts` field. In the implemented DA-T004 bridge this field is an app-local serialized `Vec<String>` and is currently empty for the temporary `engine.cli_help_smoke` command. WB-T001 can only display that returned metadata honestly, including an empty state.

## Mission Slice

Add a small read-only viewer for bridge-returned artifact metadata:

```text
Run engine.cli_help_smoke -> receive structured bridge response -> show artifact metadata count/list read-only -> explicitly show empty state when no artifacts are returned
```

## Active Source Docs

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`
- `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md`
- `audits/nullforge/DA-T004/AUDIT_REPORT.md`
- `audits/nullforge/DA-T004/FINDINGS.md`
- `reports/nullforge/DA-T004/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T004/TEST_RESULTS.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md`

## Relevant Repo Files

- `apps/nullforge-desktop/src/App.tsx`
- `apps/nullforge-desktop/src/styles.css`
- `apps/nullforge-desktop/src-tauri/src/main.rs`
- `apps/nullforge-desktop/src-tauri/capabilities/default.json`
- `apps/nullforge-desktop/package.json`
- `apps/nullforge-desktop/src-tauri/Cargo.toml`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`

## Current Repo State

- DA-T004 is closed with audit `PASS`.
- DA-T004 implemented exactly one temporary dev-only bridge command, `engine.cli_help_smoke`.
- DA-T004 response includes `artifacts`, currently an empty string array.
- DA-T004 did not capture screenshot-level visual UI proof or button-click proof.
- App-local generated outputs may exist as ignored paths under `apps/nullforge-desktop/`.
- The worktree already contains untracked app, plan, report, and audit artifacts from DA-T003-RESUME and DA-T004.

## Constraints

- Do not add new bridge commands.
- Do not change Rust process execution.
- Do not scan workspace paths.
- Do not read or write artifacts.
- Do not create fixture, dataset, raw/private, or generated data.
- Do not add dependencies.
- Do not add Tauri permissions or plugins.
- Do not claim DA-T004 produced artifacts; show an honest empty state if the returned list is empty.

## Forbidden Actions

- Sidecar behavior.
- Workspace selection, scanning, reads, or writes.
- Artifact scanning or filesystem access.
- ResearchCore Engine source/package changes.
- Data import, fixture creation, ES.zip handling, generated datasets.
- Network/cloud/telemetry/updater/signing/public release scope.
- Broker/live trading, AI/model, legal/trademark, or financial advice behavior.
- Starting `MB-T002` or M2 work.

## Required Checks

- `git status --short --untracked-files=all`
- `pnpm --dir apps/nullforge-desktop build`
- `git diff --name-only`
- `git diff --check`
- targeted scans for forbidden command/plugin/workspace/data/network/release scope
- forbidden tracked-path diff check for non-scoped engine/source/test/schema/fixture/generated-doc/CI/root package/root lockfile/docs-reference/tool changes

## Human Gate Triggers

Human review is required if WB-T001 needs any of:

- new dependencies;
- new Tauri plugins or permissions;
- a new bridge command;
- filesystem/workspace access;
- artifact scanning;
- artifact creation or mutation;
- ResearchCore Engine source/package change;
- data/fixture handling;
- network, telemetry, updater, release, broker/live, AI/model, or financial-advice scope.

## Prior Related Tickets

- `DA-T003-RESUME`: launch-only Tauri scaffold; audit `PASS`.
- `DA-T004`: one temporary dev-only bridge smoke; audit `PASS`.
- `DA-T001`: bridge contract source; audit `PASS`.
- `DA-T002`: Tauri scaffold plan source; audit `PASS`.
- `QA-T005`: isolated `.venv-qa-t005` readiness proof only; audit `PASS`.

## Excluded Context

- Full source text of all imported volumes.
- Raw/full ES.zip or private/local data.
- Incoming package milestone/ticket/prompt files.
- M2+ dataset, DCM, Logic Factory, Visual Replay, and Evidence Card details beyond high-level sequence.

## Open Questions

- None blocking. The only honest WB-T001 artifact metadata source after DA-T004 is the returned `artifacts` field, currently empty.

## Curator Verdict

Ready for planner: YES.
