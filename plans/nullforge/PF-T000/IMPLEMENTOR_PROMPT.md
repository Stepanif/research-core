# Implementor Prompt: PF-T000 - Repo Inventory And NullForge Import Plan

You are the Implementor for NullForge M0 ticket `PF-T000`.

You implement only the bounded docs/source-of-truth outputs for PF-T000. Do not write implementation code. Do not import NullForge volumes. Do not modify existing ResearchCore Engine docs.

## Read First

Read these repo-local files:

```text
plans/nullforge/PF-T000/CONTEXT_BUNDLE.md
plans/nullforge/PF-T000/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/PF-T000/PLAN.md
plans/nullforge/PF-T000/ACCEPTANCE.md
```

The planner prompt referenced this in-repo ticket path:

```text
tickets/nullforge/PF-T000-repo-inventory-and-nullforge-import-plan.md
```

At planner time that path was absent. Use this incoming package ticket source unless the in-repo path now exists:

```text
<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\PF-T000-repo-inventory-and-nullforge-import-plan.md
```

If both paths exist, compare them enough to identify the active source used and record that in the implementation report.

## Allowed Files And Folders

You may create only:

```text
docs/nullforge/import/PF-T000_REPO_INVENTORY.md
docs/nullforge/import/PF-T000_IMPORT_PLAN.md
docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md
reports/nullforge/PF-T000/IMPLEMENTATION_REPORT.md
reports/nullforge/PF-T000/CHANGED_FILES.md
reports/nullforge/PF-T000/TEST_RESULTS.md
reports/nullforge/PF-T000/AUDITOR_PROMPT.md
```

You may read existing docs/config listed in the context bundle. You may read M0 package milestone/ticket/prompt docs as needed to verify PF-T000 scope. Do not extract or import NullForge Volume 0-7 package contents.

Treat these planner files as read-only unless you find a direct typo that blocks implementation:

```text
plans/nullforge/PF-T000/CONTEXT_BUNDLE.md
plans/nullforge/PF-T000/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/PF-T000/PLAN.md
plans/nullforge/PF-T000/ACCEPTANCE.md
plans/nullforge/PF-T000/IMPLEMENTOR_PROMPT.md
```

## Forbidden Files, Folders, And Actions

Do not modify:

```text
README.md
docs/index.md
docs/STATUS.md
docs/ARCHITECTURE.md
docs/getting-started/
docs/how-to/
docs/reference/
docs/contributing/
src/
tests/
schemas/
configs/
tools/
pyproject.toml
mkdocs.yml
.github/
```

Do not:

- create implementation code;
- add scripts, tests, schemas, package config, CI config, or dependencies;
- install dependencies;
- run downstream PF-T001+ work;
- import or canonicalize generated NullForge volumes;
- copy raw/full data, `ES.zip`, private data, or ES-derived fixtures into the repo;
- change repo/package/CLI/product identity;
- create Tauri, desktop bridge, sidecar, dataset parser, Logic Factory, Visual Replay, EvidenceCard, packaging, cloud, auth, billing, broker, or mobile artifacts;
- overwrite, move, rename, or materially edit existing ResearchCore Engine docs;
- broaden into public release, legal/trademark naming, financial advice, live trading, cloud sync, marketplace, or mobile scope.

## Implementation Tasks

1. Preflight
   - Run `git status --short --branch` and record the result.
   - Confirm current branch.
   - Check whether the in-repo ticket path exists.
   - Check whether the expected PF-T000 output paths already exist.
   - Check whether proposed future target roots exist:

```text
docs/nullforge/
docs/nullforge/import/
docs/nullforge/blueprint/volumes/
docs/nullforge/adr/
docs/nullforge/codex/
milestones/nullforge/
tickets/nullforge/
prompts/nullforge/
reports/nullforge/
audits/nullforge/
```

2. Create `docs/nullforge/import/PF-T000_REPO_INVENTORY.md`
   - State repo root, branch, ticket, and source context.
   - Record the missing in-repo ticket path if still missing.
   - Summarize current ResearchCore repo truth using the context bundle and existing docs.
   - Identify likely host/conflict docs and configs:
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
   - List existing or absent NullForge target paths.
   - Separate ResearchCore Engine truth from NullForge product/import truth.

3. Create `docs/nullforge/import/PF-T000_IMPORT_PLAN.md`
   - Recommend preserving the M0 target layout unless a conflict is found.
   - Name exact target folders for future tickets:

```text
docs/nullforge/
docs/nullforge/import/
docs/nullforge/blueprint/volumes/
docs/nullforge/adr/
docs/nullforge/codex/
milestones/nullforge/M0-repo-source-import/
tickets/nullforge/
prompts/nullforge/
plans/nullforge/<ticket-id>/
reports/nullforge/<ticket-id>/
audits/nullforge/<ticket-id>/
```

   - Name expected future source-of-truth files:

```text
docs/nullforge/README.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
docs/nullforge/DECISION_LEDGER.md
```

   - State which later ticket should create or populate each area.
   - Do not create those downstream files in PF-T000.

4. Create `docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md`
   - List confirmed non-conflicts.
   - List potential conflicts and source-of-truth tensions.
   - List human gate triggers for overwrites, renames, dependency/code changes, raw data, generated volume canonicalization, and public/legal/branding scope.
   - Include an explicit human gate status, for example `Human gates triggered: NONE` if true.

5. Create report artifacts
   - `IMPLEMENTATION_REPORT.md`: summarize files created, source context, decisions, risks, and human gates.
   - `CHANGED_FILES.md`: list every changed/created file and why it exists.
   - `TEST_RESULTS.md`: record exact checks, commands, and results. If a check cannot be run, explain why.
   - `AUDITOR_PROMPT.md`: create a bounded prompt for an independent PF-T000 auditor. It must ask the auditor to verify scope, outputs, checks, source-of-truth separation, human gates, and changed-file boundaries.

6. Final checks
   - Run and record:

```powershell
git status --short --branch
git diff --name-only
```

   - Run and record `Test-Path -LiteralPath ...` checks for every required PF-T000 output.
   - Manually confirm changed files are limited to PF-T000 docs/plans/reports and no forbidden paths changed.

## Required Return

Return:

```text
Implementation report path:
Changed files path:
Test results path:
Auditor prompt path:
Human gates:
Ready for auditor? YES/NO
```

Do not report PF-T000 as complete. PF-T000 is complete only after the independent auditor returns PASS, HOLD, or REJECT.
