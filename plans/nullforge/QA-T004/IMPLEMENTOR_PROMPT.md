# QA-T004 Implementor Prompt

You are Codex working in `C:\Users\Filip\Desktop\Repos\research-core`.

Task: implement `QA-T004` only. Do not commit.

Context:
- `QA-T004` context and planner artifacts exist under `plans/nullforge/QA-T004/`.
- `QA-T001`, `HY-T001`, `QA-T002`, and `QA-T003` have audit `PASS`.
- `QA-T003` documented human-gated repair/readiness options for the local Python environment and CLI/runtime blocker.
- The unresolved blocker remains:
  - editable install visibility points outside this workspace as `<local-temp-editable-install>`;
  - `research_core.cli` is not visible to the active Python environment;
  - `python -m research_core.cli --help` fails with `No module named research_core.cli`;
  - `python -m research_core --help` is unsupported because `src/research_core/__main__.py` is absent;
  - `research-core --help` is unsupported because no console script exists.
- `QA-T004` is docs-only selected-path preparation. It must not repair the environment.
- No NullForge implementation code has started.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

Read first:
- `plans/nullforge/QA-T004/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T004/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/QA-T004/PLAN.md`
- `plans/nullforge/QA-T004/ACCEPTANCE.md`
- `plans/nullforge/QA-T004/IMPLEMENTOR_PROMPT.md`
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
- `reports/nullforge/QA-T003/TEST_RESULTS.md`
- `pyproject.toml`
- `docs/how-to/run_ci_locally.md`
- `docs/reference/cli/overview.md`
- `src/research_core/cli.py`

Allowed files:
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/QA-T004/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T004/CHANGED_FILES.md`
- `reports/nullforge/QA-T004/TEST_RESULTS.md`
- `reports/nullforge/QA-T004/AUDITOR_PROMPT.md`

Treat as read-only:
- `plans/nullforge/QA-T004/*`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md`
- all prior plans, reports, and audits
- `pyproject.toml`
- `requirements-docs.txt`
- `.github/`
- `README.md`
- `docs/` except allowed NullForge status/source-index/QA path files
- `tools/`
- `src/`
- `tests/`
- `schemas/`
- `fixtures/`
- package files
- generated docs
- ResearchCore Engine docs/code

Forbidden:
- Do not create audits for `QA-T004`.
- Do not create tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, or downstream artifacts.
- Do not modify ResearchCore Engine docs/code.
- Do not modify `pyproject.toml`, source files, tests, schemas, fixtures, CI, generated docs, README, dependencies, package files, or package metadata.
- Do not run install, uninstall, editable install, dependency sync, package build, virtual-environment creation/activation, or environment repair commands.
- Do not run full test commands, docs generation, docs build, quickstart commands, CI smoke commands, or post-repair CLI validation.
- Do not run `python -m pytest`, `python -m pytest -q`, `pytest -q`, `python tools/docs/gen_cli_ref.py`, `python tools/docs/gen_schema_ref.py`, `python tools/docs/gen_artifact_catalog.py`, `python tools/docs/verify_generated_docs_clean.py`, `python -m mkdocs build`, `pip install`, `python -m pip install`, or `python -m research_core.cli ci run --config .github/ci/ci.github.json`.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

Required work:
1. Verify current status and `QA-T001` / `HY-T001` / `QA-T002` / `QA-T003` audit `PASS`.
2. Create `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md`.
3. Document the recommended or selected repair/readiness path without executing any repair.
4. State that `QA-T004` may only prepare a human gate packet and must not repair the environment.
5. Update `docs/nullforge/CURRENT_STATUS.md` only if needed for `QA-T004` path-preparation state while preserving `No NullForge implementation code has started.` and `REPO_SOURCE_IMPORT_BASELINE`.
6. Update `docs/nullforge/SOURCE_INDEX.md` only if needed to link the QA-T004 path doc and reports after creation.
7. Create QA-T004 implementation reports:
   - `reports/nullforge/QA-T004/IMPLEMENTATION_REPORT.md`
   - `reports/nullforge/QA-T004/CHANGED_FILES.md`
   - `reports/nullforge/QA-T004/TEST_RESULTS.md`
   - `reports/nullforge/QA-T004/AUDITOR_PROMPT.md`
8. Run and record required bounded checks.

Path doc requirements:
- Ticket ID `QA-T004`.
- Purpose and non-goals.
- `QA-T001`, `HY-T001`, `QA-T002`, and `QA-T003` audit `PASS` evidence.
- `QA-T003` decision packet summary.
- The unresolved blocker summary.
- Relevant package/CLI facts from `pyproject.toml`, `docs/reference/cli/overview.md`, `docs/how-to/run_ci_locally.md`, and `src/research_core/cli.py`.
- Explicit distinction between source facts, recorded local environment observations, expected unsupported command shapes, unresolved blockers, candidate repair/readiness paths, and the recommended or selected path.
- Explicit statement that no install, uninstall, editable install, dependency sync, package build, virtual-environment work, environment repair, full tests, docs generation, docs build, quickstart, CI smoke, or post-repair CLI validation commands were run.
- Candidate repair/readiness paths with tradeoffs and required human gates.
- Recommended default path of isolated project-local virtual environment preparation unless the human prompt explicitly selects another path.
- Exact command packet for a future human-approved repair ticket may be documented, but must be labeled `not run`.
- Human decision options and stop conditions.
- Side-effect, rollback, and cleanup considerations.
- Local-path sanitization policy.
- Exact sentence: `No NullForge implementation code has started.`

Required checks:
- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `Test-Path -LiteralPath docs\nullforge\qa\ENVIRONMENT_REPAIR_PATH.md`
- `Test-Path -LiteralPath reports\nullforge\QA-T004\IMPLEMENTATION_REPORT.md`
- `Test-Path -LiteralPath reports\nullforge\QA-T004\CHANGED_FILES.md`
- `Test-Path -LiteralPath reports\nullforge\QA-T004\TEST_RESULTS.md`
- `Test-Path -LiteralPath reports\nullforge\QA-T004\AUDITOR_PROMPT.md`
- `rg -n "Decision: PASS" audits\nullforge\QA-T001\AUDIT_REPORT.md audits\nullforge\HY-T001\AUDIT_REPORT.md audits\nullforge\QA-T002\AUDIT_REPORT.md audits\nullforge\QA-T003\AUDIT_REPORT.md`
- `rg -n "QA-T004|QA-T003|python -m research_core.cli|No module named research_core.cli|local-temp-editable-install|No NullForge implementation code has started" docs\nullforge\qa\ENVIRONMENT_REPAIR_PATH.md reports\nullforge\QA-T004\IMPLEMENTATION_REPORT.md reports\nullforge\QA-T004\TEST_RESULTS.md`
- `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools`
- `Test-Path -LiteralPath tickets`
- `Test-Path -LiteralPath milestones`
- `Test-Path -LiteralPath prompts`
- `Test-Path -LiteralPath audits\nullforge\QA-T004`

Report:
- changed files
- checks run
- commands skipped
- side effects observed
- human gates
- whether `QA-T004` is ready for independent audit

Do not commit.
