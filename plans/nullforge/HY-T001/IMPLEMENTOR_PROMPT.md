# HY-T001 Implementor Prompt

You are Codex working in `<repo-root>` for this repository.

Task: implement `HY-T001` only. Do not commit.

Context:
- `HY-T001` planner artifacts exist under `plans/nullforge/HY-T001/`.
- QA-T001 is complete and pushed with audit `PASS`.
- A read-only contamination scan found no other-project code contamination.
- The only notable hygiene issue is local absolute path leakage in tracked NullForge docs/plans/reports/audits.
- This is documentation/provenance hygiene only.
- No NullForge implementation code has started.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, or downstream work.

Read first:
- `plans/nullforge/HY-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/HY-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/HY-T001/PLAN.md`
- `plans/nullforge/HY-T001/ACCEPTANCE.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`
- `reports/nullforge/QA-T001/TEST_RESULTS.md`

Allowed cleanup targets:
- Candidate files listed in `plans/nullforge/HY-T001/CONTEXT_BUNDLE.md`.
- `docs/nullforge/CURRENT_STATUS.md`, only if needed to record `HY-T001` implementation state while preserving `No NullForge implementation code has started.`
- `docs/nullforge/SOURCE_INDEX.md`, only if needed to link HY-T001 artifacts or sanitize existing source-index local paths.

Allowed report outputs:
- `reports/nullforge/HY-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/HY-T001/CHANGED_FILES.md`
- `reports/nullforge/HY-T001/TEST_RESULTS.md`
- `reports/nullforge/HY-T001/AUDITOR_PROMPT.md`

Treat as read-only unless listed above:
- `plans/nullforge/HY-T001/*`
- all other existing plans, reports, and audits except candidate cleanup targets listed in the context bundle
- ResearchCore Engine docs/code
- source code, tests, schemas, fixtures, package files, CI files, generated docs, raw data, and private data

Forbidden:
- Do not create audits for HY-T001.
- Do not create tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, or downstream artifacts.
- Do not modify ResearchCore Engine docs or code.
- Do not run tests, installs, docs generation, docs build, quickstart commands, or CI smoke commands.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

Required work:
1. Verify current status and QA-T001 audit `PASS`.
2. Re-run the bounded local-path search.
3. Sanitize safe local absolute path occurrences according to this replacement policy:
   - repo root path -> `<repo-root>` or repo-relative path
   - incoming package root -> `<nullforge-incoming-root>`
   - temp editable install path -> `<local-temp-editable-install>`
   - keep file basenames, ticket IDs, hashes, command names, package names, and repo-relative paths when useful
4. Do not change source meaning, command outcomes, audit dispositions, accepted decisions, or ticket status.
5. Create HY-T001 implementation reports.
6. Run and record bounded checks.

Required checks:
```powershell
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
git diff --check
rg -n "Decision: PASS" audits\nullforge\QA-T001\AUDIT_REPORT.md
rg -n "C:\\Users\\Filip|NullForge_Incoming|research-core-gha-clone|AppData\\Local\\Temp" docs\nullforge plans\nullforge reports\nullforge audits\nullforge
rg -n "No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\CURRENT_STATUS.md
git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools
Test-Path -LiteralPath reports\nullforge\HY-T001\IMPLEMENTATION_REPORT.md
Test-Path -LiteralPath reports\nullforge\HY-T001\CHANGED_FILES.md
Test-Path -LiteralPath reports\nullforge\HY-T001\TEST_RESULTS.md
Test-Path -LiteralPath reports\nullforge\HY-T001\AUDITOR_PROMPT.md
Test-Path -LiteralPath tickets
Test-Path -LiteralPath milestones
Test-Path -LiteralPath prompts
Test-Path -LiteralPath audits\nullforge\HY-T001
```

Report:
- changed files
- checks run
- replacements made by policy category
- any remaining local-path hits and why they remain
- human gates
- whether HY-T001 is ready for independent audit

Do not commit.
