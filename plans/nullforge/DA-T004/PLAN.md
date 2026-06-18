# DA-T004 Plan

Ticket: `DA-T004 - Engine command bridge smoke`

Role: Planner only

Date: `2026-06-17`

## Goal

Plan the first bounded desktop bridge smoke after DA-T003-RESUME closeout.

DA-T004 should prove only that the existing local Tauri shell can invoke exactly one allowlisted, dev-only ResearchCore Engine smoke command through a structured bridge path and return a bounded result. This planner does not implement that behavior.

## Source Context Used

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`
- `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md`
- `audits/nullforge/DA-T003-RESUME/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003-RESUME/FINDINGS.md`
- `audits/nullforge/QA-T005/AUDIT_REPORT.md`
- `audits/nullforge/DA-T001/AUDIT_REPORT.md`
- `audits/nullforge/DA-T002/AUDIT_REPORT.md`

## Assumptions

- DA-T003-RESUME is closed with audit `PASS`.
- The existing app scaffold remains under `apps/nullforge-desktop/`.
- Process-level launch evidence was accepted for DA-T003-RESUME, but no screenshot-level UI proof was captured.
- DA-T001 bridge contract is the active bridge planning source.
- QA-T005 proves only `.venv-qa-t005` readiness for `python -m research_core.cli --help`.
- No structured `engine.version` or `engine.doctor` command is currently proven.

## Planned DA-T004 Scope

The future implementation should target exactly one first-proof command:

`engine.cli_help_smoke`

This command is temporary and dev-only. It may wrap the currently proven QA-T005 command shape:

```text
python -m research_core.cli --help
```

inside `.venv-qa-t005`, if the environment exists and the future human prompt explicitly authorizes this bridge smoke.

The future bridge request/response should be structured and bounded. The UI may expose one explicit action to run the smoke and display `OK`, `BLOCKED`, or `ERROR` with bounded output. It must not expose shell input, arbitrary command arguments, workspace selection, data import, fixture handling, or engine operation beyond the single help-smoke.

## Out Of Scope

Out of scope for this planner and for the future DA-T004 implementation unless a later prompt changes scope:

- structured `engine.version` or `engine.doctor` source/package implementation;
- ResearchCore Engine source changes;
- package metadata or CLI entrypoint changes outside the app-local bridge needs;
- sidecar packaging or sidecar launch;
- workspace selection or workspace file access;
- artifact metadata display;
- dataset import or fixture creation;
- raw/full ES.zip handling;
- tests beyond DA-T004's targeted checks;
- docs generation or docs build;
- CI;
- app scaffold expansion beyond the bridge smoke surface;
- public release, installer, signing, updater;
- cloud, external network, telemetry, auth, billing, mobile, marketplace;
- broker/live trading, live execution, AI/model calls, legal/trademark, or financial advice behavior.

## Planned Future Allowed Implementation Files

The future DA-T004 implementor may need a separate scoped prompt that allows only the minimum app-local files required for bridge smoke, such as:

- `apps/nullforge-desktop/package.json`
- `apps/nullforge-desktop/pnpm-lock.yaml`
- `apps/nullforge-desktop/src/App.tsx`
- `apps/nullforge-desktop/src/styles.css`
- `apps/nullforge-desktop/src-tauri/Cargo.toml`
- `apps/nullforge-desktop/src-tauri/Cargo.lock`
- `apps/nullforge-desktop/src-tauri/capabilities/default.json`
- `apps/nullforge-desktop/src-tauri/src/main.rs`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T004/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T004/CHANGED_FILES.md`
- `reports/nullforge/DA-T004/TEST_RESULTS.md`
- `reports/nullforge/DA-T004/AUDITOR_PROMPT.md`

This current planner creates none of those implementation/report/status files.

## Planned Bridge Design

Future implementation should:

1. Add an allowlisted bridge command with a stable command ID equivalent to `engine.cli_help_smoke`.
2. Use fixed arguments only: no raw shell string, no user-provided executable path, no user-provided arguments.
3. Resolve `.venv-qa-t005` from the repo-local development context only.
4. If the venv or CLI is unavailable, return `BLOCKED` with a bounded error and no install/repair attempt.
5. Run with a timeout.
6. Capture bounded stdout/stderr excerpts only.
7. Return a JSON-compatible bridge response with command ID, status, duration, exit code if a process ran, warnings, and errors.
8. Display the result in the app without implying production readiness or general engine integration.

## Security And Privacy Requirements

The future implementation must:

- keep arbitrary shell execution impossible;
- avoid `cmd.exe`, PowerShell, shell string composition, and user-controlled command fragments;
- avoid broad filesystem, shell plugin, fs plugin, network plugin, updater, telemetry, credential, or release permissions;
- keep process execution limited to the single allowlisted dev smoke;
- avoid scanning parent directories or user-selected folders;
- avoid writing workspace files;
- avoid raw/private data, ES.zip, generated datasets, and fixtures;
- keep logs/output bounded and non-sensitive.

## Future Required Checks

The future DA-T004 implementation should run and report:

- `git status --short --untracked-files=all`
- exact app-local install/build command if dependencies changed
- exact app-local frontend build command
- a targeted bridge smoke command or UI/dev-run evidence proving `engine.cli_help_smoke` returns `OK` or `BLOCKED` honestly
- `git diff --name-only`
- `git diff --check`
- a runtime-forbidden scan for broad shell/filesystem/network/plugins and unsupported command shapes
- a forbidden-path diff check for source/package/test/schema/fixture/generated-doc/CI/root package/root lockfile/docs-reference/tool changes unless explicitly allowed
- final `git status --short --untracked-files=all`

If the future implementation cannot safely run the bridge smoke, it must record `BLOCKED` or `HOLD` and must not claim bridge proof.

## Planner Checks For This Ticket

This planner should run:

- `git status --short --untracked-files=all`
- `git diff --check`
- `git diff --name-only`
- a forbidden-path diff check proving only `plans/nullforge/DA-T004/` files were added by this planner

## Human Gate Triggers

Stop for human direction if future implementation requires:

- choosing `engine.version` or `engine.doctor` instead of `engine.cli_help_smoke`;
- source/package changes to create a structured engine command;
- dependency additions not explicitly allowed in the future implementation prompt;
- Tauri permission broadening beyond one custom command;
- shell plugin, filesystem plugin, network plugin, updater, telemetry, credential, or release capability;
- workspace path selection or file mutation;
- environment repair or venv creation;
- sidecar packaging;
- raw/private data or fixture handling.

## Rollback And Repair Route

If audit finds DA-T004 too broad, repair must reduce scope back to one allowlisted bridge smoke or return to planning.

If `engine.cli_help_smoke` is rejected as too weak, repair should not force it through. It should route to a separate source/package ticket to create a structured `engine.version` or `engine.doctor` command before bridge implementation.

## Planner Verdict

Ready for future implementation prompt, with a human gate on the chosen first proof command.

This planner packet itself does not implement DA-T004.
