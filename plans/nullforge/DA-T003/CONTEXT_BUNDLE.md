# DA-T003 Context Bundle

Date: `2026-06-17`

Ticket: `DA-T003 - Minimal Tauri shell scaffold plan`

Role: Context Curator + Planner

Status: Ready for scoped implementor handoff after planner artifact review.

No NullForge implementation code has started.

## Mission

Create the bounded context and implementation plan for the first implementation ticket that may create a minimal Windows/Tauri desktop shell scaffold.

This context bundle is planning-only. It does not create a Tauri app, Rust code, React code, TypeScript code, JavaScript code, CSS, HTML, frontend files, app files, `src-tauri/`, package config, dependencies, lockfiles, tests, schemas, CI, generated docs, environment repair, bridge commands, sidecar code, runtime behavior, or downstream work.

## Current State

- `docs/nullforge/CURRENT_STATUS.md` records active phase `M1_TAURI_SCAFFOLD_PLAN_COMPLETE`.
- `DA-T002` is complete with audit `PASS`.
- `DA-T002` created only `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md` as a docs-only Tauri scaffold plan source document.
- No Tauri app scaffold, Rust, React, TypeScript, JavaScript, CSS, HTML, frontend/app files, `src-tauri/`, package config, dependencies, lockfiles, bridge commands, sidecar behavior, or runtime behavior is implemented or proven.
- `DA-T001` is complete with audit `PASS` and created only a docs-only planned desktop bridge contract source document.
- `QA-T005` is complete with audit `PASS`, but proves only isolated `.venv-qa-t005` readiness for `python -m research_core.cli --help`.
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them.

## Active Decisions

### ADR-T001

`docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` records:

- working product name: `NullForge`;
- repo identity remains `research-core`;
- engine label remains `ResearchCore Engine`;
- first platform: Windows 11 x64;
- default desktop stack direction: Tauri + React/TypeScript;
- engine boundary: future Python ResearchCore Engine sidecar / scoped command bridge;
- bridge posture: narrow, allowlisted, structured, auditable, and not arbitrary shell execution.

ADR-T001 is not implementation proof and does not prove Tauri feasibility, sidecar feasibility, bridge reliability, package behavior, or public distribution readiness.

### ADR-T002

`docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md` records:

- local-first MVP posture;
- one selected local workspace as the future runtime boundary;
- local ResearchCore Engine execution as the future direction;
- no cloud storage, cloud sync, hosted backend, auth, billing, telemetry, marketplace, network requirement, mobile, broker/live, AI/model, updater/signing, public release, legal/trademark, or financial advice scope.

ADR-T002 does not implement workspace behavior, app scaffold, bridge code, sidecar code, schemas, tests, CI, package config, generated docs, telemetry enforcement, or release behavior.

### DA-T001 Bridge Contract

`docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md` records:

- future bridge requests must use allowlisted structured command IDs only;
- arbitrary shell execution is forbidden;
- Volume 3 command IDs are planned candidates unless later proven;
- DA-T001 implements no bridge command;
- first bridge proof is deferred to DA-T004 or another later scoped ticket;
- no network, cloud, telemetry, auth, billing, broker/live, AI/model, updater, signing, public release, legal/trademark, or financial advice scope is allowed.

DA-T003 must not implement or invoke bridge commands.

### DA-T002 Tauri Scaffold Plan

`docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md` records:

- DA-T003 should be the first implementation ticket for a minimal launch-only Windows/Tauri shell smoke if separately authorized after DA-T002 closeout;
- the intended future goal is a local Windows 11 x64 desktop shell that opens and displays bounded static status content;
- no bridge command implementation, bridge command invocation, arbitrary shell execution, or sidecar work belongs in DA-T003 by default;
- package manager, Tauri version, Rust toolchain, frontend scaffold shape, generated files, permissions, and smoke commands were deferred to DA-T003;
- cloud/network/telemetry/auth/billing/broker/live/AI/model/updater/signing/public release/mobile/marketplace/legal/trademark/financial advice scope remains excluded.

## Volume 3 Planning Input

Volume 3 proposes a Windows 11 x64 local desktop direction with:

- Tauri shell;
- React/TypeScript UI;
- Tauri/Rust layer for future desktop permissions and process boundary;
- separate ResearchCore Engine sidecar / command bridge;
- local workspace folders, logs, and artifacts;
- strict command allowlist;
- structured JSON-oriented bridge responses;
- no arbitrary shell strings;
- no broad file access;
- no network/cloud/broker/AI behavior for MVP bridge proof;
- public release packaging, signing, updater, store distribution, and installer policy deferred.

For DA-T003, Volume 3 should be narrowed to a launch-only shell scaffold. Workspace selection, bridge commands, sidecar behavior, artifact metadata, and packaging are not part of this first scaffold.

## Volume 7 Planning Input

Volume 7 places DA-T003 in the M1 sequence after DA-T002:

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

DA-T003 must not attempt the full M1 proof target. It should only plan the first minimal local shell scaffold proof. DA-T004 owns bridge smoke. WB-T001 owns artifact metadata display.

## Repo Inventory Snapshot

Targeted local checks found:

- no root `package.json`;
- no root `pnpm-lock.yaml`;
- no root `Cargo.toml`;
- no `apps/` directory;
- no `desktop/` directory;
- existing Python package metadata is in `pyproject.toml`;
- existing ignored local outputs include Python caches, `.venv/`, build/dist, raw data, execution outputs, and docs `site/`.

DA-T003 implementation must not alter ResearchCore Engine code, Python package metadata, generated reference docs, schemas, tests, tools, or CI.

## Planned DA-T003 Implementation Slice

The DA-T003 implementor may create a minimal launch-only Tauri shell scaffold under:

```text
apps/nullforge-desktop/
```

The plan intentionally avoids `create-tauri-app`, `pnpm create`, `pnpm dlx`, `npx`, and interactive generator commands so the expected source file list stays auditable.

The planned scaffold should:

- use `pnpm` as the package manager for the new app directory only;
- use Tauri 2 major-version dependencies resolved by lockfiles;
- use React + TypeScript + Vite for static local UI;
- use the locally installed Rust toolchain if present;
- display static bounded status content only;
- request no filesystem, shell/process, network, updater, telemetry, credential, bridge, or sidecar permissions;
- create no ResearchCore Engine invocation path;
- create no Tauri command handlers beyond default launch wiring;
- include an app-local `.gitignore` for `node_modules/`, `dist/`, and `src-tauri/target/`;
- update NullForge status/navigation only to DA-T003 implementation pending independent audit.

## Expected Future DA-T003 Commands

The DA-T003 implementor should run only these categories of toolchain commands, after the separate implementation prompt authorizes them:

```text
node --version
pnpm --version
rustc --version
cargo --version
pnpm --dir apps/nullforge-desktop install
pnpm --dir apps/nullforge-desktop build
pnpm --dir apps/nullforge-desktop tauri dev
```

The implementor must not run:

```text
pnpm create
pnpm dlx
npx
create-tauri-app
cargo install
rustup
tauri build
package/public release commands
bridge commands
sidecar commands
ResearchCore Engine commands
python -m research_core.cli --help as a bridge action
python -m research_core --help
research-core --help
```

If `node`, `pnpm`, `rustc`, or `cargo` is missing, DA-T003 implementation must stop and report `HOLD`-level blocker evidence. It must not install toolchains, repair environments, or switch package managers without a separate human-approved ticket.

## Expected Future DA-T003 File Set

The DA-T003 implementor should create or update only:

- `apps/nullforge-desktop/.gitignore`
- `apps/nullforge-desktop/index.html`
- `apps/nullforge-desktop/package.json`
- `apps/nullforge-desktop/pnpm-lock.yaml`
- `apps/nullforge-desktop/tsconfig.json`
- `apps/nullforge-desktop/vite.config.ts`
- `apps/nullforge-desktop/src/App.tsx`
- `apps/nullforge-desktop/src/main.tsx`
- `apps/nullforge-desktop/src/styles.css`
- `apps/nullforge-desktop/src-tauri/Cargo.toml`
- `apps/nullforge-desktop/src-tauri/Cargo.lock`
- `apps/nullforge-desktop/src-tauri/build.rs`
- `apps/nullforge-desktop/src-tauri/tauri.conf.json`
- `apps/nullforge-desktop/src-tauri/capabilities/default.json`
- `apps/nullforge-desktop/src-tauri/src/main.rs`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T003/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003/CHANGED_FILES.md`
- `reports/nullforge/DA-T003/TEST_RESULTS.md`
- `reports/nullforge/DA-T003/AUDITOR_PROMPT.md`

Expected local generated/ignored outputs from DA-T003 commands:

- `apps/nullforge-desktop/node_modules/`
- `apps/nullforge-desktop/dist/`
- `apps/nullforge-desktop/src-tauri/target/`
- `apps/nullforge-desktop/src-tauri/gen/`, if Tauri creates schema metadata during dev/build commands.

Ignored outputs must not be staged. If additional tracked files are required, the implementor must stop and report the discrepancy unless the file is a lockfile or directly required by Tauri 2 launch scaffolding and is documented in `CHANGED_FILES.md`.

## Non-Goals

DA-T003 planning and future implementation must not:

- implement bridge commands;
- invoke bridge commands;
- invoke ResearchCore Engine;
- package or launch a Python sidecar;
- run `python -m research_core.cli --help` as a bridge action;
- run `python -m research_core --help`;
- run `research-core --help`;
- create workspace selection, workspace write behavior, artifact browsing, dataset import, fixtures, schemas, tests, generated reference docs, CI, tools, README, docs/reference, public release packaging, updater, signing, installer, or distribution artifacts;
- add cloud, network, telemetry, auth, billing, broker/live, AI/model, mobile, marketplace, legal/trademark, or financial advice scope;
- modify ResearchCore Engine docs, code, package metadata, schemas, tests, fixtures, generated references, tools, or CI.

## Human Gates And Risks

DA-T003 implementation requires human awareness that it may:

- add Node/Tauri/Rust package dependencies inside `apps/nullforge-desktop/`;
- generate `pnpm-lock.yaml` and `Cargo.lock`;
- use network access for package registry dependency resolution during `pnpm install` and Cargo dependency resolution;
- require installed local Node, pnpm, Rust, Cargo, Microsoft C++ Build Tools, and Microsoft Edge WebView2;
- open a local desktop app window during `pnpm --dir apps/nullforge-desktop tauri dev`.

The implementor must not install missing prerequisites, repair environment state, or expand permissions. Missing prerequisites are blockers to report, not work to fix in DA-T003.

## Open Questions For The Implementor/Auditor

- Are `node`, `pnpm`, `rustc`, and `cargo` already available locally?
- Does the manually bounded Tauri 2 scaffold launch without a generator-created extra file set?
- Does `pnpm --dir apps/nullforge-desktop tauri dev` open a local static window on Windows 11 x64?
- Can GUI launch evidence be captured in the current execution environment, or must it be human-observed and recorded as a limitation?
- Does Tauri create any required generated schema files under `src-tauri/gen/`, and are they ignored or tracked by local defaults?
