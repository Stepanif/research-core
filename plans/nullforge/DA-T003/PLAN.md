# DA-T003 Plan

Date: `2026-06-17`

Ticket: `DA-T003 - Minimal Tauri shell scaffold plan`

Role: Context Curator + Planner

No NullForge implementation code has started.

## Objective

Plan the first scoped implementation ticket that may create a minimal launch-only Windows/Tauri desktop shell scaffold.

DA-T003 implementation, when separately authorized, should prove only that a minimal local Tauri shell can be scaffolded and launched on the target Windows 11 x64 environment. It must not implement bridge commands, invoke ResearchCore Engine, package a sidecar, implement workspace behavior, or make product/runtime claims beyond the launch-only shell smoke.

## Planned Implementation Target

The DA-T003 implementor should create a new app-local scaffold under:

```text
apps/nullforge-desktop/
```

The scaffold should be manually bounded rather than created by an interactive generator. The purpose is to keep the expected file list exact and auditable.

## Toolchain Decisions For DA-T003

| Decision | DA-T003 Plan |
|---|---|
| Package manager | Use `pnpm` for `apps/nullforge-desktop/` only. Do not add a root workspace or root package unless a later ticket approves it. |
| Tauri version | Use Tauri 2 major-version dependencies and record exact resolved versions in lockfiles and DA-T003 reports. |
| Rust toolchain | Use the locally installed `rustc` and `cargo` if present. Do not run `rustup`, install Rust, or repair the toolchain. |
| Frontend scaffold shape | React + TypeScript + Vite static shell. |
| App root path | `apps/nullforge-desktop/`. |
| Generated/tracked files | Only `pnpm-lock.yaml` and `src-tauri/Cargo.lock` are expected tracked lockfiles. |
| Generated/ignored files | `node_modules/`, `dist/`, `src-tauri/target/`, and optional `src-tauri/gen/` if Tauri creates local schema metadata. |
| Permissions | Empty/minimal Tauri capability permissions; no filesystem, shell/process, network, updater, telemetry, credential, bridge, or sidecar permissions. |
| Smoke command | `pnpm --dir apps/nullforge-desktop tauri dev` for launch smoke only. |
| Build check | `pnpm --dir apps/nullforge-desktop build` for frontend compile/build only. |

If any toolchain probe fails, DA-T003 implementation must stop and report the blocker. Missing tools are not repaired in DA-T003.

The local Vite loopback URL required by Tauri dev tooling is allowed only as a launch-smoke implementation detail. It must not become an app feature, remote network call, hosted backend, telemetry path, update check, or bridge transport.

## Allowed Implementor Changes

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

No other tracked files should change.

## Required App Behavior

The minimal shell should:

- open one local desktop window;
- display static NullForge status content only;
- state that DA-T003 is a launch-only shell scaffold;
- state that no bridge command, sidecar, workspace behavior, ResearchCore Engine invocation, artifact metadata, dataset import, cloud/network behavior, telemetry, broker/live behavior, updater, signing, or public release behavior is implemented;
- avoid in-app product claims, market claims, trading claims, financial advice language, and legal/trademark claims;
- avoid any command that touches ResearchCore Engine, Python environments, `.venv-qa-t005`, or unsupported CLI shapes.

The UI may be plain. DA-T003 is a technical launch smoke, not a product UI implementation ticket.

## Required App File Content Boundaries

The scaffold must not contain:

- Tauri command handlers for engine, bridge, workspace, file access, shell/process, sidecar, or network actions;
- `std::process`, `Command`, shell strings, or process-spawn code;
- `tauri-plugin-shell`, `tauri-plugin-fs`, network plugins, updater plugins, telemetry libraries, auth/billing libraries, broker/live libraries, or AI/model libraries;
- remote URLs, fetch calls, WebSocket calls, localhost services beyond the Vite dev server needed by `tauri dev`, or hosted API calls;
- Python invocation code;
- ResearchCore Engine invocation strings;
- `python -m research_core.cli --help` as bridge behavior;
- `python -m research_core --help`;
- `research-core --help`;
- workspace read/write code;
- fixture/data import code;
- generated docs, schemas, tests, CI, README, docs/reference, or tools changes.

## Implementation Steps

1. Re-read the DA-T003 planner artifacts.
2. Confirm the worktree state with `git status --short --untracked-files=all`.
3. Probe existing tool availability only:
   - `node --version`
   - `pnpm --version`
   - `rustc --version`
   - `cargo --version`
4. If any probe fails, stop and report a blocker. Do not install or repair tools.
5. Create the exact `apps/nullforge-desktop/` file set listed above.
6. Use app-local `.gitignore` to ignore `node_modules/`, `dist/`, `src-tauri/target/`, and optional `src-tauri/gen/`.
7. Run `pnpm --dir apps/nullforge-desktop install` to resolve the app-local package graph and create `apps/nullforge-desktop/pnpm-lock.yaml`.
8. Run `pnpm --dir apps/nullforge-desktop build` for frontend compile/build proof.
9. Run `pnpm --dir apps/nullforge-desktop tauri dev` for launch-only local shell smoke if the environment can support a GUI launch. Stop the dev process cleanly after launch evidence is captured.
10. Update `docs/nullforge/CURRENT_STATUS.md` to DA-T003 implemented and pending independent audit only if scaffold files were created.
11. Update `docs/nullforge/SOURCE_INDEX.md` to link DA-T003 reports and the app scaffold path only if the files exist.
12. Create DA-T003 reports under `reports/nullforge/DA-T003/`.
13. Run all required checks in `ACCEPTANCE.md`.
14. Do not commit unless separately instructed.

## Forbidden Work

The DA-T003 implementor must not:

- use `create-tauri-app`, `pnpm create`, `pnpm dlx`, `npx`, or any interactive scaffold generator;
- run `rustup`, `cargo install`, global installs, environment repair, active/global Python environment changes, or dependency installation outside `apps/nullforge-desktop/`;
- create or modify root package files, root lockfiles, root Cargo files, `pnpm-workspace.yaml`, source/package/test/schema/fixture/CI/generated-doc/docs-reference/tool/README files, or ResearchCore Engine files;
- create bridge commands, invoke bridge commands, invoke ResearchCore Engine, package or launch a sidecar, create workspace behavior, create artifact metadata behavior, create fixtures, run full tests, run docs builds, or run CI smoke;
- run `python -m research_core.cli --help` as a bridge action;
- run `python -m research_core --help`;
- run `research-core --help`;
- add shell/process, filesystem, network, updater, telemetry, auth, billing, broker/live, AI/model, signing, public release, mobile, marketplace, legal/trademark, or financial advice scope;
- start DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work;
- claim that a bridge, sidecar, workspace, package, engine, artifact, dataset, cloud absence, telemetry blocking, public release, product, market, trading, or financial advice behavior is implemented or proven.

## Status And Navigation Expectations

If DA-T003 implementation creates the app scaffold, `CURRENT_STATUS.md` should stop claiming that no NullForge implementation code has started and instead record a bounded first-implementation claim:

```text
DA-T003 created only a minimal launch-only Tauri shell scaffold under `apps/nullforge-desktop/`; no bridge command, sidecar behavior, ResearchCore Engine invocation, workspace behavior, artifact metadata, dataset import, cloud/network behavior, telemetry, updater, signing, public release, broker/live behavior, AI/model behavior, or financial advice behavior is implemented or proven.
```

The historical claim boundary must remain explicit:

- QA-T005 proves only `.venv-qa-t005` readiness for `python -m research_core.cli --help`.
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them.
- DA-T001 proves only a docs-only planned desktop bridge contract source document.
- DA-T002 proves only a docs-only Tauri scaffold plan source document.

`SOURCE_INDEX.md` should add DA-T003 plan/report links and a bounded app scaffold entry only for files that exist.

## Checks To Require

DA-T003 implementation must run:

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
- required path/content/forbidden-path checks from `ACCEPTANCE.md`

If `tauri dev` cannot be executed or observed in the local Codex environment, the implementor must record the exact reason and must not claim launch proof. A DA-T003 implementation without launch proof should be auditor-reviewed as `HOLD` unless a human explicitly accepts a weaker compile-only result.

## Risk Controls

- Keep all app implementation isolated to `apps/nullforge-desktop/`.
- Keep root repo package and Python package metadata unchanged.
- Keep package/dependency resolution app-local.
- Treat dependency downloads and Cargo resolution as implementation risk that must be recorded.
- Use empty/minimal Tauri permissions.
- Keep all bridge and sidecar behavior deferred to DA-T004 or later.
- Keep DA-T003 from becoming a product UI or workspace feature ticket.

## Done Definition

DA-T003 implementation is done when:

- the exact minimal app scaffold file set exists;
- app-local lockfiles exist and resolved versions are reported;
- the frontend build check passes;
- the Tauri shell launch smoke passes or is clearly blocked with evidence;
- status/source navigation is bounded and audit-pending;
- DA-T003 reports exist;
- required forbidden-content and forbidden-path checks pass;
- no bridge, sidecar, engine, workspace, dataset, network, telemetry, release, broker/live, AI/model, or downstream behavior is introduced;
- no broader proof is claimed.
