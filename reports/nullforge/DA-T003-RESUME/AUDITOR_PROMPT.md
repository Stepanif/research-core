# DA-T003 Resume Auditor Prompt

Audit DA-T003-RESUME only. Do not commit.

Ticket:
`DA-T003 - Minimal Tauri shell scaffold resume`

Audit role:
Independent Auditor.

Scope:
Audit the DA-T003-RESUME implementation and human-authorized repair that created the bounded launch-only Tauri shell scaffold under `apps/nullforge-desktop/`, produced app-local Node and Cargo lockfiles, added app-local pnpm/icon repair files, passed exact app-local install/build checks, and observed process-level Tauri dev launch evidence.

Read first:

- `plans/nullforge/DA-T003-RESUME/CONTEXT_BUNDLE.md`
- `plans/nullforge/DA-T003-RESUME/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/DA-T003-RESUME/PLAN.md`
- `plans/nullforge/DA-T003-RESUME/ACCEPTANCE.md`
- `plans/nullforge/DA-T003-RESUME/IMPLEMENTOR_PROMPT.md`
- `reports/nullforge/DA-T003-RESUME/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003-RESUME/CHANGED_FILES.md`
- `reports/nullforge/DA-T003-RESUME/TEST_RESULTS.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`
- `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md`
- `docs/nullforge/qa/RUST_CARGO_SETUP_PATH.md`
- `audits/nullforge/DA-T003/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003/FINDINGS.md`
- `audits/nullforge/DA-T003V/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003S/AUDIT_REPORT.md`

Audit focus:

- Verify fresh `rustc`, `cargo`, `node`, and `pnpm` probes ran before scaffold creation.
- Verify changed files are limited to the DA-T003-RESUME scaffold plus the human-authorized repair files, with no root package, root lockfile, root Cargo, root workspace, ResearchCore Engine, source/package/test/schema/fixture/CI/generated-doc/docs-reference/tool/README, ticket, milestone, prompt-folder, or audit changes.
- Verify `apps/nullforge-desktop/pnpm-workspace.yaml` is app-local, approves only `esbuild`, and no root workspace config file exists.
- Verify `apps/nullforge-desktop/src-tauri/icons/icon.ico` exists and is only an app-local launch-smoke asset.
- Verify app-local dependencies and lockfiles are bounded to `apps/nullforge-desktop/`.
- Verify React/TypeScript/Vite and Tauri 2 are app-local and resolved in lockfiles.
- Verify `pnpm --dir apps/nullforge-desktop install` and `pnpm --dir apps/nullforge-desktop build` passed in the final state.
- Verify `pnpm --dir apps/nullforge-desktop tauri dev` was attempted after repair and `nullforge-desktop.exe` process-level launch evidence is recorded.
- Verify no screenshot-level UI proof, bridge behavior, sidecar behavior, ResearchCore Engine invocation, workspace behavior, artifact metadata, dataset import, cloud/network behavior, telemetry, updater, signing, public release, broker/live behavior, AI/model behavior, or financial advice behavior is claimed.
- Verify Tauri capabilities are empty/minimal and no filesystem, shell/process, network, updater, telemetry, credential, bridge, or sidecar permission is granted.
- Verify Rust code does not use process-spawn APIs and frontend code does not invoke bridge commands.
- Verify generated local outputs were removed or remain ignored and unstaged.
- Verify status/source navigation links resolve and preserve prior QA-T005, DA-T001, DA-T002, DA-T003, DA-T003R, DA-T003H, DA-T003V, and DA-T003S boundaries.

Suggested verification commands:

- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
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
- `Test-Path -LiteralPath package.json`
- `Test-Path -LiteralPath pnpm-lock.yaml`
- `Test-Path -LiteralPath pnpm-workspace.yaml`
- `Test-Path -LiteralPath Cargo.toml`
- `Test-Path -LiteralPath Cargo.lock`
- `Test-Path -LiteralPath tickets`
- `Test-Path -LiteralPath milestones`
- `Test-Path -LiteralPath prompts`
- `rg -n "tauri = \\{ version = \\\"2|@tauri-apps/cli|react|typescript|vite|launch-only|No bridge|ResearchCore Engine|icons/icon.ico|allowBuilds|esbuild" apps\nullforge-desktop docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md reports\nullforge\DA-T003-RESUME`
- `rg -n "std::process|Command::new|tauri_plugin_shell|tauri-plugin-shell|tauri_plugin_fs|tauri-plugin-fs|fetch\\(|XMLHttpRequest|WebSocket|research_core|research-core|python -m" apps\nullforge-desktop`
- `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml Cargo.toml Cargo.lock .github README.md docs\reference tools`
- `git status --ignored --short apps\nullforge-desktop\node_modules apps\nullforge-desktop\dist apps\nullforge-desktop\src-tauri\target apps\nullforge-desktop\src-tauri\gen`

Expected disposition:

- `PASS` is appropriate only if the auditor accepts scaffold creation plus exact install/build and process-level launch evidence.
- `HOLD` is appropriate if screenshot-level UI proof remains required before DA-T003-RESUME can close.
- `REJECT` is appropriate if forbidden behavior, forbidden files, proof inflation, or boundary violations are found.
