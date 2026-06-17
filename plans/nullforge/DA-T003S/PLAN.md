# DA-T003S Plan

Date: `2026-06-17`

Ticket: `DA-T003S - Human-gated Rust/Cargo setup path`

Role: Context Curator + Planner

No NullForge implementation code has started.

## Objective

Plan the minimum human-gated path for making `rustc` and `cargo` available on PATH for Windows 11 x64, so a later scoped verification and DA-T003 resume can proceed if still in scope.

DA-T003S is planning-only. It must not install Rust/Cargo, repair PATH, run Rust/Cargo probes, create app files, run app/package-manager/dependency commands, or resume DA-T003.

## Planned Implementation Target

The future DA-T003S implementor should create a docs-only setup path source:

```text
docs/nullforge/qa/RUST_CARGO_SETUP_PATH.md
```

The source should plan the human-gated setup process. It should not execute setup commands or claim toolchain availability.

## Required Source Content

The setup path source should include:

- ticket ID `DA-T003S`;
- purpose and scope;
- source authority list;
- DA-T003 blocker summary;
- DA-T003R decision summary;
- DA-T003H gate summary;
- DA-T003V negative evidence summary;
- explicit no-code sentence: `No NullForge implementation code has started.`;
- explicit statement that DA-T003 remains blocked;
- minimum desired setup outcome: both `rustc` and `cargo` discoverable on PATH in a future verifier shell;
- human approval and safety gates;
- candidate setup paths;
- future verifier commands listed as future-only checks;
- stop conditions;
- claim boundaries and excluded scope;
- auditor prompt for the setup path source.

## Candidate Setup Paths To Plan

The setup path source should describe these candidate paths without executing them:

1. Existing local Rust/Cargo installation made visible on PATH.
2. Human-approved Rust/Cargo installation using a trusted Rust toolchain source selected by the human.
3. Separate scoped plan or ADR change if Rust/Cargo setup is not approved or cannot be completed.

The preferred minimum path is to make an existing trusted local installation visible to the shell if one already exists. If no local installation exists, the source should require a separate human-approved setup action and should not hard-code an installer source unless that later prompt explicitly authorizes it.

## Future Verification Boundary

Future verification belongs to a separate scoped ticket after setup, not DA-T003S planning.

Future verifier commands may include only:

- `where.exe rustc`
- `where.exe cargo`
- `rustc --version`
- `cargo --version`

If any command still fails, the verifier must record renewed blocker evidence and must not resume DA-T003.

If all commands pass, a later DA-T003 resume ticket may decide whether to continue the existing DA-T003 scaffold scope. Verification alone must not create app files or run Tauri/package commands.

## Allowed DA-T003S Implementor Changes

The future DA-T003S implementor may create or update only:

- `docs/nullforge/qa/RUST_CARGO_SETUP_PATH.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T003S/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003S/CHANGED_FILES.md`
- `reports/nullforge/DA-T003S/TEST_RESULTS.md`
- `reports/nullforge/DA-T003S/AUDITOR_PROMPT.md`

No other tracked files should change.

## Implementation Steps For Future DA-T003S Implementor

1. Re-read DA-T003S planner artifacts.
2. Re-read current status/source docs.
3. Re-read DA-T003 audit `HOLD`, DA-T003 findings, DA-T003R decision source, DA-T003H gate/audit source, and DA-T003V evidence.
4. Confirm worktree state with `git status --short --untracked-files=all`.
5. Create `docs/nullforge/qa/RUST_CARGO_SETUP_PATH.md` as a docs-only setup path source.
6. Update status/source navigation only to DA-T003S implementation pending independent audit.
7. Create DA-T003S reports.
8. Run documentation-safe checks only.
9. Do not commit unless explicitly asked.

## Forbidden Work

The DA-T003S planner and future setup-path implementor must not:

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
- create `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package files, lockfiles, Rust files, React files, TypeScript files, JavaScript files, CSS files, or HTML files;
- modify source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool files;
- create tickets, milestones, prompt packs, audits, fixtures, schemas, tests, CI, generated docs, README, docs/reference, or tools;
- implement or invoke bridge commands;
- invoke ResearchCore Engine;
- package or launch a sidecar;
- start DA-T003 resume, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work;
- add cloud, network, telemetry, auth, billing, broker/live, AI/model, updater, signing, public release, mobile, marketplace, legal/trademark, or financial advice scope.

## Checks To Require

DA-T003S implementation must run only documentation-safe checks:

- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `Test-Path -LiteralPath docs\nullforge\qa\RUST_CARGO_SETUP_PATH.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003S\IMPLEMENTATION_REPORT.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003S\CHANGED_FILES.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003S\TEST_RESULTS.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T003S\AUDITOR_PROMPT.md`
- `Test-Path -LiteralPath apps`
- `Test-Path -LiteralPath apps\nullforge-desktop`
- `Test-Path -LiteralPath src-tauri`
- `Test-Path -LiteralPath package.json`
- `Test-Path -LiteralPath pnpm-lock.yaml`
- `Test-Path -LiteralPath Cargo.toml`
- `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml Cargo.toml .github README.md docs\reference tools apps src-tauri`
- `Test-Path -LiteralPath tickets`
- `Test-Path -LiteralPath milestones`
- `Test-Path -LiteralPath prompts`

## Risk Controls

- DA-T003S cannot itself unblock DA-T003.
- DA-T003V is negative evidence and pending audit; if its audit result changes, the future DA-T003S implementor must reconcile that before proceeding.
- Setup source must not assume Codex PATH visibility until a later scoped verifier proves it.
- Any setup action that writes outside the repository or changes user/system PATH requires explicit human approval in a later scoped prompt.
- Any network download or installer execution requires explicit human approval in a later scoped prompt.
- App scaffold work remains separate from Rust/Cargo setup.

## Done Definition

DA-T003S planning is done when:

- `plans/nullforge/DA-T003S/CONTEXT_BUNDLE.md` exists;
- `plans/nullforge/DA-T003S/CONTEXT_BUNDLE_MANIFEST.md` exists;
- `plans/nullforge/DA-T003S/PLAN.md` exists;
- `plans/nullforge/DA-T003S/ACCEPTANCE.md` exists;
- `plans/nullforge/DA-T003S/IMPLEMENTOR_PROMPT.md` exists;
- the plan is human-gated and setup-only;
- no setup/probe/app/package/dependency/test/docs/runtime/downstream command is run;
- documentation-safe checks pass;
- no commit is created unless separately requested.
