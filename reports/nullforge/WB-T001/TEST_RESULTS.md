# WB-T001 Test Results

Ticket: `WB-T001 - Artifact metadata read-only viewer`

Date: `2026-06-18`

## Commands Run

### Initial Status

```text
git status --short --untracked-files=all
```

Result: `PASS`.

Observed existing dirty worktree from DA-T003-RESUME/DA-T004 plus new WB-T001 planner artifacts.

### App-Local Frontend Build

```text
pnpm --dir apps/nullforge-desktop build
```

Initial sandboxed result: `BLOCKED_BY_SANDBOX`.

The sandboxed command failed with:

```text
CreateProcessWithLogonW failed: 2
```

Approved outside-sandbox rerun result: `PASS`.

Relevant output:

```text
31 modules transformed.
dist/index.html
dist/assets/index-BA_hwO9W.css
dist/assets/index-rVqoIxIm.js
built in 521ms
```

### Diff Hygiene

```text
git diff --check
```

Result: `PASS`, no output.

```text
git diff --name-only
```

Result: `PASS`.

Tracked diff output:

```text
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
```

App files and WB-T001 artifacts are untracked and visible in `git status --short --untracked-files=all`.

### Forbidden Tracked-Path Diff

```text
git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml Cargo.toml Cargo.lock .github README.md docs\reference tools
```

Result: `PASS`, no output.

### Targeted Scope Scan

```text
rg -n "artifact-metadata|result\.artifacts|Command::new|run_engine_cli_help_smoke|tauri_plugin_shell|tauri-plugin-shell|tauri_plugin_fs|tauri-plugin-fs|fetch\(|XMLHttpRequest|WebSocket|workspace|scan|readFile|writeFile|artifact\.scan|sidecar|broker|live|AI|model|financial advice|telemetry|updater|signing|public release" apps\nullforge-desktop\src\App.tsx apps\nullforge-desktop\src\styles.css apps\nullforge-desktop\src-tauri\src\main.rs apps\nullforge-desktop\src-tauri\capabilities\default.json apps\nullforge-desktop\package.json apps\nullforge-desktop\src-tauri\Cargo.toml
```

Result: `PASS_WITH_EXPECTED_HITS`.

Expected hits:

- existing DA-T004 `run_engine_cli_help_smoke` and `Command::new` in Rust source;
- WB-T001 `artifact-metadata` styles;
- WB-T001 `result.artifacts` reads in React source;
- boundary text stating sidecar, workspace, scan/read/mutation, broker/live, AI/model, telemetry, updater, signing, public release, and financial advice behavior are not implemented.

No filesystem plugin, shell plugin, network API, workspace scan, file read/write API, new bridge command, dependency, or permission implementation was found.

### Ignored Generated Output

```text
git status --ignored --short apps\nullforge-desktop\dist apps\nullforge-desktop\node_modules apps\nullforge-desktop\src-tauri\target apps\nullforge-desktop\src-tauri\gen
```

Result: `PASS_WITH_IGNORED_OUTPUTS`.

Ignored outputs:

```text
!! apps/nullforge-desktop/dist/
!! apps/nullforge-desktop/node_modules/
!! apps/nullforge-desktop/src-tauri/gen/
!! apps/nullforge-desktop/src-tauri/target/
```

## Evidence Limits

- Build passed.
- WB-T001 did not run `tauri dev`.
- WB-T001 did not click the UI.
- WB-T001 did not capture screenshots.
- WB-T001 did not test a non-empty artifact array at runtime.
- The current bridge returns an empty artifact array.

## Test Verdict

Implementation checks support repo-local review or closeout.

WB-T001 is implemented but not audit-passed. Human direction is needed before treating WB-T001 as closed or starting the next scoped action.
