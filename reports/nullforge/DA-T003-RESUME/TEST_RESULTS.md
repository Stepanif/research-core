# DA-T003 Resume Test Results

Ticket: `DA-T003 - Minimal Tauri shell scaffold resume`

Date: `2026-06-17`

Result: Scaffold created; app-local install/build passed; launch process observed.

## Required Command Results

| Command | Result | Output Summary |
|---|---|---|
| `git status --short --untracked-files=all` | PASS | Showed only expected existing DA-T003-RESUME planner/report/status working-tree context before scaffold creation. |
| `rustc --version` | PASS | Initial sandboxed run failed before command launch; escalated rerun returned `rustc 1.96.0 (ac68faa20 2026-05-25)`. |
| `cargo --version` | PASS | Initial sandboxed run failed before command launch; escalated rerun returned `cargo 1.96.0 (30a34c682 2026-05-25)`. |
| `node --version` | PASS | `v24.16.0`. |
| `pnpm --version` | PASS | `11.5.3`. |
| `pnpm --dir apps/nullforge-desktop install` | PASS | After adding app-local `pnpm-workspace.yaml` with only `allowBuilds.esbuild: true`, exact install passed and ran `esbuild` postinstall. |
| `pnpm --dir apps/nullforge-desktop build` | PASS | `tsc --noEmit` and `vite build` completed successfully. |
| `pnpm --dir apps/nullforge-desktop tauri dev` | PASS with process-level evidence | After adding `src-tauri/icons/icon.ico`, `tauri dev` launched far enough that `nullforge-desktop.exe` was observed running from `target\debug\nullforge-desktop.exe`. The command timed out because the dev server/app stayed alive; processes were stopped afterward. No screenshot-level visual UI proof was captured. |

## Tauri Dev Failure Evidence

First `tauri dev` blocker:

```text
Error: EBUSY: resource busy or locked, watch '...\apps\nullforge-desktop\src-tauri\target\debug\deps\yoke_derive-...dll'
```

Implemented bounded repair:

- `apps/nullforge-desktop/vite.config.ts` now ignores `**/src-tauri/target/**` and `**/src-tauri/gen/**` for the Vite dev-server watcher.

Second `tauri dev` blocker before repair:

```text
`icons/icon.ico` not found; required for generating a Windows Resource file during tauri-build
```

At that pre-repair point, no icon file had been created and launch proof was not claimed from that failed attempt. A later human-authorized repair added the app-local icon path listed below.

Human-authorized repair:

- added `apps/nullforge-desktop/pnpm-workspace.yaml` with only `allowBuilds.esbuild: true`;
- added `apps/nullforge-desktop/src-tauri/icons/icon.ico`.

Final launch observation:

- `nullforge-desktop.exe` was observed running from `target\debug\nullforge-desktop.exe`;
- DA-T003-RESUME Node/dev/app processes were then stopped;
- no screenshot-level visual UI proof was captured.

## Required Path Checks

Expected scaffold/report paths exist:

- `apps/nullforge-desktop/.gitignore`
- `apps/nullforge-desktop/index.html`
- `apps/nullforge-desktop/package.json`
- `apps/nullforge-desktop/pnpm-lock.yaml`
- `apps/nullforge-desktop/pnpm-workspace.yaml`
- `apps/nullforge-desktop/tsconfig.json`
- `apps/nullforge-desktop/vite.config.ts`
- `apps/nullforge-desktop/src/App.tsx`
- `apps/nullforge-desktop/src/main.tsx`
- `apps/nullforge-desktop/src/styles.css`
- `apps/nullforge-desktop/src-tauri/Cargo.toml`
- `apps/nullforge-desktop/src-tauri/Cargo.lock`
- `apps/nullforge-desktop/src-tauri/build.rs`
- `apps/nullforge-desktop/src-tauri/tauri.conf.json`
- `apps/nullforge-desktop/src-tauri/capabilities/default.json`
- `apps/nullforge-desktop/src-tauri/icons/icon.ico`
- `apps/nullforge-desktop/src-tauri/src/main.rs`
- `reports/nullforge/DA-T003-RESUME/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003-RESUME/CHANGED_FILES.md`
- `reports/nullforge/DA-T003-RESUME/TEST_RESULTS.md`
- `reports/nullforge/DA-T003-RESUME/AUDITOR_PROMPT.md`

Forbidden root paths remain absent:

- `package.json`
- `pnpm-lock.yaml`
- root `pnpm-workspace.yaml`
- `Cargo.toml`
- `Cargo.lock`
- `tickets`
- `milestones`
- `prompts`

## Required Content Checks

Observed content boundaries:

- Tauri dependency major version is `2`.
- React, TypeScript, and Vite are app-local dependencies.
- `src-tauri/capabilities/default.json` grants an empty permission list.
- Rust code does not use `std::process` or `Command::new`.
- Frontend code does not invoke bridge commands.
- The app does not invoke `python -m research_core.cli --help`, `python -m research_core --help`, or `research-core --help`.
- `.gitignore` ignores `node_modules/`, `dist/`, `src-tauri/target/`, and `src-tauri/gen/`.
- Runtime UI text is static and explicitly bounded to launch-only scaffold status.
- `CURRENT_STATUS.md` and `SOURCE_INDEX.md` record DA-T003-RESUME scaffold creation, app-local install/build proof, historical pre-repair `tauri dev` blockers, app-local pnpm/icon repair, process-level launch evidence, and no screenshot-level visual UI proof.

## Skipped Checks

Skipped by scope:

- full ResearchCore Engine tests;
- docs generation or docs build;
- quickstart commands;
- CI smoke;
- `tauri build`;
- package/public release commands;
- bridge smoke;
- sidecar smoke;
- workspace selection or file-write smoke;
- artifact metadata smoke;
- dataset/fixture smoke;
- Python CLI bridge action checks;
- cloud/network/telemetry/auth/billing/broker/live/AI/updater/signing/public release checks.

## Cleanup Checks

Generated local outputs were removed after verification:

- `apps/nullforge-desktop/node_modules/`
- `apps/nullforge-desktop/dist/`
- `apps/nullforge-desktop/src-tauri/target/`
- `apps/nullforge-desktop/src-tauri/gen/`

The remaining repo changes are app source/lockfiles/app-local pnpm config/icon asset, DA-T003-RESUME plan/report artifacts, and bounded status/source navigation updates.
