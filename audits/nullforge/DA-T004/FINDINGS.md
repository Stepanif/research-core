# DA-T004 Findings

Ticket: `DA-T004 - Engine command bridge smoke`

Audit role: Independent Auditor

Decision: PASS

Date: `2026-06-18`

## Blocking Findings

None.

## Non-Blocking Findings

None.

## Non-Blocking Observations

### DA-T004-OBS-001: Audit-time process-query reruns were sandbox-blocked

Severity: Non-blocking observation

Status: Recorded; no repair required.

DA-T004 implementation test results record cleanup success and no remaining app process output after the dev-launch evidence. During this audit, independent process-query reruns with `Get-CimInstance`, `Get-Process`, and `tasklist` were unavailable because the Windows sandbox helper returned `CreateProcessWithLogonW failed: 2`.

Impact:

- This does not alter DA-T004 source behavior.
- This does not introduce forbidden files or scope.
- This does not contradict the DA-T004 recorded cleanup result.
- No cleanup command was run by the audit.

The audit therefore treats process cleanup as accepted with a recorded audit-time verification limitation.

## Observations

- DA-T004 is limited to one temporary dev-only bridge command, `engine.cli_help_smoke`.
- The command uses fixed app-owned executable/arguments equivalent to `.venv-qa-t005\Scripts\python.exe -m research_core.cli --help`.
- The UI invokes only `run_engine_cli_help_smoke` and exposes no arbitrary shell input.
- App-local dependency changes are limited to `@tauri-apps/api` and `serde`.
- No Tauri shell/filesystem/network/updater/telemetry/release plugin or broad permission was added.
- No sidecar, workspace, artifact metadata, dataset, fixture, broker/live, AI/model, public release, or financial advice behavior is implemented.
- Screenshot-level visual UI proof and button-click/UI invocation proof were not captured and are not claimed.

## Reject-Level Findings

None.
