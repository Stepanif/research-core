# QA-T001 Implementor Prompt

You are Codex working in `C:\Users\Filip\Desktop\Repos\research-core`.

Task: implement `QA-T001` only. Do not commit.

## Context

- `QA-T001` planner artifacts exist under `plans/nullforge/QA-T001/`.
- M0 is complete through `MB-T001` with audit `PASS`.
- `QA-T001` is the NullForge M1 readiness ticket for existing repo command and test discovery.
- No NullForge implementation code has started.
- Root `package.json`, `pnpm-workspace.yaml`, and `pnpm-lock.yaml` are absent in current context; current project metadata is Python-oriented through `pyproject.toml`.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, or downstream work.

## Read First

- `plans/nullforge/QA-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/QA-T001/PLAN.md`
- `plans/nullforge/QA-T001/ACCEPTANCE.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/DECISION_LEDGER.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/M0_HANDOFF.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `audits/nullforge/MB-T001/AUDIT_REPORT.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md`
- `pyproject.toml`
- `requirements-docs.txt`
- `README.md`
- `.github/workflows/research-ci.yml`
- `.github/workflows/docs.yml`
- `docs/how-to/run_ci_locally.md`
- `docs/how-to/add_new_test_and_golden.md`
- `docs/how-to/add_new_cli_command.md`
- `docs/getting-started/quickstart.md`
- `docs/reference/cli/overview.md`
- `docs/reference/cli/index.md`

## Allowed Files

- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/QA-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T001/CHANGED_FILES.md`
- `reports/nullforge/QA-T001/TEST_RESULTS.md`
- `reports/nullforge/QA-T001/AUDITOR_PROMPT.md`

## Treat As Read-Only

- `plans/nullforge/QA-T001/*`
- `docs/nullforge/DECISION_LEDGER.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/M0_HANDOFF.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/adr/`
- `docs/nullforge/blueprint/volumes/`
- `audits/nullforge/`
- existing plans/reports/audits outside `reports/nullforge/QA-T001/`
- `pyproject.toml`
- `requirements-docs.txt`
- `.github/`
- `README.md`
- `docs/` except the allowed NullForge QA/status/source-index files
- `tools/docs/`
- `src/`
- `tests/`
- `schemas/`
- ResearchCore Engine docs/code

## Forbidden

- Do not create reports outside `reports/nullforge/QA-T001/`.
- Do not create audits for QA-T001.
- Do not create tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, ES-derived fixtures, or downstream artifacts.
- Do not modify ResearchCore Engine docs/code.
- Do not modify `docs/nullforge/DECISION_LEDGER.md`.
- Do not run install commands, full test commands, docs generation, docs build, quickstart commands, or CI smoke commands.
- Do not run `python -m pytest`, `python -m pytest -q`, `python tools/docs/gen_cli_ref.py`, `python tools/docs/gen_schema_ref.py`, `python tools/docs/gen_artifact_catalog.py`, `python tools/docs/verify_generated_docs_clean.py`, `python -m mkdocs build`, `pip install`, or `python -m pip install`.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

## Required Work

1. Verify current status and all seven prerequisite audit `PASS` dispositions.
2. Run only bounded discovery commands allowed by `PLAN.md`.
3. Create `docs/nullforge/qa/COMMAND_DISCOVERY.md`.
4. Update `docs/nullforge/CURRENT_STATUS.md` only if needed for QA-T001 in-progress/discovery state while preserving `No NullForge implementation code has started.`
5. Update `docs/nullforge/SOURCE_INDEX.md` only if needed to link created QA-T001 docs and reports.
6. Create QA-T001 implementation reports:
   - `reports/nullforge/QA-T001/IMPLEMENTATION_REPORT.md`
   - `reports/nullforge/QA-T001/CHANGED_FILES.md`
   - `reports/nullforge/QA-T001/TEST_RESULTS.md`
   - `reports/nullforge/QA-T001/AUDITOR_PROMPT.md`
7. Run and record the required bounded checks from `ACCEPTANCE.md`.

## Command Discovery Requirements

`COMMAND_DISCOVERY.md` must identify:

- package metadata source, including `pyproject.toml`;
- absence of root `package.json`, `pnpm-workspace.yaml`, and `pnpm-lock.yaml`;
- Python version expectation from CI and bounded local query if run;
- existing test command candidates;
- existing docs-generation and docs-build command candidates;
- existing CLI invocation evidence, especially `python -m research_core.cli`;
- candidate commands from Volume 07 that fail or are unsupported, if observed;
- existing fixtures/sample paths;
- skipped commands and why;
- side-effect review for `.pytest_cache/`, `exec_outputs/`, docs build output, and generated docs;
- human gates and blockers.

## Checks To Run

Run the checks listed in `plans/nullforge/QA-T001/ACCEPTANCE.md`. Record each command and result in `reports/nullforge/QA-T001/TEST_RESULTS.md`.

## Report

Return:

- changed files;
- checks run;
- commands run, failed, and skipped;
- side effects observed;
- human gates;
- whether QA-T001 is ready for independent audit.

Do not commit.
