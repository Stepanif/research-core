# DA-T003H Context Bundle

Date: `2026-06-17`

Ticket: `DA-T003H - Human Rust/Cargo availability gate`

Role: Context Curator + Planner

Status: Ready for scoped implementor handoff after planner artifact review.

No NullForge implementation code has started.

## Mission

Create the bounded context and implementation plan for a human-gated Rust/Cargo availability action that can unblock DA-T003.

DA-T003H is planning-only. It must not install Rust/Cargo, repair PATH, repair environment state, run Rust/Cargo probes, run Node/pnpm/Tauri/app/package-manager/dependency commands, create app/package/Tauri/Rust/React/TypeScript/JavaScript/CSS/HTML files, modify package config, or resume DA-T003 implementation.

## Current State

- `docs/nullforge/CURRENT_STATUS.md` records active phase `M1_TAURI_SHELL_SCAFFOLD_TOOLCHAIN_HOLD`.
- Active ticket state is `DA-T003 blocked; DA-T003R complete with audit PASS`.
- DA-T003 remains blocked with audit `HOLD` because `rustc` and `cargo` are unavailable on PATH.
- DA-T003R is complete with audit `PASS` and records only a docs-only Rust/Cargo toolchain availability decision source.
- No Rust/Cargo installation, PATH repair, environment repair, Rust/Cargo probe rerun, toolchain proof, DA-T003 resume, app scaffold, package/dependency work, or runtime proof exists.
- No `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package file, lockfile, Rust, React, TypeScript, JavaScript, CSS, or HTML app file has been created.

## Blocker Authority

DA-T003 blocker authority:

- `audits/nullforge/DA-T003/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003/FINDINGS.md`
- `reports/nullforge/DA-T003/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003/TEST_RESULTS.md`

DA-T003 audit decision is `HOLD`.

The blocker is:

- `rustc --version` failed because `rustc` is not recognized;
- `cargo --version` failed because `cargo` is not recognized;
- DA-T003 stopped before scaffold creation;
- no scaffold, app package, lockfile, Rust, React, TypeScript, JavaScript, CSS, or HTML app artifact exists.

DA-T003R decision authority:

- `docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md`
- `audits/nullforge/DA-T003R/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003R/FINDINGS.md`

DA-T003R audit decision is `PASS`.

DA-T003R records that DA-T003 remains blocked until a separate human-approved action makes `rustc` and `cargo` available on PATH, or a separate scoped planning/ADR ticket changes the DA-T003 plan.

## Active Decisions

### ADR-T001

`docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` records:

- working product name: `NullForge`;
- first platform: Windows 11 x64;
- default desktop stack direction: Tauri + React/TypeScript;
- engine boundary: future Python ResearchCore Engine sidecar / scoped command bridge;
- bridge posture: narrow, allowlisted, structured, auditable, and not arbitrary shell execution.

ADR-T001 is planning truth only. It does not prove Rust availability, Tauri feasibility, sidecar feasibility, bridge reliability, package behavior, or public distribution readiness.

### ADR-T002

`docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md` records:

- local-first MVP posture;
- one selected local workspace as a future runtime boundary;
- local ResearchCore Engine execution as future direction;
- no cloud storage, cloud sync, hosted backend, auth, billing, telemetry, marketplace, network requirement, mobile, broker/live, AI/model, updater/signing, public release, legal/trademark, or financial advice scope.

ADR-T002 does not implement workspace behavior, app scaffold, bridge code, sidecar code, schemas, tests, CI, package config, generated docs, telemetry enforcement, or release behavior.

### DA-T001 Bridge Contract

`docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md` records:

- future bridge requests must use allowlisted structured command IDs only;
- arbitrary shell execution is forbidden;
- DA-T001 implements no bridge command;
- future bridge implementation remains separately scoped;
- no network, cloud, telemetry, auth, billing, broker/live, AI/model, updater, signing, public release, legal/trademark, or financial advice scope is allowed.

DA-T003H must not implement or invoke bridge commands.

### DA-T002 Tauri Scaffold Plan

`docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md` records:

- DA-T003 was intended as the first implementation ticket for a minimal desktop shell smoke;
- the intended future shell is launch-only Windows 11 x64 static status content;
- no bridge command implementation, bridge command invocation, arbitrary shell execution, or sidecar work belongs in DA-T003 by default;
- Rust toolchain and smoke commands were deferred to DA-T003.

DA-T003 attempted the toolchain probes and is now blocked before scaffold creation.

## Proof And Claim Boundaries

QA-T005 proves only:

- `research-core` can be installed editable into `.venv-qa-t005`;
- `research_core` and `research_core.cli` are import-visible inside `.venv-qa-t005`;
- `python -m research_core.cli --help` runs inside `.venv-qa-t005`.

The following command shapes remain unsupported unless a later source/package ticket changes them:

- `python -m research_core --help`
- `research-core --help`

DA-T001 proves only a docs-only planned desktop bridge contract source document.

DA-T002 proves only a docs-only Tauri scaffold plan source document.

DA-T003 proves only a blocked pre-scaffold attempt caused by missing `rustc` and `cargo` on PATH.

DA-T003R proves only a docs-only Rust/Cargo toolchain availability decision source. It does not prove Rust/Cargo availability, PATH correctness, app scaffold creation, package/dependency readiness, Tauri launch behavior, bridge command behavior, sidecar behavior, runtime behavior, or public release readiness.

DA-T003H must preserve all of these boundaries.

## Planned DA-T003H Implementation Slice

The DA-T003H implementor should create a docs-only human action checklist/record source at:

```text
docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md
```

The document should define exactly what a human must do outside Codex before DA-T003 can resume:

1. Decide whether to make Rust/Cargo available or change the DA-T003 plan.
2. If proceeding with Rust/Cargo, perform local machine setup outside Codex using a human-approved, trusted Rust toolchain source or an already installed local toolchain.
3. If Rust/Cargo is already installed, adjust PATH outside Codex so the shell used by Codex can discover both `rustc` and `cargo`.
4. Open a fresh shell outside Codex after the human action.
5. Manually verify outside Codex that `rustc --version` and `cargo --version` return version output.
6. Record the date, human actor, method category, and observed version strings in the checklist source without asking Codex to run the probes.
7. Start a separate DA-T003 resume prompt only after the human confirms both tools are visible on PATH.

The DA-T003H source document must make clear that DA-T003H does not execute the human action and does not prove Rust/Cargo availability unless a later scoped ticket is explicitly authorized to verify it.

## Expected Future DA-T003H Files

The DA-T003H implementor should create or update only:

- `docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T003H/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003H/CHANGED_FILES.md`
- `reports/nullforge/DA-T003H/TEST_RESULTS.md`
- `reports/nullforge/DA-T003H/AUDITOR_PROMPT.md`

No other tracked files should change.

## Non-Goals

DA-T003H planning and future implementation must not:

- install Rust/Cargo;
- run `rustup`;
- run `cargo install`;
- repair PATH or environment variables;
- run `rustc --version`;
- run `cargo --version`;
- run `node`, `pnpm`, Tauri, package-manager, dependency, install, build, app, bridge, sidecar, runtime, ResearchCore Engine, Python CLI, test, docs build, quickstart, or CI commands;
- create `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package files, lockfiles, Rust, React, TypeScript, JavaScript, CSS, or HTML files;
- modify root package/workspace/Cargo files;
- modify source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool files;
- implement or invoke bridge commands;
- invoke ResearchCore Engine;
- package or launch a sidecar;
- create tickets, milestones, prompt packs, audits, schemas, tests, fixtures, CI, generated docs, README, docs/reference, or tools;
- start DA-T003 resume, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work;
- add cloud, network, telemetry, auth, billing, broker/live, AI/model, updater, signing, public release, mobile, marketplace, legal/trademark, or financial advice scope.

## Human Gates And Risks

Human review is required before:

- installing Rust/Cargo;
- editing PATH;
- changing the DA-T003 Rust/Tauri prerequisite;
- changing desktop stack direction away from Tauri + React/TypeScript;
- running any DA-T003 resume command;
- creating app/package/Tauri/Rust/React/TypeScript/JavaScript/CSS/HTML files;
- running dependency resolution or launch smoke commands.

Risks to record in DA-T003H:

- Rust/Cargo may be installed for the human's shell but not visible to Codex.
- PATH changes may require a new shell or system restart before Codex can see them.
- Tauri may require additional native prerequisites after Rust/Cargo are available.
- Changing DA-T003 to avoid Rust would likely contradict ADR-T001 and should require a separate scoped decision.
- A human checklist is not runtime proof.

## Checks To Require

DA-T003H implementation must run only documentation-safe checks:

- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `Test-Path -LiteralPath docs\nullforge\qa\HUMAN_RUST_CARGO_AVAILABILITY_GATE.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003H\IMPLEMENTATION_REPORT.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003H\CHANGED_FILES.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003H\TEST_RESULTS.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003H\AUDITOR_PROMPT.md`
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

DA-T003H planning is done when:

- the five planner artifacts exist under `plans/nullforge/DA-T003H/`;
- the implementation target is limited to a docs-only human action checklist/record source plus bounded status/source/report updates;
- DA-T003 HOLD evidence and DA-T003R decision evidence are captured accurately;
- the claim boundary remains explicit;
- no Rust/Cargo install, PATH repair, environment repair, Rust/Cargo probe, app scaffold, package/dependency work, runtime command, bridge work, sidecar work, or downstream work is planned for DA-T003H;
- required planner checks pass;
- no commit is created unless separately requested.
