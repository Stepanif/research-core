# QA-T005 Implementor Prompt

Use this prompt only after the human decides whether to authorize QA-T005 environment execution.

```text
You are Codex working in C:\Users\Filip\Desktop\Repos\research-core.

Task: implement QA-T005 only. Do not commit.

Context:
- QA-T005 context and planner artifacts exist under plans/nullforge/QA-T005/.
- QA-T001, HY-T001, QA-T002, QA-T003, and QA-T004 have audit PASS.
- QA-T004 recommends isolated project-local virtual environment preparation as the default repair/readiness path, but did not execute it.
- The unresolved blocker remains:
  - editable install visibility points outside this workspace as <local-temp-editable-install>
  - research_core.cli is not visible to the active Python environment
  - python -m research_core.cli --help fails with No module named research_core.cli
  - python -m research_core --help is unsupported because src/research_core/__main__.py is absent
  - research-core --help is unsupported because no console script exists
- No NullForge implementation code has started.

Human gate:
- Do not run any environment-changing command or validation command unless this prompt explicitly includes:
  - the phrase: I approve QA-T005 environment execution
  - selected path
  - exact project-local venv path or explicit active-environment choice
  - exact install commands allowed
  - exact validation commands allowed
  - cleanup and rollback policy
  - output sanitization policy
- If any required approval item is missing, stop before execution and report the human gate. Do not create implementation reports unless the prompt explicitly asks for a gated/no-execution report.

Read first:
- plans/nullforge/QA-T005/CONTEXT_BUNDLE.md
- plans/nullforge/QA-T005/CONTEXT_BUNDLE_MANIFEST.md
- plans/nullforge/QA-T005/PLAN.md
- plans/nullforge/QA-T005/ACCEPTANCE.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- docs/nullforge/ARCHIVE_POLICY.md
- docs/nullforge/codex/CODEX_ROLE_LOOP.md
- docs/nullforge/qa/COMMAND_DISCOVERY.md
- docs/nullforge/qa/ENVIRONMENT_TRIAGE.md
- docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md
- docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md
- audits/nullforge/QA-T004/AUDIT_REPORT.md
- audits/nullforge/QA-T004/FINDINGS.md
- reports/nullforge/QA-T004/TEST_RESULTS.md
- pyproject.toml
- docs/how-to/run_ci_locally.md
- docs/reference/cli/overview.md
- src/research_core/cli.py

Allowed files if execution is approved:
- docs/nullforge/qa/ENVIRONMENT_REPAIR_EXECUTION.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- reports/nullforge/QA-T005/IMPLEMENTATION_REPORT.md
- reports/nullforge/QA-T005/CHANGED_FILES.md
- reports/nullforge/QA-T005/TEST_RESULTS.md
- reports/nullforge/QA-T005/AUDITOR_PROMPT.md

Allowed local side effects only if explicitly approved:
- approved project-local virtual environment path
- approved cache/output artifacts listed in the human cleanup policy

Treat as read-only:
- plans/nullforge/QA-T005/*
- docs/nullforge/ARCHIVE_POLICY.md
- docs/nullforge/codex/CODEX_ROLE_LOOP.md
- docs/nullforge/qa/COMMAND_DISCOVERY.md
- docs/nullforge/qa/ENVIRONMENT_TRIAGE.md
- docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md
- docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md
- all prior plans, reports, and audits
- pyproject.toml
- requirements-docs.txt
- .github/
- README.md
- docs/ except allowed NullForge status/source-index/QA execution files
- tools/
- src/
- tests/
- schemas/
- fixtures/
- package files
- generated docs
- ResearchCore Engine docs/code

Forbidden unless separately and explicitly approved in this prompt:
- install, uninstall, editable install, dependency sync, package build, virtual-environment creation/activation, environment repair, post-repair CLI validation, tests, docs generation, docs build, quickstart commands, CI smoke commands, or environment-changing commands
- source/package/dependency/test/schema/fixture/CI/generated-doc/README/docs/reference/tool changes
- adding [project.scripts], console_scripts, or src/research_core/__main__.py
- creating audits for QA-T005
- creating tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, or downstream artifacts
- starting ADR-T003, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work

Candidate command packet:
- These commands are not approved unless this prompt includes the human approval phrase and exact selected path.
- Use the human-approved venv path in place of <project-local-venv>.

Candidate commands:
- python -m venv <project-local-venv>
- <project-local-venv>\Scripts\Activate.ps1
- python -m pip install --upgrade pip
- python -m pip install -e .[dev]
- python -m pip show research-core
- python -B -c "import importlib.util; print(importlib.util.find_spec('research_core')); print(importlib.util.find_spec('research_core.cli'))"
- python -m research_core.cli --help

Still unsupported unless a separate source/package ticket authorizes changes:
- python -m research_core --help
- research-core --help

Required work if execution is approved:
1. Verify current status and prerequisite audit PASS evidence.
2. Confirm human approval phrase and exact allowed command packet are present.
3. Record before-state with bounded status/diff checks.
4. Run only approved commands, in order, stopping at the first unapproved or failing step.
5. Sanitize raw local absolute paths in any recorded output.
6. Create docs/nullforge/qa/ENVIRONMENT_REPAIR_EXECUTION.md.
7. Update docs/nullforge/CURRENT_STATUS.md only if needed for QA-T005 state while preserving No NullForge implementation code has started. and REPO_SOURCE_IMPORT_BASELINE.
8. Update docs/nullforge/SOURCE_INDEX.md only if needed to link QA-T005 docs and reports.
9. Create QA-T005 reports:
   - reports/nullforge/QA-T005/IMPLEMENTATION_REPORT.md
   - reports/nullforge/QA-T005/CHANGED_FILES.md
   - reports/nullforge/QA-T005/TEST_RESULTS.md
   - reports/nullforge/QA-T005/AUDITOR_PROMPT.md
10. Run required bounded checks and any explicitly approved validation checks.

Required baseline checks:
- git status --short --branch
- git status --short --untracked-files=all
- git diff --name-only
- git diff --check
- Test-Path -LiteralPath docs\nullforge\qa\ENVIRONMENT_REPAIR_EXECUTION.md
- Test-Path -LiteralPath reports\nullforge\QA-T005\IMPLEMENTATION_REPORT.md
- Test-Path -LiteralPath reports\nullforge\QA-T005\CHANGED_FILES.md
- Test-Path -LiteralPath reports\nullforge\QA-T005\TEST_RESULTS.md
- Test-Path -LiteralPath reports\nullforge\QA-T005\AUDITOR_PROMPT.md
- rg -n "Decision: PASS" audits\nullforge\QA-T001\AUDIT_REPORT.md audits\nullforge\HY-T001\AUDIT_REPORT.md audits\nullforge\QA-T002\AUDIT_REPORT.md audits\nullforge\QA-T003\AUDIT_REPORT.md audits\nullforge\QA-T004\AUDIT_REPORT.md
- rg -n "QA-T005|QA-T004|python -m research_core.cli|No module named research_core.cli|local-temp-editable-install|No NullForge implementation code has started" docs\nullforge\qa\ENVIRONMENT_REPAIR_EXECUTION.md reports\nullforge\QA-T005\IMPLEMENTATION_REPORT.md reports\nullforge\QA-T005\TEST_RESULTS.md
- git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools
- Test-Path -LiteralPath tickets
- Test-Path -LiteralPath milestones
- Test-Path -LiteralPath prompts
- Test-Path -LiteralPath audits\nullforge\QA-T005

Report:
- changed files
- checks run
- commands run, skipped, and failed
- side effects observed
- cleanup/rollback performed or deferred
- human gates
- whether QA-T005 is ready for independent audit

Do not commit.
```
