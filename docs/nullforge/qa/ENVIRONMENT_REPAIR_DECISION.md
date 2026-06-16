# QA-T003 Environment Repair Decision

Date: `2026-06-16`

Ticket: `QA-T003`

Status: `AUDIT_PASS_READY_FOR_CLOSEOUT`

No NullForge implementation code has started.

## Purpose

QA-T003 prepares a human-gated decision packet for the local Python environment and CLI/runtime blocker documented by QA-T002.

This ticket does not repair the environment. It records options, gates, side effects, and decision paths so a later scoped ticket can be authorized or deferred without mixing decisioning with repair execution.

## Non-Goals

QA-T003 does not:

- install, uninstall, editable install, dependency sync, package build, create/select/activate a virtual environment, or repair the Python environment;
- modify `pyproject.toml`, dependencies, package metadata, source, tests, schemas, fixtures, CI, generated docs, README, docs/reference, or tools;
- add `[project.scripts]`, `console_scripts`, or `src/research_core/__main__.py`;
- run full tests, docs generation, docs build, quickstart commands, or CI smoke commands;
- prove local install correctness, CLI smoke success, test pass status, docs build success, or package release readiness;
- start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

## Prerequisite Audit Evidence

| Ticket | Required disposition | Evidence |
|---|---|---|
| `QA-T001` | Audit `PASS` | `audits/nullforge/QA-T001/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `HY-T001` | Audit `PASS` | `audits/nullforge/HY-T001/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `QA-T002` | Audit `PASS` | `audits/nullforge/QA-T002/AUDIT_REPORT.md` contains `Decision: PASS`. |

## QA-T002 Blocker Summary

QA-T002 confirmed the local executable-readiness blocker:

- `python -B -m pip show research-core` reported editable project location `<local-temp-editable-install>`, not this workspace.
- Importlib resolved `research_core` as a namespace package from `<external-local-research-core-namespace-path>`.
- Importlib resolved `research_core.cli` as `None`.
- `python -B -m research_core.cli --help` failed with `No module named research_core.cli`.
- `python -B -m research_core --help` failed because `research_core.__main__` is absent.
- `research-core --help` failed because PowerShell did not recognize the command.

QA-T002 treated this as a local Python visibility/install-state blocker, not as absence of `src/research_core/cli.py` in the current workspace.

## Source Facts

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
| `docs/how-to/run_ci_locally.md` | Documents install, test, docs, and CI smoke commands; these commands were read as context only and were not run in QA-T003. |

## Local Environment Observations

The current QA-T003 implementation did not rerun Python environment diagnostics. It uses QA-T002 recorded observations as the latest repo-local evidence.

QA-T002 observations remain:

- installed `research-core` metadata pointed to `<local-temp-editable-install>`;
- active module visibility did not expose `research_core.cli`;
- documented CLI invocation could not be used as local readiness proof.

## Expected Unsupported Command Shapes

| Command shape | Status |
|---|---|
| `python -m research_core.cli --help` | Documented by repo docs, but blocked in QA-T002 by local environment visibility. This is the immediate readiness blocker. |
| `python -m research_core --help` | Expected unsupported unless a future scoped source/package ticket adds `src/research_core/__main__.py`. |
| `research-core --help` | Expected unsupported unless a future scoped source/package ticket adds a console script and the selected environment is installed accordingly. |

## Unresolved Blockers

- Local Python package visibility does not prove the current workspace is installed.
- `research_core.cli` was not visible to the active Python environment in QA-T002 diagnostics.
- No human-approved environment repair path has been selected.
- No CLI readiness command has been rerun after any repair because no repair has occurred.

## Candidate Repair / Readiness Paths

These paths are options for a later human decision. QA-T003 did not choose or execute any repair path.

| Option | What it would do | Tradeoff | Required human gate |
|---|---|---|---|
| Isolated project-local virtual environment | Create or select an isolated environment and install this workspace there in a later ticket. | Least likely to disturb global Python state; requires explicit venv lifecycle and cleanup decisions. | Approval for venv work, install commands, dependency sync, activation model, and later validation commands. |
| Active-environment editable reinstall | Reinstall the current workspace into the active Python environment in editable mode in a later ticket. | Faster path, but mutates the active environment and may affect unrelated work. | Approval for active-environment mutation, exact install command, rollback, and verification commands. |
| Diagnostics-only deferral | Keep the environment untouched and accept that local CLI execution remains unavailable. | No local environment risk, but executable readiness remains blocked. | Human acceptance that future work cannot depend on local CLI execution until a later ticket repairs it. |
| Source/package entrypoint ticket | Add `src/research_core/__main__.py` or console-script metadata in a separate implementation ticket if those command shapes are desired. | Addresses unsupported command shapes, not the editable install mismatch by itself. | Separate source/package scope, tests, docs updates, and audit. |
| Defer until a future M1 implementation ticket | Carry the blocker forward and avoid environment work now. | Keeps planning moving but increases risk that a later ticket is blocked by CLI execution. | Human decision that downstream work remains docs/planning-only or explicitly tolerates the blocker. |

## Recommended Human Decision Options

The human should choose one of these next directions after QA-T003 audit:

1. Authorize a separate environment repair/readiness ticket using an isolated project-local virtual environment.
2. Authorize a separate active-environment editable reinstall ticket with exact commands and rollback.
3. Defer repair and continue only with work that does not require local CLI execution.
4. Open a separate package/source decision ticket if `python -m research_core --help` or `research-core --help` support is desired.

QA-T003 does not decide among these options.

## Commands Not Run

No install, uninstall, editable install, dependency sync, package build, virtual-environment work, environment repair, full tests, docs generation, docs build, quickstart, or CI smoke commands were run.

The following command classes were intentionally skipped:

- `pip install`, `python -m pip install`, editable install, uninstall, dependency sync, package build;
- virtual environment creation, activation, deletion, or repair;
- `python -m pytest`, `python -m pytest -q`, `pytest -q`;
- docs generation and generated-doc verification commands;
- `python -m mkdocs build`;
- quickstart commands;
- `python -m research_core.cli ci run --config .github/ci/ci.github.json`.

## Side-Effect Considerations

| Area | QA-T003 state |
|---|---|
| Python environment | Not changed. |
| Editable install state | Not changed. |
| Virtual environments | Not created, selected, activated, deleted, or changed. |
| Bytecode/cache | No Python execution was used for QA-T003 implementation. |
| `exec_outputs/` | Not created or changed. |
| Generated docs | Not generated or checked. |
| Source/package/test/CI files | Not modified. |
| Local absolute paths | New QA-T003 docs use placeholders such as `<local-temp-editable-install>` instead of raw local paths. |

## Rollback Considerations

QA-T003 is docs-only. If the decision packet needs repair, the repair should be limited to:

- `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/QA-T003/*`

No environment state, source files, package metadata, tests, schemas, fixtures, CI, generated docs, raw data, private data, tickets, milestones, prompts, or audits should be changed as part of QA-T003 repair.

## Human Gates

Human approval is required before any later work:

- runs install, uninstall, editable install, dependency sync, package build, virtual-environment creation/activation, or environment repair commands;
- changes `pyproject.toml`, dependencies, package metadata, source, tests, schemas, fixtures, CI, README, docs/reference, generated docs, or tools;
- adds `[project.scripts]`, `console_scripts`, or `src/research_core/__main__.py`;
- runs full tests, docs generation, docs build, quickstart commands, or CI smoke commands;
- starts `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

## Implementation Verdict

QA-T003 prepared a human-gated repair/readiness decision packet only. QA-T003 audit decision is `PASS`, no repair is required, and the ticket is ready for closeout.
