# DA-T003H Repair Prompt

No DA-T003H repair is required. The independent audit decision is `PASS`.

Use this prompt only if later drift is found in DA-T003H. Do not use it to install Rust/Cargo, repair PATH, repair environment state, run Rust/Cargo probes, prove Rust/Cargo availability, resume DA-T003, create app/package/Tauri/Rust/React/TypeScript/JavaScript/CSS/HTML files, run dependency commands, run Tauri/Node/Rust app commands, or start downstream work.

```text
Repair DA-T003H only if later drift is found. Do not commit unless explicitly asked.

Ticket:
DA-T003H - Human Rust/Cargo availability gate

Role:
Scoped Repair Implementor.

Audit authority:
- audits/nullforge/DA-T003H/AUDIT_REPORT.md
- audits/nullforge/DA-T003H/FINDINGS.md

Mission:
Repair only bounded DA-T003H documentation drift while preserving the audit PASS boundaries. DA-T003H is docs-only human gate recording. It is not Rust/Cargo installation, PATH repair, environment repair, Rust/Cargo verification, DA-T003 resume, app scaffold creation, package configuration, dependency resolution, Tauri launch proof, bridge implementation, sidecar work, or runtime behavior.

Allowed repair paths:
- docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- reports/nullforge/DA-T003H/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T003H/CHANGED_FILES.md
- reports/nullforge/DA-T003H/TEST_RESULTS.md
- reports/nullforge/DA-T003H/AUDITOR_PROMPT.md
- audits/nullforge/DA-T003H/AUDIT_REPORT.md
- audits/nullforge/DA-T003H/FINDINGS.md
- audits/nullforge/DA-T003H/REPAIR_PROMPT.md

Preserve:
- `No NullForge implementation code has started.`
- DA-T003 remains blocked with audit `HOLD` until a separate human-approved action makes `rustc` and `cargo` available on PATH, or a separate scoped plan changes DA-T003.
- DA-T003H proves only a docs-only human Rust/Cargo availability gate source.
- DA-T003H does not prove Rust/Cargo availability.
- `rustc --version` and `cargo --version` are only human-recorded external observations or future DA-T003 resume checks, not DA-T003H execution proof.
- QA-T005 proves only `.venv-qa-t005` readiness for `python -m research_core.cli --help`.
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them.
- DA-T001 proves only a docs-only planned desktop bridge contract source document.
- DA-T002 proves only a docs-only Tauri scaffold plan source document.
- DA-T003 proves only a blocked pre-scaffold attempt.
- DA-T003R proves only a docs-only Rust/Cargo toolchain availability decision source.

Forbidden:
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
- creating tickets, milestones, prompt packs, or standalone prompt files
- starting DA-T003 resume, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work
```
