# WB-T001 Repair Prompt

Ticket: `WB-T001 - Artifact metadata read-only viewer`

Audit role: Repo-local Auditor

Decision: PASS

Date: `2026-06-18`

## Repair Requirement

No blocking repair is required for WB-T001.

## Optional Cleanup Prompt

Use this bounded cleanup prompt only if future drift reintroduces false WB-T001 proof claims, broadens the UI beyond returned artifact metadata display, or obscures the accepted evidence limits.

```text
Clean up WB-T001 documentation or implementation only. Do not commit unless explicitly asked.

Scope:
- Preserve WB-T001 audit PASS.
- Preserve that WB-T001 displays only result.artifacts returned by the existing DA-T004 engine.cli_help_smoke response.
- Preserve the honest empty state: No artifacts were returned by this bridge smoke.
- Preserve that the current DA-T004 bridge returns artifacts: [].
- Preserve that no screenshot-level visual UI proof, button-click/UI invocation proof, Tauri dev launch proof, or runtime non-empty artifact-array proof was captured for WB-T001.
- Preserve that DA-T004 remains the bridge-smoke authority.

Allowed changes:
- apps/nullforge-desktop/src/App.tsx
- apps/nullforge-desktop/src/styles.css
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- plans/nullforge/WB-T001/*
- reports/nullforge/WB-T001/*
- audits/nullforge/WB-T001/*

Forbidden:
- adding bridge commands beyond run_engine_cli_help_smoke / engine.cli_help_smoke
- changing Rust process execution or accepting user-provided executable paths, command strings, command IDs, workspace paths, or arguments
- adding dependencies
- adding Tauri permissions or plugins
- adding shell, filesystem, network, updater, telemetry, release, credential, or broad app permissions
- changing ResearchCore Engine source or package metadata
- sidecar packaging or launch
- workspace selection, scanning, reads, or writes
- artifact file creation, scanning, reading, writing, deletion, or mutation
- dataset import, fixture creation, raw/private data, generated data, or ES.zip handling
- tests, schemas, docs generation, docs build, CI, quickstart, package/public release, updater, signing, installer, or downstream work
- MB-T002, ADR-T003, or downstream M1/M2 implementation
```
