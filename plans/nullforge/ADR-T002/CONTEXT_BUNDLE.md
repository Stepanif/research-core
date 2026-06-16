# ADR-T002 Context Bundle

Ticket: `ADR-T002` - Local-first/no-cloud MVP ADR
Role: Planner context bundle
Date: `2026-06-16`

## Purpose

Provide the smallest sufficient active context for planning ADR-T002. ADR-T002 should decide the NullForge MVP boundary for local-first operation and no-cloud assumptions. This bundle does not create the ADR, reports, audits, code, schemas, fixtures, tickets, milestone docs, or downstream work.

## Prerequisite State

- ADR-T001 closeout commit: `0853dbc docs: close out nullforge ADR-T001`.
- ADR-T001 audit report contains `Decision: PASS`.
- `docs/nullforge/CURRENT_STATUS.md` says ADR-T002 is pending and ready to start only after ADR-T001 closeout.
- No `docs/nullforge/adr/ADR-T002*` file existed before this planner pass.
- Working tree was clean before planner files were created.

## Mission Slice For ADR-T002

ADR-T002 should convert the imported local-first MVP posture into one active repo-local decision record. The intended MVP remains a Windows-first, local desktop research workbench that runs against local workspace state, local datasets or safe fixtures, local engine execution, and local artifacts.

ADR-T002 should make clear that the MVP does not include SaaS, cloud sync, accounts/auth, billing, mobile, marketplace, telemetry/analytics, cloud storage, broker/live trading, live execution, public distribution, financial advice claims, or legal/trademark clearance.

## Active Source Context

### Current status

`docs/nullforge/CURRENT_STATUS.md` states:

- active phase remains `REPO_SOURCE_IMPORT_BASELINE`;
- active ticket is `None after ADR-T001 closeout`;
- next action is `ADR-T002` after ADR-T001 closeout;
- no NullForge implementation code has started;
- existing ResearchCore Engine docs, code, package metadata, schemas, tests, and generated references remain separate engine truth;
- raw/full ES.zip material, private/local data, ES-derived fixtures, desktop scaffold, bridge implementation, sidecar implementation, broker-live scope, cloud-auth-billing-mobile scope, public release claims, legal/trademark claims, and app scaffolding remain gated.

### Source index

`docs/nullforge/SOURCE_INDEX.md` identifies ADR-T002 as pending downstream: decide the local-first/no-cloud MVP boundary after ADR-T001 closeout. It also says incoming package sources are external plain text and should not be treated as resolved repo links. Prompt files are not canonical volume content unless promoted by a later audited doc.

### Decision ledger

`docs/nullforge/DECISION_LEDGER.md` contains:

- `NF-D0004`: accepted by ADR-T001 for working name, first platform, desktop stack direction, and engine boundary.
- `NF-D0005`: pending ADR for deciding the local-first/no-cloud MVP boundary. ADR-T002 owns this decision.
- accepted entries do not authorize implementation code unless a later scoped ticket does that work.

### Archive policy

`docs/nullforge/ARCHIVE_POLICY.md` says active docs are repo-local files created or imported by scoped role-loop tickets and accepted by audit disposition. Design memory can inform later work but does not authorize implementation. Raw/full ES.zip contents, private/local data, ES-derived fixtures, broker-live material, unresolved platform identity claims, and unclear provenance remain gated.

### ADR-T001

`docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` establishes:

- `NullForge` is the working product name only and not cleared for public distribution;
- repo remains `research-core`;
- internal engine label remains `ResearchCore Engine`;
- first platform is Windows 11 x64;
- Tauri + React/TypeScript is the accepted default desktop stack direction pending bridge and packaging spikes;
- intended engine boundary is a Python ResearchCore Engine sidecar / scoped command bridge;
- ADR-T001 explicitly does not decide ADR-T002 local-first/no-cloud MVP boundary.

### ADR-T001 audit

`audits/nullforge/ADR-T001/AUDIT_REPORT.md` records:

- `Decision: PASS`;
- ADR-T001 stayed docs-only;
- no ADR-T002 or downstream work was started;
- after ADR-T001 closeout, ADR-T002 is ready to start.

## Imported Volume Context

### Volume 00

Relevant ADR-T002 context from `NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md`:

- NullForge is a local-first desktop research workbench.
- Local-first means the first useful app runs on the user's Windows machine against local data and local artifacts.
- The first proof loop uses a local workspace, a small ES-derived OHLCV fixture, a DatasetCapabilityMap, a local ResearchCore Engine smoke command, artifact metadata, a visual replay fixture, and an audit/decision placeholder.
- MVP included features are Windows desktop launch, Tauri shell, local workspace create/select, tiny/small fixture, DatasetCapabilityMap display, ResearchCore Engine bridge smoke, artifact metadata viewer, visual replay fixture, and audit/decision placeholder.
- MVP exclusions include cloud sync, accounts/auth, billing, mobile app, marketplace, broker/live trading, live order execution, public release under NullForge, and full 10-year ES.zip committed to repo.
- The data posture is that full ES.zip stays local/outside repo. This can reverse only if a legal/license-safe small sample policy requires a repo fixture; full raw data should never be committed by default.
- The local-first posture is no cloud/auth for MVP, reversible only if the first proof loop cannot work locally.

### Volume 03

Relevant ADR-T002 context from `NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md`:

- Desktop-first is chosen partly because local datasets and artifacts should remain on the user machine by default.
- MVP should not depend on cloud accounts, server uptime, or auth.
- Tauri permissions should default deny and support only selected workspace folder access, workspace-owned read/write, selected fixture reads, allowlisted bridge commands, local logs, and artifact metadata display.
- MVP defaults should not include network access, updater, broker connectivity, arbitrary filesystem traversal, credential storage, or global scanning.
- Forbidden bridge behavior includes sending datasets to cloud, launching broker/live trading, installing dependencies silently, activating AI/model calls, and accepting arbitrary shell strings.
- Local workspace access should use one selected workspace at a time and avoid silently scanning parent directories.
- Full 10-year ES.zip stays outside the repo. Small ES-derived fixtures are allowed later only if license-safe and intentionally selected.
- Human gates are required before network access, telemetry/analytics, real ES.zip use, ES-derived fixtures, broker/live hooks, workspace deletion behavior, updater, public release, or Tauri permission expansion.

### Volume 07

Relevant ADR-T002 context from `NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md`:

- M0 order includes `ADR-T002` after `ADR-T001` and before `CX-T001` / `MB-T001`.
- ADR-T002 purpose is to record the local-first MVP stance and anti-goals.
- M0 explicit non-goals include no Tauri app, no engine changes, no dataset parser, no fixture creation, no desktop bridge implementation, no public release, and no repo rename.
- Roadmap anti-patterns include adding live trading, broker APIs, cloud sync, auth, billing, marketplace, mobile, or public release as MVP work.
- Human gate matrix says auth/cloud/sync/accounts introduce a scope reset and broker/live trading is explicitly out of MVP.

## ADR-T002 Decision Surface

ADR-T002 should decide:

- local-first MVP is the default;
- one selected local workspace is the runtime boundary;
- local files, local engine execution, local logs, local artifacts, and local evidence state are in MVP scope as planning assumptions only;
- tiny/small fixtures are allowed only under safe fixture policy; full ES.zip and private/raw data remain outside repo and gated;
- no cloud storage, cloud sync, hosted service, account/auth, billing, telemetry/analytics, marketplace, mobile, broker-live integration, live execution, or public distribution is part of MVP;
- no legal/trademark clearance, public brand approval, financial advice safety, trading validity, user validation, or market validation is proven by this ADR.

## Expected Implementor Scope

The implementor should create the ADR and necessary maintenance/report files only:

```text
docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
docs/nullforge/DECISION_LEDGER.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
reports/nullforge/ADR-T002/IMPLEMENTATION_REPORT.md
reports/nullforge/ADR-T002/CHANGED_FILES.md
reports/nullforge/ADR-T002/TEST_RESULTS.md
reports/nullforge/ADR-T002/AUDITOR_PROMPT.md
```

The implementor must not create `tickets/nullforge/`, `milestones/nullforge/`, `prompts/nullforge/`, schemas, code, tests, fixtures, app scaffolds, bridge code, sidecars, package changes, CI changes, generated docs, raw/private data, ES-derived fixtures, or downstream ADR/CX/MB work.

## Human Gate Triggers

Human review is required before:

- changing ResearchCore Engine docs, code, package metadata, schemas, tests, CLI names, package names, or generated references;
- changing repo/package/CLI/app/product/public identity;
- creating Tauri scaffold, bridge implementation, sidecar implementation, schemas, tests, dependencies, CI, package config, generated docs, or release config;
- importing raw/full ES.zip, private/local data, ES-derived fixtures, or any license/privacy-sensitive dataset;
- enabling cloud sync, cloud storage, network upload, telemetry/analytics, accounts/auth, billing, mobile, marketplace, broker/live trading, live execution, AI/model calls, financial advice, public release, updater, signing, or legal/trademark claims;
- promoting incoming package prompts, old chats, or unreviewed external sources to active truth.

Planner-detected human gates: none.

## Open Questions For Planner

- Should ADR-T002 mark `NF-D0005` as accepted by ADR-T002 in place, mirroring ADR-T001's treatment of `NF-D0004`?
- Should current status name ADR-T002 as active until independent audit disposition, then leave CX-T001 as the next pending M0 item?
- Should source index list ADR-T002 as an active decision record after implementation and keep CX-T001 / MB-T001 pending downstream?

Planner resolution should answer these in `PLAN.md`.

## Ready For Planner

YES.
