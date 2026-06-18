# DA-T004 Repair Prompt

Ticket: `DA-T004 - Engine command bridge smoke`

Audit role: Independent Auditor

Decision: PASS

Date: `2026-06-18`

## Repair Requirement

No blocking repair is required for DA-T004.

## Optional Cleanup Prompt

Use this bounded cleanup prompt only if future drift reintroduces false DA-T004 proof claims, broadens the bridge beyond `engine.cli_help_smoke`, or obscures the audit-time process-query limitation.

```text
Clean up DA-T004 documentation or reports only. Do not commit unless explicitly asked.

Scope:
- Preserve DA-T004 audit PASS.
- Preserve that DA-T004 implements exactly one temporary dev-only bridge command: engine.cli_help_smoke.
- Preserve that the command uses fixed app-owned executable/arguments equivalent to .venv-qa-t005\Scripts\python.exe -m research_core.cli --help.
- Preserve that no screenshot-level visual UI proof or button-click/UI invocation proof was captured.
- Preserve that audit-time process-query reruns were sandbox-blocked, while DA-T004 implementation test results recorded cleanup success.
- Preserve that DA-T004 does not prove general bridge behavior, sidecar behavior, workspace behavior, artifact metadata behavior, dataset import, fixture work, cloud/network behavior beyond local dev-server loopback, telemetry, updater, signing, public release, broker/live behavior, AI/model behavior, or financial advice behavior.

Allowed changes:
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- reports/nullforge/DA-T004/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T004/CHANGED_FILES.md
- reports/nullforge/DA-T004/TEST_RESULTS.md
- reports/nullforge/DA-T004/AUDITOR_PROMPT.md
- audits/nullforge/DA-T004/AUDIT_REPORT.md
- audits/nullforge/DA-T004/FINDINGS.md
- audits/nullforge/DA-T004/REPAIR_PROMPT.md

Forbidden:
- adding or changing bridge commands
- adding arbitrary shell execution
- adding user-provided executable paths, command strings, command IDs, workspace paths, or arguments
- adding shell, filesystem, network, updater, telemetry, release, credential, or broad Tauri permissions/plugins
- changing ResearchCore Engine source or package metadata
- sidecar packaging or launch
- workspace selection, scanning, reads, or writes
- artifact metadata behavior
- dataset import, fixture creation, raw/private data, generated data, or ES.zip handling
- tests, schemas, docs generation, docs build, CI, quickstart, package/public release, updater, signing, installer, or downstream work
- WB-T001, MB-T002, ADR-T003, or downstream M1 implementation
```
