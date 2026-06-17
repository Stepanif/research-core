# DA-T003R Auditor Prompt

Use this prompt to independently audit DA-T003R. Do not implement fixes. Do not commit.

```text
Independently audit DA-T003R. Do not implement fixes. Do not commit.

Ticket:
DA-T003R - Rust/Cargo toolchain availability decision

Role:
Independent Auditor.

Scope:
Audit only DA-T003R against its planner artifacts, acceptance criteria, implementation report, changed-file report, test results, auditor prompt, and active NullForge source docs.

Read:
- plans/nullforge/DA-T003R/CONTEXT_BUNDLE.md
- plans/nullforge/DA-T003R/CONTEXT_BUNDLE_MANIFEST.md
- plans/nullforge/DA-T003R/PLAN.md
- plans/nullforge/DA-T003R/ACCEPTANCE.md
- plans/nullforge/DA-T003R/IMPLEMENTOR_PROMPT.md
- docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- audits/nullforge/DA-T003/AUDIT_REPORT.md
- audits/nullforge/DA-T003/FINDINGS.md
- audits/nullforge/DA-T003/REPAIR_PROMPT.md
- reports/nullforge/DA-T003/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T003/CHANGED_FILES.md
- reports/nullforge/DA-T003/TEST_RESULTS.md
- reports/nullforge/DA-T003R/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T003R/CHANGED_FILES.md
- reports/nullforge/DA-T003R/TEST_RESULTS.md
- reports/nullforge/DA-T003R/AUDITOR_PROMPT.md

Audit focus:
- DA-T003R stayed docs-only.
- The decision source records DA-T003 audit HOLD as authority.
- The decision source records that DA-T003 stopped before scaffold creation because `rustc` and `cargo` are unavailable on PATH.
- The decision source preserves `No NullForge implementation code has started.`
- The decision source records that no `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package file, lockfile, Rust, React, TypeScript, JavaScript, CSS, or HTML app file has been created.
- The decision source recommends a separate human-approved Rust/Cargo availability action or separate scoped plan change before DA-T003 can resume.
- DA-T003R does not execute the human action and does not prove Rust/Cargo availability.
- `rustc --version` and `cargo --version` are listed only as future DA-T003 resume checks, not DA-T003R execution proof.
- No Rust/Cargo, Node, pnpm, Tauri, app, package-manager, dependency, bridge, sidecar, ResearchCore Engine, Python CLI, runtime, install, repair, test, docs build, quickstart, or CI command was run.
- QA-T005 limits are preserved: only `.venv-qa-t005` readiness for `python -m research_core.cli --help` is proven.
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them.
- DA-T001 limits are preserved: only a docs-only planned desktop bridge contract source document is proven.
- DA-T002 limits are preserved: only a docs-only Tauri scaffold plan source document is proven.
- DA-T003 limits are preserved: only a blocked pre-scaffold attempt is recorded.
- Cloud/network/telemetry/auth/billing/broker/live/AI/model/updater/signing/public release/mobile/marketplace/legal/trademark/financial advice scope remains excluded.
- Status/source-index updates are bounded and links resolve.
- No forbidden files/actions occurred.

Required outputs:
- audits/nullforge/DA-T003R/AUDIT_REPORT.md
- audits/nullforge/DA-T003R/FINDINGS.md
- audits/nullforge/DA-T003R/REPAIR_PROMPT.md

Required checks:
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- path checks for DA-T003R decision source and reports
- prior audit `Decision: PASS` checks through DA-T002 and DA-T003 audit `Decision: HOLD`
- DA-T003R content checks from `reports/nullforge/DA-T003R/AUDITOR_PROMPT.md`
- forbidden-path diff check for source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool/app files
- `Test-Path` checks for absent `apps`, `apps/nullforge-desktop`, `src-tauri`, `tickets`, `milestones`, and `prompts`

Verdict:
Return exactly one: `PASS`, `HOLD`, or `REJECT`.

Forbidden:
- implementing fixes
- installing Rust/Cargo or repairing environment
- running Rust/Cargo, Node, pnpm, Tauri, app, package-manager, dependency, bridge, sidecar, ResearchCore Engine, Python CLI, runtime, install, repair, test, docs build, quickstart, or CI commands
- creating app/package/Tauri/Rust/React/TypeScript/JavaScript/CSS/HTML files
- creating code/tests/schemas/fixtures/dependencies/package files/lockfiles/config files/CI/generated docs
- creating tickets, milestones, prompt packs, or standalone prompt files
- starting DA-T003 resume, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work
- committing
```
