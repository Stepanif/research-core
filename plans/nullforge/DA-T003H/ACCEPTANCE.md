# DA-T003H Acceptance

Date: `2026-06-17`

Ticket: `DA-T003H - Human Rust/Cargo availability gate`

Role: Context Curator + Planner

No NullForge implementation code has started.

## Required Files For Future Implementation

The DA-T003H implementor may create or update only:

- `docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T003H/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003H/CHANGED_FILES.md`
- `reports/nullforge/DA-T003H/TEST_RESULTS.md`
- `reports/nullforge/DA-T003H/AUDITOR_PROMPT.md`

No other tracked files should change.

## Acceptance Criteria

DA-T003H passes implementation review only if:

- DA-T003H stays docs-only;
- no Rust/Cargo installation, PATH repair, environment repair, dependency command, package-manager command, Tauri command, Node command, Rust command, app command, bridge command, sidecar command, ResearchCore Engine command, Python CLI command, runtime command, test command, docs build, quickstart command, or CI smoke command is run;
- `docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md` exists;
- the gate source records DA-T003 audit `HOLD` as blocker authority;
- the gate source records DA-T003R audit `PASS` and `docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md` as decision authority;
- the gate source records that DA-T003 stopped before scaffold creation because `rustc` and `cargo` are unavailable on PATH;
- the gate source preserves `No NullForge implementation code has started.`;
- the gate source records that no `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package file, lockfile, Rust, React, TypeScript, JavaScript, CSS, or HTML app file has been created;
- the gate source defines the Rust/Cargo availability action as human-only and outside Codex unless a later scoped prompt explicitly authorizes environment work;
- the gate source includes checklist fields for a human to record date, actor, method category, PATH visibility note, and observed `rustc --version` / `cargo --version` outputs;
- the gate source makes clear that DA-T003H does not run the human action and does not prove Rust/Cargo availability;
- future `rustc --version` and `cargo --version` checks are listed only as later DA-T003 resume checks, not as DA-T003H execution proof;
- QA-T005 limits are preserved: only `.venv-qa-t005` readiness for `python -m research_core.cli --help` is proven;
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them;
- DA-T001 limits are preserved: only a docs-only planned desktop bridge contract source document is proven;
- DA-T002 limits are preserved: only a docs-only Tauri scaffold plan source document is proven;
- DA-T003 limits are preserved: only a blocked pre-scaffold attempt is recorded;
- DA-T003R limits are preserved: only a docs-only Rust/Cargo toolchain availability decision source is proven;
- cloud/network/telemetry/auth/billing/broker/live/AI/model/updater/signing/public release/mobile/marketplace/legal/trademark/financial advice scope remains excluded;
- status/source-index updates are bounded to DA-T003H implementation pending independent audit;
- all DA-T003H report artifacts exist;
- no downstream ticket is started.

## Required Commands And Checks

The DA-T003H implementor must run:

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
- `rg -n "DA-T003H|Human Rust/Cargo|human-only|outside Codex|rustc|cargo|HOLD|PASS|No NullForge implementation code has started|apps/|apps/nullforge-desktop|src-tauri|python -m research_core.cli --help|python -m research_core --help|research-core --help|DA-T001|DA-T002|DA-T003|DA-T003R|cloud|network|telemetry|broker|live|public release" docs\nullforge\qa\HUMAN_RUST_CARGO_AVAILABILITY_GATE.md docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md reports\nullforge\DA-T003H`
- `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml Cargo.toml .github README.md docs\reference tools apps src-tauri`
- `Test-Path -LiteralPath tickets`
- `Test-Path -LiteralPath milestones`
- `Test-Path -LiteralPath prompts`

The forbidden tracked-path diff check must return no output. The `tickets`, `milestones`, and `prompts` checks must return `False`. The app/package path checks should return `False`.

## Commands To Skip

The following must remain skipped with explicit reasons:

- `rustc --version`;
- `cargo --version`;
- `node --version`;
- `pnpm --version`;
- any `pnpm --dir apps/nullforge-desktop ...` command;
- any Tauri command;
- any Rust/Cargo install or repair command;
- any PATH or environment-variable repair command;
- any dependency install or package-manager command;
- any app launch, build, or runtime command;
- full ResearchCore Engine tests;
- docs generation or docs build;
- quickstart commands;
- CI smoke;
- bridge smoke;
- sidecar smoke;
- workspace selection or file-write smoke;
- artifact metadata smoke;
- dataset/fixture smoke;
- any command using `python -m research_core.cli --help` as a bridge action;
- any command using `python -m research_core --help` or `research-core --help`;
- any cloud/network/telemetry/auth/billing/broker/live/AI/updater/signing/public release check.

## Blocker Conditions

DA-T003H implementation should stop and report a blocker if:

- creating the gate source would require environment repair or running Rust/Cargo commands;
- updating status/source navigation would require creating app/package/Tauri files;
- a requested path would require modifying source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool files;
- the implementor cannot preserve the no-code and no-scaffold claim boundaries;
- the selected path would change desktop stack direction without a separate scoped ADR or plan;
- the work would require DA-T003 resume or runtime proof.

## Auditor Focus

The DA-T003H auditor should verify:

- changed files match the allowed set;
- DA-T003H stayed docs-only;
- no Rust/Cargo, Node, pnpm, Tauri, app, package-manager, dependency, bridge, sidecar, ResearchCore Engine, Python CLI, runtime, install, repair, test, docs build, quickstart, or CI command was run;
- the gate source records a human-only action checklist without claiming toolchain availability;
- no app scaffold or package files were created;
- QA-T005, DA-T001, DA-T002, DA-T003, and DA-T003R claim boundaries are preserved;
- status/source navigation links resolve;
- no forbidden source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool/app files changed;
- no downstream ticket was started.
