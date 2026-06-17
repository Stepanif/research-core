# QA-T005 Environment Repair Execution

Date: `2026-06-16`

Ticket: `QA-T005`

Role: Implementor

Status: Ready for independent audit

No NullForge implementation code has started.

## Purpose

Execute the human-approved isolated project-local Python environment readiness path from `QA-T004` and record bounded evidence for the local CLI/runtime blocker.

This ticket is environment readiness work only. It does not modify source, package metadata, dependencies, tests, schemas, fixtures, CI, generated docs, README, `docs/reference`, or ResearchCore Engine implementation files.

## Human Approval Confirmed

The implementor prompt included the exact approval phrase:

```text
I approve QA-T005 environment execution.
```

The selected path was an isolated project-local virtual environment at `.venv-qa-t005`.

Approved commands were limited to:

- `python -m venv .venv-qa-t005`
- `.venv-qa-t005\Scripts\python.exe -m pip install --upgrade pip`
- `.venv-qa-t005\Scripts\python.exe -m pip install -e .[dev]`
- `.venv-qa-t005\Scripts\python.exe -m pip show research-core`
- `.venv-qa-t005\Scripts\python.exe -B -c "import importlib.util; print(importlib.util.find_spec('research_core')); print(importlib.util.find_spec('research_core.cli'))"`
- `.venv-qa-t005\Scripts\python.exe -m research_core.cli --help`

The prompt kept these commands and work areas forbidden:

- `python -m pytest`
- `python -m pytest -q`
- `pytest -q`
- docs generation
- docs build
- quickstart commands
- CI smoke commands
- `python -m research_core --help`
- `research-core --help`
- package/source/dependency/CI/generated-doc changes
- `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work

## Prerequisite Evidence

| Ticket | Audit evidence | Result |
|---|---|---|
| `QA-T001` | `audits/nullforge/QA-T001/AUDIT_REPORT.md` | `Decision: PASS` |
| `HY-T001` | `audits/nullforge/HY-T001/AUDIT_REPORT.md` | `Decision: PASS` |
| `QA-T002` | `audits/nullforge/QA-T002/AUDIT_REPORT.md` | `Decision: PASS` |
| `QA-T003` | `audits/nullforge/QA-T003/AUDIT_REPORT.md` | `Decision: PASS` |
| `QA-T004` | `audits/nullforge/QA-T004/AUDIT_REPORT.md` | `Decision: PASS` |

## Inherited Blocker

`QA-T002` and `QA-T004` recorded the local Python environment / CLI blocker:

- editable install visibility pointed outside this workspace as `<local-temp-editable-install>`;
- `research_core.cli` was not visible to the active Python environment;
- `python -m research_core.cli --help` failed with `No module named research_core.cli`;
- `python -m research_core --help` is unsupported because `src/research_core/__main__.py` is absent;
- `research-core --help` is unsupported because no console script exists.

## Source Facts Used

| Source | Fact |
|---|---|
| `pyproject.toml` | Declares package name `research-core`, `requires-python = ">=3.11"`, `package-dir = {"" = "src"}`, `pythonpath = ["src"]`, and no `[project.scripts]` entry. |
| `docs/reference/cli/overview.md` | Documents `python -m research_core.cli` as the CLI shape. |
| `docs/how-to/run_ci_locally.md` | Documents install, docs, test, and CI smoke commands as existing repo context, but QA-T005 did not run full tests, docs, quickstart, or CI smoke. |
| `src/research_core/cli.py` | Defines a Typer CLI app, registers `ci_app`, defines `ci run`, defines `main()`, and has an `if __name__ == "__main__"` guard. |
| `src/research_core/__main__.py` | Absent; `python -m research_core --help` remains unsupported and was not run. |

## Approved Command Results

| Step | Command | Result | Recorded evidence |
|---|---|---|---|
| Create venv | `python -m venv .venv-qa-t005` | PASS | Project-local venv created. |
| Upgrade pip | `.venv-qa-t005\Scripts\python.exe -m pip install --upgrade pip` | PASS | `pip` upgraded inside `<project-local-venv>` to `26.1.2`. |
| Editable dev install | `.venv-qa-t005\Scripts\python.exe -m pip install -e .[dev]` | PASS | `research-core==0.1.0` built as an editable wheel and installed inside `<project-local-venv>` with declared dev dependencies. |
| Package metadata | `.venv-qa-t005\Scripts\python.exe -m pip show research-core` | PASS | Location: `<project-local-venv>\Lib\site-packages`; Editable project location: `<repo-root>`; Requires: `pandas`, `pyarrow`, `typer`. |
| Module visibility | `.venv-qa-t005\Scripts\python.exe -B -c "import importlib.util; ..."` | PASS | `research_core` resolves to `<repo-root>\src\research_core\__init__.py`; `research_core.cli` resolves to `<repo-root>\src\research_core\cli.py`. |
| Documented CLI help | `.venv-qa-t005\Scripts\python.exe -m research_core.cli --help` | PASS | CLI help displayed `python -m research_core.cli [OPTIONS] COMMAND [ARGS]...` with commands including `canon`, `psa`, `validate`, `registry`, `observe`, `bundle`, `experiment`, `project`, `doctor`, `verify`, `plan`, `dataset`, `lineage`, `runset`, `risk`, `baseline`, `ci`, `release`, `prune`, and `pilot`. |

## Bounded Readiness Conclusion

Inside the approved isolated `.venv-qa-t005` environment:

- `research-core` is installed editable from `<repo-root>`;
- `research_core` is import-visible;
- `research_core.cli` is import-visible;
- `python -m research_core.cli --help` succeeds.

The original active/global Python environment blocker is not repaired or re-tested by this ticket. QA-T005 does not make `python -m research_core --help` or `research-core --help` supported, because those command shapes remain expected unsupported behavior without a separate source/package ticket.

## Side Effects Observed

| Path or area | Observation | Disposition |
|---|---|---|
| `.venv-qa-t005/` | Created by approved command and left in place. `git status --ignored` reports it as ignored. | Deferred per cleanup policy; do not stage or commit. |
| `src/research_core/**/__pycache__/` | Ignored Python cache directories observed after approved CLI help import. | Reported; not staged or cleaned. |
| `.pytest_cache/` | Ignored cache directory observed. No pytest command was run during QA-T005. | Reported; not staged or cleaned. |
| `exec_outputs/` | Not present. | No action. |
| generated docs | No docs generation or docs build was run. | No action. |
| source/package/test/schema/fixture/CI files | No tracked changes observed. | No action. |

## Skipped Commands

The following stayed skipped because they were explicitly forbidden:

- `python -m pytest`
- `python -m pytest -q`
- `pytest -q`
- docs generation
- docs build
- quickstart commands
- CI smoke commands
- `python -m research_core --help`
- `research-core --help`

## Human Gates

- Independent audit is required before closeout.
- Commit requires a later explicit closeout prompt.
- Push requires a later explicit push prompt.
- Any full test, docs build, CI smoke, active/global environment repair, source/package change, console script support, `__main__.py` support, or downstream NullForge implementation requires a separate scoped ticket and explicit human approval.

## Ready-For-Audit Verdict

Ready for independent audit.

QA-T005 executed only the approved isolated project-local environment command packet, recorded sanitized outputs, preserved `No NullForge implementation code has started.`, and left source/package/test/CI files unchanged.
