# DA-T004 Acceptance

Ticket: `DA-T004 - Engine command bridge smoke`

Date: `2026-06-17`

Role: Planner only

## Planner Acceptance

This planner ticket passes if:

- `plans/nullforge/DA-T004/CONTEXT_BUNDLE.md` exists.
- `plans/nullforge/DA-T004/CONTEXT_BUNDLE_MANIFEST.md` exists.
- `plans/nullforge/DA-T004/PLAN.md` exists.
- `plans/nullforge/DA-T004/ACCEPTANCE.md` exists.
- `plans/nullforge/DA-T004/IMPLEMENTOR_PROMPT.md` exists.
- The packet identifies `DA-T004 - Engine command bridge smoke` as the next scoped ticket.
- The packet preserves DA-T003-RESUME closeout with audit `PASS`.
- The packet preserves that process-level launch evidence was accepted and no screenshot-level UI proof was captured.
- The packet preserves QA-T005, DA-T001, DA-T002, DA-T003, DA-T003V, DA-T003S, and DA-T003-RESUME proof limits.
- The packet does not modify app/source/package/dependency/lockfile/status/source/report/audit/test/schema/fixture/generated-doc/CI files.
- The planner runs hygiene checks and no commit is created.

## Future DA-T004 Implementation Acceptance

A future DA-T004 implementation can pass only if all applicable criteria below are true.

### First-Proof Command

- Exactly one bridge command is implemented or invoked.
- The command ID is `engine.cli_help_smoke`, unless a later human-approved plan changes the command selection.
- The command is labeled dev-only and temporary.
- The command wraps only the fixed QA-T005-proven shape `python -m research_core.cli --help` inside `.venv-qa-t005`.
- If `.venv-qa-t005` or the CLI is unavailable, the command returns `BLOCKED` and does not install, repair, or mutate the environment.

### Bridge Safety

- No arbitrary shell strings are accepted.
- No user-provided executable paths or command arguments are accepted.
- No shell plugin, filesystem plugin, network plugin, updater, telemetry, credential, or release permission is added.
- No broad filesystem access is granted.
- No workspace paths are scanned or mutated.
- No raw/private data, ES.zip, generated dataset, or fixture is read or written.
- No sidecar is packaged or launched.
- No ResearchCore Engine source or package metadata is changed.

### Response Shape

The future bridge response must include:

- `request_id` or a stable local action ID;
- `bridge_version`;
- `command_id`;
- `status` as `OK`, `ERROR`, `TIMEOUT`, or `BLOCKED`;
- `duration_ms`;
- `exit_code` when a process ran;
- bounded stdout/stderr excerpts only;
- `warnings`;
- `errors`;
- no unbounded logs or raw local private data.

### UI Scope

- The app may add one explicit bridge-smoke action and one bounded result surface.
- The UI must not imply general bridge support, sidecar support, workspace support, artifact support, engine readiness, public release readiness, trading validity, financial advice safety, or production readiness.

### Required Future Reports

Future implementation must create:

- `reports/nullforge/DA-T004/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T004/CHANGED_FILES.md`
- `reports/nullforge/DA-T004/TEST_RESULTS.md`
- `reports/nullforge/DA-T004/AUDITOR_PROMPT.md`

This planner does not create those files.

### Required Future Checks

Future implementation should run and record:

- `git status --short --untracked-files=all`
- exact app-local install command if app-local dependencies changed
- exact app-local build command
- bridge smoke evidence for `engine.cli_help_smoke`, or a clear `BLOCKED` result
- `git diff --name-only`
- `git diff --check`
- targeted scans for forbidden shell, filesystem, network, plugin, sidecar, and unsupported command behavior
- forbidden-path diff check for non-scoped source/package/test/schema/fixture/generated-doc/CI/root package/root lockfile/docs-reference/tool changes
- final `git status --short --untracked-files=all`

### Source-Of-Truth Updates

Future implementation may update `docs/nullforge/CURRENT_STATUS.md` and `docs/nullforge/SOURCE_INDEX.md` only to record DA-T004 implementation pending independent audit. It must not close DA-T004 without audit.

## Forbidden-Pass Conditions

DA-T004 must not pass if:

- more than one bridge command is implemented;
- arbitrary shell execution is possible;
- user-provided command fragments can reach process execution;
- broad Tauri permissions are added;
- shell, filesystem, or network plugins are added without explicit separate human approval;
- `.venv-qa-t005` absence triggers environment repair instead of `BLOCKED`;
- engine source/package behavior is changed without a separate scoped ticket;
- workspace, artifact metadata, dataset, fixture, cloud/network, telemetry, updater, signing, public release, broker/live, AI/model, or financial advice behavior is introduced;
- process output is unbounded or sensitive;
- DA-T003-RESUME proof is inflated beyond launch-only scaffold evidence.

## Done Definition

This planner is done when the five DA-T004 planner files exist, hygiene checks pass, changed files are limited to `plans/nullforge/DA-T004/`, and no commit is created.
