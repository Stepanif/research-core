# DA-T003R Repair Prompt

DA-T003R audit decision: `PASS`.

No repair is required.

Use this prompt only if later drift is found in DA-T003R status, source navigation, decision-source wording, or report scope. Do not use it to install Rust/Cargo, repair PATH, repair environment state, rerun Rust/Cargo probes, resume DA-T003, create app/package/Tauri/Rust/React/TypeScript/JavaScript/CSS/HTML files, run dependency commands, run runtime commands, or start downstream work.

```text
Repair DA-T003R only. Do not commit unless explicitly asked.

Ticket:
DA-T003R - Rust/Cargo toolchain availability decision

Role:
Scoped Repair Implementor.

Audit authority:
- audits/nullforge/DA-T003R/AUDIT_REPORT.md
- audits/nullforge/DA-T003R/FINDINGS.md

Mission:
Repair only bounded documentation drift in DA-T003R artifacts if a later audit or closeout step identifies it. Keep DA-T003R docs-only.

Allowed repair targets:
- docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- reports/nullforge/DA-T003R/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T003R/CHANGED_FILES.md
- reports/nullforge/DA-T003R/TEST_RESULTS.md
- reports/nullforge/DA-T003R/AUDITOR_PROMPT.md
- audits/nullforge/DA-T003R/AUDIT_REPORT.md
- audits/nullforge/DA-T003R/FINDINGS.md
- audits/nullforge/DA-T003R/REPAIR_PROMPT.md

Preserve:
- No NullForge implementation code has started.
- DA-T003R is docs-only toolchain availability decisioning.
- DA-T003 remains blocked until a separate human-approved action makes `rustc` and `cargo` available on PATH, or a separate scoped plan changes DA-T003.
- DA-T003R does not execute that human action and does not prove Rust/Cargo availability.
- `rustc --version` and `cargo --version` are future DA-T003 resume checks only, not DA-T003R proof.
- No `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package file, lockfile, Rust, React, TypeScript, JavaScript, CSS, or HTML app file has been created.
- QA-T005 proves only `.venv-qa-t005` readiness for `python -m research_core.cli --help`.
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them.
- DA-T001 proves only a docs-only planned desktop bridge contract source document.
- DA-T002 proves only a docs-only Tauri scaffold plan source document.
- DA-T003 proves only a blocked pre-scaffold attempt.

Forbidden:
- installing Rust/Cargo
- running `rustup`
- running `cargo install`
- repairing PATH or environment variables
- running `rustc --version`
- running `cargo --version`
- running Node, pnpm, Tauri, package-manager, dependency, install, build, app, bridge, sidecar, runtime, ResearchCore Engine, Python CLI, test, docs build, quickstart, or CI commands
- creating app/package/Tauri/Rust/React/TypeScript/JavaScript/CSS/HTML files
- source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool changes
- bridge command implementation or invocation
- ResearchCore Engine invocation
- sidecar behavior
- creating tickets, milestones, prompt packs, or standalone prompt files
- starting DA-T003 resume, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work
```
