# ADR-T002 Repair Prompt

No repair is required for ADR-T002 because the audit decision is PASS.

If a later reviewer finds drift before closeout, use this bounded repair prompt:

```text
You are the Repair Implementor for NullForge M0 ticket `ADR-T002`.

Repair only the specific ADR-T002 audit finding provided by the human reviewer. Do not broaden scope. Do not write implementation code. Do not modify existing ResearchCore Engine docs. Do not create CX-T001, MB-T001, ADR-T003, M1, or any downstream ticket.

Allowed files are limited to the ADR-T002 files already in scope:

docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
docs/nullforge/DECISION_LEDGER.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
reports/nullforge/ADR-T002/IMPLEMENTATION_REPORT.md
reports/nullforge/ADR-T002/CHANGED_FILES.md
reports/nullforge/ADR-T002/TEST_RESULTS.md
reports/nullforge/ADR-T002/AUDITOR_PROMPT.md
audits/nullforge/ADR-T002/AUDIT_REPORT.md
audits/nullforge/ADR-T002/FINDINGS.md
audits/nullforge/ADR-T002/REPAIR_PROMPT.md

Return:

Repair report:
Changed files:
Checks:
Human gates:
Ready for re-audit? YES/NO
```
