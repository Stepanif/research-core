# DA-T003R Acceptance

Date: `2026-06-17`

Ticket: `DA-T003R - Rust/Cargo toolchain availability decision`

Role: Context Curator + Planner

No NullForge implementation code has started.

## Required Files For Future Implementation

The DA-T003R implementor may create or update only:

- `docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T003R/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003R/CHANGED_FILES.md`
- `reports/nullforge/DA-T003R/TEST_RESULTS.md`
- `reports/nullforge/DA-T003R/AUDITOR_PROMPT.md`

No other tracked files should change.

## Acceptance Criteria

DA-T003R passes implementation review only if:

- DA-T003R stays docs-only;
- no Rust/Cargo installation, PATH repair, environment repair, dependency command, package-manager command, Tauri command, Node command, Rust command, app command, bridge command, sidecar command, ResearchCore Engine command, Python CLI command, runtime command, test command, docs build, quickstart command, or CI smoke command is run;
- `docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md` exists;
- the decision source records DA-T003 audit `HOLD` as authority;
- the decision source records that DA-T003 stopped before scaffold creation because `rustc` and `cargo` are unavailable on PATH;
- the decision source preserves `No NullForge implementation code has started.`;
- the decision source records that no `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package file, lockfile, Rust, React, TypeScript, JavaScript, CSS, or HTML app file has been created;
- the decision source recommends a separate human-approved Rust/Cargo availability action or a separate scoped plan change before DA-T003 can resume;
- the decision source makes clear that DA-T003R does not execute the human action and does not prove Rust/Cargo availability;
- future `rustc --version` and `cargo --version` checks are listed only as later DA-T003 resume checks, not as DA-T003R execution proof;
- QA-T005 limits are preserved: only `.venv-qa-t005` readiness for `python -m research_core.cli --help` is proven;
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them;
- DA-T001 limits are preserved: only a docs-only planned desktop bridge contract source document is proven;
- DA-T002 limits are preserved: only a docs-only Tauri scaffold plan source document is proven;
- DA-T003 limits are preserved: only a blocked pre-scaffold attempt is recorded;
- cloud/network/telemetry/auth/billing/broker/live/AI/model/updater/signing/public release/mobile/marketplace/legal/trademark/financial advice scope remains excluded;
- status/source-index updates are bounded to DA-T003R implementation pending independent audit;
- all DA-T003R report artifacts exist;
- no downstream ticket is started.

## Required Commands And Checks

The DA-T003R implementor must run:

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
- `rg -n "DA-T003R|Rust/Cargo|rustc|cargo|HOLD|human-approved|No NullForge implementation code has started|apps/|apps/nullforge-desktop|src-tauri|python -m research_core.cli --help|python -m research_core --help|research-core --help|DA-T001|DA-T002|DA-T003|cloud|network|telemetry|broker|live|public release" docs\nullforge\qa\RUST_CARGO_TOOLCHAIN_DECISION.md docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md reports\nullforge\DA-T003R`
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

DA-T003R implementation should stop and report a blocker if:

- creating the decision source would require environment repair or running Rust/Cargo commands;
- updating status/source navigation would require creating app/package/Tauri files;
- a requested path would require modifying source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool files;
- the implementor cannot preserve the no-code and no-scaffold claim boundaries;
- the selected path would change desktop stack direction without a separate scoped ADR or plan.

## Auditor Focus

The DA-T003R auditor should verify:

- changed files match the allowed set;
- DA-T003R stayed docs-only;
- no Rust/Cargo, Node, pnpm, Tauri, app, package-manager, dependency, bridge, sidecar, ResearchCore Engine, Python CLI, runtime, install, repair, test, docs build, quickstart, or CI command was run;
- the decision source records a human-gated path without claiming toolchain availability;
- no app scaffold or package files were created;
- QA-T005, DA-T001, DA-T002, and DA-T003 claim boundaries are preserved;
- status/source navigation links resolve;
- no forbidden source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool/app files changed;
- no downstream ticket was started.
