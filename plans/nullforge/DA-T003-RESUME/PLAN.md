# DA-T003 Resume Plan

Ticket: `DA-T003 - Minimal Tauri shell scaffold resume`

Role: Context Curator + Planner only

Date: `2026-06-17`

No NullForge implementation code has started.

## Objective

Plan a later DA-T003 resume implementation ticket that may create the minimal launch-only Windows/Tauri shell scaffold under `apps/nullforge-desktop/`, after fresh independent toolchain checks pass in that implementation ticket.

This planner ticket does not create the scaffold, run probes, run package-manager commands, install dependencies, build, launch, test, repair environment state, or change status/source docs.

## Planning Inputs

The resume plan uses:

- DA-T003 audit `HOLD` and findings as blocker authority.
- DA-T003R Rust/Cargo decision source and audit `PASS`.
- DA-T003H human availability gate source and audit `PASS`.
- DA-T003V historical negative human Rust/Cargo evidence and audit `PASS`.
- DA-T003S human-approved Rust/Cargo setup evidence and audit `PASS`.
- ADR-T001 and ADR-T002 as active decisions.
- DA-T001 bridge contract as the active bridge boundary.
- DA-T002 Tauri scaffold plan as the active scaffold source.
- The original DA-T003 plan, acceptance, and implementor prompt as the baseline implementation shape.

## Resume Implementation Gate

The later implementor must run fresh checks before creating any scaffold files:

1. `rustc --version`
2. `cargo --version`
3. `node --version`
4. `pnpm --version`

If any command is unavailable, the implementor must stop and record a blocker in the DA-T003 resume reports. The implementor must not install or repair Rust, Cargo, Node, pnpm, PATH, or environment state unless a separate scoped ticket explicitly authorizes that work.

DA-T003S setup evidence can inform expectations, but it is not current-shell proof for the resume.

## Planned Future Allowed Changes

The later DA-T003 resume implementation should be bounded to:

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

The report directory is intentionally `reports/nullforge/DA-T003-RESUME/` so the original `reports/nullforge/DA-T003/` blocked-attempt reports remain immutable historical evidence.

## Human-Authorized Repair Addendum

After the DA-T003-RESUME scaffold was created, the human authorized fixing the launch-smoke blocker. The bounded repair may add:

- `apps/nullforge-desktop/pnpm-workspace.yaml` with only `allowBuilds.esbuild: true` for pnpm 11 build-script approval;
- `apps/nullforge-desktop/src-tauri/icons/icon.ico` as the minimal app-local Windows icon required by Tauri resource generation.

These files are app-local repair files only. They do not authorize a root workspace file, root package file, branding/legal/trademark claim, public release asset, bridge implementation, sidecar work, network behavior, telemetry, updater, signing, or downstream work.

## Planned Future Scaffold Shape

The later implementation should create a manually bounded scaffold, not a generated scaffold:

- app root: `apps/nullforge-desktop/`;
- frontend: React + TypeScript + Vite;
- desktop shell: Tauri 2 major version;
- content: static status content only;
- capabilities: empty or minimal default capabilities;
- no filesystem plugin;
- no shell/process plugin;
- no network plugin;
- no updater/signing/release behavior;
- no telemetry, auth, billing, broker/live, AI/model, mobile, marketplace, legal/trademark, or financial advice behavior.

The app must not implement bridge command IDs, invoke bridge commands, invoke ResearchCore Engine, package or launch a sidecar, inspect workspaces, scan artifacts, import datasets, create fixtures, or make public release claims.

## Exact Expected Future Commands

The later DA-T003 resume implementor should run, in order:

1. `git status --short --untracked-files=all`
2. `rustc --version`
3. `cargo --version`
4. `node --version`
5. `pnpm --version`
6. create the bounded manual scaffold files under `apps/nullforge-desktop/`
7. `pnpm --dir apps/nullforge-desktop install`
8. `pnpm --dir apps/nullforge-desktop build`
9. `pnpm --dir apps/nullforge-desktop tauri dev`
10. `git diff --name-only`
11. `git diff --check`
12. required path/content/forbidden-path checks from `plans/nullforge/DA-T003-RESUME/ACCEPTANCE.md`
13. final `git status --short --untracked-files=all`

If `pnpm --dir apps/nullforge-desktop tauri dev` cannot be run or observed, the implementor must record the exact reason and must not claim launch proof. Compile-only evidence should remain audit-pending or `HOLD` unless a human explicitly accepts the limitation in scope.

## Expected Future Dependency Artifacts

The future implementation may create app-local package/dependency files only:

- `apps/nullforge-desktop/package.json`
- `apps/nullforge-desktop/pnpm-lock.yaml`
- `apps/nullforge-desktop/pnpm-workspace.yaml`
- `apps/nullforge-desktop/src-tauri/Cargo.toml`
- `apps/nullforge-desktop/src-tauri/Cargo.lock`

No root package files, root lockfiles, root Cargo files, or workspace files are allowed.

## Expected Ignored Outputs

The future scaffold should include `apps/nullforge-desktop/.gitignore` entries for:

- `node_modules/`
- `dist/`
- `src-tauri/target/`
- `src-tauri/gen/`

These outputs may be produced locally by install/build/dev checks but must not be staged.

## Skipped Checks

The later implementation must skip:

- full tests;
- docs build;
- CI smoke;
- quickstart commands;
- generated docs;
- Python CLI commands;
- ResearchCore Engine commands;
- bridge commands;
- sidecar commands;
- data/fixture commands;
- public release/package/signing commands;
- cloud/network/telemetry/auth/billing checks.

The only planned verification is tool availability, app-local install/build, and a bounded launch observation for the static shell if `tauri dev` can be run and observed.

## Status Update Rule

If the later implementation creates scaffold files, it must update `docs/nullforge/CURRENT_STATUS.md` and `docs/nullforge/SOURCE_INDEX.md` to record DA-T003 resume implementation pending independent audit.

It must also replace the global no-code claim with the bounded implementation claim:

`DA-T003 created only a minimal launch-only Tauri shell scaffold under `apps/nullforge-desktop/`; no bridge command, sidecar behavior, ResearchCore Engine invocation, workspace behavior, artifact metadata, dataset import, cloud/network behavior, telemetry, updater, signing, public release, broker/live behavior, AI/model behavior, or financial advice behavior is implemented or proven.`

If the later implementation stops before creating scaffold files, it must preserve:

No NullForge implementation code has started.

## Human-Gated Risks

The later implementor must stop for human direction if:

- any required tool probe fails;
- setup or PATH repair is required;
- `pnpm install` requires a package-manager or registry policy decision not already covered by the prompt;
- Tauri creates unexpected files outside the bounded app path;
- a dev-server or desktop window cannot be observed but launch proof is required;
- scaffold creation would require root workspace or package configuration;
- any bridge, sidecar, ResearchCore Engine, Python CLI, data, fixture, cloud, network, telemetry, updater, signing, release, or public claim work becomes necessary.

## Planner Completion Criteria

This planner is complete when:

- all five DA-T003 resume planning artifacts exist under `plans/nullforge/DA-T003-RESUME/`;
- the artifacts preserve the no-code and no-scaffold boundary;
- the artifacts require fresh implementation-time probes for Rust/Cargo/Node/pnpm;
- the artifacts define exact expected implementation paths, commands, generated/ignored outputs, skipped checks, and risks;
- `git status --short --untracked-files=all` is run;
- `git diff --check` is run;
- no commit is created.
