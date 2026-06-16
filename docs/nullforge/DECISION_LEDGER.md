# NullForge Decision Ledger

Date: `2026-06-16`

This ledger records accepted and pending NullForge source-of-truth decisions. Accepted decision entries do not authorize implementation code unless a later scoped ticket does that work. Pending ADR entries are not completed decisions.

## Ledger

| Decision ID | Date | Status | Decision | Source/Evidence | Reversal/Repair | Downstream Owner |
|---|---|---|---|---|---|---|
| `NF-D0001` | `2026-06-15` | Accepted | Keep NullForge repo-local planning docs under `docs/nullforge/` without modifying existing ResearchCore Engine docs. | [PF-T000 Import Plan](import/PF-T000_IMPORT_PLAN.md), [PF-T000 Repo Inventory](import/PF-T000_REPO_INVENTORY.md), [PF-T000 audit report](../../audits/nullforge/PF-T000/AUDIT_REPORT.md) | Human-gated repair if the docs root conflicts with engine docs or repo conventions. | PF-T000, PF-T002 |
| `NF-D0002` | `2026-06-15` | Accepted | Store selected imported NullForge Volume 00-07 artifacts under `docs/nullforge/blueprint/volumes/`. | [Volume Import Manifest](blueprint/volumes/VOLUME_IMPORT_MANIFEST.md), [PF-T001 audit report](../../audits/nullforge/PF-T001/AUDIT_REPORT.md) | PF-T001 repair/audit path if imported source mismatch is found. | PF-T001 |
| `NF-D0003` | `2026-06-15` | Accepted | Create the PF-T002 status/source baseline under `docs/nullforge/` with `CURRENT_STATUS.md`, `SOURCE_INDEX.md`, `DECISION_LEDGER.md`, and `ARCHIVE_POLICY.md`. | [PF-T002 audit report](../../audits/nullforge/PF-T002/AUDIT_REPORT.md), [PF-T002 Plan](../../plans/nullforge/PF-T002/PLAN.md), [PF-T002 Acceptance](../../plans/nullforge/PF-T002/ACCEPTANCE.md) | Repair through scoped PF-T002 follow-up if source/status drift is found. | PF-T002 |
| `NF-D0004` | `2026-06-15` | Accepted by ADR-T001 | Record `NullForge` as working product name only, keep repo `research-core`, keep internal engine label `ResearchCore Engine`, set Windows 11 x64 as first platform, set Tauri + React/TypeScript as default desktop stack direction pending bridge/packaging spikes, and define the intended engine boundary as a Python ResearchCore Engine sidecar / scoped command bridge. | [ADR-T001 name/platform/stack/engine](adr/ADR-T001-name-platform-stack-engine.md), [ADR-T001 audit report](../../audits/nullforge/ADR-T001/AUDIT_REPORT.md), Volume 00, Volume 03, PF-T000 conflict/gate context. | Reverse or repair by scoped ADR if name conflict/legal/brand risk blocks use, Windows proof fails, Tauri/packaging/bridge proof fails, arbitrary shell execution is required, or app/engine split becomes impossible to communicate or maintain. | `ADR-T001` |
| `NF-D0005` | `2026-06-16` | Accepted by ADR-T002 | Record NullForge MVP as local-first by default, centered on one selected local workspace, local files/manifests/logs/run-artifact metadata/evidence placeholders, and future local ResearchCore Engine execution; exclude cloud storage, cloud sync, hosted backend, account/auth, billing, telemetry/analytics, mobile, marketplace, broker-live integration, live execution, network behavior, and public distribution from MVP scope. | [ADR-T002 local-first/no-cloud MVP](adr/ADR-T002-local-first-no-cloud-mvp.md), Volume 00, Volume 03, Volume 07 roadmap context. | Reverse or repair by scoped ADR if the first proof loop cannot work locally, local workspace behavior is unsafe or confusing, local engine execution is infeasible, validated user need requires cloud/sync/accounts, data licensing/privacy changes fixture or storage rules, or later human-gated release/network/broker scope is promoted. | `ADR-T002` |
| `NF-D0006` | `2026-06-15` | Pending source import | Determine whether incoming M0 milestone docs and ticket queue should be imported into repo-local paths. | Incoming package milestone files and PF-T002 planner decision to keep them external in this ticket. | Later scoped source import or handoff ticket may promote them. | Future M0 handoff or source import task |

## Notes

- Accepted entries above do not authorize implementation code.
- Pending ADR entries are placeholders for downstream decision work and must not be cited as completed architecture decisions.
- ResearchCore Engine docs remain authoritative for current engine behavior until a later audited decision explicitly changes that boundary.
