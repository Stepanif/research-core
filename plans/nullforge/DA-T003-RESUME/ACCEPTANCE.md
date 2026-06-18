# DA-T003 Resume Acceptance

Ticket: `DA-T003 - Minimal Tauri shell scaffold resume`

Date: `2026-06-17`

No NullForge implementation code has started.

## Planner Acceptance

This planner ticket passes acceptance if:

- `plans/nullforge/DA-T003-RESUME/CONTEXT_BUNDLE.md` exists.
- `plans/nullforge/DA-T003-RESUME/CONTEXT_BUNDLE_MANIFEST.md` exists.
- `plans/nullforge/DA-T003-RESUME/PLAN.md` exists.
- `plans/nullforge/DA-T003-RESUME/ACCEPTANCE.md` exists.
- `plans/nullforge/DA-T003-RESUME/IMPLEMENTOR_PROMPT.md` exists.
- The plan preserves `No NullForge implementation code has started.`
- The plan preserves that no `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package file, lockfile, Rust app code, React, TypeScript, JavaScript, CSS, or HTML app file has been created yet.
- The plan requires fresh implementation-time checks for `rustc --version`, `cargo --version`, `node --version`, and `pnpm --version`.
- The planner does not run those probes.
- The planner does not create app, package, source, test, schema, fixture, generated-doc, CI, README, docs-reference, or tool files.
- The planner does not update status/source docs.
- The planner runs `git status --short --untracked-files=all`.
- The planner runs `git diff --check`.
- No commit is created.

## Future Implementation Acceptance

A later DA-T003 resume implementation can pass only if all applicable criteria below are true.

### Required Fresh Tool Checks

Before scaffold creation, the future implementor must run and record:

- `rustc --version`
- `cargo --version`
- `node --version`
- `pnpm --version`

If any command fails, the implementation must stop before creating scaffold files and record a blocker.

### Allowed Files

The future implementation must be limited to:

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
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T003-RESUME/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003-RESUME/CHANGED_FILES.md`
- `reports/nullforge/DA-T003-RESUME/TEST_RESULTS.md`
- `reports/nullforge/DA-T003-RESUME/AUDITOR_PROMPT.md`

No other tracked files are allowed without a separate scoped prompt.

### App Behavior

The future scaffold must:

- be manually created, not generator-created;
- use Tauri 2 major-version dependencies;
- use React + TypeScript + Vite;
- display static status content only;
- keep Tauri capabilities empty or minimal;
- avoid filesystem, shell/process, network, updater, telemetry, credential, bridge, sidecar, auth, billing, broker/live, AI/model, signing, public release, mobile, marketplace, legal/trademark, and financial advice behavior;
- avoid arbitrary shell execution;
- avoid bridge command implementation;
- avoid bridge command invocation;
- avoid ResearchCore Engine invocation;
- avoid Python sidecar packaging;
- avoid workspace, artifact metadata, dataset, or fixture behavior.

### Required Future Checks

The future implementation must run and report:

- `git status --short --untracked-files=all`
- `rustc --version`
- `cargo --version`
- `node --version`
- `pnpm --version`
- `pnpm --dir apps/nullforge-desktop install`
- `pnpm --dir apps/nullforge-desktop build`
- `pnpm --dir apps/nullforge-desktop tauri dev`
- `git diff --name-only`
- `git diff --check`
- final `git status --short --untracked-files=all`

If `tauri dev` cannot be run or observed, the implementation must record the exact reason and must not claim launch proof.

### Required Future Path Checks

The future implementation must verify expected tracked paths exist:

- `Test-Path -LiteralPath apps\nullforge-desktop\.gitignore`
- `Test-Path -LiteralPath apps\nullforge-desktop\index.html`
- `Test-Path -LiteralPath apps\nullforge-desktop\package.json`
- `Test-Path -LiteralPath apps\nullforge-desktop\pnpm-lock.yaml`
- `Test-Path -LiteralPath apps\nullforge-desktop\pnpm-workspace.yaml`
- `Test-Path -LiteralPath apps\nullforge-desktop\tsconfig.json`
- `Test-Path -LiteralPath apps\nullforge-desktop\vite.config.ts`
- `Test-Path -LiteralPath apps\nullforge-desktop\src\App.tsx`
- `Test-Path -LiteralPath apps\nullforge-desktop\src\main.tsx`
- `Test-Path -LiteralPath apps\nullforge-desktop\src\styles.css`
- `Test-Path -LiteralPath apps\nullforge-desktop\src-tauri\Cargo.toml`
- `Test-Path -LiteralPath apps\nullforge-desktop\src-tauri\Cargo.lock`
- `Test-Path -LiteralPath apps\nullforge-desktop\src-tauri\build.rs`
- `Test-Path -LiteralPath apps\nullforge-desktop\src-tauri\tauri.conf.json`
- `Test-Path -LiteralPath apps\nullforge-desktop\src-tauri\capabilities\default.json`
- `Test-Path -LiteralPath apps\nullforge-desktop\src-tauri\icons\icon.ico`
- `Test-Path -LiteralPath apps\nullforge-desktop\src-tauri\src\main.rs`
- `Test-Path -LiteralPath reports\nullforge\DA-T003-RESUME\IMPLEMENTATION_REPORT.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003-RESUME\CHANGED_FILES.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003-RESUME\TEST_RESULTS.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003-RESUME\AUDITOR_PROMPT.md`

The future implementation must verify forbidden root paths remain absent:

- `Test-Path -LiteralPath package.json`
- `Test-Path -LiteralPath pnpm-lock.yaml`
- `Test-Path -LiteralPath pnpm-workspace.yaml`
- `Test-Path -LiteralPath Cargo.toml`
- `Test-Path -LiteralPath Cargo.lock`
- `Test-Path -LiteralPath tickets`
- `Test-Path -LiteralPath milestones`
- `Test-Path -LiteralPath prompts`

### Required Future Content Checks

The future implementation should include targeted content checks proving:

- Tauri dependency major version is `2`.
- React, TypeScript, and Vite are app-local dependencies.
- static UI text does not claim bridge, engine, package, sidecar, workspace, artifact, data, cloud, network, broker/live, AI/model, signing, public release, or financial advice capability.
- `src-tauri/capabilities/default.json` grants no broad filesystem, shell, process, network, updater, telemetry, credential, bridge, or sidecar behavior.
- Rust code does not use process-spawn APIs such as `std::process::Command`.
- frontend code does not invoke bridge commands.
- no `python -m research_core.cli --help`, `python -m research_core --help`, or `research-core --help` command is invoked by the app.
- `.gitignore` ignores `node_modules/`, `dist/`, `src-tauri/target/`, and `src-tauri/gen/`.
- `CURRENT_STATUS.md` and `SOURCE_INDEX.md` record the bounded DA-T003 resume implementation state.
- `apps/nullforge-desktop/pnpm-workspace.yaml` approves only `esbuild` builds for pnpm 11 and no root `pnpm-workspace.yaml` exists.
- `apps/nullforge-desktop/src-tauri/icons/icon.ico` is an app-local launch-smoke asset only, not branding/legal/trademark/public release proof.

### Forbidden-Path Diff Check

The future implementation must run a forbidden-path diff check for:

- `src`
- `tests`
- `schemas`
- `fixtures`
- root package files
- root lockfiles
- root Cargo files
- `.github`
- `README.md`
- `docs\reference`
- `tools`

The check must return no forbidden tracked changes. App-local files under `apps/nullforge-desktop/` are allowed only if they match the allowed file list.

## Future Auditor Focus

The independent auditor should verify:

- the planner artifacts existed before implementation;
- fresh resume probes were run before scaffold creation;
- any probe failure stopped the work before scaffold creation;
- DA-T003S evidence was treated as setup evidence only;
- generated files are app-local and ignored when appropriate;
- no original DA-T003 historical reports were overwritten;
- no bridge, sidecar, ResearchCore Engine, workspace, artifact metadata, dataset, fixture, cloud/network, telemetry, updater/signing/release, broker/live, AI/model, mobile, marketplace, legal/trademark, or financial advice behavior was added;
- status/source docs use the bounded post-scaffold claim if scaffold files exist;
- `No NullForge implementation code has started.` remains only if the implementation stopped before creating scaffold files.
