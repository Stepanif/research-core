# QA-T002 Context Bundle

## Ticket Summary

- Ticket ID: `QA-T002`
- Ticket name: Local Python environment and CLI/runtime blocker triage
- Phase: NullForge M1 readiness
- Role: Context Curator only
- Status: Ready for planner handoff

`QA-T002` should prepare a bounded path for investigating the local Python environment and CLI/runtime blocker found during `QA-T001`. The blocker is local-environment readiness only. It does not authorize package changes, dependency changes, source changes, tests, generated docs, or NullForge implementation work.

## M1 Readiness Purpose

`QA-T002` exists to clarify why current local CLI/runtime commands do not resolve the expected ResearchCore CLI surface and to prepare a later planner to define safe diagnostic scope.

The ticket should help answer:

- Whether the active local Python environment is pointed at the current workspace or at a stale editable install.
- Whether `python -m research_core.cli` should work from the current workspace without environment mutation.
- Whether the missing `research_core.__main__` and missing `research-core` console command are expected limitations or actual blockers.
- What human-approved action, if any, is needed before local CLI/test smoke work can continue.

## Non-Goals

`QA-T002` must not:

- Change Python environments, editable installs, virtual environments, dependencies, or package metadata.
- Run installs, uninstalls, full tests, docs generation, docs build, quickstart commands, or CI smoke commands.
- Create or modify app files, source code, tests, schemas, fixtures, package files, CI, generated docs, raw data, or private data.
- Start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.
- Claim CLI/runtime readiness until the blocker is resolved or explicitly accepted by a human.

## Completed Prerequisites

| Ticket | Evidence | Relevance |
| --- | --- | --- |
| `PF-T000` | Prior audit `PASS` recorded in NullForge status/index. | Repository inventory baseline. |
| `PF-T001` | Prior audit `PASS` recorded in NullForge status/index. | Source import/archive foundation. |
| `PF-T002` | Prior audit `PASS` recorded in NullForge status/index. | Canonical docs baseline. |
| `ADR-T001` | Prior audit `PASS` recorded in NullForge status/index. | Platform naming/stack decision boundary. |
| `ADR-T002` | Prior audit `PASS` recorded in NullForge status/index. | Local-first/no-cloud MVP boundary. |
| `CX-T001` | Prior audit `PASS` recorded in NullForge status/index. | Codex role-loop rules for bounded work. |
| `MB-T001` | Prior audit `PASS` recorded in NullForge status/index. | M0 handoff completion before M1 readiness. |
| `QA-T001` | `audits/nullforge/QA-T001/AUDIT_REPORT.md` contains `Decision: PASS`. | Discovered command/test surfaces and the local CLI/runtime blocker. |
| `HY-T001` | `audits/nullforge/HY-T001/AUDIT_REPORT.md` contains `Decision: PASS`. | Sanitized local absolute path leakage; blocker evidence now uses placeholders. |

## QA-T001 Blocker Summary

`QA-T001` found that local command discovery could not treat the CLI/runtime surface as ready:

- `python -m pip show research-core` reported an editable install from `<local-temp-editable-install>`, not from the current workspace.
- `python -m research_core.cli --help` failed with `No module named research_core.cli`.
- `python -m research_core --help` failed because `research_core` has no `__main__`.
- `research-core --help` was not recognized as a command.
- `python -m pytest --version` was available, but full test execution was intentionally skipped.

The blocker is environmental and executable-readiness related. It is not evidence that the source tree lacks a CLI module.

## Package And CLI Metadata

The current repository metadata and source surface indicate:

- `pyproject.toml` is the package metadata source.
- Project name: `research-core`.
- Project version: `0.1.0`.
- Required Python: `>=3.11`.
- Declared runtime dependencies include `pandas`, `pyarrow`, and `typer`.
- Declared dev extra includes `pytest`.
- Setuptools package discovery uses `package-dir = {"" = "src"}` and finds packages under `src`.
- Pytest config sets `pythonpath = ["src"]` and `testpaths = ["tests"]`.
- No `[project.scripts]` or console script entry point is declared in `pyproject.toml`.
- `src/research_core/cli.py` exists and contains a Typer CLI surface with a `main` entrypoint and module guard.
- `src/research_core/__main__.py` is absent, so `python -m research_core` failing is likely expected unless a later ticket intentionally adds that module.
- CI and repo docs reference `python -m research_core.cli`, including `.github/workflows/research-ci.yml`, `docs/how-to/run_ci_locally.md`, and `docs/reference/cli/overview.md`.
- Root Node package files are absent in the current Python-oriented repository context: `package.json`, `pnpm-workspace.yaml`, and `pnpm-lock.yaml`.

## Relevant Files For Later Planning

Likely relevant read-only context for the `QA-T002` planner:

- `plans/nullforge/QA-T002/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T002/CONTEXT_BUNDLE_MANIFEST.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/M0_HANDOFF.md`
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`
- `reports/nullforge/QA-T001/TEST_RESULTS.md`
- `audits/nullforge/HY-T001/AUDIT_REPORT.md`
- `reports/nullforge/HY-T001/TEST_RESULTS.md`
- `pyproject.toml`
- `README.md`
- `docs/how-to/run_ci_locally.md`
- `docs/reference/cli/overview.md`
- `docs/reference/cli/index.md`
- `.github/workflows/research-ci.yml`
- `.github/workflows/docs.yml`
- `src/research_core/cli.py`
- `src/research_core/__init__.py`
- The absence of `src/research_core/__main__.py`

## Explicitly Excluded

The following are out of scope for `QA-T002` curation and should remain excluded unless a later human-approved ticket changes scope:

- Source edits under `src/`
- Test edits or new tests under `tests/`
- Schema or fixture edits under `schemas/` or `fixtures/`
- Package/dependency metadata edits, including `pyproject.toml`, lockfiles, or package manager files
- CI edits under `.github/`
- Generated docs or docs generation output
- Local environment mutation, including install, uninstall, editable install, venv recreation, dependency sync, or package repair
- Full test runs, docs builds, quickstart commands, and CI smoke commands
- `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, or downstream product work
- Raw/private data, ES-derived fixtures, incoming package material, marketplace/public distribution work

## Current Repo State

Pre-curation status check:

```text
git status --short --branch
## main...origin/main
```

Only the approved `QA-T002` context curator artifacts should be created by this ticket.

`No NullForge implementation code has started.`

## Known Gates

Human approval is required before any later stage:

- Runs an install, uninstall, editable install, environment repair, dependency sync, or venv recreation.
- Modifies `pyproject.toml`, source files, tests, generated docs, package files, or CI.
- Treats missing `research_core.__main__` or missing `research-core` console command as a product requirement rather than a local readiness finding.
- Runs full tests, docs generation, docs build, quickstart commands, or CI smoke commands.
- Starts `ADR-T003`, app scaffolding, desktop shell, bridge, sidecar, or downstream M1 implementation.

## Stop Conditions

Stop and return to the human if:

- The working tree contains unrelated changes outside approved QA-T002 planning paths.
- Any diagnostic command would mutate the Python environment or produce generated artifacts.
- A command requires installing, uninstalling, or changing dependencies.
- Source/package/CI changes appear necessary to continue.
- The blocker cannot be separated from broader CLI contract or packaging design decisions.

## Constraints And Forbidden Actions

For later planning, keep `QA-T002` bounded to local environment and CLI/runtime blocker triage. The planner may propose diagnostic commands, but should separate:

- Read-only or low-side-effect diagnostics that can run without environment mutation.
- Commands that may create bytecode/cache side effects and therefore need a side-effect policy such as `python -B` or `PYTHONDONTWRITEBYTECODE=1`.
- Environment-changing repair commands that require explicit human approval and likely a separate implementation scope.

No NullForge implementation code, app code, source repair, package repair, or downstream work is authorized by this context bundle.

## Required Checks For Later Stages

Minimum checks expected for later planner/implementor/auditor stages:

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `Test-Path -LiteralPath pyproject.toml`
- `Test-Path -LiteralPath src\research_core\cli.py`
- `Test-Path -LiteralPath src\research_core\__main__.py`
- `rg -n "Decision: PASS" audits\nullforge\QA-T001\AUDIT_REPORT.md audits\nullforge\HY-T001\AUDIT_REPORT.md`
- `rg -n "local-temp-editable-install|python -m research_core.cli|No module named research_core.cli|research-core --help" docs\nullforge\qa\COMMAND_DISCOVERY.md reports\nullforge\QA-T001\TEST_RESULTS.md`
- `rg -n "\[project\.scripts\]|console_scripts|package-dir|pythonpath|typer|def main|if __name__ == \"__main__\"" pyproject.toml src\research_core\cli.py`
- `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools`

Any later Python import/runtime diagnostic should avoid environment mutation and should account for bytecode/cache side effects.

## Open Questions

- Should `QA-T002` remain diagnose-only, or may a later implementor perform a human-approved local editable install repair?
- Should local CLI readiness be judged by `python -m research_core.cli` only, or should a future ticket add a console script?
- Is `python -m research_core` intentionally unsupported, or should that become a separate future ticket?
- Should CLI reference docs be trusted as current contract, or should any mismatch be handled through a later generated-docs verification ticket?

## Ready-For-Planner Verdict

`QA-T002` is ready for planner handoff.

The planner should create bounded `PLAN.md`, `ACCEPTANCE.md`, and `IMPLEMENTOR_PROMPT.md` artifacts only, with explicit human gates before any environment-changing action.
