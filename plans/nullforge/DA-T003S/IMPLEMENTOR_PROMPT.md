# DA-T003S Implementor Prompt

Use this prompt to implement DA-T003S only. Do not commit.

```text
Implement DA-T003S only. Do not commit.

Ticket:
DA-T003S - Human-gated Rust/Cargo setup path

Role:
Scoped Implementor.

Mission:
Create the repo-local docs-only Rust/Cargo setup path source document planned by DA-T003S. This ticket records the human-gated setup path needed before any future Rust/Cargo verification or DA-T003 resume. It must not install Rust/Cargo, repair PATH, repair environment state, run Rust/Cargo probes, run Node/pnpm/Tauri/app/package-manager/dependency commands, create app/package/Tauri/Rust/React/TypeScript/JavaScript/CSS/HTML files, modify package config, prove Rust/Cargo availability, prove runtime behavior, or resume DA-T003.

Read first:
- plans/nullforge/DA-T003S/CONTEXT_BUNDLE.md
- plans/nullforge/DA-T003S/CONTEXT_BUNDLE_MANIFEST.md
- plans/nullforge/DA-T003S/PLAN.md
- plans/nullforge/DA-T003S/ACCEPTANCE.md
- plans/nullforge/DA-T003S/IMPLEMENTOR_PROMPT.md
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

Allowed changes:
- docs/nullforge/qa/RUST_CARGO_SETUP_PATH.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- reports/nullforge/DA-T003S/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T003S/CHANGED_FILES.md
- reports/nullforge/DA-T003S/TEST_RESULTS.md
- reports/nullforge/DA-T003S/AUDITOR_PROMPT.md

Requirements:
- Preserve: `No NullForge implementation code has started.`
- Define DA-T003S as docs-only Rust/Cargo setup path planning, not setup execution.
- Use DA-T003 audit `HOLD` and findings as blocker authority.
- Use DA-T003R as decision authority.
- Use DA-T003H as human gate authority.
- Use DA-T003V as negative human evidence pending independent audit unless a later audit disposition changes it.
- Record that DA-T003 remains blocked.
- Record that `rustc` and `cargo` are still unavailable based on DA-T003V human evidence.
- Define a human-gated setup path for Windows 11 x64.
- Prefer existing trusted local Rust/Cargo installation made visible on PATH if available; otherwise require a separate human-approved trusted toolchain source.
- List `where.exe rustc`, `where.exe cargo`, `rustc --version`, and `cargo --version` only as future verifier checks, not DA-T003S executed checks.
- Make clear that DA-T003S does not prove Rust/Cargo availability, Codex PATH correctness, Tauri app scaffold, package/dependency readiness, bridge behavior, sidecar behavior, runtime behavior, or public release readiness.
- Preserve QA-T005 limits: only `.venv-qa-t005` readiness for `python -m research_core.cli --help` is proven.
- Keep `python -m research_core --help` and `research-core --help` unsupported unless a later source/package ticket changes them.
- Preserve DA-T001, DA-T002, DA-T003, DA-T003R, DA-T003H, and DA-T003V limits.
- Exclude app scaffold, Tauri runtime, package/dependency work, bridge/sidecar work, tests, docs build, CI, cloud/network/telemetry/auth/billing/broker/live/AI/updater/signing/public release/mobile/marketplace/legal/trademark/financial advice scope.
- Update status/source navigation only to DA-T003S implementation pending independent audit.

Run:
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- required path/content/forbidden-path checks from `plans/nullforge/DA-T003S/ACCEPTANCE.md`

Forbidden:
- installing Rust/Cargo
- running `rustup`
- running `cargo install`
- downloading installers
- repairing PATH or environment variables
- running `where.exe rustc`
- running `where.exe cargo`
- running `rustc --version`
- running `cargo --version`
- running `node`, `pnpm`, Tauri, package-manager, dependency, install, build, app, bridge, sidecar, runtime, ResearchCore Engine, Python CLI, test, docs build, quickstart, or CI commands
- creating `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package files, lockfiles, Rust, React, TypeScript, JavaScript, CSS, or HTML files
- source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool changes
- bridge command implementation or invocation
- ResearchCore Engine invocation
- sidecar behavior
- starting DA-T003 resume, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work
- committing unless explicitly asked
```
