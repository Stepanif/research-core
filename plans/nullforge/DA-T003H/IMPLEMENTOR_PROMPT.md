# DA-T003H Implementor Prompt

Use this prompt to implement DA-T003H only. Do not commit.

```text
Implement DA-T003H only. Do not commit.

Ticket:
DA-T003H - Human Rust/Cargo availability gate

Role:
Scoped Implementor.

Mission:
Create the repo-local docs-only human Rust/Cargo availability gate source document planned by DA-T003H. This ticket records the human-only action/checklist needed before DA-T003 can resume. It must not install Rust/Cargo, repair PATH, repair environment state, rerun Rust/Cargo probes, create app/package/Tauri/Rust/React/TypeScript/JavaScript/CSS/HTML files, modify package config, run dependency commands, run Tauri/Node/Rust app commands, prove Rust/Cargo availability, or resume DA-T003 implementation.

Read first:
- plans/nullforge/DA-T003H/CONTEXT_BUNDLE.md
- plans/nullforge/DA-T003H/CONTEXT_BUNDLE_MANIFEST.md
- plans/nullforge/DA-T003H/PLAN.md
- plans/nullforge/DA-T003H/ACCEPTANCE.md
- plans/nullforge/DA-T003H/IMPLEMENTOR_PROMPT.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md
- audits/nullforge/DA-T003/AUDIT_REPORT.md
- audits/nullforge/DA-T003/FINDINGS.md
- audits/nullforge/DA-T003/REPAIR_PROMPT.md
- audits/nullforge/DA-T003R/AUDIT_REPORT.md
- audits/nullforge/DA-T003R/FINDINGS.md
- reports/nullforge/DA-T003/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T003/CHANGED_FILES.md
- reports/nullforge/DA-T003/TEST_RESULTS.md

Allowed changes:
- docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- reports/nullforge/DA-T003H/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T003H/CHANGED_FILES.md
- reports/nullforge/DA-T003H/TEST_RESULTS.md
- reports/nullforge/DA-T003H/AUDITOR_PROMPT.md

Requirements:
- Preserve: `No NullForge implementation code has started.`
- Define DA-T003H as docs-only human Rust/Cargo availability gate recording, not Rust/Cargo installation, PATH repair, environment repair, toolchain verification, or DA-T003 resume.
- Use `audits/nullforge/DA-T003/AUDIT_REPORT.md` and `audits/nullforge/DA-T003/FINDINGS.md` as DA-T003 blocker authority.
- Use `docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md` and `audits/nullforge/DA-T003R/AUDIT_REPORT.md` as DA-T003R decision authority.
- Record that DA-T003 stopped before scaffold creation because `rustc` and `cargo` are unavailable on PATH.
- Record that no `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package file, lockfile, Rust, React, TypeScript, JavaScript, CSS, or HTML app file has been created.
- Recommend a separate human-only Rust/Cargo availability action or separate scoped plan change before DA-T003 can resume.
- Include checklist fields for a human to record date, actor, method category, PATH visibility note, and observed `rustc --version` / `cargo --version` outputs.
- Make clear that DA-T003H does not execute the human action and does not prove Rust/Cargo availability.
- List `rustc --version` and `cargo --version` only as human-recorded external observations or future DA-T003 resume checks, not as commands run by DA-T003H.
- Preserve QA-T005 limits: only `.venv-qa-t005` readiness for `python -m research_core.cli --help` is proven.
- Keep `python -m research_core --help` and `research-core --help` unsupported unless a later source/package ticket changes them.
- Preserve DA-T001 limits: only a docs-only planned desktop bridge contract source document is proven.
- Preserve DA-T002 limits: only a docs-only Tauri scaffold plan source document is proven.
- Preserve DA-T003 limits: only a blocked pre-scaffold attempt is recorded.
- Preserve DA-T003R limits: only a docs-only Rust/Cargo toolchain availability decision source is proven.
- Exclude cloud/network/telemetry/auth/billing/broker/live/AI/model/updater/signing/public release/mobile/marketplace/legal/trademark/financial advice scope.
- Update status/source navigation only to DA-T003H implementation pending independent audit.

Run:
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- required path/content/forbidden-path checks from `plans/nullforge/DA-T003H/ACCEPTANCE.md`

Forbidden:
- installing Rust/Cargo
- running `rustup`
- running `cargo install`
- repairing PATH or environment variables
- running `rustc --version`
- running `cargo --version`
- running `node`, `pnpm`, Tauri, package-manager, dependency, install, build, app, bridge, sidecar, runtime, ResearchCore Engine, Python CLI, test, docs build, quickstart, or CI commands
- creating `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package files, lockfiles, Rust, React, TypeScript, JavaScript, CSS, or HTML files
- root package/workspace/Cargo files
- source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool changes
- bridge command implementation or invocation
- ResearchCore Engine invocation
- sidecar behavior
- creating audits, tickets, milestones, prompt packs, or standalone prompt files outside the allowed DA-T003H report `AUDITOR_PROMPT.md`
- starting DA-T003 resume, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work

Do not commit unless explicitly asked.
```
