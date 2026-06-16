# QA-T001 Command Discovery

Date: `2026-06-16`

Ticket: `QA-T001`

Status: `AUDIT_PASS_READY_FOR_CLOSEOUT`

No NullForge implementation code has started.

## Purpose

QA-T001 records the existing ResearchCore repository command and test surfaces before NullForge M1 implementation planning proceeds. It is a docs-only readiness ticket: it discovers candidate commands, local environment blockers, package metadata, CI references, fixture/sample locations, and command side-effect boundaries.

QA-T001 does not run full tests, install dependencies, generate docs, build docs, create code, create tests, create schemas, create fixtures, or start ADR-T003, desktop shell, bridge, sidecar, app scaffolding, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

## Prerequisite Audit Evidence

| Ticket | Required disposition | Evidence |
|---|---|---|
| `PF-T000` | Audit `PASS` | `audits/nullforge/PF-T000/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `PF-T001` | Audit `PASS` | `audits/nullforge/PF-T001/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `PF-T002` | Audit `PASS` | `audits/nullforge/PF-T002/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `ADR-T001` | Audit `PASS` | `audits/nullforge/ADR-T001/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `ADR-T002` | Audit `PASS` | `audits/nullforge/ADR-T002/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `CX-T001` | Audit `PASS` | `audits/nullforge/CX-T001/AUDIT_REPORT.md` contains `Decision: PASS`. |
| `MB-T001` | Audit `PASS` | `audits/nullforge/MB-T001/AUDIT_REPORT.md` contains `Decision: PASS`. |

## Package Metadata

| Item | Discovery |
|---|---|
| Primary package metadata | `pyproject.toml`. |
| Project name | `research-core`. |
| Project version | `0.1.0`. |
| Python requirement | `>=3.11` from `pyproject.toml`; CI currently uses Python `3.13.7`. |
| Runtime dependencies | `pandas>=2.2.0`, `pyarrow>=16.0.0`, `typer>=0.12.0`. |
| Dev dependency surface | Optional `dev` extra includes `pytest>=8.0.0`. |
| Pytest configuration | `pythonpath = ["src"]`; `testpaths = ["tests"]`. |
| Console script entrypoint | None found in `pyproject.toml`. |
| Docs dependency file | `requirements-docs.txt`. |
| Root `package.json` | Absent by bounded `Test-Path`. |
| Root `pnpm-workspace.yaml` | Absent by bounded `Test-Path`. |
| Root `pnpm-lock.yaml` | Absent by bounded `Test-Path`. |

## Local Runtime Discovery

| Command | Result |
|---|---|
| `python --version` | Succeeded with `Python 3.13.7`. |
| `python -m pip --version` | Succeeded with `pip 25.2` for Python 3.13. |
| `python -m pip show research-core` | Succeeded, but the editable project location points to `C:\Users\Filip\AppData\Local\Temp\research-core-gha-clone-4240fe0c-bf57-4da4-9836-29bf7009cdca`, not the current workspace. |
| `python -m pip show pyarrow` | Succeeded with installed `pyarrow` version `23.0.1`. |
| `python -m pip show pytest` | Succeeded with installed `pytest` version `9.0.2`. |
| `python -m pytest --version` | Succeeded with `pytest 9.0.2`. |

The local package visibility is not proven to match this workspace. Future tickets that depend on executing the current repo package should treat the editable install location mismatch as a blocker until a scoped, human-approved environment step resolves it.

## Existing Test Command Candidates

| Candidate | Evidence | QA-T001 action |
|---|---|---|
| `python -m pytest -q` | Referenced by `README.md`, `.github/workflows/research-ci.yml`, and `docs/how-to/run_ci_locally.md`. | Candidate only; not run because full tests are forbidden in QA-T001. |
| `pytest -q` | Referenced by local CI docs as a shorthand test command. | Candidate only; not run because full tests are forbidden in QA-T001. |
| `python -m pytest --version` | Allowed bounded discovery command. | Run only as version discovery; it does not execute the test suite. |

QA-T001 does not prove test pass/fail status. It only identifies existing command candidates.

## Existing Docs Command Candidates

| Candidate | Evidence | QA-T001 action |
|---|---|---|
| `python tools/docs/gen_cli_ref.py` | Referenced by `README.md`, `.github/workflows/docs.yml`, and `docs/how-to/run_ci_locally.md`. | Candidate only; not run because docs generation is forbidden in QA-T001. |
| `python tools/docs/gen_schema_ref.py` | Referenced by `README.md`, `.github/workflows/docs.yml`, and `docs/how-to/run_ci_locally.md`. | Candidate only; not run because docs generation is forbidden in QA-T001. |
| `python tools/docs/gen_artifact_catalog.py` | Referenced by `README.md`, `.github/workflows/docs.yml`, and `docs/how-to/run_ci_locally.md`. | Candidate only; not run because docs generation is forbidden in QA-T001. |
| `python tools/docs/verify_generated_docs_clean.py` | Referenced by `README.md`, `.github/workflows/docs.yml`, and `docs/how-to/run_ci_locally.md`. | Candidate only; not run because generated-doc verification is forbidden in QA-T001. |
| `python -m mkdocs build` | Referenced by `.github/workflows/docs.yml` and `docs/how-to/run_ci_locally.md`. | Candidate only; not run because docs build is forbidden in QA-T001. |

## Existing CLI Invocation Evidence

| Candidate | Evidence or observed result | QA-T001 action |
|---|---|---|
| `python -m research_core.cli --help` | Documented CLI invocation pattern in `docs/reference/cli/overview.md` and local docs. Bounded local query failed with `No module named research_core.cli`. | Observed as unsupported in the current local Python visibility; likely blocked by editable install mismatch or package path state. |
| `python -m research_core --help` | Volume 07 lists this as a command candidate to verify, not assume. Bounded local query failed because `research_core` has no `__main__`. | Observed unsupported in current local environment. |
| `research-core --help` | Volume 07 lists this as a command candidate to verify, not assume. Bounded local query failed because the command is not recognized by PowerShell. | Observed unsupported in current local environment; `pyproject.toml` has no console script entrypoint. |
| `python -m research_core.cli ci run --config .github/ci/ci.github.json` | Referenced by `.github/workflows/research-ci.yml` and `docs/how-to/run_ci_locally.md`. | Candidate only; not run because CI smoke commands are forbidden in QA-T001. |

## Existing Fixture And Sample Paths

The repo already contains test fixtures and golden/sample-style paths documented by existing test docs and local context. QA-T001 did not create, edit, copy, or validate fixture data.

Likely relevant paths for later scoped work include:

- `tests/fixtures/`
- `tests/fixtures/raw_small_sample.txt`
- `tests/fixtures/raw_bad_ohlc.txt`
- `tests/fixtures/raw_duplicate_ts.txt`
- `tests/fixtures/raw_bad_timestamp.txt`
- `tests/fixtures/exp_specs/`
- `tests/golden/`

## Commands Run

Only bounded discovery commands allowed by the QA-T001 plan were run. Full tests, docs generation, docs build, installs, quickstart commands, and CI smoke commands were not run.

| Command | Result |
|---|---|
| `git status --short --branch` | Succeeded; before implementation file creation, only QA-T001 planner artifacts were untracked. |
| `git status --short --untracked-files=all` | Succeeded; before implementation file creation, listed the five QA-T001 planner files only. |
| `git diff --name-only` | Succeeded with no output before implementation edits. |
| `git diff --check` | Succeeded with no output before implementation edits. |
| `Test-Path -LiteralPath package.json` | `False`. |
| `Test-Path -LiteralPath pnpm-workspace.yaml` | `False`. |
| `Test-Path -LiteralPath pnpm-lock.yaml` | `False`. |
| `Test-Path -LiteralPath pyproject.toml` | `True`. |
| `Test-Path -LiteralPath requirements-docs.txt` | `True`. |
| `python --version` | Succeeded with `Python 3.13.7`. |
| `python -m pip --version` | Succeeded with `pip 25.2`. |
| `python -m pip show research-core` | Succeeded; package is installed editable from a temporary clone path, not this workspace. |
| `python -m pip show pyarrow` | Succeeded with `pyarrow 23.0.1`. |
| `python -m pip show pytest` | Succeeded with `pytest 9.0.2`. |
| `python -m pytest --version` | Succeeded with `pytest 9.0.2`. |
| `python -m research_core.cli --help` | Failed with `No module named research_core.cli`. |
| `python -m research_core --help` | Failed because `research_core` has no `__main__`. |
| `research-core --help` | Failed because `research-core` is not recognized as a command. |
| `rg -n "python -m pytest|pytest -q|python -m research_core.cli|pip install|mkdocs build|gen_cli_ref|gen_schema_ref|gen_artifact_catalog|verify_generated_docs_clean" README.md docs .github pyproject.toml requirements-docs.txt` | Succeeded and found existing command references in README, CI workflows, local CI docs, CLI docs, and generated/reference docs. |

## Commands Skipped

| Command or class | Reason |
|---|---|
| `python -m pytest` | Explicitly forbidden full test command. |
| `python -m pytest -q` | Explicitly forbidden full test command. |
| `python tools/docs/gen_cli_ref.py` | Explicitly forbidden docs-generation command. |
| `python tools/docs/gen_schema_ref.py` | Explicitly forbidden docs-generation command. |
| `python tools/docs/gen_artifact_catalog.py` | Explicitly forbidden docs-generation command. |
| `python tools/docs/verify_generated_docs_clean.py` | Explicitly forbidden generated-doc verification command. |
| `python -m mkdocs build` | Explicitly forbidden docs-build command. |
| `pip install` and `python -m pip install` | Explicitly forbidden install commands. |
| Quickstart commands | Explicitly forbidden in QA-T001. |
| CI smoke command `python -m research_core.cli ci run --config .github/ci/ci.github.json` | Explicitly forbidden CI smoke command. |

## Side-Effect Review

Before QA-T001 implementation files were created, post-discovery `git status` and `git diff` showed only the pre-existing untracked QA-T001 planner artifacts and no tracked diff. No artifact-producing commands were run. QA-T001 did not intentionally create or modify `.pytest_cache/`, `exec_outputs/`, docs build output, or generated docs; no such side effects appeared in the bounded status/diff checks.

## Human Gates And Blockers

No human gate was triggered during QA-T001 implementation because no forbidden command, dependency change, code change, fixture change, generated-doc update, or ResearchCore Engine modification was performed.

The local command environment has a blocker for future executable work: `research-core` is installed from a temporary clone path, and the documented CLI module command failed in the current local visibility. A later scoped ticket should either resolve the environment/install state with human approval or treat local CLI execution as unavailable.

## Ready For Audit

QA-T001 has audit decision `PASS` and is ready for closeout. The next scoped ticket requires human direction. ADR-T003, desktop shell, bridge, sidecar, app scaffolding, and downstream M1 implementation remain not started.
