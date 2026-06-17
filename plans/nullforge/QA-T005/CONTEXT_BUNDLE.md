# QA-T005 Context Bundle

Date: `2026-06-16`

Ticket: `QA-T005`

Role: Context Curator

Status: Ready for planner

No NullForge implementation code has started.

## Ticket Summary

`QA-T005` is a NullForge M1 readiness ticket for curating context around a future human-approved local Python environment repair/readiness execution path after `QA-T004`.

This context bundle prepares the later planner to define a bounded execution ticket. It does not plan implementation details, choose final commands, run diagnostics, install packages, create or activate a virtual environment, repair the active Python environment, change source/package files, run tests, generate docs, build docs, run quickstart commands, run CI smoke commands, run post-repair CLI validation, or start downstream implementation.

## M1 Readiness Purpose

M1 readiness remains blocked for any work that depends on local CLI execution because the active local Python environment has not proven visibility to this workspace's `research_core.cli`.

`QA-T004` recommended isolated project-local virtual environment preparation as the default future repair/readiness path, but explicitly did not authorize or execute it. `QA-T005` should give the planner the smallest sufficient context to prepare a later human-gated execution path without mutating environment state during curation or planning.

## Non-Goals

`QA-T005` context curation does not:

- install, uninstall, editable install, dependency sync, or build packages;
- create, select, activate, delete, or mutate a virtual environment;
- repair or mutate Python environment state;
- run `python -m research_core.cli --help`, `python -m research_core --help`, `research-core --help`, tests, docs generation, docs build, quickstart commands, CI smoke commands, post-repair CLI validation, or other runtime validation;
- change `pyproject.toml`, dependencies, package metadata, source, tests, schemas, fixtures, CI, generated docs, README, docs/reference, or tools;
- add `[project.scripts]`, `console_scripts`, or `src/research_core/__main__.py`;
- create `PLAN.md`, `ACCEPTANCE.md`, `IMPLEMENTOR_PROMPT.md`, reports, audits, QA docs, tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, or downstream artifacts;
- start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

## Completed Prerequisites

| Ticket | Status | Evidence |
|---|---|---|
| `QA-T001` | Complete; audit `PASS` | `audits/nullforge/QA-T001/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `HY-T001` | Complete; audit `PASS` | `audits/nullforge/HY-T001/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `QA-T002` | Complete; audit `PASS` | `audits/nullforge/QA-T002/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `QA-T003` | Complete; audit `PASS` | `audits/nullforge/QA-T003/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `QA-T004` | Complete; audit `PASS` | `audits/nullforge/QA-T004/AUDIT_REPORT.md` contains `Decision: PASS`. |

Earlier M0 dependencies remain complete and active through current status and source index: `PF-T000`, `PF-T001`, `PF-T002`, `ADR-T001`, `ADR-T002`, `CX-T001`, and `MB-T001`.

## QA-T004 Recommended Path Summary

`QA-T004` created `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md` as a human-gated repair/readiness path packet. Its audit decision is `PASS`, no repair is required, and no environment repair was performed.

The QA-T004 path packet:

- preserves the exact no-code posture;
- keeps environment repair behind explicit human approval;
- recommends isolated project-local virtual environment preparation as the default future path;
- records active-environment editable reinstall, diagnostics-only deferral, source/package entrypoint work, and deferral to later M1 implementation as alternatives;
- labels the future command packet as `not run`;
- requires explicit human direction for venv location, creation command, install command, activation model, validation commands, output sanitization, and cleanup policy;
- keeps `python -m research_core --help` and `research-core --help` as expected unsupported command shapes unless a separate package/source ticket changes them.

## Unresolved Local Python Environment / CLI Blocker

The unresolved blocker remains:

- editable install visibility points outside this workspace as `<local-temp-editable-install>`;
- `research_core.cli` is not visible to the active Python environment;
- `python -m research_core.cli --help` fails with `No module named research_core.cli`;
- `python -m research_core --help` is unsupported because `src/research_core/__main__.py` is absent;
- `research-core --help` is unsupported because no console script exists.

This blocker is based on QA-T001 and QA-T002 recorded evidence and was carried through QA-T003 and QA-T004. QA-T005 context curation did not rerun Python diagnostics or repair commands.

## Existing Package And CLI Facts

| Source | Fact |
|---|---|
| `pyproject.toml` | Project name is `research-core`; version is `0.1.0`; `requires-python = ">=3.11"`. |
| `pyproject.toml` | Runtime dependencies include `pandas>=2.2.0`, `pyarrow>=16.0.0`, and `typer>=0.12.0`. |
| `pyproject.toml` | Optional `dev` extra includes `pytest>=8.0.0`. |
| `pyproject.toml` | Package layout uses `package-dir = {"" = "src"}` and package discovery under `src`. |
| `pyproject.toml` | Pytest config sets `pythonpath = ["src"]` and `testpaths = ["tests"]`. |
| `pyproject.toml` | No `[project.scripts]` or `console_scripts` entry point is declared. |
| `src/research_core/cli.py` | File exists and defines a Typer app, registered subcommands, `main()`, and an `if __name__ == "__main__"` guard. |
| `src/research_core/__main__.py` | Recorded as absent in prior QA-T002/QA-T004 context. |
| root Node package files | `package.json`, `pnpm-workspace.yaml`, and `pnpm-lock.yaml` were absent in prior QA-T001/QA-T004 context. |
| `docs/reference/cli/overview.md` | Documents `python -m research_core.cli [OPTIONS] COMMAND [ARGS]...`. |
| `docs/how-to/run_ci_locally.md` | Documents install, test, docs generation/build, and CI smoke commands. These are context only and remain forbidden for QA-T005 curation. |

## Candidate Human-Approved Repair / Readiness Execution Boundaries

QA-T005 planning should keep execution boundaries explicit. Candidate boundaries include:

| Boundary | What a later execution ticket may cover only if approved | Required human gate |
|---|---|---|
| Isolated project-local virtual environment | Create/select a project-local venv, install this workspace there, and run bounded visibility checks. | Approve venv path, creation command, activation model, install command, validation commands, output sanitization, cache policy, and cleanup/rollback. |
| Active-environment editable reinstall | Repoint the active Python environment's editable install to this workspace. | Approve active-environment mutation, exact reinstall command, before/after evidence, rollback, and validation commands. |
| Diagnostics-only deferral | Reconfirm no execution will happen and document that CLI readiness remains unavailable. | Accept that future executable work remains blocked until later repair. |
| Source/package entrypoint work | Add `src/research_core/__main__.py` or console-script metadata if those command shapes are desired. | Open a separate implementation ticket with package/source edits, tests, docs updates, and audit. |
| Broader validation after repair | Run full tests, docs generation, docs build, quickstart commands, CI smoke, or post-repair CLI validation. | Explicitly authorize each validation class and its side effects. |

Context curation does not select one of these as executable work. The planner should decide only what a later implementor may do under explicit human approval.

## Recommended Planning Inputs For Isolated Project-Local Venv Readiness

If the human chooses the QA-T004 recommended default path, the later planner should require:

- exact project-local venv path or naming convention;
- whether the venv directory should be ignored, cleaned after use, or preserved locally;
- exact creation command and shell assumptions;
- exact activation or invocation model;
- exact install command, including whether `.[dev]` is allowed;
- whether `python -m pip install --upgrade pip` is allowed;
- whether validation is limited to `python -m pip show research-core`, importlib visibility, and `python -m research_core.cli --help`;
- whether full tests, docs generation, docs build, quickstart, and CI smoke remain forbidden;
- how to prevent or clean `__pycache__/`, `.pytest_cache/`, `exec_outputs/`, venv artifacts, and generated docs;
- local-path sanitization requirements for any diagnostic output;
- rollback conditions and stop conditions if install or module visibility fails;
- whether unsupported `python -m research_core --help` and `research-core --help` stay out of scope.

## Files And Folders Likely Relevant To Later QA-T005 Planning

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
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`
- `audits/nullforge/HY-T001/AUDIT_REPORT.md`
- `audits/nullforge/QA-T002/AUDIT_REPORT.md`
- `audits/nullforge/QA-T003/AUDIT_REPORT.md`
- `audits/nullforge/QA-T004/AUDIT_REPORT.md`
- `audits/nullforge/QA-T004/FINDINGS.md`
- `reports/nullforge/QA-T004/TEST_RESULTS.md`
- `pyproject.toml`
- `docs/how-to/run_ci_locally.md`
- `docs/reference/cli/overview.md`
- `src/research_core/cli.py`

## Files And Folders Explicitly Excluded

- `src/` edits, including `src/research_core/cli.py` and any future `src/research_core/__main__.py`
- `tests/`
- `schemas/`
- `fixtures/`
- `pyproject.toml`
- `requirements-docs.txt`
- package files and dependency lockfiles
- `.github/`
- `README.md`
- `docs/reference/`
- `tools/`
- generated docs
- raw/private data
- ES-derived fixtures
- `tickets/`
- `milestones/`
- `prompts/`
- `reports/nullforge/QA-T005/`
- `audits/nullforge/QA-T005/`
- downstream `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution artifacts

## Current Repo State

Before QA-T005 context artifact creation, `git status --short --branch` reported:

```text
## main...origin/main
```

`main` is clean and aligned with `origin/main`. QA-T004 is complete and pushed with audit `PASS`.

## Known Gates And Stop Conditions

Human approval is required before:

- any install, uninstall, editable install, dependency sync, package build, virtual-environment creation/activation, environment repair, post-repair CLI validation, or command that mutates Python environment state;
- modifying `pyproject.toml`, dependencies, package metadata, source, tests, schemas, fixtures, CI, generated docs, README, docs/reference, or tools;
- adding `[project.scripts]`, `console_scripts`, or `src/research_core/__main__.py`;
- running full tests, docs generation, docs build, quickstart commands, or CI smoke commands;
- changing ResearchCore Engine behavior;
- starting `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

Stop if:

- working tree changes appear outside `plans/nullforge/QA-T005/`;
- a required prerequisite audit is missing or not `PASS`;
- context curation requires choosing exact repair commands;
- context curation requires live environment mutation;
- package/source/test/CI/generated-doc changes appear necessary;
- a command would mutate Python environment state;
- scope drifts toward implementation, tests, dependency changes, app work, or `ADR-T003`.

## Constraints And Forbidden Actions

- Context curation may create only `plans/nullforge/QA-T005/CONTEXT_BUNDLE.md` and `plans/nullforge/QA-T005/CONTEXT_BUNDLE_MANIFEST.md`.
- Do not modify existing files.
- Do not run installs, uninstalls, editable installs, dependency sync, package builds, virtual-environment creation/activation, environment repair, tests, docs generation, docs builds, quickstart commands, CI smoke commands, post-repair CLI validation, or other environment-changing commands.
- Do not create `PLAN.md`, `ACCEPTANCE.md`, `IMPLEMENTOR_PROMPT.md`, reports, audits, QA docs, tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, or downstream artifacts.
- Preserve `No NullForge implementation code has started.`

## Required Checks For Later Stages

The later planner should preserve or refine bounded checks such as:

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- prerequisite `Decision: PASS` searches for `QA-T001`, `HY-T001`, `QA-T002`, `QA-T003`, and `QA-T004`
- path existence checks for planned outputs
- source-term searches for `QA-T005`, `QA-T004`, `python -m research_core.cli`, `No module named research_core.cli`, `local-temp-editable-install`, and `No NullForge implementation code has started`
- forbidden tracked-path diff checks covering `src`, `tests`, `schemas`, `fixtures`, `pyproject.toml`, `requirements-docs.txt`, dependency/package files, `.github`, `README.md`, `docs/reference`, and `tools`
- explicit checks proving no `tickets`, `milestones`, `prompts`, `reports/nullforge/QA-T005`, or `audits/nullforge/QA-T005` exist before later roles create allowed artifacts

If a later implementor is authorized to repair the environment, that authorization must be explicit and should define exact commands, allowed side effects, rollback/cleanup expectations, output sanitization expectations, and validation commands.

## Open Questions Requiring Human Decision

- Is QA-T005 expected to plan execution of the isolated project-local virtual environment path recommended by QA-T004?
- What project-local venv path or naming convention is acceptable?
- May the later ticket run `python -m venv`, activate the venv, upgrade pip, or run `python -m pip install -e .[dev]`?
- Are post-repair checks limited to package visibility and `python -m research_core.cli --help`, or should tests, docs, quickstart, or CI smoke be included?
- Should `python -m research_core --help` and `research-core --help` remain explicitly unsupported, or should a separate source/package ticket be created?
- What cleanup is required for venv artifacts, caches, `exec_outputs/`, and generated files if they appear?
- Should command outputs continue to sanitize local absolute paths in all QA-T005 reports and audits?
- If install or CLI validation fails, should the later ticket stop, roll back, or proceed with diagnostics-only reporting?

## Ready-For-Planner Verdict

Ready for planner.

The planner can create bounded QA-T005 planning artifacts using this context, but must not implement, install, repair, validate CLI behavior, or broaden scope without explicit human approval.
