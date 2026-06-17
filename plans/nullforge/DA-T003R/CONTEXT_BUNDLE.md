# DA-T003R Context Bundle

Date: `2026-06-17`

Ticket: `DA-T003R - Rust/Cargo toolchain availability decision`

Role: Context Curator + Planner

Status: Ready for scoped implementor handoff after planner artifact review.

No NullForge implementation code has started.

## Mission

Create the bounded context and implementation plan for resolving the DA-T003 `HOLD` caused by missing `rustc` and `cargo` on PATH.

DA-T003R is planning-only. It must not install Rust/Cargo, repair environment state, create app/package/Tauri/Rust/React/TypeScript/JavaScript/CSS/HTML files, modify package config, run dependency commands, run Tauri/Node/Rust app commands, or resume DA-T003 implementation.

## Current State

- `docs/nullforge/CURRENT_STATUS.md` records active phase `M1_TAURI_SHELL_SCAFFOLD_TOOLCHAIN_HOLD`.
- `DA-T003` is blocked with audit `HOLD`.
- DA-T003 stopped before scaffold creation because `rustc` and `cargo` are unavailable on PATH.
- No `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package file, lockfile, Rust, React, TypeScript, JavaScript, CSS, or HTML app file has been created.
- `No NullForge implementation code has started.` remains valid.
- DA-T004, WB-T001, MB-T002, ADR-T003, app implementation, bridge implementation, sidecar work, additional environment repair, dependency changes, runtime commands, and downstream M1 work remain blocked until separately authorized.

## DA-T003 Blocker Authority

`audits/nullforge/DA-T003/AUDIT_REPORT.md` is the audit authority for DA-T003.

The DA-T003 audit decision is `HOLD`, not `PASS` or `REJECT`.

The audit found:

- DA-T003 stopped at the required toolchain blocker because `rustc` and `cargo` were unavailable.
- No app scaffold was created.
- No dependency install, Tauri command, package-manager install, app launch, bridge command, sidecar command, ResearchCore Engine command, environment repair, or downstream work occurred.
- `No NullForge implementation code has started.` remains valid for the blocked attempt.
- QA-T005, DA-T001, and DA-T002 claim boundaries remain preserved.

`audits/nullforge/DA-T003/FINDINGS.md` records blocking finding `DA-T003-HOLD-001: Rust/Cargo toolchain unavailable`.

`audits/nullforge/DA-T003/REPAIR_PROMPT.md` states that DA-T003 may resume only after a separate human-approved action makes `rustc` and `cargo` available on PATH, or after a separate scoped planning change replaces that prerequisite.

## DA-T003 Report Evidence

`reports/nullforge/DA-T003/IMPLEMENTATION_REPORT.md` records:

- `node --version` returned `v24.16.0`;
- `pnpm --version` returned `11.5.3`;
- `rustc --version` failed because `rustc` is not recognized;
- `cargo --version` failed because `cargo` is not recognized;
- no Rust installation, toolchain repair, environment repair, package-manager switch, or scaffold workaround was attempted.

`reports/nullforge/DA-T003/TEST_RESULTS.md` records:

- `pnpm --dir apps/nullforge-desktop install` was not run;
- `pnpm --dir apps/nullforge-desktop build` was not run;
- `pnpm --dir apps/nullforge-desktop tauri dev` was not run;
- no launch proof exists.

DA-T003R should treat this evidence as historical blocker evidence. DA-T003R should not rerun Rust/Cargo, Node, pnpm, Tauri, app, install, build, or runtime commands.

## Active Decisions

### ADR-T001

`docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` records:

- working product name: `NullForge`;
- repo identity remains `research-core`;
- engine label remains `ResearchCore Engine`;
- first platform: Windows 11 x64;
- default desktop stack direction: Tauri + React/TypeScript;
- engine boundary: future Python ResearchCore Engine sidecar / scoped command bridge;
- bridge posture: narrow, allowlisted, structured, auditable, and not arbitrary shell execution.

ADR-T001 is planning truth only. It does not prove Tauri feasibility, Rust availability, sidecar feasibility, bridge reliability, package behavior, or public distribution readiness.

### ADR-T002

`docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md` records:

- local-first MVP posture;
- one selected local workspace as the future runtime boundary;
- local ResearchCore Engine execution as future direction;
- no cloud storage, cloud sync, hosted backend, auth, billing, telemetry, marketplace, network requirement, mobile, broker/live, AI/model, updater/signing, public release, legal/trademark, or financial advice scope.

ADR-T002 does not implement workspace behavior, app scaffold, bridge code, sidecar code, schemas, tests, CI, package config, generated docs, telemetry enforcement, or release behavior.

### DA-T001 Bridge Contract

`docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md` records:

- future bridge requests must use allowlisted structured command IDs only;
- arbitrary shell execution is forbidden;
- Volume 3 command IDs are planned candidates unless later proven;
- DA-T001 implements no bridge command;
- first bridge proof is deferred to DA-T004 or another later scoped ticket;
- no network, cloud, telemetry, auth, billing, broker/live, AI/model, updater, signing, public release, legal/trademark, or financial advice scope is allowed.

DA-T003R must not implement or invoke bridge commands.

### DA-T002 Tauri Scaffold Plan

`docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md` records:

- future DA-T003 should be the first implementation ticket for a minimal desktop shell smoke;
- the intended future goal is a launch-only Windows 11 x64 desktop shell scaffold that opens and displays bounded static status content;
- no bridge command implementation, bridge command invocation, arbitrary shell execution, or sidecar work belongs in DA-T003 by default;
- Rust toolchain and smoke commands were deferred to DA-T003.

DA-T003 attempted the initial toolchain probes and is now blocked before scaffold creation.

## Proof And Claim Boundaries

QA-T005 proves only these bounded readiness facts:

- `research-core` can be installed editable into `.venv-qa-t005`;
- `research_core` and `research_core.cli` are import-visible inside `.venv-qa-t005`;
- `python -m research_core.cli --help` runs inside `.venv-qa-t005`.

The following command shapes remain unsupported unless a later source/package ticket changes them:

- `python -m research_core --help`
- `research-core --help`

DA-T001 proves only a docs-only planned desktop bridge contract source document.

DA-T002 proves only a docs-only Tauri scaffold plan source document.

DA-T003 proves only that the first implementation attempt stopped before scaffold creation because `rustc` and `cargo` were unavailable. It does not prove app scaffold creation, Tauri launch behavior, package/dependency readiness, Rust/React/TypeScript/JavaScript/CSS/HTML behavior, bridge command behavior, sidecar behavior, runtime behavior, or public release readiness.

## Planned DA-T003R Implementation Slice

The DA-T003R implementor should create a docs-only decision/repair path source document at:

```text
docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md
```

The document should record a recommended human-gated path for resolving the DA-T003 HOLD:

1. Keep DA-T003 blocked until a human-approved action makes `rustc` and `cargo` available on PATH, or changes the DA-T003 plan.
2. Do not install Rust/Cargo, repair PATH, run dependency commands, create app files, or resume DA-T003 inside DA-T003R.
3. After the human-approved action is complete, use a separate scoped DA-T003 resume prompt to verify `rustc --version` and `cargo --version` and continue only if the tools are already available.
4. If a human chooses not to make Rust/Cargo available, require a separate scoped planning/ADR decision before changing the desktop stack or DA-T003 implementation approach.

The DA-T003R source document should distinguish:

- blocker evidence already proven by DA-T003;
- the recommended human action path;
- commands listed for a future resume prompt but not run in DA-T003R;
- alternatives and stop conditions;
- non-proofs and claim boundaries.

## Expected Future DA-T003R Files

The DA-T003R implementor should create or update only:

- `docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T003R/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003R/CHANGED_FILES.md`
- `reports/nullforge/DA-T003R/TEST_RESULTS.md`
- `reports/nullforge/DA-T003R/AUDITOR_PROMPT.md`

No other tracked files should change.

## Non-Goals

DA-T003R planning and future implementation must not:

- install Rust/Cargo;
- run `rustup`;
- run `cargo install`;
- repair PATH or environment variables;
- run `rustc --version` or `cargo --version`;
- run `node`, `pnpm`, Tauri, package-manager, dependency, install, build, app, bridge, sidecar, runtime, ResearchCore Engine, or Python CLI commands;
- create `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package files, lockfiles, Rust files, React files, TypeScript files, JavaScript files, CSS files, or HTML files;
- create or modify root package/workspace/Cargo files;
- implement bridge commands;
- invoke bridge commands;
- invoke ResearchCore Engine;
- package or launch a sidecar;
- create workspace behavior, artifact metadata behavior, dataset behavior, fixtures, schemas, tests, CI, generated docs, README, docs/reference, or tools;
- add cloud, network, telemetry, auth, billing, broker/live, AI/model, updater, signing, public release, mobile, marketplace, legal/trademark, or financial advice scope;
- start DA-T003 resume, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work.

## Human Gates And Risks

Human review is required before:

- installing Rust/Cargo;
- editing PATH;
- changing DA-T003's Rust/Tauri prerequisite;
- changing desktop stack direction away from Tauri + React/TypeScript;
- running any DA-T003 resume command;
- creating app/package/Tauri/Rust/React/TypeScript/JavaScript/CSS/HTML files;
- running dependency resolution or launch smoke commands.

Risks to record in DA-T003R:

- Rust/Cargo may be installed but not visible in the shell PATH used by Codex.
- Tauri may require additional native prerequisites after Rust/Cargo are available.
- Changing DA-T003 to avoid Rust would likely contradict the ADR-T001 Tauri direction and needs a separate scoped decision.
- A toolchain availability decision is not a runtime proof.

## Checks To Require

DA-T003R implementation must run only documentation-safe checks:

- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `Test-Path -LiteralPath docs\nullforge\qa\RUST_CARGO_TOOLCHAIN_DECISION.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003R\IMPLEMENTATION_REPORT.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003R\CHANGED_FILES.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003R\TEST_RESULTS.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003R\AUDITOR_PROMPT.md`
- `Test-Path -LiteralPath apps`
- `Test-Path -LiteralPath apps\nullforge-desktop`
- `Test-Path -LiteralPath src-tauri`
- `Test-Path -LiteralPath package.json`
- `Test-Path -LiteralPath pnpm-lock.yaml`
- `Test-Path -LiteralPath pnpm-workspace.yaml`
- `Test-Path -LiteralPath Cargo.toml`
- `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml Cargo.toml .github README.md docs\reference tools apps src-tauri`
- `Test-Path -LiteralPath tickets`
- `Test-Path -LiteralPath milestones`
- `Test-Path -LiteralPath prompts`

The forbidden tracked-path diff check must return no output. The absent app/package/toolchain path checks should return `False`.

## Done Definition

DA-T003R planning is done when:

- the five planner artifacts exist under `plans/nullforge/DA-T003R/`;
- the implementation target is limited to a docs-only Rust/Cargo toolchain decision source document plus bounded status/source/report updates;
- DA-T003 HOLD evidence is captured accurately;
- the claim boundary remains explicit;
- no Rust/Cargo install, environment repair, app scaffold, package/dependency work, runtime command, bridge work, sidecar work, or downstream work is planned for DA-T003R;
- required planner checks pass;
- no commit is created unless separately requested.
