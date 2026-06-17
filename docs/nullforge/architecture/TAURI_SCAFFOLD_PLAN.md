# NullForge Tauri Scaffold Plan

Date: `2026-06-17`

Ticket: `DA-T002`

Status: DA-T002 source complete; audit `PASS`.

No NullForge implementation code has started.

## Authority And Scope

This document is the repo-local docs-only scaffold plan source for a future minimal Windows/Tauri shell scaffold.

It is derived from:

- `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`
- `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`
- `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_EXECUTION.md`
- `audits/nullforge/QA-T005/AUDIT_REPORT.md`
- `audits/nullforge/DA-T001/AUDIT_REPORT.md`
- `audits/nullforge/DA-T002/AUDIT_REPORT.md`

Existing ResearchCore Engine docs, code, package metadata, schemas, tests, CLI behavior, and generated references remain authoritative for current engine behavior.

DA-T002 is docs-only scaffold planning. It is not Tauri app implementation, not app scaffold creation, not package configuration, not dependency selection, not runtime proof, not bridge implementation, and not sidecar work. It does not prove Tauri feasibility, app launch behavior, bridge reliability, sidecar behavior, package behavior, local workspace enforcement, no-cloud technical enforcement, telemetry blocking, product validation, market validation, trading validity, financial advice safety, legal/trademark clearance, or public distribution safety.

## Current Proof Boundary

QA-T005 proves only these bounded readiness facts:

- `research-core` can be installed editable into `.venv-qa-t005`;
- `research_core` and `research_core.cli` are import-visible inside `.venv-qa-t005`;
- `python -m research_core.cli --help` runs inside `.venv-qa-t005`.

QA-T005 does not prove active/global Python environment correctness, full test suite pass status, docs build success, CI smoke success, Tauri behavior, sidecar behavior, bridge command behavior, or packaged app behavior.

The following command shapes remain unsupported unless a later source/package ticket changes them:

- `python -m research_core --help`
- `research-core --help`

DA-T001 proves only a docs-only planned desktop bridge contract source document. No bridge, app, sidecar, Tauri, package, or runtime behavior is implemented or proven.

## DA-T002 Non-Proof Statement

DA-T002 does not create:

- `src-tauri/`;
- app folders;
- frontend folders;
- Rust, React, TypeScript, JavaScript, CSS, or HTML files;
- package manifests, lockfiles, dependency config, Tauri config, frontend config, or build config;
- tests, schemas, fixtures, CI, generated docs, README, docs-reference, or tool files;
- bridge commands;
- sidecar code;
- runtime behavior;
- environment repair.

DA-T002 does not run Tauri, Node, Rust, package manager, install, environment, test, docs build, quickstart, CI, app, bridge, sidecar, or runtime commands.

## Future DA-T003 Scaffold Goal

If separately authorized after DA-T002 closeout, DA-T003 should be the first implementation ticket for a minimal desktop shell smoke.

The intended future goal is a launch-only Windows 11 x64 desktop shell scaffold that can open locally and display a bounded static status surface. It should prove only that the selected scaffold can launch on the target machine, if DA-T003 explicitly implements and audits that behavior.

DA-T003 should not implement bridge commands by default. Bridge command smoke belongs to DA-T004 or another later scoped ticket after the scaffold exists and is audited.

## Future DA-T003 Non-Goals

The future scaffold implementation should not include unless separately scoped:

- ResearchCore Engine invocation;
- bridge command implementation;
- bridge command invocation;
- Python sidecar packaging;
- artifact metadata display;
- workspace mutation beyond a separately approved minimal workspace action;
- full ES.zip import;
- fixture creation;
- generated docs;
- public release packaging;
- updater or signing behavior;
- telemetry or analytics;
- cloud, hosted backend, account/auth, billing, marketplace, mobile, broker/live, AI/model, legal/trademark, financial advice, or public distribution scope.

## Scaffold Planning Principles

| Principle | DA-T002 Plan |
|---|---|
| Smallest shell first | Future DA-T003 should start with the smallest launchable desktop shell that can be audited. |
| Local-first | The shell should assume local Windows 11 x64 use and no cloud requirement. |
| Bridge deferred | No bridge command should be implemented or invoked by DA-T002; DA-T003 should avoid bridge execution unless a later plan changes scope. |
| Sidecar deferred | No sidecar work belongs to DA-T002; sidecar packaging remains later spike work. |
| Deny by default | Filesystem, process, network, updater, telemetry, credential, and broad storage permissions should start closed. |
| No arbitrary shell | No arbitrary shell execution is allowed. |
| No proof inflation | Planned scaffold details must not be described as implemented behavior. |

## Future DA-T003 Decision Register

These decisions remain unresolved and must be made by DA-T003 or a separate scoped decision ticket before implementation changes are made.

| Decision | DA-T002 Status | Notes |
|---|---|---|
| Package manager | Future DA-T003 decision | No Node package manager is selected or invoked by DA-T002. |
| Tauri version | Future DA-T003 decision | No Tauri dependency or CLI version is selected or installed by DA-T002. |
| Rust toolchain | Future DA-T003 decision | No Rust command or toolchain probe is run by DA-T002. |
| Frontend scaffold shape | Future DA-T003 decision | React/TypeScript is the ADR-T001 direction, but no app files are created by DA-T002. |
| App root path | Future DA-T003 decision | No `src-tauri/`, app directory, or workspace package path is created by DA-T002. |
| Generated files | Future DA-T003 decision | Exact generated files must be listed before DA-T003 creates any scaffold. |
| Tauri permissions | Future DA-T003 decision | A launch-only shell should request the smallest permission set possible. |
| Smoke command | Future DA-T003 decision | The smoke command must not cross into bridge, sidecar, install, or environment repair work. |
| Audit evidence | Future DA-T003 decision | DA-T003 must record exact commands, output, changed files, and skipped checks. |

## Planned Future Scaffold Shape

DA-T003 should prefer the narrowest possible scaffold shape compatible with the selected toolchain:

- one desktop window;
- static local status content only;
- no engine invocation;
- no bridge command surface;
- no sidecar process;
- no artifact browser;
- no network behavior;
- no telemetry;
- no updater;
- no signing or public release configuration;
- no raw/private data or fixtures;
- no broad filesystem access.

If DA-T003 needs to create any package files, lockfiles, config files, generated files, or app directories, it must list those paths in its own plan or prompt before creation and explain why each file is required for a launch-only scaffold.

## Permission Boundary For Future Scaffold

Future DA-T003 permissions should begin from deny-by-default.

| Capability | DA-T002 Planned Default | Expansion Gate |
|---|---|---|
| Filesystem | No broad filesystem access for launch-only scaffold. | Human gate before workspace selection or file writes. |
| Shell/process | No bridge command and no arbitrary shell. | Human gate before any allowlisted bridge command implementation. |
| Network | Off / not required. | Separate privacy/security review. |
| Telemetry/analytics | Off. | Separate scoped decision. |
| Updater/signing/public release | Off. | Post-MVP release decision and legal review. |
| Credential storage | Off. | Separate security review. |

No bridge command implementation, no bridge command invocation, no arbitrary shell execution, and no sidecar work are allowed in DA-T002.

## Bridge Boundary

The DA-T001 bridge contract remains authoritative for future bridge behavior.

DA-T002 does not:

- implement `engine.version`;
- implement `engine.doctor`;
- implement `workspace.inspect`;
- implement `fixture.smoke`;
- implement `artifact.scan`;
- implement `engine.cli_help_smoke`;
- invoke `python -m research_core.cli --help` as a bridge action;
- invoke `python -m research_core --help`;
- invoke `research-core --help`;
- define a Rust command adapter;
- define a sidecar launcher;
- define a runtime process command.

Future bridge work must use allowlisted structured command IDs only. Arbitrary shell strings remain forbidden.

## Excluded Scope

The following remain outside DA-T002 and the planned launch-only scaffold unless later scoped and audited:

- cloud storage;
- cloud sync;
- hosted backend;
- network behavior;
- telemetry/analytics;
- account/auth;
- billing;
- marketplace;
- mobile;
- broker/live trading;
- live execution;
- AI/model calls;
- updater;
- signing;
- installer or public release;
- legal/trademark claims;
- financial advice claims;
- raw/full ES.zip;
- private/local data import;
- generated datasets;
- ES-derived fixtures;
- product, market, trading, or validation claims.

## Human Gates Before DA-T003

Human review is required before DA-T003 creates any scaffold or runs any toolchain command.

DA-T003 should explicitly confirm:

- selected package manager;
- selected Tauri setup path;
- selected app root path;
- expected generated files;
- expected package/config/lock files;
- exact commands to run;
- exact smoke check;
- expected skipped checks;
- whether any dependency install or environment mutation is required;
- whether a separate ADR is needed before toolchain selection.

Human review is also required before any bridge implementation, sidecar behavior, package/dependency change, source/package change, runtime command, filesystem permission expansion, network/cloud/telemetry/auth/billing/broker/live/AI/updater/signing/public release scope, fixture/data handling, or downstream M1 implementation.

## Future DA-T003 Audit Focus

A future DA-T003 audit should verify:

- changed files match the DA-T003 allowed scaffold file list;
- exact toolchain commands are recorded;
- generated package/config/lock files are intentional and bounded;
- no arbitrary shell execution is introduced;
- no bridge command implementation exists;
- no bridge command is invoked;
- no sidecar work is started;
- no broad filesystem, network, telemetry, updater, signing, or release behavior is added;
- no source/package/test/schema/fixture/generated-doc/CI/docs-reference/tool changes occur unless explicitly authorized;
- no QA-T005 or DA-T001 proof boundary is inflated;
- no downstream DA-T004, WB-T001, MB-T002, ADR-T003, package spike, public release, broker/live, AI/model, or cloud work is started.

## Open Questions For DA-T003 Or Later

- Should DA-T003 use React/TypeScript immediately, or create the smallest framework-compatible shell generated by the selected Tauri path?
- Should DA-T003 include workspace selection, or defer workspace UI until after launch-only smoke passes?
- What exact local smoke command should prove the shell opens without requiring bridge behavior?
- Should Tauri/plugin/package decisions require a new ADR before implementation?
- Should DA-T003 stay launch-only and leave all permissions closed, or include read-only workspace selection behind explicit acceptance criteria?
