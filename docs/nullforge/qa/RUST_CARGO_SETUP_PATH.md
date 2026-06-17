# NullForge Rust/Cargo Setup Path

Date: `2026-06-17`

Ticket: `DA-T003S`

Status: Complete; audit `PASS`.

No NullForge implementation code has started.

## Purpose

This document records the human-approved Rust/Cargo setup action for resolving the DA-T003 toolchain blocker far enough that a later scoped DA-T003 resume ticket can independently verify and decide whether to proceed.

DA-T003S is Rust/Cargo setup evidence only. It is not DA-T003 resume, Tauri app scaffold creation, app package creation, dependency readiness, bridge behavior, sidecar behavior, ResearchCore Engine invocation, runtime behavior, test proof, docs build proof, CI proof, or public release proof.

## Source Authority

DA-T003S uses these sources as authority:

- `plans/nullforge/DA-T003S/CONTEXT_BUNDLE.md`
- `plans/nullforge/DA-T003S/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/DA-T003S/PLAN.md`
- `plans/nullforge/DA-T003S/ACCEPTANCE.md`
- `plans/nullforge/DA-T003S/IMPLEMENTOR_PROMPT.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md`
- `docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md`
- `audits/nullforge/DA-T003/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003/FINDINGS.md`
- `reports/nullforge/DA-T003V/EVIDENCE_RECORD.md`
- `reports/nullforge/DA-T003V/TEST_RESULTS.md`

The DA-T003 audit `HOLD` and findings remain the blocker authority. DA-T003R remains the decision authority for requiring a separate human-approved setup path or a separate scoped plan change. DA-T003H remains the human-gate authority. DA-T003V remains negative human evidence from before DA-T003S setup.

Closeout audit authority:

- `audits/nullforge/DA-T003S/AUDIT_REPORT.md` records `Decision: PASS`.

## Human Approval

Filip Stepanian / project owner explicitly approved Rust/Cargo setup for DA-T003S.

The approved scope was limited to:

- minimum Rust/Cargo setup for Windows 11 x64;
- exact setup/probe evidence recording;
- no app scaffold;
- no Tauri, Node, pnpm, package-manager app command, bridge command, sidecar command, ResearchCore Engine command, test, docs build, quickstart, CI, or downstream implementation.

## Setup Path Selected

DA-T003S used the standard Windows Rust setup path through `rustup-init` for x64 Windows.

The setup source was the Rust Windows x64 installer endpoint:

```text
https://win.rustup.rs/x86_64
```

The setup used the minimal rustup profile:

```text
rustup-init-x86_64-pc-windows-msvc.exe -y --profile minimal --default-toolchain stable
```

This action installed Rust/Cargo under the user toolchain area outside the repository. It did not create app/package files in the repository.

## Commands And Observations

### Approved setup action

Command shape:

```text
Invoke-WebRequest -Uri 'https://win.rustup.rs/x86_64' -OutFile <temp>\rustup-init-x86_64-pc-windows-msvc.exe
<temp>\rustup-init-x86_64-pc-windows-msvc.exe -y --profile minimal --default-toolchain stable
```

Observed setup output summary:

```text
stable-x86_64-pc-windows-msvc installed - rustc 1.96.0 (ac68faa20 2026-05-25)
profile set to minimal
default host triple is x86_64-pc-windows-msvc
default toolchain set to stable-x86_64-pc-windows-msvc
```

The installer also reported that an existing rustup settings file was present at:

```text
C:\Users\Filip\.rustup\settings.toml
```

### Bare current-shell probes

Immediately after setup, these probes still failed in the inherited Codex shell PATH:

```text
rustc --version
cargo --version
```

Both returned command-not-recognized errors because the current Codex shell had not reloaded PATH after setup.

### Installed executable checks

The installed executable checks returned `True`:

```text
Test-Path -LiteralPath C:\Users\Filip\.cargo\bin\rustc.exe
Test-Path -LiteralPath C:\Users\Filip\.cargo\bin\cargo.exe
```

### User PATH persistence check

The user PATH check found:

```text
C:\Users\Filip\.cargo\bin
```

### Current-process PATH probe

After temporarily prepending `C:\Users\Filip\.cargo\bin` to the current process PATH for this setup evidence command, the required version probes succeeded:

```text
rustc 1.96.0 (ac68faa20 2026-05-25)
cargo 1.96.0 (30a34c682 2026-05-25)
```

This is DA-T003S setup evidence only. It does not resume DA-T003 and does not prove that a later DA-T003 resume shell has already loaded the updated PATH.

### Persisted user/machine PATH probe

After loading the current process PATH from persisted user and machine environment values, the required version probes also succeeded:

```text
rustc 1.96.0 (ac68faa20 2026-05-25)
cargo 1.96.0 (30a34c682 2026-05-25)
```

This simulates a fresh shell environment for DA-T003S setup evidence. It is still not DA-T003 resume proof.

## DA-T003 Boundary

DA-T003 remains blocked until a separate scoped DA-T003 resume ticket independently verifies and proceeds.

That later ticket may run only the checks allowed by its own prompt. At minimum, it should independently verify:

- `rustc --version`
- `cargo --version`

If that future shell does not resolve the commands, the resume ticket must stop and record the renewed blocker. It must not install or repair Rust/Cargo unless a separate scoped ticket explicitly authorizes that work.

## Repository Boundary

DA-T003S did not create:

- `apps/`;
- `apps/nullforge-desktop/`;
- `src-tauri/`;
- package files;
- lockfiles;
- Rust app files;
- React files;
- TypeScript files;
- JavaScript files;
- CSS files;
- HTML app files.

DA-T003S did not run:

- Node commands;
- pnpm commands;
- Tauri commands;
- app launch/build/runtime commands;
- package-manager dependency commands;
- bridge commands;
- sidecar commands;
- ResearchCore Engine commands;
- Python CLI commands;
- tests;
- docs builds;
- quickstart commands;
- CI commands.

## Preserved Claim Boundaries

QA-T005 proves only:

- `research-core` can be installed editable into `.venv-qa-t005`;
- `research_core` and `research_core.cli` are import-visible inside `.venv-qa-t005`;
- `python -m research_core.cli --help` runs inside `.venv-qa-t005`.

The following command shapes remain unsupported unless a later source/package ticket changes them:

- `python -m research_core --help`
- `research-core --help`

DA-T001 proves only a docs-only planned desktop bridge contract source document.

DA-T002 proves only a docs-only Tauri scaffold plan source document.

DA-T003 proves only a blocked pre-scaffold implementation attempt caused by missing `rustc` and `cargo` on PATH.

DA-T003R proves only a docs-only Rust/Cargo toolchain availability decision source.

DA-T003H proves only a docs-only human Rust/Cargo availability gate source.

DA-T003V proves only that a human reported Rust/Cargo were unavailable from local PowerShell at `2026-06-17 2:28 PM ET`.

DA-T003S proves only that the human-approved Rust/Cargo setup action ran, that installed `rustc.exe` and `cargo.exe` exist under `C:\Users\Filip\.cargo\bin`, that the user PATH contains that directory, and that `rustc --version` and `cargo --version` return version output when the current process PATH includes that directory or is loaded from persisted user/machine PATH values. DA-T003S does not prove app scaffold creation, Tauri launch behavior, package/dependency readiness, bridge behavior, sidecar behavior, ResearchCore Engine behavior, test readiness, docs build readiness, CI readiness, or public release readiness.

## Excluded Scope

The following remain excluded:

- DA-T003 resume;
- app scaffold creation;
- package/dependency artifacts;
- bridge command implementation or invocation;
- ResearchCore Engine invocation;
- sidecar behavior;
- tests;
- docs build;
- CI;
- DA-T004, WB-T001, MB-T002, ADR-T003, or downstream M1 work;
- cloud storage;
- cloud sync;
- hosted backend;
- network behavior in NullForge runtime;
- telemetry/analytics;
- account/auth;
- billing;
- marketplace;
- mobile;
- broker/live trading;
- live execution;
- AI/model calls;
- updater;
- signing;
- NullForge installer or public release;
- legal/trademark claims;
- financial advice claims;
- raw/full ES.zip;
- private/local data import;
- generated datasets;
- ES-derived fixtures;
- product, market, trading, or validation claims.
