# QA-T002 Repair Prompt

Ticket: `QA-T002`

Status: Not required

Audit verdict: PASS

No repair is required. QA-T002 passed independent audit.

If future drift invalidates this audit, use a new scoped repair prompt that:

- reads `audits/nullforge/QA-T002/AUDIT_REPORT.md`, `audits/nullforge/QA-T002/FINDINGS.md`, `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`, and `reports/nullforge/QA-T002/TEST_RESULTS.md`;
- modifies only files explicitly authorized by the new repair scope;
- does not run install, uninstall, editable install, dependency sync, package build, environment repair, full test, docs generation, docs build, quickstart, or CI smoke commands without a separate human gate;
- preserves `No NullForge implementation code has started.`;
- does not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, package changes, dependency changes, or downstream work.
