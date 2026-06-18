# DA-T003 Resume Implementor Prompt

Implement DA-T003 resume only. Do not commit.

Ticket:
`DA-T003 - Minimal Tauri shell scaffold resume`

Role:
Scoped Implementor.

Mission:
Resume DA-T003 by creating the minimal launch-only local Windows/Tauri shell scaffold planned by DA-T003 and DA-T003-RESUME, but only after fresh independent resume checks pass. This may create app-local Tauri, Rust, React, TypeScript, JavaScript, CSS, HTML, package, dependency, and lockfile artifacts only under the bounded allowed paths. Do not implement bridge commands, invoke bridge commands, invoke ResearchCore Engine, package or launch a sidecar, create workspace behavior, create artifact metadata behavior, create dataset/fixture behavior, run full tests, run docs builds, run CI smoke, create schemas, create generated docs, modify ResearchCore Engine files, or start downstream work.

Read first:

- `plans/nullforge/DA-T003-RESUME/CONTEXT_BUNDLE.md`
- `plans/nullforge/DA-T003-RESUME/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/DA-T003-RESUME/PLAN.md`
- `plans/nullforge/DA-T003-RESUME/ACCEPTANCE.md`
- `plans/nullforge/DA-T003-RESUME/IMPLEMENTOR_PROMPT.md`
- `plans/nullforge/DA-T003/PLAN.md`
- `plans/nullforge/DA-T003/ACCEPTANCE.md`
- `plans/nullforge/DA-T003/IMPLEMENTOR_PROMPT.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`
- `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md`
- `docs/nullforge/qa/RUST_CARGO_SETUP_PATH.md`
- `audits/nullforge/DA-T003/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003/FINDINGS.md`
- `audits/nullforge/DA-T003V/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003S/AUDIT_REPORT.md`

Allowed changes:

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

Requirements:

- Run fresh independent resume checks before creating scaffold files:
  - `rustc --version`
  - `cargo --version`
  - `node --version`
  - `pnpm --version`
- If any required tool is missing or unavailable, stop and record a blocker. Do not install tools or repair PATH/environment state.
- Create a manually bounded scaffold under `apps/nullforge-desktop/`; do not use `create-tauri-app`, `pnpm create`, `pnpm dlx`, `npx`, or interactive generator commands.
- Use `pnpm` only inside `apps/nullforge-desktop/`.
- Use Tauri 2 major-version dependencies and record exact resolved versions in lockfiles and reports.
- Use React + TypeScript + Vite for a static launch-only shell.
- If pnpm 11 requires build-script approval for Vite dependencies, keep that approval app-local and limited to `allowBuilds.esbuild: true`.
- If Tauri Windows resource generation requires an icon, use only the app-local `src-tauri/icons/icon.ico` path as a launch-smoke asset.
- Display static status content only.
- Include an app-local `.gitignore` for `node_modules/`, `dist/`, `src-tauri/target/`, and `src-tauri/gen/`.
- Keep Tauri capabilities empty or minimal.
- Do not add filesystem, shell/process, network, updater, telemetry, credential, bridge, sidecar, auth, billing, broker/live, AI/model, signing, public release, mobile, marketplace, legal/trademark, or financial advice behavior.
- Do not implement or invoke bridge commands.
- Do not invoke ResearchCore Engine.
- Do not invoke `.venv-qa-t005`.
- Do not run `python -m research_core.cli --help` as a bridge action.
- Keep `python -m research_core --help` and `research-core --help` unsupported unless a later source/package ticket changes them.
- Preserve QA-T005 limits: only `.venv-qa-t005` readiness for `python -m research_core.cli --help` is proven.
- Preserve DA-T001 limits: only a docs-only planned desktop bridge contract source document is proven.
- Preserve DA-T002 limits: only a docs-only Tauri scaffold plan source document is proven.
- Preserve DA-T003R limits: only a docs-only Rust/Cargo toolchain availability decision source is proven.
- Preserve DA-T003H limits: only a docs-only human Rust/Cargo availability gate source is proven.
- Preserve DA-T003V limits: only historical human-provided negative Rust/Cargo evidence is recorded.
- Preserve DA-T003S limits: only human-approved Rust/Cargo setup evidence is recorded; no DA-T003 resume, app scaffold, package/dependency readiness, Tauri runtime, bridge behavior, sidecar behavior, or runtime behavior is proven by DA-T003S.
- Update status/source navigation only to DA-T003 resume implementation pending independent audit.
- Because this resume may create the first bounded app scaffold, do not keep claiming globally that no NullForge implementation code has started after scaffold files are created. Replace that claim with:

`DA-T003 created only a minimal launch-only Tauri shell scaffold under `apps/nullforge-desktop/`; no bridge command, sidecar behavior, ResearchCore Engine invocation, workspace behavior, artifact metadata, dataset import, cloud/network behavior, telemetry, updater, signing, public release, broker/live behavior, AI/model behavior, or financial advice behavior is implemented or proven.`

Run:

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
- required path/content/forbidden-path checks from `plans/nullforge/DA-T003-RESUME/ACCEPTANCE.md`
- final `git status --short --untracked-files=all`

If `pnpm --dir apps/nullforge-desktop tauri dev` cannot be run or observed, record the exact reason and do not claim launch proof. A compile-only result should be treated as blocked or audit-pending `HOLD` unless a human explicitly accepts it.

Forbidden:

- root package files, root lockfiles, root Cargo files, `pnpm-workspace.yaml`, source/package/test/schema/fixture/CI/generated-doc/docs-reference/tool/README changes, ResearchCore Engine files
- `create-tauri-app`, `pnpm create`, `pnpm dlx`, `npx`, interactive generators, `rustup`, `cargo install`, global installs, environment repair, package/dependency changes outside `apps/nullforge-desktop/`
- bridge command implementation, bridge command invocation, ResearchCore Engine invocation, Python sidecar packaging, workspace behavior, artifact metadata behavior, dataset import, fixture creation, tests, schemas, CI, generated docs, docs build, quickstart, package/public release commands
- arbitrary shell execution, process-spawn adapters, raw shell strings, filesystem plugins, shell plugins, network plugins, updater/signing/public release behavior, telemetry/auth/billing/broker/live/AI/model/mobile/marketplace/legal/trademark/financial advice scope
- creating audits, tickets, milestones, prompt packs, or standalone prompt files outside the allowed DA-T003 resume report `AUDITOR_PROMPT.md`
- starting DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work

Do not commit unless explicitly asked.
