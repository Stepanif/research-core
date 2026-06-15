# NullForge Decision Ledger

Date: `2026-06-15`

This ledger records accepted and pending NullForge source-of-truth decisions. Pending ADR entries are not completed decisions.

## Ledger

| Decision ID | Date | Status | Decision | Source/Evidence | Reversal/Repair | Downstream Owner |
|---|---|---|---|---|---|---|
| `NF-D0001` | `2026-06-15` | Accepted | Keep NullForge repo-local planning docs under `docs/nullforge/` without modifying existing ResearchCore Engine docs. | [PF-T000 Import Plan](import/PF-T000_IMPORT_PLAN.md), [PF-T000 Repo Inventory](import/PF-T000_REPO_INVENTORY.md), [PF-T000 audit report](../../audits/nullforge/PF-T000/AUDIT_REPORT.md) | Human-gated repair if the docs root conflicts with engine docs or repo conventions. | PF-T000, PF-T002 |
| `NF-D0002` | `2026-06-15` | Accepted | Store selected imported NullForge Volume 00-07 artifacts under `docs/nullforge/blueprint/volumes/`. | [Volume Import Manifest](blueprint/volumes/VOLUME_IMPORT_MANIFEST.md), [PF-T001 audit report](../../audits/nullforge/PF-T001/AUDIT_REPORT.md) | PF-T001 repair/audit path if imported source mismatch is found. | PF-T001 |
| `NF-D0003` | `2026-06-15` | In progress until audit | Create the PF-T002 status/source baseline under `docs/nullforge/` with `CURRENT_STATUS.md`, `SOURCE_INDEX.md`, `DECISION_LEDGER.md`, and `ARCHIVE_POLICY.md`. | [PF-T002 Plan](../../plans/nullforge/PF-T002/PLAN.md), [PF-T002 Acceptance](../../plans/nullforge/PF-T002/ACCEPTANCE.md) | Auditor `HOLD` or `REJECT` requires a bounded repair prompt before closeout. | PF-T002 |
| `NF-D0004` | `2026-06-15` | Pending ADR | Decide NullForge name, platform, stack, and ResearchCore Engine boundary. | Volume 00, Volume 03, PF-T000 conflict/gate context. | Must be resolved by scoped ADR ticket; do not treat as accepted in PF-T002. | `ADR-T001` |
| `NF-D0005` | `2026-06-15` | Pending ADR | Decide local-first/no-cloud MVP boundary. | Volume 00, Volume 03, Volume 07 roadmap context. | Must be resolved by scoped ADR ticket; do not treat as accepted in PF-T002. | `ADR-T002` |
| `NF-D0006` | `2026-06-15` | Pending source import | Determine whether incoming M0 milestone docs and ticket queue should be imported into repo-local paths. | Incoming package milestone files and PF-T002 planner decision to keep them external in this ticket. | Later scoped source import or handoff ticket may promote them. | Future M0 handoff or source import task |

## Notes

- Accepted entries above do not authorize implementation code.
- Pending ADR entries are placeholders for downstream decision work and must not be cited as completed architecture decisions.
- ResearchCore Engine docs remain authoritative for current engine behavior until a later audited decision explicitly changes that boundary.
