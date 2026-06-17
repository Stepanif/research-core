# DA-T003H Auditor Prompt

Use this prompt to independently audit DA-T003H. Do not implement fixes. Do not commit.

```text
Independently audit DA-T003H. Do not implement fixes. Do not commit.

Ticket:
DA-T003H - Human Rust/Cargo availability gate

Role:
Independent Auditor.

Scope:
Audit only DA-T003H against its planner artifacts, acceptance criteria, implementation report, changed-file report, test results, auditor prompt, DA-T003 blocker authority, DA-T003R decision authority, and active NullForge source docs.

Read:
- plans/nullforge/DA-T003H/CONTEXT_BUNDLE.md
- plans/nullforge/DA-T003H/CONTEXT_BUNDLE_MANIFEST.md
- plans/nullforge/DA-T003H/PLAN.md
- plans/nullforge/DA-T003H/ACCEPTANCE.md
- plans/nullforge/DA-T003H/IMPLEMENTOR_PROMPT.md
- docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md
- docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- audits/nullforge/DA-T003/AUDIT_REPORT.md
- audits/nullforge/DA-T003/FINDINGS.md
- audits/nullforge/DA-T003/REPAIR_PROMPT.md
- audits/nullforge/DA-T003R/AUDIT_REPORT.md
- audits/nullforge/DA-T003R/FINDINGS.md
- reports/nullforge/DA-T003/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T003/CHANGED_FILES.md
- reports/nullforge/DA-T003/TEST_RESULTS.md
- reports/nullforge/DA-T003H/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T003H/CHANGED_FILES.md
- reports/nullforge/DA-T003H/TEST_RESULTS.md
- reports/nullforge/DA-T003H/AUDITOR_PROMPT.md

Audit focus:
- DA-T003H stayed docs-only.
- The gate source records DA-T003 audit HOLD as blocker authority.
- The gate source records DA-T003R audit PASS and the Rust/Cargo decision source as decision authority.
- The gate source records that DA-T003 stopped before scaffold creation because `rustc` and `cargo` are unavailable on PATH.
- The gate source preserves `No NullForge implementation code has started.`
- The gate source records that no `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package file, lockfile, Rust, React, TypeScript, JavaScript, CSS, or HTML app file has been created.
- The gate source defines a human-only Rust/Cargo availability checklist and does not claim toolchain availability.
- DA-T003H did not execute the human action and does not prove Rust/Cargo availability.
- `rustc --version` and `cargo --version` are listed only as human-recorded external observations or future DA-T003 resume checks, not DA-T003H execution proof.
- No Rust/Cargo, Node, pnpm, Tauri, app, package-manager, dependency, bridge, sidecar, ResearchCore Engine, Python CLI, runtime, install, repair, test, docs build, quickstart, or CI command was run.
- QA-T005 limits are preserved: only `.venv-qa-t005` readiness for `python -m research_core.cli --help` is proven.
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them.
- DA-T001 limits are preserved: only a docs-only planned desktop bridge contract source document is proven.
- DA-T002 limits are preserved: only a docs-only Tauri scaffold plan source document is proven.
- DA-T003 limits are preserved: only a blocked pre-scaffold attempt is recorded.
- DA-T003R limits are preserved: only a docs-only Rust/Cargo toolchain availability decision source is proven.
- Cloud/network/telemetry/auth/billing/broker/live/AI/model/updater/signing/public release/mobile/marketplace/legal/trademark/financial advice scope remains excluded.
- Status/source-index updates are bounded and links resolve.
- No forbidden files/actions occurred.

Required outputs:
- audits/nullforge/DA-T003H/AUDIT_REPORT.md
- audits/nullforge/DA-T003H/FINDINGS.md
- audits/nullforge/DA-T003H/REPAIR_PROMPT.md

Required checks:
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- path checks for DA-T003H gate source and reports
- checks that `apps`, `apps/nullforge-desktop`, and `src-tauri` are absent
- prior audit checks: QA-T005 `PASS`, DA-T001 `PASS`, DA-T002 `PASS`, DA-T003 `HOLD`, DA-T003R `PASS`
- DA-T003H content checks from `reports/nullforge/DA-T003H/AUDITOR_PROMPT.md`
- forbidden-path diff check for source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool/app files
- `Test-Path` checks for absent `tickets`, `milestones`, and `prompts`

Verdict:
Return exactly one: `PASS`, `HOLD`, or `REJECT`.

Expected verdict:
PASS, unless the auditor finds forbidden changes, missing required artifacts, unresolved acceptance gaps, false proof claims, or forbidden commands.

Forbidden:
- implementing fixes
- installing Rust/Cargo
- running `rustup`
- running `cargo install`
- repairing PATH or environment variables
- running `rustc --version`
- running `cargo --version`
- running `node`, `pnpm`, Tauri, package-manager, dependency, install, build, app, bridge, sidecar, runtime, ResearchCore Engine, Python CLI, test, docs build, quickstart, or CI commands
- creating `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package files, lockfiles, Rust, React, TypeScript, JavaScript, CSS, or HTML files
- creating code/tests/schemas/fixtures/dependencies/package files/CI/generated docs
- bridge command implementation or invocation
- ResearchCore Engine invocation
- sidecar behavior
- creating tickets, milestones, prompt packs, or standalone prompt files
- starting DA-T003 resume, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work
- committing
```
