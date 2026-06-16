# QA-T001 Plan

Date: `2026-06-16`

Ticket: `QA-T001`

Role: Planner

Planner verdict: `READY_FOR_IMPLEMENTOR`

## Goal

Create a bounded command and test discovery record for the existing `research-core` repo before later NullForge M1 implementation tickets assume how to run, test, or invoke the ResearchCore Engine.

No NullForge implementation code has started.

## Non-Goals

- Do not implement NullForge.
- Do not create or modify ResearchCore Engine code.
- Do not create tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, app files, desktop shell, bridge, sidecar, or downstream M1 artifacts.
- Do not start `ADR-T003`, `DA-T001`, desktop bridge work, app scaffolding, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model calls, or public distribution work.
- Do not prove test pass status, docs build status, package installation health, bridge feasibility, Tauri feasibility, product validation, market validation, trading validity, financial advice safety, legal clearance, data licensing safety, or release readiness.

## Source Context Used

- `plans/nullforge/QA-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/DECISION_LEDGER.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/M0_HANDOFF.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `audits/nullforge/MB-T001/AUDIT_REPORT.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md`
- `pyproject.toml`
- `requirements-docs.txt`
- `README.md`
- `.github/workflows/research-ci.yml`
- `.github/workflows/docs.yml`
- `docs/how-to/run_ci_locally.md`
- `docs/how-to/add_new_test_and_golden.md`
- `docs/how-to/add_new_cli_command.md`
- `docs/getting-started/quickstart.md`
- `docs/reference/cli/overview.md`
- `docs/reference/cli/index.md`

## Assumptions

- M0 is complete through `MB-T001` audit `PASS`.
- `QA-T001` has human direction to proceed as the next scoped ticket after M0 closeout.
- `QA-T001` is a docs/discovery ticket, not an implementation ticket.
- `pyproject.toml` is the current package metadata source.
- Root `package.json`, `pnpm-workspace.yaml`, and `pnpm-lock.yaml` are absent and should be documented as absent, not created.
- Existing CI and docs files are discovery sources only and must not be modified.
- Existing tests, fixtures, goldens, schemas, generated docs, and ResearchCore Engine code are read-only for this ticket.

## Implementation Scope For Later Implementor

The later implementor should create a repo-local QA command discovery document and standard QA-T001 implementation reports. It should source its findings from existing files and a small set of bounded discovery commands.

The discovery document should identify:

- Python version expectation from current workflows and local runtime if queried.
- Package manager and package metadata evidence.
- Virtual environment expectations if source docs or local command output show them.
- Existing test command candidates.
- Existing docs-generation and docs-build command candidates.
- Existing CLI command surface and supported invocation form.
- Existing CI smoke command.
- Existing fixture/sample locations.
- Whether local dependency state blocks reliable command verification.
- Commands explicitly not run and why.
- No-code and no-implementation boundaries.

## Command Execution Decision

The later implementor may run bounded discovery commands only. It must not run install, build, full test, docs generation, docs build, quickstart, CI smoke, or artifact-producing commands without a new human approval.

Allowed bounded discovery commands for the later implementor:

```text
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
git diff --check
Test-Path -LiteralPath package.json
Test-Path -LiteralPath pnpm-workspace.yaml
Test-Path -LiteralPath pnpm-lock.yaml
Test-Path -LiteralPath pyproject.toml
Test-Path -LiteralPath requirements-docs.txt
python --version
python -m pip --version
python -m pip show research-core
python -m pip show pyarrow
python -m pip show pytest
python -m pytest --version
python -m research_core.cli --help
python -m research_core --help
research-core --help
rg -n "python -m pytest|pytest -q|python -m research_core.cli|pip install|mkdocs build|gen_cli_ref|gen_schema_ref|gen_artifact_catalog|verify_generated_docs_clean" README.md docs .github pyproject.toml requirements-docs.txt
```

Expected behavior:

- Passing commands may be recorded as verified local discovery.
- Failing commands such as `python -m research_core --help` or `research-core --help` may be valuable evidence and should be recorded as failed candidates, not repaired.
- `python -m pytest --version` is allowed for discovery; `python -m pytest`, `python -m pytest -q`, or any full test run is not allowed in QA-T001 without human approval.
- `python -m pip show ...` is allowed; `pip install`, `python -m pip install`, package upgrades, or dependency changes are forbidden.

## Side-Effect Policy

Forbidden side effects:

- `.pytest_cache/`
- `exec_outputs/`
- `site/`
- `docs/site/`
- `htmlcov/`
- generated `docs/reference/` changes
- generated schema or artifact reference changes
- package metadata or lockfile creation
- CI or workflow changes
- test, fixture, schema, golden, or source code changes

The later implementor must not run commands expected to create those outputs. If an allowed discovery command unexpectedly creates local side effects, the implementor must stop, report the paths, and ask for human direction before cleanup or continuation.

## Explicitly Out Of Scope

- Full test execution.
- Docs generation.
- Docs site build.
- CI smoke execution.
- Quickstart execution.
- Installing or upgrading dependencies.
- Creating or modifying tests, schemas, fixtures, goldens, package files, CI, generated docs, or implementation code.
- Creating `tickets/`, `milestones/`, `prompts/`, app files, bridge files, sidecar files, or downstream M1 artifacts.
- Importing incoming package milestone, ticket, prompt, raw/private, or ES.zip material.

## Proposed Allowed Files For Later Implementor

- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/QA-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T001/CHANGED_FILES.md`
- `reports/nullforge/QA-T001/TEST_RESULTS.md`
- `reports/nullforge/QA-T001/AUDITOR_PROMPT.md`

`docs/nullforge/CURRENT_STATUS.md` and `docs/nullforge/SOURCE_INDEX.md` should be updated only if needed to link created QA-T001 docs/reports and preserve `No NullForge implementation code has started.`

## Implementation Steps For Later Implementor

1. Verify working tree status and prerequisite `PASS` evidence.
2. Re-read the QA-T001 context bundle, plan, acceptance criteria, and implementor prompt.
3. Inspect existing command/test sources without changing them.
4. Run only the bounded discovery commands allowed above.
5. Create `docs/nullforge/qa/COMMAND_DISCOVERY.md` with source-backed and command-backed findings.
6. Update `docs/nullforge/CURRENT_STATUS.md` and `docs/nullforge/SOURCE_INDEX.md` only if needed and only within QA-T001 closeout scope.
7. Create the four QA-T001 report files.
8. Run required bounded checks.
9. Report human gates, blockers, skipped commands, side effects, and audit readiness.

## Acceptance Criteria

- `docs/nullforge/qa/COMMAND_DISCOVERY.md` exists and records existing command/test discovery without claiming full test success.
- QA-T001 reports exist under `reports/nullforge/QA-T001/`.
- Discovery records the absent root `package.json`, `pnpm-workspace.yaml`, and `pnpm-lock.yaml`.
- Discovery records `pyproject.toml`, Python dependency expectations, CI Python version, and docs dependency source.
- Discovery records source-backed test, docs, CI, and CLI command candidates.
- Discovery records bounded command results or skipped reasons.
- No implementation code, tests, schemas, fixtures, generated docs, package files, CI, raw data, app files, bridge files, sidecar files, or downstream artifacts are created or modified.
- No install, full test, docs generation, docs build, quickstart, or CI smoke command is run without human approval.
- `No NullForge implementation code has started.` remains present in status/discovery/reporting.

## Required Checks For Later Implementor

```text
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
git diff --check
Test-Path -LiteralPath docs\nullforge\qa\COMMAND_DISCOVERY.md
Test-Path -LiteralPath reports\nullforge\QA-T001\IMPLEMENTATION_REPORT.md
Test-Path -LiteralPath reports\nullforge\QA-T001\CHANGED_FILES.md
Test-Path -LiteralPath reports\nullforge\QA-T001\TEST_RESULTS.md
Test-Path -LiteralPath reports\nullforge\QA-T001\AUDITOR_PROMPT.md
rg -n "Decision: PASS" audits\nullforge\PF-T000\AUDIT_REPORT.md audits\nullforge\PF-T001\AUDIT_REPORT.md audits\nullforge\PF-T002\AUDIT_REPORT.md audits\nullforge\ADR-T001\AUDIT_REPORT.md audits\nullforge\ADR-T002\AUDIT_REPORT.md audits\nullforge\CX-T001\AUDIT_REPORT.md audits\nullforge\MB-T001\AUDIT_REPORT.md
rg -n "QA-T001|command|test|pyproject|package.json|pnpm-workspace|pnpm-lock|python -m pytest|python -m research_core.cli|No NullForge implementation code has started" docs\nullforge\qa\COMMAND_DISCOVERY.md reports\nullforge\QA-T001\IMPLEMENTATION_REPORT.md reports\nullforge\QA-T001\TEST_RESULTS.md
git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github tools docs\reference README.md
Test-Path -LiteralPath tickets
Test-Path -LiteralPath milestones
Test-Path -LiteralPath prompts
Test-Path -LiteralPath audits\nullforge\QA-T001
```

The implementor should record any skipped command with an exact reason.

## Human Gates

Stop and ask for human direction before:

- dependency installation, package metadata changes, lockfile creation, or package upgrades;
- running full tests, docs generation, docs build, quickstart commands, or CI smoke commands;
- modifying `src/`, `tests/`, `schemas/`, `fixtures/`, `tools/`, `.github/`, `docs/reference/`, generated docs, package files, or ResearchCore Engine docs/code;
- creating or modifying raw/private data, ES-derived fixtures, generated datasets, or `exec_outputs/`;
- changing source-of-truth decisions, ADRs, architecture boundaries, or package/CLI identity;
- starting `ADR-T003`, desktop app, bridge, sidecar, Tauri, M1 implementation, or downstream work.

## Stop Conditions

- Working tree has changes outside `plans/nullforge/QA-T001/` before implementation starts.
- Any prerequisite audit `Decision: PASS` is missing.
- Existing docs conflict on QA-T001 scope or allowed outputs.
- Bounded discovery commands are insufficient to answer the ticket without installs or broader execution.
- An allowed discovery command creates unexpected side effects.
- Dependency or environment state blocks reliable local verification and requires human choice.
- The implementor needs to modify forbidden files to proceed.

## Rollback And Repair Route

If implementation drifts, remove only QA-T001-created files and restore any QA-T001 edits to `docs/nullforge/CURRENT_STATUS.md` or `docs/nullforge/SOURCE_INDEX.md` through a scoped repair prompt. Do not revert unrelated user or repo changes. If audit returns `HOLD` or `REJECT`, perform one bounded repair pass only against the auditor findings and re-audit.

## Ready-For-Implementor Verdict

`YES`.

QA-T001 is ready for a bounded implementor handoff that creates command discovery docs/reports and runs only low-side-effect discovery commands.
