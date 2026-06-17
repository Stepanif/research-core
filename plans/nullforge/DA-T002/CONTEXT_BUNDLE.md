# DA-T002 Context Bundle

Date: `2026-06-17`

Ticket: `DA-T002 - Tauri app scaffold plan`

Role: Context Curator + Planner

Status: Ready for scoped implementor handoff.

No NullForge implementation code has started.

## Mission

Create the bounded context and implementation plan for a docs-only Tauri app scaffold plan. DA-T002 must not create a Tauri app, Rust code, React/TypeScript code, package config, dependencies, tests, schemas, CI, generated docs, environment repair, bridge commands, sidecar code, runtime behavior, or downstream work.

The planned implementation target is a repo-local source document:

```text
docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md
```

That source document should plan the minimal future Windows/Tauri shell scaffold for DA-T003, but it must not create the scaffold.

## Current State

- `docs/nullforge/CURRENT_STATUS.md` records active phase `M1_DESKTOP_BRIDGE_CONTRACT_COMPLETE`.
- `DA-T001` is complete with audit `PASS`.
- `DA-T001` created only `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md` as a docs-only planned bridge contract source.
- No bridge, app, sidecar, Tauri, package, or runtime behavior is implemented or proven.
- `QA-T005` is complete with audit `PASS`, but proves only isolated `.venv-qa-t005` readiness for `python -m research_core.cli --help`.
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them.

## Active Decisions

### ADR-T001

`docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` records:

- working product name: `NullForge`;
- first platform: Windows 11 x64;
- default desktop stack direction: Tauri + React/TypeScript;
- engine label: `ResearchCore Engine`;
- engine boundary: future Python ResearchCore Engine sidecar / scoped command bridge;
- bridge posture: narrow, allowlisted, structured, auditable, and not arbitrary shell execution.

ADR-T001 is a planning decision only. It does not prove Tauri feasibility, sidecar feasibility, bridge reliability, package behavior, or public distribution readiness.

### ADR-T002

`docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md` records:

- local-first MVP posture;
- one selected local workspace as the future runtime boundary;
- local ResearchCore Engine execution as the future direction;
- no cloud storage, cloud sync, hosted backend, auth, billing, telemetry, marketplace, network requirement, mobile, broker/live, AI/model, updater/signing, public release, legal/trademark, or financial advice scope;
- no workspace implementation, app scaffold, bridge code, sidecar code, schemas, tests, CI, package config, generated docs, telemetry enforcement, or release behavior.

### DA-T001 Bridge Contract

`docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md` records:

- the future bridge must accept allowlisted structured command IDs only;
- arbitrary shell execution is forbidden;
- Volume 3 command IDs are planned candidates unless later proven;
- no bridge command is implemented by DA-T001;
- future first-proof selection is deferred to DA-T004 or another later scoped ticket;
- no network, cloud, telemetry, auth, billing, broker/live, AI/model, updater, signing, public release, legal/trademark, or financial advice scope is allowed.

DA-T002 must not alter that contract or promote any candidate command into implemented behavior.

## Volume 3 Planning Input

Volume 3 proposes a Windows 11 x64 local desktop direction with:

- a Tauri shell;
- React/TypeScript UI;
- a Tauri/Rust layer for desktop permissions and future process boundary;
- a separate ResearchCore Engine sidecar / command bridge;
- local workspace folders, logs, and artifacts;
- strict command allowlist;
- structured JSON-oriented bridge responses;
- no arbitrary shell strings;
- no broad file access;
- no network/cloud/broker/AI behavior for the MVP bridge proof;
- public release packaging, signing, updater, store distribution, and installer policy deferred.

Volume 3 also says a minimal Tauri shell should be created only after ticket approval. DA-T002 is not that implementation ticket; it only plans the scaffold source document for a future DA-T003 implementation.

## Volume 7 Planning Input

Volume 7 places DA-T002 in M1 after DA-T001:

```text
DA-T001 - Desktop bridge contract finalization
DA-T002 - Tauri app scaffold plan
DA-T003 - Tauri shell smoke implementation
DA-T004 - Engine command bridge smoke
WB-T001 - Artifact metadata read-only viewer
MB-T002 - Desktop bridge proof audit/handoff
```

Volume 7 describes M1's eventual proof target as:

```text
Open app -> run one allowed bridge command -> produce/read artifact metadata -> no arbitrary shell execution -> audit result recorded.
```

DA-T002 must not attempt that proof. It only prepares a plan for a future minimal app scaffold source.

## DA-T002 Implementation Boundary

The implementor should create a docs-only scaffold plan source document and implementation reports. The document should:

- identify the intended future minimal shell target for DA-T003;
- define non-goals and forbidden work for DA-T002;
- preserve the DA-T001 bridge boundary;
- preserve the QA-T005 readiness limit;
- record that no app scaffold, Tauri command, Rust, React, TypeScript, package, dependency, bridge, sidecar, test, schema, CI, generated-doc, environment, runtime, or release work is done;
- keep public release, updater, signing, telemetry, cloud, network, auth, billing, broker/live, AI/model, mobile, marketplace, financial advice, legal/trademark, and data fixture scope excluded.

Expected implementor output files:

- `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T002/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T002/CHANGED_FILES.md`
- `reports/nullforge/DA-T002/TEST_RESULTS.md`
- `reports/nullforge/DA-T002/AUDITOR_PROMPT.md`

## Non-Goals

DA-T002 must not:

- create `src-tauri/`, app folders, frontend folders, Rust files, React files, TypeScript files, JavaScript files, CSS files, HTML files, package files, lockfiles, config files, or environment files;
- run Tauri, Node, Rust, package manager, install, environment, test, docs build, quickstart, CI, bridge, sidecar, app, or runtime commands;
- implement bridge commands or invoke candidate command IDs;
- modify ResearchCore Engine code, package metadata, schemas, tests, generated references, fixtures, README, docs/reference, tools, or CI;
- create audits, tickets, milestones, prompt packs, DA-T003, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work;
- claim Tauri, bridge, sidecar, package, runtime, cloud absence, telemetry blocking, public release, product, market, trading, or financial-advice proof.

## Open Questions For Later Tickets

- What package manager, Tauri version, Rust toolchain, and frontend toolchain should DA-T003 use if implementation is later authorized?
- Should DA-T003 create the smallest possible launch-only shell, or also include local workspace selection UI?
- What exact Tauri permissions should be enabled for a launch-only shell before workspace selection exists?
- Should any package/dependency decision require a separate ADR before DA-T003?
- What smoke command should validate a future scaffold without crossing into bridge or sidecar behavior?
