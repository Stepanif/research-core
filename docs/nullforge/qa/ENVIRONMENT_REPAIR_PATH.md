# QA-T004 Environment Repair Path

Date: `2026-06-16`

Ticket: `QA-T004`

Status: `AUDIT_PASS_READY_FOR_CLOSEOUT`

No NullForge implementation code has started.

## Purpose

QA-T004 prepares a human-gated local Python environment repair/readiness path after QA-T003. It turns the QA-T003 option set into a concrete recommended path packet for a later ticket.

This document does not repair the environment. It records the recommended path, alternatives, command packet, side effects, rollback considerations, and human gates so the human can authorize or defer a later repair/readiness ticket without mixing path selection with execution.

## Non-Goals

QA-T004 does not:

- install, uninstall, editable install, dependency sync, package build, create/select/activate a virtual environment, or repair the Python environment;
- run full tests, docs generation, docs build, quickstart commands, CI smoke commands, or post-repair CLI validation;
- run `python -m research_core.cli --help`, `python -m research_core --help`, or `research-core --help`;
- modify `pyproject.toml`, dependencies, package metadata, source, tests, schemas, fixtures, CI, generated docs, README, docs/reference, or tools;
- add `[project.scripts]`, `console_scripts`, or `src/research_core/__main__.py`;
- prove local install correctness, CLI readiness, test pass status, docs build success, or package release readiness;
- start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

## Prerequisite Audit Evidence

| Ticket | Required disposition | Evidence |
|---|---|---|
| `QA-T001` | Audit `PASS` | `audits/nullforge/QA-T001/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `HY-T001` | Audit `PASS` | `audits/nullforge/HY-T001/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `QA-T002` | Audit `PASS` | `audits/nullforge/QA-T002/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `QA-T003` | Audit `PASS` | `audits/nullforge/QA-T003/AUDIT_REPORT.md` contains `Decision: PASS`. |

## QA-T003 Decision Packet Summary

QA-T003 created `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md` as a human-gated decision packet. It documented candidate repair/readiness paths, required human gates, expected unsupported command shapes, side-effect considerations, rollback considerations, and the unresolved local Python environment blocker.

QA-T003 did not choose or execute a repair. QA-T004 selects a recommended default path for a later human decision, but still does not execute repair.

## Unresolved Blocker Summary

The unresolved local Python environment and CLI/runtime blocker remains:

- editable install visibility points outside this workspace as `<local-temp-editable-install>`;
- `research_core.cli` is not visible to the active Python environment;
- `python -m research_core.cli --help` fails with `No module named research_core.cli`;
- `python -m research_core --help` is unsupported because `src/research_core/__main__.py` is absent;
- `research-core --help` is unsupported because no console script exists.

This is inherited evidence from QA-T001 and QA-T002. QA-T004 did not rerun diagnostics and did not attempt repair.

## Relevant Package And CLI Facts

| Source | Fact |
|---|---|
| `pyproject.toml` | Project name is `research-core`, version is `0.1.0`, and `requires-python = ">=3.11"`. |
| `pyproject.toml` | Runtime dependencies include `pandas>=2.2.0`, `pyarrow>=16.0.0`, and `typer>=0.12.0`. |
| `pyproject.toml` | Optional `dev` extra includes `pytest>=8.0.0`. |
| `pyproject.toml` | Package layout uses `package-dir = {"" = "src"}` and package discovery under `src`. |
| `pyproject.toml` | Pytest config sets `pythonpath = ["src"]` and `testpaths = ["tests"]`. |
| `pyproject.toml` | No `[project.scripts]` or `console_scripts` entry point is declared. |
| `src/research_core/cli.py` | The file exists and defines a Typer app, registered subcommands, `main()`, and an `if __name__ == "__main__"` guard. |
| `docs/reference/cli/overview.md` | Documents `python -m research_core.cli [OPTIONS] COMMAND [ARGS]...`. |
| `docs/how-to/run_ci_locally.md` | Documents install, test, docs, and CI smoke commands. These commands are context only and were not run in QA-T004. |

## Distinctions

### Source Facts

The workspace contains `src/research_core/cli.py`, and project metadata uses `src` package layout. The workspace does not declare a console script and does not contain `src/research_core/__main__.py`.

### Recorded Local Environment Observations

QA-T001 and QA-T002 recorded that the active local Python environment did not resolve `research_core.cli` from this workspace and that editable install visibility pointed to `<local-temp-editable-install>`.

### Expected Unsupported Command Shapes

- `python -m research_core --help` is expected to remain unsupported unless a future scoped source/package ticket adds `src/research_core/__main__.py`.
- `research-core --help` is expected to remain unsupported unless a future scoped source/package ticket adds a console script and the selected environment is installed accordingly.

### Unresolved Blockers

- No human-approved repair path has been executed.
- `python -m research_core.cli --help` cannot be used as local readiness proof until the environment visibility issue is resolved.
- No full test, docs build, quickstart, or CI smoke status is proven by QA-T004.

## Candidate Repair / Readiness Paths

| Candidate | Tradeoff | Required human gate |
|---|---|---|
| Isolated project-local virtual environment | Least likely to disturb active global Python state; creates a separate local environment that can be documented and cleaned up. | Approve venv location, creation command, install command, activation model, validation commands, output sanitization, and cleanup policy. |
| Active-environment editable reinstall | Faster path to make the active Python environment point at this workspace, but mutates active local state and may affect unrelated work. | Approve active-environment mutation, exact reinstall command, rollback, and validation commands. |
| Diagnostics-only deferral | Keeps the environment untouched, but executable readiness remains blocked. | Accept that future executable tickets cannot depend on local CLI execution until a later repair. |
| Source/package entrypoint ticket | Addresses `python -m research_core --help` or `research-core --help` command shapes if desired, but does not fix the editable install mismatch by itself. | Open a separate implementation ticket for package/source changes, tests, docs, and audit. |
| Defer to later M1 implementation ticket | Avoids repair now but carries the blocker into later work. | Accept the risk that downstream tickets stop when local CLI execution is needed. |

## Recommended Path

Recommended default path: isolated project-local virtual environment preparation.

Rationale:

- it avoids mutating the active global Python environment;
- it can be scoped to this repository;
- it allows a later ticket to prove `python -m research_core.cli --help` against a known local environment;
- it keeps unsupported command shapes separate from the immediate environment visibility blocker;
- it provides a cleaner rollback path than active-environment mutation.

This recommendation is not authorization to create a virtual environment, install dependencies, run tests, or validate the CLI. The next human decision must explicitly authorize exact commands and allowed side effects.

## Future Command Packet

The following command packet is a draft for a future human-approved repair/readiness ticket. Every command is `not run` in QA-T004.

| Step | Command or class | QA-T004 status |
|---|---|---|
| Select venv location | Human chooses project-local venv path and cleanup policy. | `not run` |
| Create isolated environment | `python -m venv <project-local-venv>` | `not run` |
| Activate isolated environment | `<project-local-venv>\Scripts\Activate.ps1` | `not run` |
| Upgrade/install package tooling if authorized | `python -m pip install --upgrade pip` | `not run` |
| Install workspace editable with dev extra if authorized | `python -m pip install -e .[dev]` | `not run` |
| Verify package metadata points at this workspace | `python -m pip show research-core` | `not run` |
| Verify module visibility | `python -B -c "import importlib.util; print(importlib.util.find_spec('research_core.cli'))"` | `not run` |
| Verify documented CLI help | `python -m research_core.cli --help` | `not run` |
| Optional later tests | `python -m pytest -q` or `pytest -q` only if separately authorized. | `not run` |
| Optional later CI smoke | `python -m research_core.cli ci run --config .github/ci/ci.github.json` only if separately authorized. | `not run` |

The future repair ticket should decide whether to use `python -B` for diagnostics that do not need bytecode, whether to run CLI help without `-B`, and how to handle generated `__pycache__/`, `.pytest_cache/`, `exec_outputs/`, or venv artifacts if they appear.

## Human Decision Options

After QA-T004 audit, the human can choose one of these directions:

1. Authorize a scoped repair/readiness ticket for an isolated project-local virtual environment.
2. Authorize a scoped repair/readiness ticket for active-environment editable reinstall.
3. Defer repair and continue only with docs/planning work that does not need local CLI execution.
4. Open a separate source/package decision ticket if `python -m research_core --help` or `research-core --help` support is desired.
5. Stop M1 readiness until the local Python environment policy is clarified.

## Stop Conditions For Future Repair

Future repair work should stop before execution if:

- the human has not approved exact commands;
- the venv location or cleanup policy is unclear;
- active-environment mutation is requested without explicit approval;
- package/source changes appear necessary;
- full tests, docs generation, docs build, quickstart, or CI smoke commands are requested without explicit scope;
- raw local absolute paths would be recorded without sanitization;
- `ADR-T003`, desktop bridge/app work, M1 implementation, or downstream work enters scope.

## Side Effects, Rollback, And Cleanup

| Area | QA-T004 state | Future consideration |
|---|---|---|
| Python environment | Not changed. | Future ticket must define whether to use isolated or active environment. |
| Editable install state | Not changed. | Future ticket must record before/after package visibility. |
| Virtual environments | Not created or activated. | Future isolated path should define venv location, deletion policy, and `.gitignore` expectations if needed. |
| Bytecode/cache | No Python execution was used for QA-T004 implementation. | Future diagnostics should decide whether to use `-B` and how to clean `__pycache__/`. |
| `.pytest_cache/` | Not created or changed by QA-T004. | Future tests may create it and should be explicitly authorized. |
| `exec_outputs/` | Not created or changed by QA-T004. | Future CI smoke may create it and should be explicitly authorized. |
| Generated docs | Not generated or checked by QA-T004. | Future docs commands should remain separate unless explicitly authorized. |
| Source/package/test/CI files | Not modified by QA-T004. | Source/package changes require a separate scoped implementation ticket. |

Rollback for a future isolated venv path should be limited to deactivating and deleting the selected project-local venv plus removing any explicitly authorized cache/output artifacts. Rollback for active-environment mutation must be defined before the command is run.

## Local-Path Sanitization Policy

QA-T004 uses placeholders rather than raw local absolute paths:

- `<repo-root>` for this repository root;
- `<local-temp-editable-install>` for the prior temporary editable install location;
- `<external-local-research-core-namespace-path>` for prior external namespace resolution;
- `<python-313-install>` or `<python-313-site-packages>` for prior Python install paths when needed.

Future repair reports should preserve command meaning while sanitizing raw local absolute paths.

## Commands Not Run

No install, uninstall, editable install, dependency sync, package build, virtual-environment work, environment repair, full tests, docs generation, docs build, quickstart, CI smoke, or post-repair CLI validation commands were run.

The following command classes were intentionally skipped:

- `pip install`, `python -m pip install`, editable install, uninstall, dependency sync, package build;
- virtual environment creation, activation, deletion, or repair;
- `python -m research_core.cli --help`;
- `python -m research_core --help`;
- `research-core --help`;
- `python -m pytest`, `python -m pytest -q`, `pytest -q`;
- docs generation and generated-doc verification commands;
- `python -m mkdocs build`;
- quickstart commands;
- `python -m research_core.cli ci run --config .github/ci/ci.github.json`.

## QA-T004 Verdict

QA-T004 prepared a recommended human-gated repair/readiness path packet only. It recommends isolated project-local virtual environment preparation as the default next repair path, but it does not execute that path and does not prove CLI readiness.

QA-T004 audit decision is `PASS` and QA-T004 is ready for closeout.
