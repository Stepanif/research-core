# ADR-T002 - Local-first/no-cloud MVP boundary

Date: `2026-06-16`

Status: Accepted for M0 planning and source-of-truth purposes; not implementation proof.

## Context

ADR-T002 records the NullForge local-first / no-cloud MVP boundary after ADR-T001 closed out the working name, first platform, desktop stack direction, and ResearchCore Engine boundary. ADR-T001 has audit decision `PASS`.

Primary sources:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/DECISION_LEDGER.md`
- `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`
- `audits/nullforge/ADR-T001/AUDIT_REPORT.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md`

Existing ResearchCore Engine docs, code, package metadata, schemas, tests, and generated references remain separate engine truth. ADR-T002 does not implement local workspace behavior, cloud absence enforcement, telemetry blocking, bridge code, sidecar code, fixtures, schemas, tests, app scaffolding, packaging, or release behavior.

No NullForge implementation code has started.

## Decision Summary

| Area | Decision | Boundary |
|---|---|---|
| MVP posture | Local-first by default | First useful app runs on the user's Windows machine against local workspace state and local artifacts. |
| Runtime boundary | One selected local workspace | Planning assumption only; no workspace implementation or filesystem enforcement is created by ADR-T002. |
| Engine execution | Local ResearchCore Engine execution | Future scoped sidecar / command bridge work; not implemented or proven here. |
| Local state | Files, manifests, logs, run/artifact metadata, evidence placeholders | In MVP planning boundary only; exact schemas and implementation remain later scoped work. |
| Fixture posture | Tiny/small fixtures only through later approved fixture policy | Full ES.zip, raw/private data, generated datasets, and ES-derived fixtures remain gated and not committed by default. |
| Cloud/network posture | No cloud required for MVP | No cloud storage, cloud sync, hosted backend, auth, billing, telemetry, marketplace, or network behavior is in MVP scope. |
| Broker/release posture | Out of MVP | No broker-live integration, live execution, mobile, public distribution, legal/trademark clearance, or financial advice scope. |

## Chosen Decisions

### Local-first MVP

Treat the MVP as local-first by default.

The first useful NullForge app should run on Windows 11 x64 against a selected local workspace, local workspace files, local logs, local artifacts, local run metadata, local evidence placeholders, and future local ResearchCore Engine execution.

This is a planning/source-of-truth decision. It does not prove that the desktop app exists, that workspace permissions are implemented, that Tauri is feasible, that the bridge works, that packaging works, or that local file handling is safe.

### Local Workspace Boundary

Use one selected local workspace as the MVP runtime boundary.

The workspace boundary is intended to contain or reference local manifests, logs, runs, artifacts, evidence placeholders, safe fixtures after approval, and future ResearchCore Engine outputs.

ADR-T002 does not define final workspace schemas, destructive file behavior, cleanup behavior, deletion behavior, import behavior, or path enforcement. Those remain later scoped tickets with tests and audit.

### Local Engine Execution Boundary

Keep the MVP oriented around local ResearchCore Engine execution.

The future bridge remains the ADR-T001 direction: Python ResearchCore Engine sidecar / scoped command bridge. ADR-T002 does not add bridge commands, sidecar binaries, scripts, Tauri permissions, package configuration, engine code, CLI behavior, or tests.

### Fixture And Data Boundary

Allow tiny/small fixtures only through a later approved fixture policy.

Full ES.zip, raw/private data, generated datasets, and ES-derived fixtures remain gated and must not be committed by default. Data licensing, privacy, provenance, fixture selection, fixture generation, and DatasetCapabilityMap details remain later scoped work.

### No-cloud MVP Boundary

Exclude the following from MVP scope:

- cloud storage;
- cloud sync;
- hosted backend;
- account/auth;
- billing;
- telemetry/analytics;
- mobile app;
- marketplace;
- broker-live integration;
- live order execution;
- public distribution;
- updater/signing/release channel;
- financial advice scope.

No network behavior is required for the MVP. Any later network access, telemetry, cloud, auth, billing, broker/live, updater, signing, or public release work requires a scoped ADR or ticket and human review before implementation.

## Options Considered

| Option | Decision | Rationale |
|---|---|---|
| Local-only MVP with no cloud/auth/billing | Chosen | Matches the first user, local data/artifact workflow, first proof loop, and risk posture. |
| Local-first MVP with optional later cloud hooks | Deferred | May become useful later, but adding hooks now increases scope and security/privacy review burden before proof. |
| Hosted/cloud-first MVP | Rejected for MVP | Conflicts with local data posture and would require auth, storage, privacy, and service operations too early. |
| Hybrid desktop with remote services | Rejected for MVP | Adds network, lifecycle, privacy, and reliability complexity before local bridge proof. |
| Defer local/cloud decision | Not chosen | M0 needs a clear boundary before Codex role-loop docs and M1 planning. |

## Consequences

- ADR-T002 gives later tickets a concrete local-first/no-cloud scope boundary.
- CX-T001 can define role-loop docs with a clear MVP non-cloud posture.
- M1 planning should not introduce cloud, auth, billing, telemetry, broker/live, public release, or mobile work.
- Workspace, fixture, bridge, sidecar, DatasetCapabilityMap, evidence, and replay details still need later scoped tickets.
- Any attempt to add network/cloud/account/billing/telemetry/live-trading behavior becomes a human-gated scope change.

## Risks And Unknowns

- Local workspace behavior may be confusing or unsafe without careful path, import, and deletion rules.
- Local-only execution may expose packaging or environment complexity.
- Future users may eventually need multi-device, cloud sync, sharing, or collaboration, but that need is unproven.
- No-cloud scope can be mistaken for implemented enforcement; ADR-T002 is only a planning boundary.
- Fixture language can be misread as permission to commit ES-derived data; it is not.
- Telemetry absence can be misread as audited privacy enforcement; no app code exists yet.
- Users could still confuse local research artifacts with trading validity or financial advice without later UX boundaries.

## Human Gates

Human review is required before:

- changing ResearchCore Engine docs, code, package metadata, schemas, tests, CLI names, package names, or generated references;
- changing repo, package, CLI, app, product, or public identity;
- creating Tauri scaffolds, bridge implementation, sidecar implementation, dependencies, schemas, tests, CI, package config, generated docs, app files, or release config;
- importing raw/full ES.zip, private/local data, generated data, ES-derived fixtures, or license/privacy-sensitive datasets;
- enabling cloud storage, cloud sync, hosted backend, network upload, telemetry/analytics, account/auth, billing, mobile, marketplace, broker/live trading, live execution, AI/model calls, updater, signing, public release, legal/trademark claims, or financial advice claims;
- changing workspace deletion, cleanup, external-reference, or broad filesystem behavior;
- promoting incoming package prompts, old chats, or unreviewed external sources to active truth;
- starting CX-T001, MB-T001, ADR-T003, M1, or downstream work before ADR-T002 audit disposition.

## Reversal Conditions

Reverse or repair this ADR through a scoped later ADR/ticket if:

- the first proof loop cannot work locally;
- the local workspace model proves unsafe, confusing, or unable to protect user files;
- local ResearchCore Engine execution is infeasible and a remote service is explicitly approved by later ADR and human gate;
- validated user need requires multi-device collaboration, cloud sync, cloud storage, or accounts;
- data licensing/privacy review changes fixture or storage rules;
- public release, telemetry, auth, billing, broker/live, network, updater, signing, or mobile scope is intentionally promoted by a later scoped ADR and human review;
- no-cloud wording blocks an otherwise safe local-first implementation detail;
- a human gate requires deferral or repair.

## Non-Decisions

ADR-T002 does not decide or implement:

- Tauri scaffold;
- bridge command contract;
- sidecar implementation;
- package manager, Rust, Node, Python, or Tauri versions;
- local workspace schema;
- workspace deletion or cleanup behavior;
- dataset import implementation;
- DatasetCapabilityMap contract;
- fixture selection, generation, or licensing safety;
- ES.zip parsing or import;
- schemas, tests, CI, or generated docs;
- telemetry enforcement;
- network security controls;
- cloud architecture;
- auth, billing, mobile, marketplace, broker/live, AI/model calls, updater, signing, or public release;
- financial advice, trading validity, product validation, user validation, market validation, legal/trademark clearance, or public distribution safety;
- CX-T001, MB-T001, ADR-T003, or M1 work.

## Next Action

After ADR-T002 independent audit disposition, the next ticket is `CX-T001`.
