# WB-T001 Implementor Prompt

Implement WB-T001 only. Do not commit.

Ticket:
`WB-T001 - Artifact metadata read-only viewer`

Role:
Scoped Implementor.

Mission:
Add a read-only artifact metadata viewer to the existing DA-T004 bridge-smoke UI. Display only the `artifacts` array returned by `engine.cli_help_smoke`; show an honest empty state when the array is empty.

Read first:

- `plans/nullforge/WB-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/WB-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/WB-T001/PLAN.md`
- `plans/nullforge/WB-T001/ACCEPTANCE.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `audits/nullforge/DA-T004/AUDIT_REPORT.md`
- `reports/nullforge/DA-T004/IMPLEMENTATION_REPORT.md`
- `apps/nullforge-desktop/src/App.tsx`
- `apps/nullforge-desktop/src/styles.css`

Allowed changes:

- `apps/nullforge-desktop/src/App.tsx`
- `apps/nullforge-desktop/src/styles.css`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/WB-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/WB-T001/CHANGED_FILES.md`
- `reports/nullforge/WB-T001/TEST_RESULTS.md`
- `reports/nullforge/WB-T001/AUDITOR_PROMPT.md`

Forbidden:

- Rust bridge command changes.
- More bridge commands.
- New dependencies.
- Tauri permission or plugin changes.
- Workspace selection, scanning, reads, or writes.
- Artifact creation, scanning, reading, or mutation.
- ResearchCore Engine source/package changes.
- Dataset, fixture, raw/private data, generated data, or ES.zip handling.
- Sidecar, network, cloud, telemetry, updater, signing, public release, broker/live, AI/model, legal/trademark, or financial advice behavior.
- Starting `MB-T002` or downstream M1/M2 work.

Required checks:

- `git status --short --untracked-files=all`
- `pnpm --dir apps/nullforge-desktop build`
- `git diff --name-only`
- `git diff --check`
- targeted forbidden-scope scan
- forbidden tracked-path diff check for non-scoped source/package/test/schema/fixture/generated-doc/CI/root package/root lockfile/docs-reference/tool changes

Required reports:

- `reports/nullforge/WB-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/WB-T001/CHANGED_FILES.md`
- `reports/nullforge/WB-T001/TEST_RESULTS.md`
- `reports/nullforge/WB-T001/AUDITOR_PROMPT.md`

Stop and ask for human direction if real artifact scanning, workspace access, filesystem permissions, a new bridge command, Rust changes, dependency changes, or source/package changes appear necessary.

Do not mark WB-T001 audit-passed. Stop when the implementation package is ready for human direction.
