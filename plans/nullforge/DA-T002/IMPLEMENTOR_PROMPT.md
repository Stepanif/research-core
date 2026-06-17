# DA-T002 Implementor Prompt

Use this prompt to implement DA-T002 only.

```text
Implement DA-T002 only. Do not commit.

Ticket:
DA-T002 - Tauri app scaffold plan

Role:
Scoped Implementor.

Mission:
Create the repo-local docs-only Tauri scaffold plan source document planned by DA-T002. Do not create a Tauri app scaffold, Rust code, React code, TypeScript code, JavaScript code, frontend files, app files, package config, dependencies, lockfiles, tests, schemas, fixtures, CI, generated docs, environment repair, bridge commands, sidecar code, runtime behavior, or downstream work.

Read first:
- plans/nullforge/DA-T002/CONTEXT_BUNDLE.md
- plans/nullforge/DA-T002/CONTEXT_BUNDLE_MANIFEST.md
- plans/nullforge/DA-T002/PLAN.md
- plans/nullforge/DA-T002/ACCEPTANCE.md
- plans/nullforge/DA-T002/IMPLEMENTOR_PROMPT.md

Allowed changes:
- docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- reports/nullforge/DA-T002/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T002/CHANGED_FILES.md
- reports/nullforge/DA-T002/TEST_RESULTS.md
- reports/nullforge/DA-T002/AUDITOR_PROMPT.md

Requirements:
- Preserve: `No NullForge implementation code has started.`
- Define DA-T002 as docs-only scaffold planning, not app/scaffold implementation.
- Preserve QA-T005 limits: only `.venv-qa-t005` readiness for `python -m research_core.cli --help` is proven.
- Keep `python -m research_core --help` and `research-core --help` unsupported unless a later source/package ticket changes them.
- Preserve DA-T001 limits: only a docs-only planned desktop bridge contract source document is proven; no bridge/app/sidecar/Tauri/package/runtime behavior is implemented or proven.
- Keep the bridge boundary narrow: no bridge command implementation, no bridge command invocation, no arbitrary shell execution, no sidecar work.
- Mark package manager, Tauri version, Rust toolchain, frontend scaffold shape, generated files, permissions, and smoke commands as future DA-T003 decisions unless already proven by a later scoped source.
- Exclude cloud/network/telemetry/auth/billing/broker/live/AI/model/updater/signing/public release/mobile/marketplace/legal/trademark/financial advice scope.
- Update status/source navigation only to DA-T002 implementation pending independent audit.

Run:
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- required path/content checks from `plans/nullforge/DA-T002/ACCEPTANCE.md`

Forbidden:
- code, tests, schemas, fixtures, dependencies, package files, lockfiles, config files, CI, generated docs, README, docs-reference, tools
- app files, frontend files, `src-tauri/`, Rust, React, TypeScript, JavaScript, CSS, HTML
- install/environment commands
- Tauri/Node/Rust/package-manager/app/bridge/sidecar/runtime commands
- creating audits, tickets, milestones, prompt packs, or standalone prompt files outside the allowed DA-T002 report `AUDITOR_PROMPT.md`
- starting DA-T003, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work

Do not commit unless explicitly asked.
```
