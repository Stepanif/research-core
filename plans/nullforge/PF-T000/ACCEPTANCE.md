# PF-T000 Acceptance

Ticket: PF-T000 - Repo inventory and NullForge import plan

## Testable Acceptance Criteria

- `docs/nullforge/import/PF-T000_REPO_INVENTORY.md` exists.
- `PF-T000_REPO_INVENTORY.md` identifies existing repo docs/config likely to host or conflict with NullForge docs, including at minimum:
  - `README.md`
  - `docs/index.md`
  - `docs/STATUS.md`
  - `docs/ARCHITECTURE.md`
  - `docs/getting-started/repo-tour.md`
  - `docs/how-to/run_ci_locally.md`
  - `docs/contributing/docs_style_guide.md`
  - `docs/README_ANALYSIS_ES5M.md`
  - `docs/dataset_catalog_spec_v1.md`
  - `pyproject.toml`
- `PF-T000_REPO_INVENTORY.md` records which proposed NullForge paths existed or were absent before implementation.
- `docs/nullforge/import/PF-T000_IMPORT_PLAN.md` exists.
- `PF-T000_IMPORT_PLAN.md` names exact target folders for NullForge volumes, ADRs, current status, prompts, tickets, milestone docs, role-loop artifacts, reports, and audits.
- `PF-T000_IMPORT_PLAN.md` keeps NullForge product truth separate from existing ResearchCore Engine truth.
- `docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md` exists.
- `PF-T000_CONFLICTS_AND_GATES.md` lists human gates for overwrite, rename, dependency/code, raw data, source-of-truth, and public-branding concerns.
- `reports/nullforge/PF-T000/IMPLEMENTATION_REPORT.md` exists and summarizes what changed, what sources were used, and whether human gates were triggered.
- `reports/nullforge/PF-T000/CHANGED_FILES.md` exists and lists every changed/created file with a short purpose.
- `reports/nullforge/PF-T000/TEST_RESULTS.md` exists and records required checks with exact command names and outcomes.
- `reports/nullforge/PF-T000/AUDITOR_PROMPT.md` exists and gives a bounded PF-T000-only audit prompt.
- No implementation files are changed.
- No generated NullForge Volume 0-7 content is imported or marked canonical.
- No root README, package, CI, engine code, tests, schemas, or existing ResearchCore Engine docs are modified.

## Required Checks And Commands

Run and record:

```powershell
git status --short --branch
```

Run and record existence checks for all PF-T000 outputs:

```powershell
Test-Path -LiteralPath docs\nullforge\import\PF-T000_REPO_INVENTORY.md
Test-Path -LiteralPath docs\nullforge\import\PF-T000_IMPORT_PLAN.md
Test-Path -LiteralPath docs\nullforge\import\PF-T000_CONFLICTS_AND_GATES.md
Test-Path -LiteralPath reports\nullforge\PF-T000\IMPLEMENTATION_REPORT.md
Test-Path -LiteralPath reports\nullforge\PF-T000\CHANGED_FILES.md
Test-Path -LiteralPath reports\nullforge\PF-T000\TEST_RESULTS.md
Test-Path -LiteralPath reports\nullforge\PF-T000\AUDITOR_PROMPT.md
```

Run and record existence checks for proposed future target roots:

```powershell
Test-Path -LiteralPath docs\nullforge
Test-Path -LiteralPath docs\nullforge\import
Test-Path -LiteralPath docs\nullforge\blueprint\volumes
Test-Path -LiteralPath docs\nullforge\adr
Test-Path -LiteralPath docs\nullforge\codex
Test-Path -LiteralPath milestones\nullforge
Test-Path -LiteralPath tickets\nullforge
Test-Path -LiteralPath prompts\nullforge
Test-Path -LiteralPath reports\nullforge
Test-Path -LiteralPath audits\nullforge
```

Run and record changed-file review:

```powershell
git diff --name-only
git status --short --branch
```

Manual review required:

- Confirm changed files are limited to PF-T000 docs/plans/reports paths.
- Confirm no implementation code, tests, schemas, package files, CI files, raw data, or engine docs changed.
- Confirm the in-repo ticket path absence is documented if still absent.

Optional checks:

- Run `python -m mkdocs build` only if docs nav or mkdocs-visible surfaces are changed.
- Run `python tools/docs/verify_generated_docs_clean.py` only if generated docs tooling or generated reference files are changed.
- Do not install dependencies for optional checks. If skipped or unavailable, document why in `TEST_RESULTS.md`.

## Docs Update Expectations

- Use repo-truth-only language.
- Prefer TODO markers for unknown or unverified details.
- Do not guess flags, paths, schema keys, commands, or implementation behavior.
- Treat generated setup/volume packages as draft inputs, not canonical repo truth.
- Preserve existing ResearchCore Engine docs as authoritative for the current engine state.
- Keep NullForge product/source-import docs under clearly separated NullForge paths.

## Done Definition

PF-T000 implementation is ready for auditor when:

- All required PF-T000 docs and reports exist.
- Required checks are recorded in `reports/nullforge/PF-T000/TEST_RESULTS.md`.
- Changed files are scoped to docs/plans/reports for PF-T000.
- Human gate status is explicitly reported.
- `reports/nullforge/PF-T000/AUDITOR_PROMPT.md` is ready for an independent auditor.

PF-T000 itself is not complete until an auditor returns PASS, HOLD, or REJECT and the result is recorded by the appropriate later handoff workflow.

## Conditions That Force HOLD Or REJECT

Return HOLD or REJECT if any of these occur:

- Existing ResearchCore Engine docs are overwritten, moved, renamed, or materially edited.
- Repo/package/CLI/product identity is changed.
- Code, tests, package files, schemas, scripts, CI behavior, or dependencies are added or modified.
- Raw/full data, `ES.zip`, private data, or ES-derived fixtures enter the repo.
- Generated NullForge volumes are imported wholesale or marked canonical.
- The import plan contradicts existing ResearchCore status/architecture truth.
- Required checks are skipped without explanation.
- Changed files cannot be bounded to PF-T000 docs/plans/reports.
- A human gate is triggered and work continues without human approval.
- Downstream M0 ticket work starts before PF-T000 audit disposition.
