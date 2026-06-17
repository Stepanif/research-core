# DA-T002 Acceptance

Date: `2026-06-17`

Ticket: `DA-T002 - Tauri app scaffold plan`

Role: Context Curator + Planner

No NullForge implementation code has started.

## Required Files

The DA-T002 implementor may create or update only:

- `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T002/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T002/CHANGED_FILES.md`
- `reports/nullforge/DA-T002/TEST_RESULTS.md`
- `reports/nullforge/DA-T002/AUDITOR_PROMPT.md`

## Acceptance Criteria

DA-T002 passes implementation review only if:

- it remains docs-only;
- it creates `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md`;
- the source document is a scaffold plan, not a Tauri/app scaffold;
- the exact sentence `No NullForge implementation code has started.` is preserved;
- QA-T005 limits are preserved: only `.venv-qa-t005` readiness for `python -m research_core.cli --help` is proven;
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them;
- DA-T001 limits are preserved: only a docs-only planned desktop bridge contract source document is proven;
- bridge commands remain unimplemented and uninvoked;
- arbitrary shell execution remains forbidden;
- sidecar work remains unstarted;
- package/dependency/toolchain decisions remain future decisions, not implemented changes;
- cloud, network, telemetry, auth, billing, broker/live, AI/model, updater, signing, public release, mobile, marketplace, legal/trademark, and financial advice scope remain excluded;
- status/source-index updates are bounded to DA-T002 audit-pending navigation and links;
- all DA-T002 report artifacts exist;
- no forbidden files or commands are introduced.

## Required Checks

The DA-T002 implementor must run:

- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `Test-Path -LiteralPath docs\nullforge\architecture\TAURI_SCAFFOLD_PLAN.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T002\IMPLEMENTATION_REPORT.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T002\CHANGED_FILES.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T002\TEST_RESULTS.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T002\AUDITOR_PROMPT.md`
- `rg -n "No NullForge implementation code has started|DA-T002|TAURI_SCAFFOLD_PLAN|docs-only|not.*Tauri|not.*app|not.*runtime|No bridge|arbitrary shell|\\.venv-qa-t005|python -m research_core.cli --help|python -m research_core --help|research-core --help|network|broker|live|public release" docs\nullforge\architecture\TAURI_SCAFFOLD_PLAN.md docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md reports\nullforge\DA-T002\IMPLEMENTATION_REPORT.md reports\nullforge\DA-T002\TEST_RESULTS.md`
- `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools`
- `Test-Path -LiteralPath tickets`
- `Test-Path -LiteralPath milestones`
- `Test-Path -LiteralPath prompts`

The forbidden tracked-path diff check must return no output. The `tickets`, `milestones`, and `prompts` checks must return `False`.

## Checks To Skip

The following must remain skipped with explicit reasons:

- full tests;
- docs generation or docs build;
- quickstart commands;
- CI smoke;
- install or environment commands;
- Tauri, Node, Rust, package manager, app, bridge, sidecar, or runtime commands;
- bridge smoke;
- sidecar smoke;
- any command using `python -m research_core --help` or `research-core --help`;
- any cloud/network/telemetry/auth/billing/broker/live/AI/updater/signing/public release check.

## Auditor Focus

The DA-T002 auditor should verify:

- changed files match the allowed set;
- the source document is planning-only;
- no app scaffold or package/dependency change exists;
- no bridge command implementation or arbitrary shell path is introduced;
- QA-T005 and DA-T001 claim boundaries are preserved;
- status/source navigation links resolve;
- no source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool files changed;
- no downstream ticket was started.
