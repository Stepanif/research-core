# DA-T004 Implementation Report

Ticket: `DA-T004 - Engine command bridge smoke`

Role: Scoped Implementor

Date: `2026-06-17`

Branch: `main`

## Summary

Implemented DA-T004 only.

DA-T004 adds exactly one temporary, dev-only bridge command to the existing app-local Tauri scaffold:

`engine.cli_help_smoke`

The command is registered as a single Tauri invoke handler, `run_engine_cli_help_smoke`, under `apps/nullforge-desktop/src-tauri/src/main.rs`. It uses only the fixed command shape authorized for this ticket:

```text
.venv-qa-t005\Scripts\python.exe -m research_core.cli --help
```

The command accepts no user-provided executable path, command string, command ID, workspace path, or arguments. It returns a JSON-compatible response with:

- `request_id`
- `bridge_version`
- `command_id`
- `status` as `OK`, `ERROR`, `TIMEOUT`, or `BLOCKED`
- `duration_ms`
- `exit_code`
- bounded `stdout_excerpt`
- bounded `stderr_excerpt`
- engine metadata
- empty artifacts
- warnings
- errors

If `.venv-qa-t005` or `research_core.cli` is unavailable, the command returns `BLOCKED` and does not install, repair, or mutate the environment.

The React UI now exposes one small `Run smoke` action and a bounded result surface for that command. It does not expose shell input, command input, workspace selection, file browsing, sidecar behavior, artifact metadata, data import, network behavior, telemetry, updater/signing/release behavior, broker/live behavior, AI/model behavior, or financial advice behavior.

## Files Changed

DA-T004 changed only the following existing app/status files and created this report folder:

- `apps/nullforge-desktop/package.json`
- `apps/nullforge-desktop/pnpm-lock.yaml`
- `apps/nullforge-desktop/src/App.tsx`
- `apps/nullforge-desktop/src/styles.css`
- `apps/nullforge-desktop/src-tauri/Cargo.toml`
- `apps/nullforge-desktop/src-tauri/Cargo.lock`
- `apps/nullforge-desktop/src-tauri/src/main.rs`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T004/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T004/CHANGED_FILES.md`
- `reports/nullforge/DA-T004/TEST_RESULTS.md`
- `reports/nullforge/DA-T004/AUDITOR_PROMPT.md`

The broader `apps/nullforge-desktop/`, DA-T003-RESUME plan/report/audit artifacts, and DA-T004 planner artifacts were already untracked in the worktree before DA-T004 implementation began.

## Dependency Changes

App-local only:

- Added `@tauri-apps/api` to `apps/nullforge-desktop/package.json` and `apps/nullforge-desktop/pnpm-lock.yaml` so the React UI can call the single Tauri command through `invoke`.
- Added `serde` to `apps/nullforge-desktop/src-tauri/Cargo.toml` and app-local `Cargo.lock` so the Rust bridge response can serialize as a structured JSON-compatible object.

No root `package.json`, root `pnpm-lock.yaml`, root `pnpm-workspace.yaml`, root `Cargo.toml`, or root `Cargo.lock` was created or modified.

## Implementation Details

Rust bridge:

- Registers exactly one Tauri command handler: `run_engine_cli_help_smoke`.
- Uses `Command::new` once, with a repo-local fixed Python executable path and fixed arguments only.
- Resolves the dev-only `.venv-qa-t005` path from the app-local compile context, not from user input.
- Uses `stdin(Stdio::null())`, piped stdout/stderr, a 5 second timeout, and bounded 2,000-character excerpts.
- Returns `BLOCKED` if the venv, process start, or `research_core.cli` availability is missing.
- Returns `TIMEOUT` and kills the child process if the command exceeds the timeout.
- Returns `ERROR` for other nonzero fixed-command failures.

Frontend:

- Imports only `invoke` from `@tauri-apps/api/core`.
- Calls exactly `run_engine_cli_help_smoke` with no payload.
- Displays status, duration, exit code, bridge version, bounded stdout/stderr excerpts, warnings, and errors.
- Keeps boundary text explicit that this is not general bridge, sidecar, workspace, artifact, dataset, network, telemetry, release, broker/live, AI/model, or financial advice functionality.

## Evidence

Exact fixed command target:

```text
.venv-qa-t005\Scripts\python.exe -m research_core.cli --help
```

Result: `PASS`, exit code `0`.

Observed output included:

```text
Usage: python -m research_core.cli [OPTIONS] COMMAND [ARGS]...
```

App-local frontend build:

```text
pnpm --dir apps/nullforge-desktop build
```

Result: `PASS`.

App-local Rust compile check:

```text
cargo check --manifest-path apps\nullforge-desktop\src-tauri\Cargo.toml
```

Result: `PASS` on the longer rerun after the first compile attempt timed out while building the Tauri graph.

Tauri dev launch:

```text
pnpm --dir apps/nullforge-desktop tauri dev
```

Result: process-level launch evidence observed. `nullforge-desktop.exe` was observed running with PID `165420`, then DA-T004 cleanup stopped the app/dev processes. No screenshot-level visual UI proof or button-click proof was captured.

## Acceptance Status

Implemented:

- Exactly one bridge command: `engine.cli_help_smoke`.
- Fixed executable and arguments only.
- No user-provided executable path, command string, command ID, workspace path, or arguments.
- Structured JSON-compatible response.
- Timeout.
- Bounded stdout/stderr excerpts.
- `BLOCKED` path for missing `.venv-qa-t005` or missing `research_core.cli`.
- Smallest UI surface for one trigger and bounded result display.
- App-local dependency changes only.
- DA-T003-RESUME audit `PASS`, process-level launch evidence, and no-screenshot boundary preserved.

Not implemented:

- general bridge support;
- `engine.version`;
- `engine.doctor`;
- sidecar behavior;
- workspace selection, scanning, reads, or writes;
- artifact metadata behavior;
- dataset or fixture behavior;
- cloud/network behavior beyond local Vite/Tauri dev-server loopback;
- telemetry, updater, signing, installer, public release;
- broker/live, live execution, AI/model, legal/trademark, or financial advice behavior.

## Deviations And Limits

- `cargo fmt --manifest-path apps\nullforge-desktop\src-tauri\Cargo.toml` could not run because `cargo-fmt.exe` is not installed for the local stable Rust toolchain. No install or repair was attempted.
- Runtime UI button-click proof was not captured. Evidence is limited to the exact fixed command target returning exit code `0`, Rust compile check, frontend build, and process-level Tauri launch evidence.
- No screenshot-level visual UI proof was captured.

## Human Gate Status

Resolved by latest human prompt:

- Use of `engine.cli_help_smoke` as the temporary dev-only first bridge proof.

No unresolved DA-T004 implementation gate was used to expand scope.

## Next Recommended Action

Run the independent DA-T004 audit.

Do not start `WB-T001`, `MB-T002`, sidecar work, workspace work, artifact metadata work, structured engine command work, public release work, broker/live work, AI/model work, or financial advice work from this implementation report.
