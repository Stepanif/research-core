# QA-T004 Implementation Report

Date: `2026-06-16`

Ticket: `QA-T004`

Branch: `main`

No NullForge implementation code has started.

## Summary

Implemented QA-T004 as a docs-only local Python environment repair/readiness path preparation ticket.

The implementation created a human-gated path packet at `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md`, updated NullForge status/source index references, and created QA-T004 reports. It recommends isolated project-local virtual environment preparation as the default future repair/readiness path, but does not execute any repair or validation commands.

## Files Changed

- `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/QA-T004/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T004/CHANGED_FILES.md`
- `reports/nullforge/QA-T004/TEST_RESULTS.md`
- `reports/nullforge/QA-T004/AUDITOR_PROMPT.md`

## Acceptance Status

| Criterion | Status |
|---|---|
| QA-T004 path doc exists | PASS |
| QA-T004 reports exist | PASS |
| Prerequisite audit `Decision: PASS` evidence for QA-T001, HY-T001, QA-T002, and QA-T003 is recorded | PASS |
| Unresolved blocker includes `python -m research_core.cli` and `No module named research_core.cli` | PASS |
| `<local-temp-editable-install>` is retained as sanitized inherited evidence | PASS |
| Source facts, recorded observations, unsupported command shapes, unresolved blockers, candidate paths, and recommended path are separated | PASS |
| No repair, install, test, docs build, CI smoke, package, source, or downstream work was run | PASS |
| Human gates are explicit | PASS |

## Commands Run

Only bounded read/status/search/file operations were run.

- `git status --short --branch`
- `Get-Content -LiteralPath ...` for required source files
- `rg -n "Decision: PASS" ...`
- `rg -n '\[project\.scripts\]|console_scripts|package-dir|pythonpath|typer|def main|if __name__ == "__main__"|app = typer|ci run|research_core\.cli' ...`
- `New-Item -ItemType Directory -Force -Path reports\nullforge\QA-T004`

One supplemental `rg` metadata command failed because of PowerShell quote handling and was rerun with safe quoting. The directory creation first hit a Windows sandbox helper launch issue and was rerun with approval for the same allowed QA-T004 reports directory.

## Commands Skipped

The following were forbidden and not run:

- install, uninstall, editable install, dependency sync, package build;
- virtual-environment creation, activation, deletion, selection, or repair;
- `python -m research_core.cli --help`;
- `python -m research_core --help`;
- `research-core --help`;
- `python -m pytest`, `python -m pytest -q`, `pytest -q`;
- docs generation and generated-doc verification;
- `python -m mkdocs build`;
- quickstart commands;
- `python -m research_core.cli ci run --config .github/ci/ci.github.json`.

## Deviations

No scope deviations.

QA-T004 documents a future command packet labeled `not run`. It does not execute the packet.

## Dependency / Security / Migration / Deployment Changes

None.

No dependencies, package metadata, source files, tests, schemas, fixtures, CI, generated docs, migration files, auth, permissions, deployment, public distribution, or ResearchCore Engine implementation files were changed.

## Data And File Access Changes

None.

No raw/private data, ES-derived fixtures, generated datasets, or external package material were imported.

## Known Issues

The local Python environment and CLI/runtime blocker remains unresolved by design:

- editable install visibility points outside this workspace as `<local-temp-editable-install>`;
- `research_core.cli` is not visible to the active Python environment;
- `python -m research_core.cli --help` fails with `No module named research_core.cli`;
- `python -m research_core --help` is unsupported because `src/research_core/__main__.py` is absent;
- `research-core --help` is unsupported because no console script exists.

## Human Gate Status

No human gate was triggered during QA-T004 implementation because no repair or environment-changing command was run.

Human approval is still required before any later install, editable install, dependency sync, package build, virtual environment work, environment repair, full tests, docs generation, docs build, quickstart command, CI smoke command, package/source change, `ADR-T003`, desktop bridge/app work, or downstream M1 implementation.

## Next Recommended Action

Run independent audit for QA-T004.
