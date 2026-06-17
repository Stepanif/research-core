# DA-T002 Plan

Date: `2026-06-17`

Ticket: `DA-T002 - Tauri app scaffold plan`

Role: Context Curator + Planner

No NullForge implementation code has started.

## Objective

Plan a docs-only source document for the future minimal Windows/Tauri shell scaffold. DA-T002 implementation should create the source document and handoff reports only; it must not create app scaffold files or run app/toolchain commands.

## Planned Implementation Target

The DA-T002 implementor should create:

```text
docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md
```

The document should describe the bounded future scaffold plan for DA-T003. It must not create or prove a Tauri app.

## Allowed Implementor Changes

- `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T002/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T002/CHANGED_FILES.md`
- `reports/nullforge/DA-T002/TEST_RESULTS.md`
- `reports/nullforge/DA-T002/AUDITOR_PROMPT.md`

No other files should change.

## Required Source Document Content

`TAURI_SCAFFOLD_PLAN.md` should include:

- ticket/date/status and the exact claim sentence `No NullForge implementation code has started.`;
- authority from ADR-T001, ADR-T002, DA-T001 bridge contract, Volume 3, Volume 7, QA-T005, and DA-T001 audit `PASS`;
- clear statement that DA-T002 is docs-only and not Tauri/app/scaffold/runtime proof;
- future minimal shell scaffold goal for DA-T003;
- future scaffold non-goals;
- planned future shell boundaries:
  - Windows 11 x64 first;
  - Tauri + React/TypeScript direction only;
  - selected local workspace as later boundary;
  - no bridge commands in DA-T002;
  - no sidecar in DA-T002;
  - no arbitrary shell execution;
  - no cloud/network/telemetry/auth/billing/broker/live/AI/updater/signing/public release scope;
- planned future DA-T003 decisions that remain unresolved:
  - package manager;
  - Tauri version;
  - Rust toolchain;
  - frontend scaffold shape;
  - exact commands to run;
  - exact generated files;
  - permission configuration;
  - smoke check;
- human gates before any later scaffold implementation;
- future audit focus for DA-T003.

## Implementation Steps

1. Re-read the DA-T002 planner artifacts.
2. Create `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md` as a docs-only source document.
3. Update `docs/nullforge/CURRENT_STATUS.md` to reflect DA-T002 implemented and pending independent audit.
4. Update `docs/nullforge/SOURCE_INDEX.md` to link the DA-T002 source document and DA-T002 report artifacts that exist.
5. Create DA-T002 reports under `reports/nullforge/DA-T002/`.
6. Run only the allowed read-only Git, path, and content checks listed in `ACCEPTANCE.md`.
7. Do not commit unless separately instructed.

## Forbidden Work

The DA-T002 implementor must not:

- create app files, `src-tauri/`, frontend folders, Rust, React, TypeScript, JavaScript, CSS, HTML, package files, lockfiles, config files, dependency files, schemas, tests, fixtures, generated docs, CI, tools, README, or docs/reference files;
- run Tauri, Node, Rust, package manager, install, environment, test, docs build, quickstart, CI, bridge, sidecar, app, or runtime commands;
- create bridge commands or sidecar behavior;
- alter ResearchCore Engine code, package metadata, CLI behavior, generated references, schemas, tests, fixtures, or docs/reference;
- create audits, tickets, milestones, prompt packs, DA-T003, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work;
- claim that a desktop app, Tauri shell, scaffold, bridge, sidecar, package, permission boundary, network absence, telemetry blocking, public release, product, market, trading, or financial advice behavior is implemented or proven.

## Status And Navigation Expectations

`CURRENT_STATUS.md` should move to a DA-T002 audit-pending state only after the source document is created. It should preserve:

- `No NullForge implementation code has started.`
- QA-T005 proof is limited to `.venv-qa-t005` readiness for `python -m research_core.cli --help`.
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them.
- DA-T001 proof is limited to a docs-only planned desktop bridge contract source document.
- DA-T002 proof is limited to a docs-only Tauri scaffold plan source document.

`SOURCE_INDEX.md` should add DA-T002 source/report links only for files that exist.

## Risk Controls

- Treat Tauri/React/Rust/package manager details as planned future decisions, not current repo state.
- Keep DA-T003 blocked until DA-T002 independent audit disposition and a separate human prompt.
- Keep all bridge command execution deferred to DA-T004 or later.
- Keep all package/dependency/toolchain installation deferred to a later implementation ticket with explicit human approval.
- Keep all cloud/network/telemetry/auth/billing/broker/live/AI/updater/signing/public release scope excluded.

## Done Definition

DA-T002 implementation is done when:

- the docs-only scaffold plan source exists;
- status/source navigation is bounded and audit-pending;
- DA-T002 reports exist;
- required checks pass;
- no forbidden files or commands are introduced;
- no implementation proof is claimed.
