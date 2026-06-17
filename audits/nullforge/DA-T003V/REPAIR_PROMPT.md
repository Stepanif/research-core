# DA-T003V Repair Prompt

No repair is required for DA-T003V because the audit decision is PASS.

Use this prompt only if a later human review finds drift from the DA-T003V audit result and explicitly asks for a bounded DA-T003V repair.

```text
Repair DA-T003V only. Do not commit unless explicitly asked.

Scope:
- Repair only the specific DA-T003V audit drift identified by the human reviewer.
- Preserve that DA-T003V records only historical human-provided negative Rust/Cargo evidence from 2026-06-17 2:28 PM ET.
- Preserve that DA-T003V did not run Codex-side Rust/Cargo probes, install Rust/Cargo, repair PATH, repair environment state, prove Rust/Cargo availability, resume DA-T003, create an app scaffold, create package/dependency artifacts, or prove runtime behavior.
- Preserve that DA-T003S later setup evidence is setup evidence only, not a DA-T003V contradiction and not DA-T003 resume proof.
- Preserve: No NullForge implementation code has started.
- Preserve QA-T005, DA-T001, DA-T002, DA-T003, DA-T003R, DA-T003H, DA-T003V, and DA-T003S claim boundaries.

Allowed files:
- reports/nullforge/DA-T003V/EVIDENCE_RECORD.md
- reports/nullforge/DA-T003V/CHANGED_FILES.md
- reports/nullforge/DA-T003V/TEST_RESULTS.md
- reports/nullforge/DA-T003V/AUDITOR_PROMPT.md
- audits/nullforge/DA-T003V/AUDIT_REPORT.md
- audits/nullforge/DA-T003V/FINDINGS.md
- audits/nullforge/DA-T003V/REPAIR_PROMPT.md
- docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md

Forbidden:
- installing Rust/Cargo
- repairing PATH or environment variables
- running rustc --version
- running cargo --version
- running node, pnpm, Tauri, package-manager, dependency, install, build, app, bridge, sidecar, runtime, ResearchCore Engine, Python CLI, test, docs build, quickstart, or CI commands
- creating apps/, apps/nullforge-desktop/, src-tauri/, package files, lockfiles, Rust, React, TypeScript, JavaScript, CSS, or HTML files
- creating source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool changes
- bridge command implementation or invocation
- ResearchCore Engine invocation
- sidecar behavior
- creating tickets, milestones, prompt packs, or standalone prompt files
- starting DA-T003 resume, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work

Required checks:
- git status --short --untracked-files=all
- git diff --name-only
- git diff --check
- forbidden-path diff check for source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool/app files
- Test-Path checks for absent apps, apps/nullforge-desktop, src-tauri, tickets, milestones, and prompts
```
