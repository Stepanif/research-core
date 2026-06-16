# QA-T002 Environment Triage

Date: `2026-06-16`

Ticket: `QA-T002`

Status: `AUDIT_PASS_READY_FOR_CLOSEOUT`

No NullForge implementation code has started.

## Purpose

QA-T002 records bounded local Python environment and CLI/runtime blocker triage after QA-T001 command discovery. It is a docs-only readiness ticket.

This document separates:

- source-tree facts,
- current local environment observations,
- expected unsupported commands,
- unresolved blockers,
- human-gated repair decisions.

## Non-Goals

QA-T002 does not:

- install, uninstall, repair, or change the Python environment;
- change editable install state;
- change `pyproject.toml`, source code, tests, schemas, fixtures, dependencies, CI, generated docs, or package metadata;
- run full tests, docs generation, docs build, quickstart commands, or CI smoke commands;
- add a console script, add `src/research_core/__main__.py`, or modify `src/research_core/cli.py`;
- start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

## Prerequisite Audit Evidence

| Ticket | Required disposition | Evidence |
|---|---|---|
| `QA-T001` | Audit `PASS` | `audits/nullforge/QA-T001/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `HY-T001` | Audit `PASS` | `audits/nullforge/HY-T001/AUDIT_REPORT.md` contains `Decision: PASS`. |

## Inherited Blocker From QA-T001

QA-T001 found local executable readiness blockers:

- `python -m pip show research-core` reported editable install provenance from `<local-temp-editable-install>`, not this workspace.
- `python -m research_core.cli --help` failed with `No module named research_core.cli`.
- `python -m research_core --help` failed because `research_core` has no `__main__`.
- `research-core --help` was not recognized by PowerShell.

QA-T001 correctly treated this as a future executable-work blocker, not as a QA-T001 failure.

## Source-Tree Facts

| Item | Observation |
|---|---|
| Package metadata | `pyproject.toml` exists and is the current Python package metadata source. |
| Package layout | `pyproject.toml` declares `package-dir = {"" = "src"}` and package discovery under `src`. |
| Pytest config | `pyproject.toml` declares `pythonpath = ["src"]` and `testpaths = ["tests"]`. |
| Runtime dependency | `typer>=0.12.0` is declared. |
| Console script | No `[project.scripts]` or `console_scripts` entry point was found. |
| CLI module file | `src/research_core/cli.py` exists. |
| CLI app | `src/research_core/cli.py` imports Typer, defines `app = typer.Typer(...)`, registers subcommands, defines `main()`, and has an `if __name__ == "__main__"` guard. |
| Package executable module | `src/research_core/__main__.py` is absent. |
| Node package files | Root `package.json`, `pnpm-workspace.yaml`, and `pnpm-lock.yaml` are absent. |

## Current Local Environment Observations

Bounded read-only diagnostics were run with `python -B` for Python commands.

| Diagnostic | Result |
|---|---|
| `python -B -m pip show research-core` | Succeeded. Reported `research-core` version `0.1.0`, package location under `<python-313-site-packages>`, and editable project location `<local-temp-editable-install>`. |
| Python executable/prefix diagnostic | Succeeded. Reported Python executable and prefixes under `<python-313-install>`. `sys.path[0]` was blank for the `-c` command. |
| Importlib module-resolution diagnostic | Succeeded. `research_core` resolved as a namespace package from `<external-local-research-core-namespace-path>`. `research_core.cli` resolved as `None`. |
| `python -B -m research_core.cli --help` | Failed with `No module named research_core.cli`. |
| `python -B -m research_core --help` | Failed with `No module named research_core.__main__; 'research_core' is a package and cannot be directly executed`. |
| `research-core --help` | Failed because PowerShell did not recognize `research-core` as a command, function, script file, or executable program. |

## Interpretation

### Source Facts

The current workspace contains a CLI module at `src/research_core/cli.py`, and that module exposes a Typer app and `main()` entrypoint. The package metadata uses a `src` layout and does not declare a console script.

### Environment Observations

The active Python environment is not resolving `research_core.cli` from this workspace. Package metadata still points at `<local-temp-editable-install>`, and module discovery found `research_core` as a namespace package from `<external-local-research-core-namespace-path>` with no `research_core.cli` module.

This confirms the QA-T001 executable-readiness blocker still exists.

### Expected Unsupported Commands

- `python -m research_core --help` is expected to fail unless a future scoped ticket adds `src/research_core/__main__.py`.
- `research-core --help` is expected to fail unless a future scoped ticket adds a console script and the environment is installed accordingly.

### Unresolved Blocker

`python -m research_core.cli --help` is documented by repo CLI docs and local CI docs, but it still fails in the current local environment. The likely blocker is local Python visibility/install state, not absence of `src/research_core/cli.py` in the current workspace.

## Side-Effect Review

The diagnostics were read-only. No install, uninstall, environment repair, full test, docs generation, docs build, quickstart, or CI smoke command was run.

Post-diagnostic status before QA-T002 documentation edits showed only the pre-existing untracked QA-T002 planning artifacts. No tracked diff existed at that point.

The final required checks should verify that no unexpected changes occurred under:

- `.pytest_cache/`
- `__pycache__/`
- `exec_outputs/`
- docs build output
- generated docs
- `src/`
- `tests/`
- `schemas/`
- `fixtures/`
- package files
- `.github/`
- `README.md`
- `docs/reference/`
- `tools/`

## Human Gates

Human approval is required before any later work:

- runs `pip install`, `python -m pip install`, uninstall, editable install, dependency sync, package build, or environment repair;
- changes `pyproject.toml`, dependencies, package metadata, source, tests, schemas, fixtures, CI, generated docs, or README;
- adds a console script or `src/research_core/__main__.py`;
- runs full tests, docs generation, docs build, quickstart commands, or CI smoke commands;
- starts `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

## Recommended Next Decision

After independent audit and closeout, the next decision should be human-directed:

- authorize a separate environment repair/readiness ticket to align the local editable install or virtual environment with this workspace, or
- accept that local CLI execution remains blocked and continue only with docs/planning work that does not require CLI execution.

Do not treat QA-T002 as proof of local install correctness or CLI smoke success.

## Readiness Verdict

QA-T002 audit decision is `PASS`; no repair is required. QA-T002 is ready for closeout, and the next scoped ticket requires human direction.
