# DA-T003S Acceptance

Date: `2026-06-17`

Ticket: `DA-T003S - Human-gated Rust/Cargo setup path`

Role: Context Curator + Planner

No NullForge implementation code has started.

## Required Planner Files

DA-T003S planning passes only if these files exist:

- `plans/nullforge/DA-T003S/CONTEXT_BUNDLE.md`
- `plans/nullforge/DA-T003S/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/DA-T003S/PLAN.md`
- `plans/nullforge/DA-T003S/ACCEPTANCE.md`
- `plans/nullforge/DA-T003S/IMPLEMENTOR_PROMPT.md`

## Acceptance Criteria

DA-T003S passes planning review only if:

- DA-T003S stays planning-only;
- no Rust/Cargo installation, PATH repair, environment repair, download, dependency command, package-manager command, Tauri command, Node command, Rust command, app command, bridge command, sidecar command, ResearchCore Engine command, Python CLI command, runtime command, test command, docs build, quickstart command, or CI smoke command is run;
- DA-T003 audit `HOLD` is treated as blocker authority;
- DA-T003R is treated as docs-only decision authority;
- DA-T003H is treated as docs-only human gate authority;
- DA-T003V negative human evidence is captured as current working-tree input pending independent audit;
- the plan records that DA-T003 remains blocked;
- the future setup path is human-gated and separate from DA-T003 resume;
- future `where.exe rustc`, `where.exe cargo`, `rustc --version`, and `cargo --version` checks are listed only as future verifier checks, not DA-T003S execution proof;
- the plan does not claim Rust/Cargo availability;
- the plan does not create or authorize app scaffold, Tauri runtime, package/dependency work, bridge/sidecar work, tests, docs build, CI, or downstream implementation;
- `No NullForge implementation code has started.` is preserved;
- QA-T005 limits are preserved: only `.venv-qa-t005` readiness for `python -m research_core.cli --help` is proven;
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them;
- DA-T001, DA-T002, DA-T003, DA-T003R, DA-T003H, and DA-T003V limits are preserved;
- cloud/network/telemetry/auth/billing/broker/live/AI/updater/signing/public release/mobile/marketplace/legal/trademark/financial advice scope remains excluded;
- no source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool/app files are changed;
- no tickets, milestones, prompt packs, audits, or downstream work are created.

## Required Checks

The DA-T003S planner must run:

- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `Test-Path -LiteralPath plans\nullforge\DA-T003S\CONTEXT_BUNDLE.md`
- `Test-Path -LiteralPath plans\nullforge\DA-T003S\CONTEXT_BUNDLE_MANIFEST.md`
- `Test-Path -LiteralPath plans\nullforge\DA-T003S\PLAN.md`
- `Test-Path -LiteralPath plans\nullforge\DA-T003S\ACCEPTANCE.md`
- `Test-Path -LiteralPath plans\nullforge\DA-T003S\IMPLEMENTOR_PROMPT.md`
- `rg -n "DA-T003S|human-gated|Rust/Cargo setup|DA-T003 remains blocked|DA-T003V|negative|No NullForge implementation code has started|future verifier|rustc --version|cargo --version|python -m research_core.cli --help|python -m research_core --help|research-core --help|DA-T001|DA-T002|DA-T003|DA-T003R|DA-T003H|cloud|network|telemetry|broker|live|public release" plans\nullforge\DA-T003S`
- `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml Cargo.toml .github README.md docs\reference tools apps src-tauri`
- `Test-Path -LiteralPath apps`
- `Test-Path -LiteralPath apps\nullforge-desktop`
- `Test-Path -LiteralPath src-tauri`
- `Test-Path -LiteralPath package.json`
- `Test-Path -LiteralPath pnpm-lock.yaml`
- `Test-Path -LiteralPath Cargo.toml`
- `Test-Path -LiteralPath tickets`
- `Test-Path -LiteralPath milestones`
- `Test-Path -LiteralPath prompts`

The forbidden tracked-path diff check must return no output. The app/package/ticket/milestone/prompt checks should return `False`.

## Commands To Skip

The following must remain skipped:

- `where.exe rustc`;
- `where.exe cargo`;
- `rustc --version`;
- `cargo --version`;
- `rustup`;
- `cargo install`;
- installer downloads;
- PATH repair;
- environment variable changes;
- `node`;
- `pnpm`;
- Tauri commands;
- package-manager commands;
- dependency commands;
- app launch/build/runtime commands;
- bridge commands;
- sidecar commands;
- ResearchCore Engine commands;
- Python CLI commands;
- tests;
- docs build;
- quickstart;
- CI.

## Auditor Focus

The DA-T003S auditor should verify:

- the changed files match the planner artifact set;
- DA-T003S stayed planning-only;
- no Rust/Cargo setup/probe command was run;
- the plan keeps DA-T003 blocked;
- DA-T003V is treated as negative evidence, not toolchain proof;
- future setup and future verification are separated;
- no app/package/runtime/bridge/sidecar/downstream work was created;
- no forbidden source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool/app files changed.
