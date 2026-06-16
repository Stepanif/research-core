# QA-T003 Context Bundle

Date: `2026-06-16`

Ticket: `QA-T003`

Role: Context Curator

Status: Ready for planner

No NullForge implementation code has started.

## Ticket Summary

`QA-T003` is a NullForge M1 readiness ticket for local Python environment repair decisioning after `QA-T002`.

The ticket should prepare a later planner to decide how to frame a human-gated environment readiness step. It must not perform environment repair, choose a repair path, run installs, change package metadata, change source, run tests, generate docs, build docs, run quickstart commands, run CI smoke commands, or start downstream implementation.

## M1 Readiness Purpose

`QA-T003` exists because `QA-T002` confirmed that local executable readiness is blocked:

- active Python package visibility does not point at the current workspace;
- `research_core.cli` is not visible to the active Python environment;
- `python -m research_core.cli --help` fails locally;
- `python -m research_core --help` is unsupported because `src/research_core/__main__.py` is absent;
- `research-core --help` is unsupported because no console script is declared.

The readiness purpose is to help a planner prepare a bounded, human-approved path for resolving or explicitly deferring the local environment blocker before any future ticket relies on local CLI execution.

## Non-Goals

`QA-T003` context curation does not:

- repair or mutate the Python environment;
- install, uninstall, editable install, sync dependencies, or build packages;
- change `pyproject.toml`, source code, tests, schemas, fixtures, dependency files, CI, generated docs, README, or package metadata;
- add a console script or `src/research_core/__main__.py`;
- run full tests, docs generation, docs build, quickstart commands, or CI smoke commands;
- start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work;
- treat local CLI readiness as proven.

## Completed Prerequisites

| Ticket | Status | Evidence |
|---|---|---|
| `QA-T001` | Complete; audit `PASS` | `audits/nullforge/QA-T001/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `HY-T001` | Complete; audit `PASS` | `audits/nullforge/HY-T001/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `QA-T002` | Complete; audit `PASS` | `audits/nullforge/QA-T002/AUDIT_REPORT.md` contains `Decision: PASS`. |

Earlier M0 dependencies remain complete and active through current status and source index: `PF-T000`, `PF-T001`, `PF-T002`, `ADR-T001`, `ADR-T002`, `CX-T001`, and `MB-T001`.

## QA-T002 Blocker Summary

`QA-T002` records the following local environment observations:

- `python -B -m pip show research-core` succeeded but reported editable project location `<local-temp-editable-install>`, not the current workspace.
- Python diagnostics used `python -B` and did not intentionally create bytecode.
- Importlib resolved `research_core` as a namespace package from `<external-local-research-core-namespace-path>`.
- Importlib resolved `research_core.cli` as `None`.
- `python -B -m research_core.cli --help` failed with `No module named research_core.cli`.
- `python -B -m research_core --help` failed because `research_core.__main__` is absent.
- `research-core --help` failed because PowerShell did not recognize the command.

`QA-T002` interprets this as a local Python visibility/install-state blocker, not absence of `src/research_core/cli.py` in the current workspace.

## Existing Package And CLI Facts

| Source | Fact |
|---|---|
| `pyproject.toml` | Project name is `research-core`; version is `0.1.0`; `requires-python = ">=3.11"`. |
| `pyproject.toml` | Runtime dependencies are `pandas>=2.2.0`, `pyarrow>=16.0.0`, and `typer>=0.12.0`. |
| `pyproject.toml` | Optional `dev` extra includes `pytest>=8.0.0`. |
| `pyproject.toml` | `package-dir = {"" = "src"}` and package discovery is under `src`. |
| `pyproject.toml` | Pytest config sets `pythonpath = ["src"]` and `testpaths = ["tests"]`. |
| `pyproject.toml` | No `[project.scripts]` or `console_scripts` entry point is present. |
| `src/research_core/cli.py` | File exists and defines a Typer `app`, registered subcommands, `main()`, and an `if __name__ == "__main__"` guard. |
| `docs/reference/cli/overview.md` | Documents `python -m research_core.cli [OPTIONS] COMMAND [ARGS]...`. |
| `docs/how-to/run_ci_locally.md` | Documents install, pytest, docs generation/build, and CI smoke commands that remain forbidden for QA-T003 curation. |
| `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md` | Distinguishes source facts from environment observations and keeps repair human-gated. |

## Candidate Repair Paths For Later Human Approval

These are decision inputs only. QA-T003 context curation does not choose or execute them.

| Candidate | What it could address | Required human gate |
|---|---|---|
| Reinstall current workspace editable in the active Python environment | Align `research-core` package visibility with the current workspace so `python -m research_core.cli --help` can be retried. | Requires explicit approval for install/editable install and environment mutation. |
| Create or select a project-local virtual environment, then install the current workspace there | Avoid modifying unrelated global Python state and isolate local readiness commands. | Requires explicit approval for venv creation/selection, install commands, dependency sync, and possible activation instructions. |
| Run diagnostics only and keep CLI execution blocked | Preserve current environment while documenting that future work cannot rely on local CLI execution. | Requires human acceptance that local executable readiness remains unavailable. |
| Add package metadata or source entrypoint support in a future implementation ticket | Could make `research-core --help` or `python -m research_core --help` supported if product direction requires it. | Requires a separate scoped code/package ticket; not a QA-T003 repair-only action. |
| Defer environment repair until a later M1 implementation ticket | Keeps planning moving but preserves blocker for any executable work. | Requires human decision that downstream work will not rely on local CLI execution until resolved. |

## Files And Folders Likely Relevant To Later Planning

- `plans/nullforge/QA-T003/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T003/CONTEXT_BUNDLE_MANIFEST.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`
- `audits/nullforge/HY-T001/AUDIT_REPORT.md`
- `audits/nullforge/QA-T002/AUDIT_REPORT.md`
- `reports/nullforge/QA-T002/TEST_RESULTS.md`
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
- `reports/nullforge/QA-T003/`
- `audits/nullforge/QA-T003/`
- downstream `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, or M1 implementation artifacts

## Current Repo State

Before QA-T003 context artifact creation, `git status --short --branch` reported:

```text
## main...origin/main
```

`main` is clean and aligned with `origin/main`. QA-T002 is complete and pushed with audit `PASS`.

## Known Gates And Stop Conditions

Human approval is required before:

- any install, uninstall, editable install, dependency sync, package build, venv creation, venv activation workflow, or environment repair command;
- modifying `pyproject.toml`, dependencies, package metadata, source, tests, schemas, fixtures, CI, generated docs, README, or docs/reference files;
- adding `[project.scripts]`, `console_scripts`, or `src/research_core/__main__.py`;
- running full tests, docs generation, docs build, quickstart commands, or CI smoke commands;
- changing ResearchCore Engine behavior;
- starting `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

Stop if:

- the working tree is dirty outside `plans/nullforge/QA-T003/`;
- a required prerequisite audit is missing or not `PASS`;
- the planner needs to choose a repair path without human direction;
- local environment repair appears necessary to complete planning;
- package/source/test/CI/generated-doc changes appear necessary;
- a command would mutate Python environment state;
- acceptance criteria require executable proof rather than decisioning.

## Constraints And Forbidden Actions

- Context curation may create only `plans/nullforge/QA-T003/CONTEXT_BUNDLE.md` and `plans/nullforge/QA-T003/CONTEXT_BUNDLE_MANIFEST.md`.
- Do not modify existing files.
- Do not run installs, uninstalls, editable installs, dependency sync, package builds, environment repair, full tests, docs generation, docs builds, quickstart commands, or CI smoke commands.
- Do not create `PLAN.md`, `ACCEPTANCE.md`, `IMPLEMENTOR_PROMPT.md`, reports, audits, QA docs, tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, or downstream artifacts.
- Preserve `No NullForge implementation code has started.`

## Required Checks For Later Stages

The later planner should preserve or refine bounded checks such as:

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- prerequisite `Decision: PASS` searches for `QA-T001`, `HY-T001`, and `QA-T002`
- path existence checks for planned outputs
- source-term searches for `python -m research_core.cli`, `No module named research_core.cli`, `<local-temp-editable-install>`, and `No NullForge implementation code has started`
- forbidden tracked-path diff checks covering `src`, `tests`, `schemas`, `fixtures`, `pyproject.toml`, dependency/package files, `.github`, `README.md`, `docs/reference`, and `tools`
- explicit checks proving no `tickets`, `milestones`, `prompts`, `reports/nullforge/QA-T003`, or `audits/nullforge/QA-T003` exist before later roles create allowed artifacts

If a later implementor is authorized to repair the environment, that authorization must be explicit and should define exact commands, allowed side effects, rollback/cleanup expectations, and whether command output may include local absolute paths.

## Open Questions

- Should the next scoped ticket authorize an isolated project-local virtual environment, an active-environment editable reinstall, diagnostics-only deferral, or a different repair path?
- Should `python -m research_core.cli --help` be the only immediate readiness target, or should future tickets also consider `research-core --help` and `python -m research_core --help` support?
- Is global Python environment mutation acceptable, or must any repair be isolated to a project-local environment?
- Should local absolute diagnostic paths continue to be sanitized in all QA-T003 reports and audits?

## Ready-For-Planner Verdict

Ready for planner.

The planner can create bounded planning artifacts for `QA-T003` using this context, but must not implement, install, repair, or broaden scope without explicit human approval.
