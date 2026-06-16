# QA-T004 Context Bundle

Date: `2026-06-16`

Ticket: `QA-T004`

Role: Context Curator

Status: Ready for planner

No NullForge implementation code has started.

## Ticket Summary

`QA-T004` is a NullForge M1 readiness ticket for choosing and preparing a local Python environment repair/readiness path after `QA-T003`.

This context bundle prepares the later planner to frame a human-approved repair/readiness step. It does not choose a repair path, run diagnostics, install packages, create or activate a virtual environment, repair the active Python environment, change source/package files, run tests, generate docs, build docs, run quickstart commands, run CI smoke commands, or start downstream implementation.

## M1 Readiness Purpose

M1 readiness remains blocked for any work that depends on local CLI execution because the active local Python environment has not proven visibility to this workspace's `research_core.cli`.

`QA-T004` should help the planner define the next scoped decision around one of the repair/readiness paths documented by `QA-T003`, while preserving the human gate before any environment mutation.

## Non-Goals

`QA-T004` context curation does not:

- install, uninstall, editable install, dependency sync, or build packages;
- create, select, activate, delete, or mutate a virtual environment;
- repair or mutate Python environment state;
- run `python -m research_core.cli --help`, `python -m research_core --help`, `research-core --help`, tests, docs generation, docs build, quickstart commands, or CI smoke commands;
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

Earlier M0 dependencies remain complete and active through current status and source index: `PF-T000`, `PF-T001`, `PF-T002`, `ADR-T001`, `ADR-T002`, `CX-T001`, and `MB-T001`.

## QA-T003 Decision Packet Summary

`QA-T003` created `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md` as a human-gated decision packet. Its audit decision is `PASS`, no repair is required, and no environment repair was performed.

The QA-T003 decision packet:

- preserves the exact no-code posture;
- records the unresolved QA-T002 local Python environment and CLI/runtime blocker;
- distinguishes source facts from local environment observations;
- identifies expected unsupported command shapes;
- lists repair/readiness options without choosing or executing one;
- requires human approval before any install, editable install, dependency sync, package build, virtual-environment work, environment repair, source/package change, full test, docs generation, docs build, quickstart command, CI smoke command, `ADR-T003`, desktop bridge/app work, or downstream M1 work.

## Unresolved Local Python Environment / CLI Blocker

The unresolved blocker remains:

- editable install visibility points outside this workspace as `<local-temp-editable-install>`;
- `research_core.cli` is not visible to the active Python environment;
- `python -m research_core.cli --help` fails with `No module named research_core.cli`;
- `python -m research_core --help` is unsupported because `src/research_core/__main__.py` is absent;
- `research-core --help` is unsupported because no console script exists.

This blocker is based on QA-T001 and QA-T002 recorded evidence. QA-T004 context curation did not rerun Python diagnostics or repair commands.

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
| `src/research_core/__main__.py` | Absent by bounded `Test-Path`. |
| root Node package files | `package.json`, `pnpm-workspace.yaml`, and `pnpm-lock.yaml` are absent by bounded `Test-Path`. |
| `docs/reference/cli/overview.md` | Documents `python -m research_core.cli [OPTIONS] COMMAND [ARGS]...`. |
| `docs/how-to/run_ci_locally.md` | Documents install, test, docs generation/build, and CI smoke commands. These are context only and remain forbidden for QA-T004 curation. |

## Candidate Repair / Readiness Paths From QA-T003

These are candidate paths for later planning only. QA-T004 context curation does not choose or execute any of them.

| Candidate | Decision value | Required human gate |
|---|---|---|
| Isolated project-local virtual environment | Could isolate local readiness from global Python state and make future CLI checks reproducible. | Approval for venv creation/selection, install commands, dependency sync, activation model, validation commands, and cleanup policy. |
| Active-environment editable reinstall | Could align the active environment's `research-core` visibility with this workspace faster. | Approval for active-environment mutation, exact install command, rollback, and verification commands. |
| Diagnostics-only deferral | Keeps environment untouched and explicitly accepts that local CLI execution remains unavailable. | Human acceptance that future executable work remains blocked until a later repair ticket. |
| Source/package entrypoint ticket | Could add `src/research_core/__main__.py` or console-script metadata if those command shapes are desired. | Separate source/package implementation scope, tests, docs updates, and audit. |
| Defer until future M1 implementation ticket | Avoids environment work now but preserves the blocker for future executable tickets. | Human decision that downstream work does not rely on local CLI execution until resolved. |

## Recommended Planning Inputs For Later Human-Approved Repair Path

The planner should require explicit human direction on:

- which repair/readiness path to prepare;
- whether the target is an isolated project-local environment, the active Python environment, diagnostics-only deferral, source/package entrypoint work, or a later M1 ticket;
- exact commands that may be run, if any;
- exact commands that remain forbidden;
- allowed environment side effects;
- cleanup and rollback expectations;
- whether local absolute paths in diagnostic output must be sanitized in reports;
- whether full tests, docs generation, docs build, quickstart commands, and CI smoke commands remain forbidden or become explicitly authorized for a later ticket;
- whether success means only package/module visibility, `python -m research_core.cli --help`, a CI smoke command, or a broader readiness proof;
- how to handle the unsupported `python -m research_core --help` and `research-core --help` command shapes.

## Files And Folders Likely Relevant To Later QA-T004 Planning

- `plans/nullforge/QA-T004/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T004/CONTEXT_BUNDLE_MANIFEST.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md`
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`
- `audits/nullforge/HY-T001/AUDIT_REPORT.md`
- `audits/nullforge/QA-T002/AUDIT_REPORT.md`
- `audits/nullforge/QA-T003/AUDIT_REPORT.md`
- `audits/nullforge/QA-T003/FINDINGS.md`
- `reports/nullforge/QA-T003/TEST_RESULTS.md`
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
- `reports/nullforge/QA-T004/`
- `audits/nullforge/QA-T004/`
- downstream `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution artifacts

## Current Repo State

Before QA-T004 context artifact creation, `git status --short --branch` reported:

```text
## main...origin/main
```

`main` is clean and aligned with `origin/main`. QA-T003 is complete and pushed with audit `PASS`.

## Known Gates And Stop Conditions

Human approval is required before:

- any install, uninstall, editable install, dependency sync, package build, virtual-environment creation/activation, environment repair, or command that mutates Python environment state;
- modifying `pyproject.toml`, dependencies, package metadata, source, tests, schemas, fixtures, CI, generated docs, README, docs/reference, or tools;
- adding `[project.scripts]`, `console_scripts`, or `src/research_core/__main__.py`;
- running full tests, docs generation, docs build, quickstart commands, or CI smoke commands;
- changing ResearchCore Engine behavior;
- starting `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

Stop if:

- working tree changes appear outside `plans/nullforge/QA-T004/`;
- a required prerequisite audit is missing or not `PASS`;
- context curation requires choosing a repair path;
- context curation requires live environment mutation;
- package/source/test/CI/generated-doc changes appear necessary;
- a command would mutate Python environment state;
- scope drifts toward implementation, tests, dependency changes, app work, or `ADR-T003`.

## Constraints And Forbidden Actions

- Context curation may create only `plans/nullforge/QA-T004/CONTEXT_BUNDLE.md` and `plans/nullforge/QA-T004/CONTEXT_BUNDLE_MANIFEST.md`.
- Do not modify existing files.
- Do not run installs, uninstalls, editable installs, dependency sync, package builds, virtual-environment creation/activation, environment repair, tests, docs generation, docs builds, quickstart commands, CI smoke commands, or other environment-changing commands.
- Do not create `PLAN.md`, `ACCEPTANCE.md`, `IMPLEMENTOR_PROMPT.md`, reports, audits, QA docs, tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, or downstream artifacts.
- Preserve `No NullForge implementation code has started.`

## Required Checks For Later Stages

The later planner should preserve or refine bounded checks such as:

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- prerequisite `Decision: PASS` searches for `QA-T001`, `HY-T001`, `QA-T002`, and `QA-T003`
- path existence checks for planned outputs
- source-term searches for `QA-T004`, `QA-T003`, `python -m research_core.cli`, `No module named research_core.cli`, `local-temp-editable-install`, and `No NullForge implementation code has started`
- forbidden tracked-path diff checks covering `src`, `tests`, `schemas`, `fixtures`, `pyproject.toml`, dependency/package files, `.github`, `README.md`, `docs/reference`, and `tools`
- explicit checks proving no `tickets`, `milestones`, `prompts`, `reports/nullforge/QA-T004`, or `audits/nullforge/QA-T004` exist before later roles create allowed artifacts

If a later implementor is authorized to repair the environment, that authorization must be explicit and should define exact commands, allowed side effects, rollback/cleanup expectations, output sanitization expectations, and validation commands.

## Open Questions Requiring Human Decision

- Which repair/readiness path should QA-T004 plan: isolated project-local virtual environment, active-environment editable reinstall, diagnostics-only deferral, source/package entrypoint work, or deferral to a later M1 implementation ticket?
- Is global Python environment mutation acceptable, or must any repair be isolated to a project-local environment?
- Should the immediate readiness target be only `python -m research_core.cli --help`, or should the later ticket also address `python -m research_core --help` and `research-core --help`?
- Are full tests, docs generation, docs build, quickstart commands, or CI smoke commands still forbidden for the later repair ticket, or should any be explicitly authorized after the environment repair step?
- What rollback or cleanup action is required if an install, virtual environment, or active-environment change fails?
- Should command outputs continue to sanitize local absolute paths in all QA-T004 reports and audits?

## Ready-For-Planner Verdict

Ready for planner.

The planner can create bounded QA-T004 planning artifacts using this context, but must not implement, install, repair, or broaden scope without explicit human approval.
