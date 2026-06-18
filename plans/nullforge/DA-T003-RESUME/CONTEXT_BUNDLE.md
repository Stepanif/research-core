# DA-T003 Resume Context Bundle

Ticket: `DA-T003 - Minimal Tauri shell scaffold resume`

Role: Context Curator + Planner only

Date: `2026-06-17`

No NullForge implementation code has started.

## Mission

Create the bounded context for a later DA-T003 resume implementation ticket. The later implementation may create the minimal launch-only Windows/Tauri desktop shell scaffold that DA-T003 originally planned, but this planner ticket does not create the scaffold, run tool probes, run package-manager commands, or prove runtime behavior.

The resume exists because the original DA-T003 implementation stopped before scaffold creation at the required Rust/Cargo toolchain gate. DA-T003S later recorded human-approved Rust/Cargo setup evidence, but DA-T003S is setup evidence only and is not DA-T003 resume proof.

## Current State

Current NullForge status records:

- `DA-T003V` is complete with audit `PASS`.
- `DA-T003S` is complete with audit `PASS`.
- `DA-T003` remains blocked until a separate scoped DA-T003 resume ticket independently verifies `rustc --version` and `cargo --version` and proceeds.
- No `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package file, lockfile, Rust app code, React, TypeScript, JavaScript, CSS, or HTML app file has been created.
- No NullForge implementation code has started.

This planning ticket preserves that state. It does not update product status, create app files, or start implementation.

## Authority Chain

Primary status/navigation sources:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`

Architecture and decision sources:

- `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`
- `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`
- `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`
- `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md`

DA-T003 original plan and blocker sources:

- `plans/nullforge/DA-T003/PLAN.md`
- `plans/nullforge/DA-T003/ACCEPTANCE.md`
- `plans/nullforge/DA-T003/IMPLEMENTOR_PROMPT.md`
- `reports/nullforge/DA-T003/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003/CHANGED_FILES.md`
- `reports/nullforge/DA-T003/TEST_RESULTS.md`
- `audits/nullforge/DA-T003/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003/FINDINGS.md`

Toolchain decision and evidence sources:

- `docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md`
- `docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md`
- `docs/nullforge/qa/RUST_CARGO_SETUP_PATH.md`
- `reports/nullforge/DA-T003V/EVIDENCE_RECORD.md`
- `reports/nullforge/DA-T003V/TEST_RESULTS.md`
- `audits/nullforge/DA-T003R/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003H/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003V/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003S/AUDIT_REPORT.md`

Prior proof boundaries:

- `audits/nullforge/QA-T005/AUDIT_REPORT.md`
- `audits/nullforge/DA-T001/AUDIT_REPORT.md`
- `audits/nullforge/DA-T002/AUDIT_REPORT.md`

## Preserved Proof Boundaries

QA-T005 proves only `.venv-qa-t005` readiness for:

- `python -m research_core.cli --help`

The following command shapes remain unsupported unless a later source/package ticket changes them:

- `python -m research_core --help`
- `research-core --help`

DA-T001 proves only a docs-only planned desktop bridge contract source document.

DA-T002 proves only a docs-only Tauri scaffold plan source document.

DA-T003 proves only a blocked pre-scaffold attempt caused by missing `rustc` and `cargo` on PATH at the time of that attempt.

DA-T003R proves only a docs-only Rust/Cargo toolchain availability decision source.

DA-T003H proves only a docs-only human Rust/Cargo availability gate source.

DA-T003V proves only historical human-provided negative Rust/Cargo evidence from `2026-06-17 2:28 PM ET`.

DA-T003S proves only human-approved Rust/Cargo setup evidence. It does not prove DA-T003 resume readiness, app scaffold creation, package/dependency readiness, Tauri launch behavior, bridge behavior, sidecar behavior, ResearchCore Engine invocation, or runtime behavior.

## DA-T003S Setup Evidence To Consider

DA-T003S recorded these setup facts as setup evidence only:

- `rustup-init` installed `stable-x86_64-pc-windows-msvc`.
- Installed `rustc.exe` and `cargo.exe` exist under `C:\Users\Filip\.cargo\bin`.
- User PATH contains `C:\Users\Filip\.cargo\bin`.
- Bare `rustc --version` and `cargo --version` failed in the stale inherited Codex shell PATH immediately after setup.
- `rustc --version` and `cargo --version` returned version output after temporarily prepending `C:\Users\Filip\.cargo\bin` to the current process PATH.
- `rustc --version` and `cargo --version` also returned version output when process PATH was loaded from persisted user/machine environment values.

A later DA-T003 resume implementor must not rely on those facts as current-shell proof. The implementor must run fresh independent resume checks in the implementation ticket.

## Resume Implementation Target

The planned resume implementation target is the same narrow DA-T003 target:

- a manually bounded minimal launch-only local Windows/Tauri shell scaffold;
- path root `apps/nullforge-desktop/`;
- React + TypeScript + Vite static frontend;
- Tauri 2 major-version desktop shell;
- static status content only;
- app-local package and lock files only;
- minimal or empty Tauri capabilities;
- app-local `.gitignore` for generated or dependency outputs.

The planned implementation must not use `create-tauri-app`, `pnpm create`, `pnpm dlx`, `npx`, or interactive generator commands.

## Required Fresh Resume Checks

The later DA-T003 resume implementor must run these checks before creating scaffold files:

- `rustc --version`
- `cargo --version`
- `node --version`
- `pnpm --version`

If any required tool is unavailable, the implementor must stop and record a blocker. The implementor must not install tools, repair PATH, repair environment state, or continue into scaffold creation unless a separate scoped prompt explicitly authorizes that work.

This planner ticket must not run those probes.

## Future Allowed Scaffold Paths

The later DA-T003 resume implementation may be scoped to these app files:

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

The later implementation may also update:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T003-RESUME/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003-RESUME/CHANGED_FILES.md`
- `reports/nullforge/DA-T003-RESUME/TEST_RESULTS.md`
- `reports/nullforge/DA-T003-RESUME/AUDITOR_PROMPT.md`

Using `reports/nullforge/DA-T003-RESUME/` preserves the original blocked `reports/nullforge/DA-T003/` evidence.

## Expected Ignored Or Generated Outputs

The later implementation may cause the following app-local outputs during install/build/dev checks. They should be ignored and not staged:

- `apps/nullforge-desktop/node_modules/`
- `apps/nullforge-desktop/dist/`
- `apps/nullforge-desktop/src-tauri/target/`
- `apps/nullforge-desktop/src-tauri/gen/` if Tauri creates it

Unexpected generated files outside the bounded app path are a stop condition.

## Hard Non-Goals

The later implementation must not include:

- bridge command implementation;
- bridge command invocation;
- arbitrary shell execution;
- process-spawn adapters;
- ResearchCore Engine invocation;
- Python sidecar packaging;
- sidecar launch behavior;
- workspace behavior;
- artifact metadata behavior;
- dataset import;
- fixture creation;
- full tests;
- docs build;
- CI smoke;
- generated docs;
- root package files;
- root lockfiles;
- root Cargo files;
- `pnpm-workspace.yaml`;
- source/package/test/schema/fixture/CI/README/docs-reference/tool changes;
- cloud, network, telemetry, auth, billing, broker/live, AI/model, updater, signing, public release, mobile, marketplace, legal/trademark, or financial advice scope.

## Claim Boundary After Future Scaffold Creation

If a later DA-T003 resume implementation creates scaffold files, status docs must stop claiming globally that no NullForge implementation code has started. They must replace that global claim with the bounded implementation claim from the DA-T003 plan:

`DA-T003 created only a minimal launch-only Tauri shell scaffold under `apps/nullforge-desktop/`; no bridge command, sidecar behavior, ResearchCore Engine invocation, workspace behavior, artifact metadata, dataset import, cloud/network behavior, telemetry, updater, signing, public release, broker/live behavior, AI/model behavior, or financial advice behavior is implemented or proven.`

Until that future implementation occurs, the current claim remains:

No NullForge implementation code has started.
