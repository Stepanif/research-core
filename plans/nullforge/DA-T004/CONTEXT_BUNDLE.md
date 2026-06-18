# DA-T004 Context Bundle

Ticket: `DA-T004 - Engine command bridge smoke`

Role: Context Curator + Planner only

Date: `2026-06-17`

## Mission Slice

Prepare the bounded context for the next M1 ticket after DA-T003-RESUME closeout.

The current source docs identify `DA-T004` as the next scoped M1 bridge proof candidate before `WB-T001` and `MB-T002`. DA-T004 should be planned as the first desktop bridge smoke ticket, but this context/planning packet does not implement any app, bridge, sidecar, engine, dependency, runtime, workspace, data, cloud/network, telemetry, release, broker/live, AI/model, or financial-advice behavior.

## Ticket Identity

Final next ticket identified from current sources:

`DA-T004 - Engine command bridge smoke`

Basis:

- `docs/nullforge/CURRENT_STATUS.md` says DA-T003-RESUME is closed with audit `PASS` and downstream `DA-T004`, `WB-T001`, and `MB-T002` remain blocked until separately authorized.
- `docs/nullforge/SOURCE_INDEX.md` lists `DA-T004`, `WB-T001`, and `MB-T002` as pending downstream work after separate human direction.
- `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md` states bridge command smoke belongs to DA-T004 or a later scoped ticket after the shell exists and is audited.
- `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md` names DA-T004 as the first-proof command selection point.
- Volume 07 design memory labels `DA-T004` as `Engine command bridge smoke`, followed by `WB-T001` and `MB-T002`. Design memory informs sequence but does not override active source docs.

## Current State

DA-T003-RESUME is closed with audit `PASS`.

Proven by DA-T003-RESUME:

- A minimal launch-only Tauri/React/TypeScript/Vite shell scaffold exists under `apps/nullforge-desktop/`.
- App-local install/build passed.
- App-local pnpm and icon repairs were added.
- Process-level `nullforge-desktop.exe` launch evidence was accepted by independent audit.
- No screenshot-level visual UI proof was captured.

Not proven by DA-T003-RESUME:

- bridge command behavior;
- sidecar behavior;
- ResearchCore Engine behavior;
- workspace behavior;
- artifact metadata behavior;
- dataset or fixture behavior;
- tests, docs build, CI, installer behavior, or public release readiness.

## Active Source Docs

Primary:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`
- `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md`

Audit authority:

- `audits/nullforge/DA-T003-RESUME/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003-RESUME/FINDINGS.md`
- `audits/nullforge/QA-T005/AUDIT_REPORT.md`
- `audits/nullforge/DA-T001/AUDIT_REPORT.md`
- `audits/nullforge/DA-T002/AUDIT_REPORT.md`

Supporting design memory:

- `docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md`

Design memory is not implementation authority. It only helps explain why DA-T004 is the next planned sequence item.

## Relevant Repo Files And Folders

Existing launch-only app scaffold:

- `apps/nullforge-desktop/package.json`
- `apps/nullforge-desktop/pnpm-lock.yaml`
- `apps/nullforge-desktop/pnpm-workspace.yaml`
- `apps/nullforge-desktop/src/App.tsx`
- `apps/nullforge-desktop/src/main.tsx`
- `apps/nullforge-desktop/src/styles.css`
- `apps/nullforge-desktop/vite.config.ts`
- `apps/nullforge-desktop/src-tauri/Cargo.toml`
- `apps/nullforge-desktop/src-tauri/Cargo.lock`
- `apps/nullforge-desktop/src-tauri/capabilities/default.json`
- `apps/nullforge-desktop/src-tauri/src/main.rs`

Existing engine boundary:

- `src/research_core/cli.py`
- `pyproject.toml`
- `.venv-qa-t005/` if present locally, ignored and not a source artifact

The current planner does not read, modify, or execute app or engine files beyond source-context review already required by current docs.

## Proof Boundaries To Preserve

QA-T005 proves only:

- `research-core` can be installed editable into `.venv-qa-t005`;
- `research_core` and `research_core.cli` are import-visible inside `.venv-qa-t005`;
- `python -m research_core.cli --help` runs inside `.venv-qa-t005`.

Unsupported unless a later source/package ticket changes them:

- `python -m research_core --help`
- `research-core --help`

DA-T001 proves only a docs-only bridge contract. It does not prove bridge implementation.

DA-T002 proves only a docs-only Tauri scaffold plan. It does not prove app runtime.

DA-T003-RESUME proves only a bounded launch-only shell scaffold with accepted process-level launch evidence. It does not prove bridge or engine behavior.

## DA-T004 Proposed First Proof

The only currently proven engine-adjacent command shape is:

```text
python -m research_core.cli --help
```

inside `.venv-qa-t005`.

The DA-T001 bridge contract marks `engine.cli_help_smoke` as an optional DA-T004 candidate and explicitly notes that it requires later human approval because CLI help is not structured engine output.

This planner therefore proposes a future DA-T004 implementation around exactly one dev-only allowlisted command:

`engine.cli_help_smoke`

DA-T004 implementation should use that command only if the human starts the implementation with explicit approval for this temporary dev smoke. If the human wants a structured `engine.version` or `engine.doctor` command first, DA-T004 must stop and route to a separate source/package or bridge-contract update ticket before implementation.

## Future DA-T004 Implementation Boundary

The future DA-T004 implementation, if explicitly authorized, should:

- add one allowlisted Tauri command for `engine.cli_help_smoke`;
- execute only a fixed command shape with no user-provided shell string or arguments;
- use `.venv-qa-t005` only as the known QA-T005 readiness environment, if present;
- return a bounded structured response to the UI;
- display a small local-only bridge smoke result in the existing launch-only shell;
- record exact pass/fail/blocked evidence in DA-T004 reports.

It must not:

- add arbitrary shell execution;
- add a general process runner;
- add unbounded filesystem access;
- add cloud, external network, telemetry, auth, billing, updater, signing, public release, broker/live, AI/model, or financial advice behavior;
- mutate workspace files;
- import data or fixtures;
- package a sidecar;
- change ResearchCore Engine source or package metadata.

## Human Gates

Human approval is required before future DA-T004 implementation:

- uses `engine.cli_help_smoke` as the first proof command;
- adds any app-local dependency;
- broadens Tauri permissions;
- invokes `.venv-qa-t005`;
- invokes any ResearchCore Engine command;
- changes ResearchCore Engine source/package behavior;
- handles workspace paths, files, data, fixtures, or raw/private material.

If a future DA-T004 implementor discovers that a structured `engine.version` or `engine.doctor` source command is needed before bridge proof, it must stop and report a blocker rather than inventing one inside DA-T004.

## Required Checks For This Planner

This planner should run:

- `git status --short --untracked-files=all`
- `git diff --check`
- a forbidden-path diff check proving only `plans/nullforge/DA-T004/` files were added by this planner

No Node, pnpm, Rust, Tauri, Python, bridge, sidecar, engine, test, docs build, quickstart, CI, or runtime command should be run by this planner.

## Excluded Context

Excluded from active context:

- raw/full ES.zip;
- private/local data;
- old chats;
- standalone prompt packs;
- incoming ticket/milestone package files not promoted to active repo-local truth;
- any external network or package registry state;
- unreviewed archive/quarantine material.

## Open Questions For Future Implementation

- Should the human explicitly approve `engine.cli_help_smoke` as the temporary dev-only first proof, or require a structured source/package command first?
- If `.venv-qa-t005` is absent locally, should DA-T004 stop as blocked or should a new environment-readiness ticket prepare a DA-scoped venv?
- What exact Tauri permission entry is required for one custom command without filesystem, shell plugin, or network permissions?
- Should a later ticket replace `engine.cli_help_smoke` with `engine.version` or `engine.doctor` after source support exists?

## Curator Verdict

Ready for planner.

The next ticket is `DA-T004 - Engine command bridge smoke`. The current packet is context/planning only and does not authorize implementation in this turn.
