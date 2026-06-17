# QA-T005 Plan

Date: `2026-06-16`

Ticket: `QA-T005`

Role: Planner

Status: Ready for conditional implementor handoff

No NullForge implementation code has started.

## Goal

Create a bounded plan for a future human-approved local Python environment repair/readiness execution path after `QA-T004`.

`QA-T005` should prepare an implementor to execute the QA-T004 recommended isolated project-local virtual environment path only if the human explicitly authorizes environment mutation and validation commands in the implementor prompt. Without that approval, the implementor must stop at the human gate and report that execution is blocked.

## Non-Goals

`QA-T005` planning does not:

- implement the repair path;
- run install, uninstall, editable install, dependency sync, package build, virtual-environment creation/activation, environment repair, full test, docs generation, docs build, quickstart, CI smoke, post-repair CLI validation, or environment-changing commands;
- modify `pyproject.toml`, source files, tests, schemas, fixtures, dependencies, package metadata, CI, generated docs, README, docs/reference, or tools;
- add `[project.scripts]`, `console_scripts`, or `src/research_core/__main__.py`;
- create reports, audits, QA implementation docs, tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, or downstream artifacts;
- prove local install correctness, CLI readiness, test pass status, docs build success, CI smoke success, package release readiness, or broader M1 implementation readiness;
- start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

## Source Context Used

- `plans/nullforge/QA-T005/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T005/CONTEXT_BUNDLE_MANIFEST.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md`
- `audits/nullforge/QA-T004/AUDIT_REPORT.md`
- `audits/nullforge/QA-T004/FINDINGS.md`
- `reports/nullforge/QA-T004/TEST_RESULTS.md`
- `pyproject.toml`
- `docs/how-to/run_ci_locally.md`
- `docs/reference/cli/overview.md`
- `src/research_core/cli.py`

Read-only source inspection confirmed:

- `pyproject.toml` declares `research-core`, `requires-python = ">=3.11"`, `package-dir = {"" = "src"}`, `pythonpath = ["src"]`, and no console script.
- `src/research_core/cli.py` defines a Typer `app`, registers `ci_app`, defines `ci run`, defines `main()`, and has an `if __name__ == "__main__"` guard.
- `docs/reference/cli/overview.md` documents `python -m research_core.cli`.
- `docs/how-to/run_ci_locally.md` documents install, test, docs, and CI smoke commands as context only.

## Assumptions

- QA-T001, HY-T001, QA-T002, QA-T003, and QA-T004 have audit `PASS`.
- QA-T004 is complete and pushed, but `CURRENT_STATUS.md` still names `QA-T004` until a later scoped ticket updates status.
- The local Python blocker remains unresolved.
- The default recommended path is isolated project-local virtual environment preparation.
- No explicit human approval to mutate the Python environment is present in this planner task.
- A later implementor prompt must include exact human approval before running any environment-changing or validation command.
- Local absolute paths in future outputs must be sanitized with placeholders such as `<repo-root>` and `<local-temp-editable-install>`.

## Later Implementor Scope

The later implementor may proceed in one of two modes.

### Mode A: Human Approval Missing

If the later implementor prompt does not explicitly approve QA-T005 environment execution, the implementor must:

- stop before running environment-changing commands;
- create no environment artifacts;
- not run CLI validation;
- report the missing human approval as a blocker.

### Mode B: Human Approval Present

If the later implementor prompt explicitly approves QA-T005 execution and names the allowed venv path, command classes, validation commands, side effects, cleanup policy, and rollback policy, the implementor may:

- create the approved project-local virtual environment;
- install this workspace into that environment only with the approved command;
- run only approved bounded visibility and CLI validation checks;
- record sanitized command outputs;
- update only allowed NullForge status/source-index/QA docs and QA-T005 reports;
- stop immediately if any command needs broader scope.

Mode B still must not modify source, package metadata, dependencies, tests, schemas, fixtures, CI, generated docs, README, docs/reference, tools, or downstream NullForge implementation artifacts.

## Human-Gate Policy

Before any environment mutation or validation command, the implementor must confirm the prompt includes all of the following:

- explicit approval phrase: `I approve QA-T005 environment execution`;
- selected path: isolated project-local virtual environment, active-environment reinstall, diagnostics-only deferral, source/package entrypoint ticket, or another named path;
- exact venv path if isolated venv is selected;
- exact install and validation commands allowed;
- whether `python -m pip install --upgrade pip` is allowed;
- whether `python -m pip install -e .[dev]` is allowed;
- whether `python -m research_core.cli --help` is allowed;
- whether full tests, docs generation, docs build, quickstart, or CI smoke remain forbidden or become explicitly authorized;
- cleanup and rollback expectations;
- output sanitization expectations.

If any item is missing, the implementor must stop and request the missing decision.

## Recommended Isolated Venv Path

The recommended path from QA-T004 remains:

1. Use an isolated project-local virtual environment.
2. Install this workspace into that environment.
3. Verify package metadata and module visibility.
4. Verify the documented CLI module shape if explicitly approved.
5. Keep unsupported command shapes out of scope unless a separate source/package ticket authorizes them.

The planner does not select a concrete venv directory. A future human approval should name a path such as `<repo-root>\.venv-qa-t005` or another project-local path and define whether it is preserved or cleaned up after the ticket.

## Candidate Command Packet

These commands are candidates only. They are not run, not approved, and not authorized by this plan.

| Step | Candidate command | Current approval |
|---|---|---|
| Create isolated environment | `python -m venv <project-local-venv>` | `not run`; requires human approval |
| Activate isolated environment | `<project-local-venv>\Scripts\Activate.ps1` | `not run`; requires human approval |
| Upgrade pip | `python -m pip install --upgrade pip` | `not run`; requires human approval |
| Install workspace editable with dev extra | `python -m pip install -e .[dev]` | `not run`; requires human approval |
| Show package metadata | `python -m pip show research-core` | `not run`; requires human approval |
| Check module visibility | `python -B -c "import importlib.util; print(importlib.util.find_spec('research_core')); print(importlib.util.find_spec('research_core.cli'))"` | `not run`; requires human approval |
| Verify documented CLI help | `python -m research_core.cli --help` | `not run`; requires human approval |
| Optional full tests | `python -m pytest -q` or `pytest -q` | `not run`; out of scope unless separately approved |
| Optional CI smoke | `python -m research_core.cli ci run --config .github/ci/ci.github.json` | `not run`; out of scope unless separately approved |
| Optional docs generation/build | docs generation and `python -m mkdocs build` commands | `not run`; out of scope unless separately approved |

Expected unsupported command shapes remain out of scope:

- `python -m research_core --help`
- `research-core --help`

Those require a separate source/package decision if support is desired.

## Side-Effect Policy

| Area | Policy |
|---|---|
| Python environment | No mutation unless explicit human approval is present. |
| Venv artifacts | Only the approved project-local venv path may be created. It must not be staged or committed. Cleanup/preservation must follow the human decision. |
| Editable install state | Active global environment must not be changed unless explicitly approved. Prefer isolated venv path. |
| Bytecode/cache | Use `python -B` for diagnostics where practical. Record and clean or preserve `__pycache__/` only according to human-approved cleanup policy. |
| `.pytest_cache/` | Must not be created unless tests are separately authorized. If created, report and clean/preserve by human policy. |
| `exec_outputs/` | Must not be created unless CI smoke is separately authorized. If created, report and clean/preserve by human policy. |
| Generated docs | Must not be generated or verified unless explicitly authorized. |
| Local paths | Sanitize raw local absolute paths in reports using placeholders such as `<repo-root>`, `<project-local-venv>`, `<local-temp-editable-install>`, `<python-313-install>`, and `<python-313-site-packages>`. |
| Source/package/test/CI files | Must remain unchanged unless a separate scoped ticket authorizes them. |

## Out Of Scope

- Environment mutation without explicit human approval.
- Active-environment editable reinstall unless explicitly selected by the human.
- Full tests, docs generation, docs build, quickstart, CI smoke, or post-repair validation beyond explicitly approved bounded checks.
- Source, package metadata, dependency, test, schema, fixture, CI, README, docs/reference, tools, or generated-doc changes.
- `src/research_core/__main__.py`, `[project.scripts]`, or `console_scripts` changes.
- `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, public distribution, or downstream work.
- Raw/private data, ES-derived fixtures, prompt imports, ticket imports, or milestone imports.

## Proposed Allowed Files For Later Implementor

If execution is explicitly approved, the later implementor may create or update only:

- `docs/nullforge/qa/ENVIRONMENT_REPAIR_EXECUTION.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/QA-T005/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T005/CHANGED_FILES.md`
- `reports/nullforge/QA-T005/TEST_RESULTS.md`
- `reports/nullforge/QA-T005/AUDITOR_PROMPT.md`

The later implementor may create the approved project-local venv path only as a local side effect if explicitly approved. That path must not be staged or committed.

## Acceptance Criteria

- QA-T005 planner artifacts exist at the allowed paths.
- Planner artifacts preserve the exact no-code sentence.
- Planner artifacts require explicit human approval before any environment mutation or validation command.
- Planner artifacts include the QA-T004 recommended isolated project-local venv path as a candidate path, not as executed work.
- Candidate commands are labeled `not run` and not approved until human authorization.
- Out-of-scope items and forbidden actions are explicit.
- Required checks pass.
- No existing files outside QA-T005 planner artifacts are modified.
- No install, repair, test, docs, CI, quickstart, or validation command is run during planning.

## Required Checks

Planner checks:

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `Test-Path -LiteralPath plans\nullforge\QA-T005\PLAN.md`
- `Test-Path -LiteralPath plans\nullforge\QA-T005\ACCEPTANCE.md`
- `Test-Path -LiteralPath plans\nullforge\QA-T005\IMPLEMENTOR_PROMPT.md`
- `rg -n "Decision: PASS" audits\nullforge\QA-T001\AUDIT_REPORT.md audits\nullforge\HY-T001\AUDIT_REPORT.md audits\nullforge\QA-T002\AUDIT_REPORT.md audits\nullforge\QA-T003\AUDIT_REPORT.md audits\nullforge\QA-T004\AUDIT_REPORT.md`
- `rg -n "QA-T005|QA-T004|python -m research_core.cli|No module named research_core.cli|local-temp-editable-install|No NullForge implementation code has started" plans\nullforge\QA-T005\PLAN.md plans\nullforge\QA-T005\ACCEPTANCE.md plans\nullforge\QA-T005\IMPLEMENTOR_PROMPT.md`

Recommended later implementor checks should include the above plus any exact commands explicitly approved by the human.

## Human Gates And Stop Conditions

Human gate before execution:

- any venv creation, activation, deletion, or mutation;
- any install, uninstall, editable install, dependency sync, package build, or pip upgrade;
- any CLI validation command;
- any full test, docs generation, docs build, quickstart, or CI smoke command;
- any source/package/test/schema/fixture/CI/generated-doc/README/docs/reference/tool change;
- any active-environment mutation;
- any raw local path reporting without sanitization policy;
- any downstream `ADR-T003`, desktop bridge/app, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

Stop if:

- explicit human approval phrase and exact decisions are absent;
- the working tree has changes outside allowed files;
- an approved command needs broader permissions or scope than documented;
- any command fails in a way that suggests package/source changes are needed;
- a venv path is outside the repo or not explicitly approved;
- generated files, caches, or outputs appear outside the approved cleanup policy;
- a forbidden path is modified.

## Rollback / Repair Route

Planner repair is docs-only and limited to:

- `plans/nullforge/QA-T005/PLAN.md`
- `plans/nullforge/QA-T005/ACCEPTANCE.md`
- `plans/nullforge/QA-T005/IMPLEMENTOR_PROMPT.md`

For a future execution ticket, rollback must be defined before execution. The default isolated-venv rollback should be:

- deactivate the venv if active;
- delete only the explicitly approved project-local venv path if cleanup is approved;
- remove or preserve caches/outputs according to the human-approved cleanup policy;
- do not modify source/package/test/CI files to force success;
- report any unresolved blocker and route to independent audit or repair.

## Ready-For-Implementor Verdict

Ready for conditional implementor handoff.

The later implementor must not run environment-changing or validation commands unless the human explicitly approves QA-T005 environment execution and supplies the required command, side-effect, cleanup, and rollback decisions.
