# DA-T003V Auditor Prompt

Use this prompt to independently audit DA-T003V. Do not implement fixes. Do not commit.

```text
Independently audit DA-T003V. Do not implement fixes. Do not commit.

Ticket:
DA-T003V - Human Rust/Cargo availability evidence

Role:
Independent Auditor.

Scope:
Audit only DA-T003V against the human evidence record, changed-file report, test results, active status/source docs, DA-T003 blocker authority, DA-T003R decision source, and DA-T003H gate/audit source.

Read:
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md
- docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md
- audits/nullforge/DA-T003/AUDIT_REPORT.md
- audits/nullforge/DA-T003/FINDINGS.md
- audits/nullforge/DA-T003H/AUDIT_REPORT.md
- reports/nullforge/DA-T003V/EVIDENCE_RECORD.md
- reports/nullforge/DA-T003V/CHANGED_FILES.md
- reports/nullforge/DA-T003V/TEST_RESULTS.md
- reports/nullforge/DA-T003V/AUDITOR_PROMPT.md

Audit focus:
- DA-T003V stayed docs-only.
- DA-T003V records only human-provided evidence and does not execute verification commands.
- Human evidence is negative: `rustc` and `cargo` remain unavailable from human local PowerShell.
- DA-T003 remains blocked and is not ready to resume.
- DA-T003V does not prove Rust/Cargo availability, Codex PATH correctness, Tauri app scaffold, package/dependency readiness, bridge behavior, sidecar behavior, runtime behavior, or public release readiness.
- `No NullForge implementation code has started.` remains preserved.
- No `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package file, lockfile, Rust, React, TypeScript, JavaScript, CSS, or HTML app file was created.
- QA-T005 limits are preserved: only `.venv-qa-t005` readiness for `python -m research_core.cli --help` is proven.
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them.
- DA-T001, DA-T002, DA-T003, DA-T003R, and DA-T003H limits are preserved.
- Cloud/network/telemetry/auth/billing/broker/live/AI/updater/signing/public release/mobile/marketplace/legal/trademark/financial advice scope remains excluded.
- Status/source-index updates are bounded and links resolve.
- No forbidden files/actions occurred.

Required outputs:
- audits/nullforge/DA-T003V/AUDIT_REPORT.md
- audits/nullforge/DA-T003V/FINDINGS.md
- audits/nullforge/DA-T003V/REPAIR_PROMPT.md

Required checks:
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- path checks for DA-T003V reports
- content checks for negative human Rust/Cargo evidence and preserved claim boundaries
- forbidden-path diff check for source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool/app files
- `Test-Path` checks for absent `apps`, `apps/nullforge-desktop`, `src-tauri`, package files, lockfiles, `tickets`, `milestones`, and `prompts`

Verdict:
Return exactly one: `PASS`, `HOLD`, or `REJECT`.

Expected verdict:
PASS if DA-T003V accurately records the negative human evidence and preserves DA-T003 as blocked. This PASS would not unblock DA-T003.

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
- creating source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool changes
- bridge command implementation or invocation
- ResearchCore Engine invocation
- sidecar behavior
- starting DA-T003 resume, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work
- committing
```
