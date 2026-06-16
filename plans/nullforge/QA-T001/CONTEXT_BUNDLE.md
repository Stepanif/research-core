# QA-T001 Context Bundle

Date: `2026-06-16`

Ticket: `QA-T001`

Role: Context Curator

Ready-for-planner verdict: `YES`

## Ticket Summary

`QA-T001` is the first scoped M1 readiness ticket after M0 closeout. Its mission is to discover the existing `research-core` command and test surface before any NullForge implementation ticket assumes how to build, run, test, lint, type-check, or invoke the current ResearchCore Engine.

`QA-T001` is discovery only. It must not create product implementation, app scaffolding, tests, schemas, fixtures, dependencies, package files, CI changes, generated docs, raw data, or downstream M1 artifacts.

No NullForge implementation code has started.

## M1 Readiness Purpose

M1 is named in Volume 07 as `Desktop Shell + ResearchCore Engine Bridge Proof`, but `QA-T001` exists before bridge or desktop implementation. It should establish the current repo reality for commands and blockers so later M1 tickets do not invent commands, assume package managers, or miss local environment constraints.

The later planner should preserve this narrow purpose:

- identify actual existing command/test/documentation surfaces;
- identify package manager and Python environment expectations;
- identify current CLI entrypoints and documented smoke commands;
- identify whether dependencies such as `pyarrow` can block local tests;
- identify current fixtures/sample locations without creating new data;
- identify existing CI workflows and docs-generation checks;
- report blockers and human gates.

## Non-Goals

- No NullForge implementation code.
- No app, Tauri, bridge, sidecar, desktop shell, or workbench work.
- No new tests, schemas, fixtures, package files, dependencies, or CI.
- No generated docs updates.
- No raw/private data handling.
- No ES.zip import, extraction, parsing, fixture publication, or generated dataset work.
- No `ADR-T003`, `DA-T001`, `DA-T002`, M1 implementation, or downstream ticket work.
- No package install, build, or test command execution during context curation.
- No source-of-truth promotion from old prompts, incoming package files, archive material, or quarantine.

## Completed Prerequisites

| Ticket | Status | Evidence | Relevance |
|---|---|---|---|
| `PF-T000` | Audit `PASS` | `audits/nullforge/PF-T000/AUDIT_REPORT.md` | Established import plan, repo inventory, conflicts, and gates. |
| `PF-T001` | Audit `PASS` | `audits/nullforge/PF-T001/AUDIT_REPORT.md` | Imported selected Volume 00-07 planning sources. |
| `PF-T002` | Audit `PASS` | `audits/nullforge/PF-T002/AUDIT_REPORT.md` | Created current status, source index, decision ledger, and archive policy. |
| `ADR-T001` | Audit `PASS` | `audits/nullforge/ADR-T001/AUDIT_REPORT.md` | Preserves working name, platform, stack direction, and ResearchCore Engine boundary. |
| `ADR-T002` | Audit `PASS` | `audits/nullforge/ADR-T002/AUDIT_REPORT.md` | Preserves local-first/no-cloud MVP boundary and no-implementation proof caveat. |
| `CX-T001` | Audit `PASS` | `audits/nullforge/CX-T001/AUDIT_REPORT.md` | Provides the role-loop workflow for QA-T001 execution. |
| `MB-T001` | Audit `PASS` | `audits/nullforge/MB-T001/AUDIT_REPORT.md` | Closes M0 handoff and names `QA-T001` as the recommended next scoped ticket after human direction. |

## Active Source Docs Used

| Source | Role for QA-T001 |
|---|---|
| `docs/nullforge/CURRENT_STATUS.md` | Current NullForge status, dependency state, gates, and out-of-scope boundaries. |
| `docs/nullforge/SOURCE_INDEX.md` | Active repo-local NullForge source map and pending downstream context. |
| `docs/nullforge/DECISION_LEDGER.md` | Accepted decisions `NF-D0001` through `NF-D0005` and pending `NF-D0006`. |
| `docs/nullforge/ARCHIVE_POLICY.md` | Source authority, archive, quarantine, prompt, and promotion rules. |
| `docs/nullforge/M0_HANDOFF.md` | M0 result, human closeout state, and M1 readiness statement. |
| `docs/nullforge/codex/CODEX_ROLE_LOOP.md` | Role responsibilities, artifacts, PASS/HOLD/REJECT rules, gates, and stop conditions. |
| `audits/nullforge/MB-T001/AUDIT_REPORT.md` | Latest M0 audit evidence and handoff closeout basis. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` | Roadmap source naming `QA-T001` and its command/test discovery intent. |

## Existing Repo Command And Test Discovery Targets

### Project Metadata

- `pyproject.toml` exists and is the active Python project metadata source.
- `requirements-docs.txt` exists for docs dependencies.
- Requested root Node files are absent in the current repo state:
  - `package.json`
  - `pnpm-workspace.yaml`
  - `pnpm-lock.yaml`
- `pyproject.toml` declares:
  - project name `research-core`;
  - Python requirement `>=3.11`;
  - runtime dependencies `pandas`, `pyarrow`, and `typer`;
  - optional `dev` dependency `pytest`;
  - pytest config with `pythonpath = ["src"]` and `testpaths = ["tests"]`.
- CI workflows use Python `3.13.7`.

### Existing CI And Docs Commands

Current workflow and docs sources identify these command families for later verification:

- `.github/workflows/research-ci.yml`
  - `pip install -e .[dev]`
  - `python -m pytest -q`
  - `python -m pytest -q`
  - `python -m research_core.cli ci run --config .github/ci/ci.github.json`
- `.github/workflows/docs.yml`
  - `python -m pip install --upgrade pip`
  - `python -m pip install -e .`
  - `python -m pip install -r requirements-docs.txt`
  - `python tools/docs/gen_cli_ref.py`
  - `python tools/docs/gen_schema_ref.py`
  - `python tools/docs/gen_artifact_catalog.py`
  - `python tools/docs/verify_generated_docs_clean.py`
  - `python -m mkdocs build`
- `docs/how-to/run_ci_locally.md` mirrors both workflows and records local PowerShell equivalents.
- `README.md` lists typical local verification:
  - `python tools/docs/gen_cli_ref.py`
  - `python tools/docs/gen_schema_ref.py`
  - `python tools/docs/gen_artifact_catalog.py`
  - `python tools/docs/verify_generated_docs_clean.py`
  - `python -m pytest -q`

These commands were read from source files only. They were not run during context curation.

### Existing CLI Surface

Primary CLI implementation source:

- `src/research_core/cli.py`

Generated CLI docs:

- `docs/reference/cli/overview.md`
- `docs/reference/cli/index.md`
- `docs/reference/cli/canon.md`
- `docs/reference/cli/risk.md`
- `docs/reference/cli/risk_run.md`
- `docs/reference/cli/risk_runset.md`

`docs/reference/cli/overview.md` documents this root usage:

```text
python -m research_core.cli [OPTIONS] COMMAND [ARGS]...
```

The generated overview lists root commands:

```text
canon
psa
validate
registry
observe
bundle
experiment
project
doctor
verify
plan
dataset
lineage
runset
risk
baseline
ci
release
prune
pilot
```

Volume 07 gives initial candidates to verify, not assume:

```text
python --version
python -m pytest
python -m pip show research-core
python -m pip show pyarrow
python -m research_core --help
research-core --help
```

Current repo docs more strongly support `python -m research_core.cli ...` than `python -m research_core` or `research-core`. `QA-T001` should record that distinction based on actual verification in its own implementor phase if the planner allows command execution.

### Existing Test And Fixture Surface

Discovery found an existing `tests/` suite with smoke, determinism, golden fixture regression, fail-loud, and contract-style tests. Representative existing patterns are documented in `docs/how-to/add_new_test_and_golden.md`:

- `tests/test_*_smoke.py`
- `tests/test_*_determinism.py`
- `tests/test_*_golden_fixture_regression.py`
- `tests/golden/*.sha256`

Existing sample/fixture paths include:

- `tests/fixtures/raw_small_sample.txt`
- `tests/fixtures/raw_bad_ohlc.txt`
- `tests/fixtures/raw_duplicate_ts.txt`
- `tests/fixtures/raw_bad_timestamp.txt`
- `tests/fixtures/exp_specs/`

QA-T001 must not modify tests, fixtures, goldens, or generated outputs. Later command execution, if allowed, should account for possible local side effects such as `.pytest_cache/` or `exec_outputs/`.

### Existing Docs And Contract Targets

Useful read-only discovery targets for the planner:

- `README.md`
- `docs/how-to/run_ci_locally.md`
- `docs/how-to/add_new_test_and_golden.md`
- `docs/how-to/add_new_cli_command.md`
- `docs/getting-started/quickstart.md`
- `docs/reference/cli/`
- `docs/reference/contracts/v1/`
- `docs/reference/artifacts/catalog.v1.yml`
- `tools/docs/`
- `.github/ci/ci.github.json`

## Files And Folders Likely Relevant To Later QA-T001 Planning

- `pyproject.toml`
- `requirements-docs.txt`
- `.github/workflows/research-ci.yml`
- `.github/workflows/docs.yml`
- `.github/ci/ci.github.json`
- `README.md`
- `docs/how-to/run_ci_locally.md`
- `docs/how-to/add_new_test_and_golden.md`
- `docs/how-to/add_new_cli_command.md`
- `docs/getting-started/quickstart.md`
- `docs/reference/cli/`
- `docs/reference/contracts/v1/`
- `tools/docs/`
- `src/research_core/cli.py`
- `src/research_core/`
- `tests/`
- `tests/fixtures/`
- `tests/golden/`
- `schemas/`

These are discovery targets only. They should remain read-only unless a later scoped ticket explicitly permits edits.

## Files And Folders Explicitly Excluded

- `docs/nullforge/qa/` during context curation.
- `reports/nullforge/QA-T001/` during context curation.
- `audits/nullforge/QA-T001/` during context curation.
- `tickets/`, `milestones/`, and `prompts/`.
- Any app, Tauri, bridge, sidecar, desktop shell, package, installer, signing, updater, release, or distribution paths.
- Any package or dependency files, including `pyproject.toml`, `requirements-docs.txt`, lock files, and future package manifests.
- `src/`, `tests/`, `schemas/`, `fixtures`, `.github/`, `tools/docs/`, `docs/reference/`, and existing ResearchCore Engine docs as edit targets.
- Raw/full ES.zip, private/local data, generated datasets, ES-derived fixtures, and broker/live material.
- M1 downstream artifacts other than the allowed QA-T001 context curator files.

## Current Repo State

- Branch/status before curator file creation: `main...origin/main`.
- `main` was clean and pushed after `MB-T001` closeout.
- During curation, only `plans/nullforge/QA-T001/CONTEXT_BUNDLE.md` and `plans/nullforge/QA-T001/CONTEXT_BUNDLE_MANIFEST.md` are expected to become untracked.
- Root Node package files requested by the prompt are absent: `package.json`, `pnpm-workspace.yaml`, and `pnpm-lock.yaml`.
- Python metadata exists through `pyproject.toml`; docs dependencies are listed in `requirements-docs.txt`.
- One read-only file discovery query required escalation because the Windows sandbox helper failed; it only enumerated existing files and did not modify the repo.

## Known Gates And Stop Conditions

Human gate triggers:

- Any dependency installation, dependency change, or package metadata change.
- Any new test, fixture, schema, generated doc, package file, CI change, or code edit.
- Any command execution that writes broad local outputs, touches private/raw data, or requires cleanup outside explicitly allowed paths.
- Any missing dependency or Python environment blocker that prevents trustworthy command discovery.
- Any need to import incoming milestone/ticket/prompt files or promote archive/quarantine material.
- Any request to start `ADR-T003`, desktop bridge, sidecar, app scaffold, M1 implementation, data import, broker/live, AI/model calls, public distribution, or release work.

Stop conditions:

- Working tree is dirty outside `plans/nullforge/QA-T001/` before planning.
- M0 prerequisite audit `PASS` evidence is missing or contradicted.
- Current status no longer names QA-T001 as the next scoped direction after human closeout.
- Required command/test discovery scope cannot be bounded without running install/build/test commands.
- Planner cannot decide whether QA-T001 should run commands or only document existing command candidates.
- A package manager conflict appears, such as Node/pnpm assumptions conflicting with Python-only repo metadata.
- A command would require private/local data, generated datasets, ES.zip, network access, dependency download, or broad file writes.

## Constraints And Forbidden Actions

- Do not implement QA-T001 during curation.
- Do not create `PLAN.md`, `ACCEPTANCE.md`, `IMPLEMENTOR_PROMPT.md`, reports, audits, QA docs, tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, or downstream artifacts.
- Do not modify existing files.
- Do not run install/build/test commands during curation.
- Do not start `ADR-T003`, implementation work, or downstream M1 work.
- Treat ResearchCore Engine implementation docs/code/tests as existing truth and discovery targets only.
- Preserve `No NullForge implementation code has started.`

## Required Checks For Later Stages

Planner stage should verify:

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- QA-T001 context files exist.
- All prerequisite audits still contain `Decision: PASS`.
- `CURRENT_STATUS.md`, `SOURCE_INDEX.md`, and `M0_HANDOFF.md` still name QA-T001/M1 boundaries and preserve the no-code sentence.

Implementor stage, if later approved, should be planned separately and may need to:

- create only the explicitly allowed QA-T001 discovery outputs;
- record the actual package manager and absent package files;
- identify and possibly verify Python version and package installation state;
- identify existing test commands without creating new tests;
- identify CLI help/entrypoint behavior without changing code;
- identify CI/docs commands from source files;
- record skipped commands with exact reasons when dependency or side-effect gates apply;
- avoid leaving local caches or generated outputs unless explicitly allowed and reported.

Auditor stage should verify:

- changed files remain bounded to the approved QA-T001 outputs;
- no implementation code, tests, schemas, fixtures, package files, CI, generated docs, raw/private data, or downstream artifacts were created or modified;
- command/test discovery evidence is source-backed and does not overclaim successful execution;
- blockers and human gates are clearly reported;
- no later ticket assumes commands beyond what QA-T001 established.

## Open Questions

- Should the QA-T001 implementor run any commands, or only document existing command candidates from repo files?
- If command execution is allowed later, are `python --version`, `python -m research_core.cli --help`, `python -m pytest --version`, or `python -m pytest -q` in scope?
- Should generated side effects such as `.pytest_cache/`, `exec_outputs/`, or docs build outputs be forbidden entirely, cleaned up, or reported as expected local-only outputs?
- Should QA-T001 create `docs/nullforge/qa/COMMAND_DISCOVERY.md`, as Volume 07 suggests, or should the later planner keep outputs under reports only?
- Is the absence of `package.json`, `pnpm-workspace.yaml`, and `pnpm-lock.yaml` expected and sufficient to close Node/pnpm discovery?

## Ready-For-Planner Verdict

`YES`.

The repo has enough active source context for a bounded QA-T001 planner pass. The planner should decide exact QA-T001 outputs, whether any command execution is allowed, and how to handle side effects or dependency blockers before implementation begins.
