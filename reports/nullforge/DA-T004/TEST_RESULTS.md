# DA-T004 Test Results

Ticket: `DA-T004 - Engine command bridge smoke`

Date: `2026-06-17`

## Commands Run

### Initial Status

```text
git status --short --untracked-files=all
```

Result: `PASS`.

Observed the existing dirty worktree from prior DA-T003-RESUME closeout plus untracked DA-T004 planner artifacts before DA-T004 implementation began.

### App-Local Dependency Install

```text
pnpm --dir apps/nullforge-desktop add @tauri-apps/api@^2.0.0
```

Result: `PASS`.

Notes:

- Added `@tauri-apps/api 2.11.0` app-locally.
- Reused/resolved the existing app-local dependency graph.
- No root package, root lockfile, or root workspace file was created.

### Formatter

```text
cargo fmt --manifest-path apps\nullforge-desktop\src-tauri\Cargo.toml
```

Result: `SKIPPED_BLOCKED`.

Output:

```text
error: 'cargo-fmt.exe' is not installed for the toolchain 'stable-x86_64-pc-windows-msvc'.
help: run `rustup component add rustfmt` to install it
```

No Rust toolchain repair or component install was attempted.

### App-Local Frontend Build

```text
pnpm --dir apps/nullforge-desktop build
```

Result: `PASS`.

Relevant output:

```text
vite v7.3.5 building client environment for production...
31 modules transformed.
dist/index.html
dist/assets/index-5Mpmp8er.css
dist/assets/index-f7EPH73m.js
built in 448ms
tsc --noEmit && vite build
```

### App-Local Rust Compile Check

```text
cargo check --manifest-path apps\nullforge-desktop\src-tauri\Cargo.toml
```

First result: `TIMEOUT` after 124 seconds while compiling the Tauri graph.

Rerun result: `PASS`.

Relevant output:

```text
Compiling nullforge-desktop v0.0.0 (...\apps\nullforge-desktop\src-tauri)
Finished `dev` profile [unoptimized + debuginfo] target(s) in 2m 28s
```

Final rerun after report/status edits:

```text
Checking nullforge-desktop v0.0.0 (...\apps\nullforge-desktop\src-tauri)
Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.83s
```

### Fixed Engine Help-Smoke Target

```text
.venv-qa-t005\Scripts\python.exe -m research_core.cli --help
```

Result: `PASS`, exit code `0`.

Relevant output:

```text
Usage: python -m research_core.cli [OPTIONS] COMMAND [ARGS]...
Options
--help  Show this message and exit.
Commands
canon
psa
validate
registry
observe
bundle
experiment
project
doctor
verify
plan
dataset
lineage
runset
risk
baseline
ci
release
prune
pilot
```

This is the exact fixed command target wrapped by the DA-T004 `engine.cli_help_smoke` bridge command.

### Tauri Dev Launch Evidence

Command launched through a bounded PowerShell `Start-Process` wrapper:

```text
pnpm --dir apps/nullforge-desktop tauri dev
```

First launch attempt result: `INCONCLUSIVE`.

- The first attempt was stopped while Tauri was still compiling.
- It produced Vite readiness output but no `nullforge-desktop.exe` process evidence.

Second launch attempt result: `PASS` for process-level app launch evidence.

Observed:

```text
DA-T004_APP_PROCESS_QUERY_BEGIN
ProcessId Name
165420    nullforge-desktop.exe
DA-T004_APP_PROCESS_QUERY_END
```

Relevant stderr tail:

```text
Finished `dev` profile [unoptimized + debuginfo] target(s) in 38.48s
Running `target\debug\nullforge-desktop.exe`
```

Cleanup:

```text
DA-T004_REMAINING_APP_PROCESS_QUERY_BEGIN
DA-T004_REMAINING_APP_PROCESS_QUERY_END
```

No screenshot-level visual UI proof or button-click proof was captured.

### Dependency Evidence Scan

```text
rg -n "@tauri-apps/api|serde" apps\nullforge-desktop\package.json apps\nullforge-desktop\pnpm-lock.yaml apps\nullforge-desktop\src-tauri\Cargo.toml apps\nullforge-desktop\src-tauri\Cargo.lock
```

Result: `PASS`.

Relevant output:

```text
apps\nullforge-desktop\package.json:13:    "@tauri-apps/api": "^2.11.0",
apps\nullforge-desktop\pnpm-lock.yaml:11:      '@tauri-apps/api':
apps\nullforge-desktop\pnpm-lock.yaml:438:  '@tauri-apps/api@2.11.0':
apps\nullforge-desktop\src-tauri\Cargo.toml:13:serde = { version = "1", features = ["derive"] }
```

### Runtime-Forbidden Scan

```text
rg -n "run_engine_cli_help_smoke|Command::new|std::process|tauri_plugin_shell|tauri-plugin-shell|tauri_plugin_fs|tauri-plugin-fs|fetch\(|XMLHttpRequest|WebSocket|sidecar|workspace|engine\.version|engine\.doctor|python -m research_core|research-core" apps\nullforge-desktop\src-tauri\src\main.rs apps\nullforge-desktop\src\App.tsx apps\nullforge-desktop\src\styles.css apps\nullforge-desktop\src-tauri\Cargo.toml apps\nullforge-desktop\src-tauri\capabilities\default.json apps\nullforge-desktop\package.json
```

Result: `PASS_WITH_EXPECTED_HITS`.

Expected hits:

- `run_engine_cli_help_smoke` appears once as the command function and once in the invoke handler.
- `Command::new` appears once for the fixed `.venv-qa-t005` help command.
- `python -m research_core.cli --help` appears only in DA-T004 UI boundary text.
- `sidecar` and `workspace` appear only in UI boundary text stating they are not implemented.

No shell plugin, filesystem plugin, network API, unsupported `engine.version`, unsupported `engine.doctor`, `python -m research_core --help`, or `research-core --help` implementation hit was found.

An initial broad scan also included ignored Tauri-generated schemas under `apps/nullforge-desktop/src-tauri/gen/`; those hits were excluded from the source-scope scan and recorded only as ignored generated output.

### Final Hygiene

```text
git diff --name-only
```

Result: `PASS`.

Tracked diff output:

```text
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
```

Untracked DA-T004 app/report files are visible in `git status --short --untracked-files=all`, not in tracked diff output.

```text
git diff --check
```

Result: `PASS`, no output.

```text
git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml Cargo.toml Cargo.lock .github README.md docs\reference tools
```

Result: `PASS`, no output.

```text
rg -n "[ \t]$" apps\nullforge-desktop docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md reports\nullforge\DA-T004 plans\nullforge\DA-T004
```

Result: `PASS`, no trailing-whitespace hits.

```text
Test-Path -LiteralPath package.json
Test-Path -LiteralPath pnpm-lock.yaml
Test-Path -LiteralPath Cargo.toml
```

Result: all returned `False`.

```text
git status --ignored --short apps\nullforge-desktop\node_modules apps\nullforge-desktop\dist apps\nullforge-desktop\src-tauri\target apps\nullforge-desktop\src-tauri\gen
```

Result: `PASS_WITH_IGNORED_OUTPUTS`.

Ignored generated/local output present from DA-T004 install/build/check/dev commands:

```text
!! apps/nullforge-desktop/dist/
!! apps/nullforge-desktop/node_modules/
!! apps/nullforge-desktop/src-tauri/gen/
!! apps/nullforge-desktop/src-tauri/target/
```

These paths are app-local ignored outputs and were not staged.

```text
Get-CimInstance -Query "SELECT ProcessId,Name,ExecutablePath,CommandLine FROM Win32_Process WHERE Name = 'nullforge-desktop.exe'"
```

Result: `PASS`, no app process output.

Filtered DA-T004 dev-process query excluding the current PowerShell process:

```text
DA-T004_FINAL_FILTERED_DEV_PROCESS_QUERY_BEGIN
none
DA-T004_FINAL_FILTERED_DEV_PROCESS_QUERY_END
```

Result: `PASS`.

## Evidence Limits

- The exact fixed command target returned exit code `0`.
- The Rust command compiled and is registered with Tauri.
- The app launched far enough to observe `nullforge-desktop.exe`.
- No screenshot-level visual UI proof was captured.
- No button-click/UI invocation proof was captured.
- No sidecar, workspace, artifact, dataset, network, telemetry, updater, signing, public release, broker/live, AI/model, or financial advice behavior was tested or claimed.

## Test Verdict

Implementation checks support DA-T004 audit review.

The ticket is not closed. Independent audit is still required.
