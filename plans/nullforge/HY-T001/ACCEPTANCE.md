# HY-T001 Acceptance Criteria

Ticket: `HY-T001`

## Required Outcome

`HY-T001` is acceptable when local absolute path leakage in the approved NullForge docs/plans/reports/audits target set is sanitized without changing source meaning or starting implementation work.

## Functional Criteria

- The implementor re-runs the bounded local-path search before editing.
- The implementor edits only files allowed by the `HY-T001` implementor prompt.
- Repo-root absolute paths are replaced with `<repo-root>` or repo-relative paths.
- Incoming package root paths are replaced with `<nullforge-incoming-root>`.
- Temp editable install paths are replaced with `<local-temp-editable-install>`.
- File basenames, ticket IDs, hash strings, command names, package names, and repo-relative paths remain intact where useful.
- `No NullForge implementation code has started.` remains unchanged.
- Any remaining local-path search hits are justified as intentional policy references or human-gated exceptions.

## Non-Regression Criteria

- No code files are modified.
- No tests, schemas, fixtures, package files, CI files, generated docs, raw data, or private data are modified.
- No tickets, milestones, prompts, app files, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, `ADR-T003`, or downstream artifacts are created.
- No audit files are created during implementation.
- Existing audit decisions and report outcomes are not changed.

## Required Checks

The later implementor must run and record:

```powershell
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
git diff --check
rg -n "C:\\Users\\Filip|NullForge_Incoming|research-core-gha-clone|AppData\\Local\\Temp" docs\nullforge plans\nullforge reports\nullforge audits\nullforge
rg -n "No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\CURRENT_STATUS.md
git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools
Test-Path -LiteralPath tickets
Test-Path -LiteralPath milestones
Test-Path -LiteralPath prompts
Test-Path -LiteralPath audits\nullforge\HY-T001
```

If implementation reports are created, also run:

```powershell
Test-Path -LiteralPath reports\nullforge\HY-T001\IMPLEMENTATION_REPORT.md
Test-Path -LiteralPath reports\nullforge\HY-T001\CHANGED_FILES.md
Test-Path -LiteralPath reports\nullforge\HY-T001\TEST_RESULTS.md
Test-Path -LiteralPath reports\nullforge\HY-T001\AUDITOR_PROMPT.md
```

## Human Gates

Human approval is required if:

- A path appears in immutable imported source content.
- A replacement would remove evidence needed to understand ticket history.
- Cleanup requires changes outside the candidate NullForge docs/plans/reports/audits set.
- Cleanup would require running tests, installs, docs generation, docs build, quickstart commands, or CI smoke commands.
- A remaining local path cannot be classified as safe to sanitize or safe to keep.

## Audit Readiness

HY-T001 is ready for independent audit when:

- The approved cleanup edits and implementation reports exist.
- Bounded checks are recorded.
- Any residual local-path hits are explained.
- No forbidden files or folders were created or modified.
