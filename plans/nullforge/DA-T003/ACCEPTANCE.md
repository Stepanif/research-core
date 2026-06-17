# DA-T003 Acceptance

Date: `2026-06-17`

Ticket: `DA-T003 - Minimal Tauri shell scaffold plan`

Role: Context Curator + Planner

No NullForge implementation code has started.

## Required Files For Future Implementation

The DA-T003 implementor may create or update only:

- `apps/nullforge-desktop/.gitignore`
- `apps/nullforge-desktop/index.html`
- `apps/nullforge-desktop/package.json`
- `apps/nullforge-desktop/pnpm-lock.yaml`
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
- `apps/nullforge-desktop/src-tauri/src/main.rs`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T003/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003/CHANGED_FILES.md`
- `reports/nullforge/DA-T003/TEST_RESULTS.md`
- `reports/nullforge/DA-T003/AUDITOR_PROMPT.md`

Expected ignored local outputs:

- `apps/nullforge-desktop/node_modules/`
- `apps/nullforge-desktop/dist/`
- `apps/nullforge-desktop/src-tauri/target/`
- `apps/nullforge-desktop/src-tauri/gen/`, if Tauri creates local schema metadata.

Ignored local outputs must not be staged.

## Acceptance Criteria

DA-T003 passes implementation review only if:

- the implementation is limited to a minimal launch-only local Windows/Tauri shell scaffold;
- the scaffold is isolated under `apps/nullforge-desktop/`;
- the app uses Tauri 2 major-version dependencies, React, TypeScript, Vite, and pnpm only within the app directory;
- exact resolved package and Cargo versions are recorded in DA-T003 reports or lockfiles;
- no root package file, root lockfile, root Cargo file, root workspace file, ResearchCore Engine file, source/package/test/schema/fixture/CI/generated-doc/docs-reference/tool/README file is changed;
- the app displays only bounded static status content;
- the app does not implement bridge commands;
- the app does not invoke bridge commands;
- the app does not invoke ResearchCore Engine;
- the app does not run `python -m research_core.cli --help` as a bridge action;
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them;
- arbitrary shell execution remains absent;
- sidecar work remains unstarted;
- workspace selection, workspace writes, artifact metadata display, dataset import, fixtures, tests, schemas, CI, generated docs, docs/reference, README, tools, packaging, updater, signing, public release, broker/live, AI/model, cloud/network/telemetry/auth/billing/mobile/marketplace/legal/trademark/financial advice scope remain absent;
- QA-T005 limits are preserved: only `.venv-qa-t005` readiness for `python -m research_core.cli --help` is proven;
- DA-T001 limits are preserved: only a docs-only planned desktop bridge contract source document is proven;
- DA-T002 limits are preserved: only a docs-only Tauri scaffold plan source document is proven;
- status/source-index updates are bounded to DA-T003 implementation pending independent audit;
- all DA-T003 report artifacts exist;
- no downstream ticket is started.

## Required Commands And Checks

The DA-T003 implementor must run:

- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `node --version`
- `pnpm --version`
- `rustc --version`
- `cargo --version`
- `pnpm --dir apps/nullforge-desktop install`
- `pnpm --dir apps/nullforge-desktop build`
- `pnpm --dir apps/nullforge-desktop tauri dev`
- `Test-Path -LiteralPath apps\nullforge-desktop\package.json`
- `Test-Path -LiteralPath apps\nullforge-desktop\pnpm-lock.yaml`
- `Test-Path -LiteralPath apps\nullforge-desktop\src-tauri\Cargo.toml`
- `Test-Path -LiteralPath apps\nullforge-desktop\src-tauri\Cargo.lock`
- `Test-Path -LiteralPath apps\nullforge-desktop\src-tauri\tauri.conf.json`
- `Test-Path -LiteralPath reports\nullforge\DA-T003\IMPLEMENTATION_REPORT.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003\CHANGED_FILES.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003\TEST_RESULTS.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003\AUDITOR_PROMPT.md`
- `rg -n "DA-T003|launch-only|Tauri shell|no bridge|No bridge|no sidecar|ResearchCore Engine|python -m research_core.cli --help|python -m research_core --help|research-core --help|cloud|network|telemetry|broker|live|public release" apps\nullforge-desktop docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md reports\nullforge\DA-T003`
- `rg -n "std::process|Command::new|tauri_plugin_shell|tauri-plugin-shell|tauri_plugin_fs|tauri-plugin-fs|https://|fetch\\(|XMLHttpRequest|WebSocket|broker|live trading|telemetry|analytics|research_core|research-core|python -m" apps\nullforge-desktop`
- `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml Cargo.toml .github README.md docs\reference tools`
- `git status --ignored --short apps\nullforge-desktop\node_modules apps\nullforge-desktop\dist apps\nullforge-desktop\src-tauri\target`
- `Test-Path -LiteralPath tickets`
- `Test-Path -LiteralPath milestones`
- `Test-Path -LiteralPath prompts`

The forbidden tracked-path diff check must return no output. The `tickets`, `milestones`, and `prompts` checks must return `False`.

The forbidden-content `rg` check must return no matches except for explicitly documented explanatory text in reports/status docs; any match inside app runtime files requires audit review. A local Vite `http://localhost` or `http://127.0.0.1` dev URL in Tauri config is allowed only as launch-smoke tooling and must not be treated as app network behavior.

## Checks To Skip

The following must remain skipped with explicit reasons:

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
- any command using `python -m research_core.cli --help` as a bridge action;
- any command using `python -m research_core --help` or `research-core --help`;
- any cloud/network/telemetry/auth/billing/broker/live/AI/updater/signing/public release check.

## Blocker Conditions

DA-T003 implementation should stop and report a blocker if:

- `node`, `pnpm`, `rustc`, or `cargo` is unavailable;
- dependency resolution requires changing root package/workspace files;
- Tauri requires broad filesystem, shell/process, network, updater, telemetry, credential, or sidecar permissions for the launch-only shell;
- the manual file set cannot launch without generator-created unknown files;
- `pnpm --dir apps/nullforge-desktop tauri dev` cannot be run or observed and no human accepts a weaker compile-only result;
- additional files outside the allowed list appear necessary;
- any bridge, sidecar, ResearchCore Engine, Python CLI, workspace, artifact, dataset, cloud/network/telemetry, broker/live, AI/model, updater/signing/public release, legal/trademark, or financial advice behavior becomes necessary.

## Auditor Focus

The DA-T003 auditor should verify:

- changed files match the allowed set;
- app-local package/dependency changes are bounded to `apps/nullforge-desktop/`;
- no root package/workspace/Cargo files are introduced;
- the static shell launches or launch proof is correctly marked blocked;
- no arbitrary shell execution or process-spawn path exists;
- no bridge command implementation or invocation exists;
- no sidecar work exists;
- no ResearchCore Engine invocation exists;
- no broad Tauri permissions or plugins are added;
- no network/cloud/telemetry/auth/billing/broker/live/AI/model/updater/signing/public release/mobile/marketplace/legal/trademark/financial advice scope appears;
- QA-T005, DA-T001, and DA-T002 claim boundaries are preserved;
- status/source navigation links resolve;
- no forbidden source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool files changed;
- no downstream ticket was started.
