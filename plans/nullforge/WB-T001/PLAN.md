# WB-T001 Plan

Ticket: `WB-T001 - Artifact metadata read-only viewer`

Role: Planner

Date: `2026-06-18`

## Goal

Add a small read-only artifact metadata viewer to the existing DA-T004 bridge-smoke UI. The viewer must display only the `artifacts` array returned by `engine.cli_help_smoke` and must show an honest empty state when no artifacts are returned.

This ticket is an implementation ticket for frontend display only. It does not create artifacts and does not scan or read a workspace.

## Source Context Used

- `plans/nullforge/WB-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/WB-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`
- `audits/nullforge/DA-T004/AUDIT_REPORT.md`
- `reports/nullforge/DA-T004/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T004/TEST_RESULTS.md`

## Assumptions

- DA-T004 audit `PASS` is the authority for proceeding.
- The bridge response `artifacts` field is available in the frontend type as `string[]`.
- DA-T004 currently returns an empty artifact array.
- A truthful empty-state display satisfies WB-T001 if no artifacts exist.

## Scope

Allowed implementation:

- Add a read-only artifact metadata section to `apps/nullforge-desktop/src/App.tsx`.
- Add app-local styling for that section in `apps/nullforge-desktop/src/styles.css`.
- Update `docs/nullforge/CURRENT_STATUS.md` and `docs/nullforge/SOURCE_INDEX.md` to record WB-T001 implementation and next human direction.
- Create WB-T001 implementation reports:
  - `reports/nullforge/WB-T001/IMPLEMENTATION_REPORT.md`
  - `reports/nullforge/WB-T001/CHANGED_FILES.md`
  - `reports/nullforge/WB-T001/TEST_RESULTS.md`
  - `reports/nullforge/WB-T001/AUDITOR_PROMPT.md`

## Out Of Scope

- Rust bridge command changes.
- New bridge commands.
- New dependencies.
- Tauri permission or plugin changes.
- Workspace selection, scanning, reads, or writes.
- Artifact creation, scanning, reading, or mutation.
- ResearchCore Engine source/package changes.
- Dataset/fixture/raw/private data handling.
- Sidecar, network, cloud, telemetry, updater, signing, public release, broker/live, AI/model, or financial-advice behavior.
- `MB-T002` handoff or audit work.

## Planned File Changes

- `apps/nullforge-desktop/src/App.tsx`
- `apps/nullforge-desktop/src/styles.css`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/WB-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/WB-T001/CHANGED_FILES.md`
- `reports/nullforge/WB-T001/TEST_RESULTS.md`
- `reports/nullforge/WB-T001/AUDITOR_PROMPT.md`

## Implementation Steps

1. Inspect the DA-T004 app response type and result UI.
2. Add an artifact metadata section inside the result display.
3. Render a count and read-only list when `result.artifacts.length > 0`.
4. Render a clear empty state when the array is empty.
5. Keep boundary text explicit that WB-T001 does not create, scan, or read artifacts.
6. Update styles without introducing layout instability.
7. Update status/source docs to identify WB-T001 as implemented and ready for human direction, not audit-passed.
8. Create reports and auditor prompt.
9. Run required checks.

## Required Checks

- `git status --short --untracked-files=all`
- `pnpm --dir apps/nullforge-desktop build`
- `git diff --name-only`
- `git diff --check`
- targeted forbidden-scope scan over app source/manifests/status/reports
- forbidden tracked-path diff check:

```text
git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml Cargo.toml Cargo.lock .github README.md docs\reference tools
```

## Security, Privacy, And Data Considerations

WB-T001 must remain display-only. It must not add filesystem access, workspace selection, artifact scanning, raw/private data handling, or new process execution. The UI must not imply artifact proof beyond the returned bridge response metadata.

## Human Gate Triggers

Stop for human direction if implementation needs a new dependency, a Rust bridge change, a Tauri permission/plugin, workspace access, artifact scanning, ResearchCore Engine changes, data handling, or any broader M1/M2 behavior.

## Rollback And Repair Route

If later review finds scope drift, repair should remove the added viewer or reduce it to a truthful display of `result.artifacts` only. If real artifact metadata is required, route to a later bridge/workspace ticket such as `artifact.scan`; do not force it into WB-T001.

## Planner Verdict

Ready for scoped implementation.
