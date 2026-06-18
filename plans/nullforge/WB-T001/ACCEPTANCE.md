# WB-T001 Acceptance

Ticket: `WB-T001 - Artifact metadata read-only viewer`

Date: `2026-06-18`

## Acceptance Criteria

WB-T001 passes implementation review if:

- DA-T004 audit `PASS` remains recorded and not inflated.
- The UI displays an artifact metadata section after a bridge response exists.
- The artifact metadata section reads only `result.artifacts`.
- Empty artifact arrays render an honest empty state.
- Non-empty artifact arrays, if ever returned by the same response shape, render as read-only text entries.
- No artifact is created, scanned, read from disk, written, deleted, or mutated.
- No new bridge command is added.
- No Rust process execution logic is changed.
- No dependency is added.
- No Tauri permission or plugin is added.
- No ResearchCore Engine source/package file is changed.
- Reports and a repo-local auditor prompt are created under `reports/nullforge/WB-T001/`.
- `CURRENT_STATUS.md` and `SOURCE_INDEX.md` mark WB-T001 as implemented and ready for human direction, not audit-passed.

## Required Outputs

- `reports/nullforge/WB-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/WB-T001/CHANGED_FILES.md`
- `reports/nullforge/WB-T001/TEST_RESULTS.md`
- `reports/nullforge/WB-T001/AUDITOR_PROMPT.md`

## Required Checks

- `git status --short --untracked-files=all`
- `pnpm --dir apps/nullforge-desktop build`
- `git diff --name-only`
- `git diff --check`
- targeted scan for forbidden bridge/workspace/artifact/data/plugin/network/release behavior
- forbidden tracked-path diff check for non-scoped source/package/test/schema/fixture/generated-doc/CI/root package/root lockfile/docs-reference/tool changes

## Forbidden Pass Conditions

WB-T001 must not pass if:

- it creates or reads artifact files;
- it scans a workspace or filesystem;
- it adds any bridge command beyond `engine.cli_help_smoke`;
- it changes `run_engine_cli_help_smoke` process execution;
- it adds dependencies, Tauri plugins, or permissions;
- it changes ResearchCore Engine source/package behavior;
- it introduces dataset, fixture, raw/private data, cloud/network, telemetry, updater, signing, public release, broker/live, AI/model, legal/trademark, or financial-advice behavior;
- it claims DA-T004 produced real artifacts when the response has an empty artifact array;
- it claims screenshot or button-click proof if none was captured.

## Done Definition

WB-T001 implementation is done when the app changes and reports exist, checks are recorded, status/source docs say the implementation is ready for human direction, and `reports/nullforge/WB-T001/AUDITOR_PROMPT.md` is available as a repo-local review aid.
