# ADR-T001 - Name/platform/stack/engine boundary

Date: `2026-06-15`

Status: Accepted for M0 planning and source-of-truth purposes; not implementation proof.

## Context

ADR-T001 records the first NullForge architecture/product boundary decisions after PF-T002 established the current status, source index, decision ledger, and archive policy. PF-T002 has audit decision `PASS`.

Primary sources:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/DECISION_LEDGER.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine_System_v0_4.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md`

Existing ResearchCore Engine docs, code, package metadata, schemas, tests, and generated references remain separate engine truth. ADR-T001 does not rename or rewrite the engine.

No NullForge implementation code has started.

## Decision Summary

| Area | Decision | Boundary |
|---|---|---|
| Product name | `NullForge` | Working product name only. Not legally/trademark cleared and not approved for public distribution. |
| Repo identity | `research-core` | Existing repo name remains unchanged. |
| Engine label | `ResearchCore Engine` | Existing internal engine label remains unchanged. |
| First platform | Windows 11 x64 | First future desktop proof target. Not a cross-platform claim. |
| Desktop stack | Tauri + React/TypeScript | Accepted default desktop stack direction pending bridge and packaging spikes. |
| Engine boundary | Python ResearchCore Engine sidecar / scoped command bridge | Intended future boundary. Narrow, allowlisted, structured command protocol; not arbitrary shell execution. |

## Chosen Decisions

### Working Product Name

Use `NullForge` as the working product name for planning docs and future app-facing language.

This does not perform trademark clearance, legal review, public release approval, company identity creation, domain purchase, distribution approval, repo rename, package rename, or CLI rename.

### Repo And Engine Identity

Keep the repository name `research-core`.

Keep the internal engine label `ResearchCore Engine`.

Existing ResearchCore Engine docs and implementation remain authoritative for current engine behavior. NullForge is a planned product/workbench layer around the engine, not a replacement for it.

### First Platform

Use Windows 11 x64 as the first platform for future desktop proof work.

This reflects the initial user and M0/M1 proof path. It does not claim macOS, Linux, mobile, browser, hosted service, or cloud deployment support.

### Default Desktop Stack Direction

Use Tauri + React/TypeScript as the accepted default desktop stack direction pending bridge and packaging spikes.

This is a planning decision. It does not prove Tauri feasibility, packaging feasibility, sidecar feasibility, bridge reliability, development velocity, or public distribution readiness.

### Engine Boundary

Treat the existing Python ResearchCore Engine as a separate engine controlled by a future Python sidecar / scoped command bridge.

The intended bridge is:

- narrow;
- allowlisted;
- structured;
- auditable;
- designed around explicit command IDs and structured outputs;
- not arbitrary shell execution;
- not a reason to rewrite engine internals for UI convenience.

## Options Considered

### Name Options

| Option | Decision | Rationale |
|---|---|---|
| `NullForge` as working product name | Chosen | Matches imported planning docs and separates future product/workbench language from the existing engine repo. |
| Keep `ResearchCore` only | Not chosen | Would blur product/workbench and engine boundaries. |
| Defer naming | Not chosen | M0 needs a stable working label for docs, ADRs, and later ticket references. |

### Platform Options

| Option | Decision | Rationale |
|---|---|---|
| Windows 11 x64 first | Chosen | Matches first-user environment and M1 proof path. |
| Cross-platform from start | Not chosen | Too broad for M0/M1 and would raise packaging/scope risk. |
| Defer platform | Not chosen | M1 bridge proof needs a concrete target. |

### Stack Options

| Option | Decision | Rationale |
|---|---|---|
| Tauri + React/TypeScript | Chosen as default direction pending spikes | Matches imported planning docs and supports a local desktop shell direction with explicit permission/bridge boundaries. |
| Electron | Not chosen now | Viable fallback if Tauri blocks file access, sidecar bridge, packaging, or dev velocity. |
| Native Python UI | Not chosen now | Viable fallback if Tauri or Electron introduce unacceptable bridge/packaging complexity. |
| Defer stack | Not chosen | M1 needs a default direction for bridge-proof planning. |

### Engine Boundary Options

| Option | Decision | Rationale |
|---|---|---|
| Dev command bridge to local Python environment | Chosen as early proof path | Fastest way to test a narrow bridge without packaging claims. |
| Packaged Python sidecar | Chosen as later spike target | Needed before stronger desktop distribution claims. |
| Embedded Python distribution | Not chosen now | Possible fallback, but more custom packaging complexity. |
| Local service/API | Not chosen now | Clear boundary, but too much for MVP bridge proof. |
| Rewrite engine | Rejected | Violates ResearchCore Engine preservation and would expand scope. |

## Consequences

- NullForge docs can use a stable working product name without changing repo or package identity.
- Future M1 planning has a concrete first-platform and stack direction.
- ResearchCore Engine remains the engine truth and can continue evolving separately.
- Bridge work must be scoped through later tickets and audited before any implementation claim.
- Public naming, legal/trademark clearance, packaging, installer signing, updater, and distribution remain gated.

## Risks And Unknowns

- `NullForge` may conflict legally or publicly; no clearance has been performed.
- Tauri may not support the required filesystem, process, permission, packaging, or dev-velocity needs.
- Python sidecar packaging may be fragile or too large for the intended local desktop path.
- A dev command bridge may hide packaged-sidecar problems.
- A command bridge can become unsafe if it expands beyond allowlisted structured commands.
- Users could confuse a planned workbench with implemented validation, product proof, financial advice, or live-trading readiness.

## Human Gates

Human review is required before:

- changing repo, package, CLI, app, product, or public identity;
- public release or distribution under `NullForge`;
- trademark/domain/legal claims or clearance statements;
- adding dependencies, Tauri plugins, scaffolds, sidecar binaries, bridge code, packaging configs, tests, schemas, generated docs tooling, CI changes, or release/build config;
- changing ResearchCore Engine command behavior;
- broadening Tauri filesystem/process permissions;
- importing raw/full ES.zip, private/local data, or ES-derived fixtures;
- adding broker/live trading, financial advice, cloud sync, auth, billing, marketplace, or mobile scope.

## Reversal Conditions

Reverse or repair this ADR through a scoped later ADR/ticket if:

- name conflict, legal risk, brand risk, or public release review invalidates `NullForge`;
- Windows 11 x64 blocks first-user proof or a later audited decision changes platform priority;
- Tauri cannot support required filesystem, process, permission, packaging, or dev-velocity needs;
- the sidecar / command bridge repeatedly fails;
- the bridge requires arbitrary shell execution;
- packaged sidecar work proves worse than an alternative engine API;
- app/engine split becomes impossible to communicate or maintain;
- a human gate requires deferral or repair.

## Non-Decisions

ADR-T001 does not decide:

- ADR-T002 local-first/no-cloud MVP boundary;
- M1 bridge contract details;
- Tauri scaffold implementation;
- sidecar implementation;
- package manager, Tauri CLI, Rust, Node, or Python versions;
- installer signing, updater, or public distribution;
- ES fixture safety or data import policy beyond existing gates;
- cloud/auth/billing/mobile/broker/live-trading scope;
- financial advice language beyond keeping it gated.

## Next Action

After ADR-T001 independent audit disposition, the next ticket is `ADR-T002`.
