# DA-T003S Context Bundle

Date: `2026-06-17`

Ticket: `DA-T003S - Human-gated Rust/Cargo setup path`

Role: Context Curator + Planner

Status: Ready for scoped implementor handoff after planner artifact review.

No NullForge implementation code has started.

## Mission

Create the bounded context and implementation plan for a human-approved Rust/Cargo setup action that can make `rustc` and `cargo` available on PATH for a later DA-T003 resume.

DA-T003S is planning-only. It does not install Rust/Cargo, repair PATH, repair environment state, run Rust/Cargo probes, run Node/pnpm/Tauri/app/package-manager/dependency commands, create app/package/Tauri/Rust/React/TypeScript/JavaScript/CSS/HTML files, modify package config, prove runtime behavior, or resume DA-T003.

## Current State

- `docs/nullforge/CURRENT_STATUS.md` records active phase `M1_TAURI_SHELL_SCAFFOLD_TOOLCHAIN_HOLD`.
- DA-T003 remains blocked with audit `HOLD`.
- DA-T003R is complete with audit `PASS` and records only a docs-only Rust/Cargo toolchain availability decision source.
- DA-T003H is complete with audit `PASS` and records only a docs-only human Rust/Cargo availability gate source.
- DA-T003V is recorded in the current working tree as human-provided negative Rust/Cargo evidence pending independent audit.
- DA-T003V evidence says human local PowerShell could not resolve `rustc` or `cargo` via PATH at `2026-06-17 2:28 PM ET`.
- No app scaffold, app package, lockfile, Rust, React, TypeScript, JavaScript, CSS, or HTML app artifact exists.

## Blocker Authority

DA-T003 blocker authority:

- `audits/nullforge/DA-T003/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003/FINDINGS.md`

DA-T003 audit decision is `HOLD`.

The blocker remains:

- `rustc` is unavailable on PATH;
- `cargo` is unavailable on PATH;
- DA-T003 stopped before scaffold creation;
- no `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package file, lockfile, Rust, React, TypeScript, JavaScript, CSS, or HTML app file has been created.

## Decision And Gate Authority

DA-T003R decision authority:

- `docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md`

DA-T003R records that DA-T003 remains blocked until one of these separately authorized paths occurs:

1. A human-approved action makes `rustc` and `cargo` available on PATH.
2. A separate scoped planning or ADR ticket changes the DA-T003 plan.

DA-T003H gate authority:

- `docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md`
- `audits/nullforge/DA-T003H/AUDIT_REPORT.md`

DA-T003H records a human-only gate. It does not prove Rust/Cargo availability and does not authorize DA-T003 resume.

DA-T003V evidence authority:

- `reports/nullforge/DA-T003V/EVIDENCE_RECORD.md`
- `reports/nullforge/DA-T003V/CHANGED_FILES.md`
- `reports/nullforge/DA-T003V/TEST_RESULTS.md`
- `reports/nullforge/DA-T003V/AUDITOR_PROMPT.md`

DA-T003V is current working-tree evidence pending independent audit. It records negative human evidence only and does not unblock DA-T003.

## Active Product And Scope Decisions

ADR-T001 keeps the first desktop stack direction as Tauri + React/TypeScript on Windows 11 x64, with a future ResearchCore Engine sidecar and narrow bridge. DA-T003S does not change that stack direction.

ADR-T002 keeps the MVP local-first and no-cloud. DA-T003S does not add cloud, network, telemetry, auth, billing, broker/live, AI/model, updater, signing, public release, mobile, marketplace, legal/trademark, or financial advice scope.

DA-T001 proves only a docs-only planned desktop bridge contract source document. DA-T003S does not implement or invoke bridge commands.

DA-T002 proves only a docs-only Tauri scaffold plan source document. DA-T003S does not create a Tauri scaffold.

## Claim Boundaries

QA-T005 proves only:

- `research-core` can be installed editable into `.venv-qa-t005`;
- `research_core` and `research_core.cli` are import-visible inside `.venv-qa-t005`;
- `python -m research_core.cli --help` runs inside `.venv-qa-t005`.

The following command shapes remain unsupported unless a later source/package ticket changes them:

- `python -m research_core --help`
- `research-core --help`

DA-T003 proves only a blocked pre-scaffold attempt caused by missing `rustc` and `cargo` on PATH.

DA-T003S must preserve that DA-T003 remains blocked until a later scoped ticket independently verifies `rustc --version` and `cargo --version`, or until a separate scoped plan changes DA-T003.

## Planned DA-T003S Implementation Slice

The DA-T003S implementor should create a repo-local docs-only setup path source, likely:

```text
docs/nullforge/qa/RUST_CARGO_SETUP_PATH.md
```

That source should record the human-gated setup path without executing setup. It should:

- identify the DA-T003 `HOLD` blocker;
- cite DA-T003R, DA-T003H, and DA-T003V;
- state that DA-T003V is negative evidence and does not unblock DA-T003;
- define the minimum acceptable setup outcome: `rustc` and `cargo` are available on PATH in the shell context a later scoped verifier will use;
- distinguish human setup steps from Codex verification steps;
- list future verification commands as future-only checks, not DA-T003S proof;
- require a separate DA-T003 resume ticket after toolchain availability is independently verified;
- preserve no-code and no-scaffold boundaries.

## Human-Gated Setup Direction

The recommended setup path to plan is:

1. Keep DA-T003 blocked.
2. Require explicit human approval before any Rust/Cargo setup action.
3. Prefer making an existing trusted local Rust/Cargo installation visible on PATH if one already exists.
4. If no local Rust/Cargo installation exists, require the human to select and approve a trusted Rust toolchain source outside this planner ticket.
5. Apply setup outside DA-T003 and outside app/package paths.
6. Open a fresh shell/session after setup.
7. Run a separate verification ticket that may check only `where.exe rustc`, `where.exe cargo`, `rustc --version`, and `cargo --version`.
8. Resume DA-T003 only through a separate scoped DA-T003 resume ticket after verification succeeds.

DA-T003S planning does not execute any of these steps.

## Non-Goals

DA-T003S must not:

- install Rust/Cargo;
- run `rustup`;
- run `cargo install`;
- download installers;
- repair PATH or environment variables;
- run `where.exe rustc`;
- run `where.exe cargo`;
- run `rustc --version`;
- run `cargo --version`;
- run `node`, `pnpm`, Tauri, package-manager, dependency, install, build, app, bridge, sidecar, runtime, ResearchCore Engine, Python CLI, test, docs build, quickstart, or CI commands;
- create `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package files, lockfiles, Rust, React, TypeScript, JavaScript, CSS, or HTML files;
- modify source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool files;
- implement or invoke bridge commands;
- invoke ResearchCore Engine;
- package or launch a sidecar;
- start DA-T003 resume, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work;
- commit unless explicitly asked.

## Done Definition

DA-T003S planning is done when:

- the five planner artifacts exist under `plans/nullforge/DA-T003S/`;
- the future setup path is bounded and human-gated;
- DA-T003 remains blocked;
- no setup command, probe command, app command, package/dependency command, test, docs build, runtime command, or downstream work is run;
- no app/package/source/test/schema/fixture/generated-doc/CI/README/docs-reference/tool file is created or changed;
- documentation-safe checks pass;
- no commit is created unless separately requested.
