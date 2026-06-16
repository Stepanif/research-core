# PF-T000 Plan

Ticket: PF-T000 - Repo inventory and NullForge import plan
Milestone: M0 - Repo Source Import + Canonical Baseline
Role: Planner

## Purpose

Produce a bounded, docs-only implementation plan for PF-T000. The implementor will inventory the existing `research-core` documentation, identify source-of-truth and path conflicts, and write a non-destructive import plan for NullForge planning sources.

PF-T000 does not import NullForge volumes, change engine docs, modify code, install dependencies, or start downstream M0 tickets.

## Source Context Used

- `plans/nullforge/PF-T000/CONTEXT_BUNDLE.md`
- `plans/nullforge/PF-T000/CONTEXT_BUNDLE_MANIFEST.md`
- Active ticket source from incoming package:
  - `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\PF-T000-repo-inventory-and-nullforge-import-plan.md`
- The in-repo path requested by the planner prompt is currently absent:
  - `tickets/nullforge/PF-T000-repo-inventory-and-nullforge-import-plan.md`

The context bundle records these relevant repo truth sources for the implementor to inspect or cite:

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

## Dependencies And Current Status

- PF-T000 has no prior ticket dependency.
- Current branch: `docs/PF-T000-nullforge-import-plan`.
- Current scoped planner output path: `plans/nullforge/PF-T000/`.
- M0 is serial by doctrine:

```text
PF-T000 -> PF-T001 -> PF-T002 -> ADR-T001 -> ADR-T002 -> CX-T001 -> MB-T001
```

- Downstream tickets must remain blocked until PF-T000 has implementation output and an auditor result.
- The context bundle was created as a curator artifact only; PF-T000 implementation has not started.

## Exact Scope

The implementor may create PF-T000 docs and reports only:

```text
docs/nullforge/import/PF-T000_REPO_INVENTORY.md
docs/nullforge/import/PF-T000_IMPORT_PLAN.md
docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md
reports/nullforge/PF-T000/IMPLEMENTATION_REPORT.md
reports/nullforge/PF-T000/CHANGED_FILES.md
reports/nullforge/PF-T000/TEST_RESULTS.md
reports/nullforge/PF-T000/AUDITOR_PROMPT.md
```

The auditor may later create audit artifacts under:

```text
audits/nullforge/PF-T000/
```

PF-T000 may propose future target paths but must not create downstream imported volume, ADR, prompt, ticket, milestone, or status files.

## Forbidden Actions

- Do not modify `src/`, `tests/`, `schemas/`, package files, CI files, or engine internals.
- Do not rewrite, move, rename, or overwrite existing ResearchCore Engine docs.
- Do not change `README.md`, `docs/STATUS.md`, `docs/ARCHITECTURE.md`, or `pyproject.toml`.
- Do not create a Tauri app, desktop bridge, sidecar, parser, compiler, visual replay UI, or other implementation code.
- Do not install dependencies.
- Do not import, extract, copy, or canonicalize NullForge Volume 0-7 contents in PF-T000.
- Do not commit full `ES.zip`, raw/private data, ES-derived fixtures, or unsafe data samples.
- Do not rename repo, package, CLI, product, or public identity.
- Do not start PF-T001 or any downstream M0 ticket.
- Do not broaden into public release, legal/trademark decisions, live trading, financial advice, auth, billing, cloud sync, marketplace, or mobile scope.

## Likely Files Changed

Planner pass:

```text
plans/nullforge/PF-T000/PLAN.md
plans/nullforge/PF-T000/ACCEPTANCE.md
plans/nullforge/PF-T000/IMPLEMENTOR_PROMPT.md
```

Implementor pass:

```text
docs/nullforge/import/PF-T000_REPO_INVENTORY.md
docs/nullforge/import/PF-T000_IMPORT_PLAN.md
docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md
reports/nullforge/PF-T000/IMPLEMENTATION_REPORT.md
reports/nullforge/PF-T000/CHANGED_FILES.md
reports/nullforge/PF-T000/TEST_RESULTS.md
reports/nullforge/PF-T000/AUDITOR_PROMPT.md
```

No other files should change.

## Step-By-Step Docs/Source Update Plan

1. Preflight
   - Record `git status --short --branch`.
   - Confirm current branch is `docs/PF-T000-nullforge-import-plan`.
   - Confirm the in-repo ticket path is absent or, if it now exists, compare it with the incoming package ticket and record the source used.
   - Confirm proposed target paths do not already contain conflicting files.

2. Inventory existing repo truth
   - Inspect the repo docs/config listed in the context bundle.
   - Identify existing docs likely to host or conflict with NullForge docs:
     - root `README.md`
     - `docs/index.md`
     - `docs/STATUS.md`
     - `docs/ARCHITECTURE.md`
     - `docs/getting-started/repo-tour.md`
     - `docs/how-to/run_ci_locally.md`
     - `docs/contributing/docs_style_guide.md`
     - `docs/README_ANALYSIS_ES5M.md`
     - `docs/dataset_catalog_spec_v1.md`
     - `pyproject.toml`
   - Record that ResearchCore repo docs and implemented code remain authoritative for engine truth.
   - Record that NullForge setup/volume packages remain draft inputs until imported and audited.

3. Write `PF-T000_REPO_INVENTORY.md`
   - State repo root, branch, and source context.
   - Summarize current ResearchCore repo state without overstating completeness.
   - List observed absent NullForge paths:
     - `docs/nullforge/`
     - `docs/nullforge/import/`
     - `milestones/nullforge/`
     - `tickets/nullforge/`
     - `prompts/nullforge/`
     - `reports/nullforge/`
     - `audits/nullforge/`
   - Identify conflicts and non-conflicts.
   - Note the missing in-repo ticket path and use of the incoming package ticket source.

4. Write `PF-T000_IMPORT_PLAN.md`
   - Recommend preserving the M0 target layout because no conflicting repo paths were observed.
   - Name exact future target folders:

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

   - Plan PF-T001 as the ticket that imports reviewed volume material under `docs/nullforge/blueprint/volumes/`.
   - Plan PF-T002 as the ticket that creates `CURRENT_STATUS.md`, `SOURCE_INDEX.md`, and `DECISION_LEDGER.md`.
   - Plan ADR and role-loop docs only after their dependencies pass.
   - Do not require root README or engine docs edits in PF-T000.

5. Write `PF-T000_CONFLICTS_AND_GATES.md`
   - Separate ResearchCore Engine truth from NullForge product truth.
   - List source-of-truth risks, data/privacy risks, dependency/code risks, identity/branding risks, and downstream sequencing risks.
   - Mark any triggered gates as `NONE` if none were triggered.
   - Explicitly state gates that would require human review.

6. Write implementation reports
   - `IMPLEMENTATION_REPORT.md`: summarize actions taken, source context, human gates, and remaining work.
   - `CHANGED_FILES.md`: list every changed/created file with purpose.
   - `TEST_RESULTS.md`: include exact commands/checks run and results.
   - `AUDITOR_PROMPT.md`: give the auditor a bounded prompt to verify PF-T000 only.

7. Final verification
   - Run `git status --short --branch`.
   - Run directory/file existence checks for the PF-T000 output paths and proposed future target roots.
   - Run `git diff --name-only` or equivalent changed-file review.
   - Manually confirm changed files are docs/plans/reports only.
   - Do not run dependency-installing commands.

## Tests And Checks Required

Required:

```text
git status --short --branch
Test-Path -LiteralPath <each expected PF-T000 output path>
Test-Path -LiteralPath <each proposed target root>
git diff --name-only
manual review that changed files are docs/plans/reports only
```

Optional, only if the implementor changes docs navigation or generated docs surfaces:

```text
python -m mkdocs build
python tools/docs/verify_generated_docs_clean.py
```

Do not install dependencies to make optional checks pass. If a check cannot be run, record why in `reports/nullforge/PF-T000/TEST_RESULTS.md`.

## Security, Privacy, And Data Considerations

- No raw/full ES data enters the repo.
- No ES-derived fixture enters the repo without a later explicit license/safety/data decision.
- No cloud, network, auth, billing, broker, or live-trading scope is introduced.
- No generated volume is promoted to canonical truth during PF-T000.
- The import plan must preserve the boundary between draft design memory and repo-governed source truth.

## Source-Of-Truth Risks

- The active ticket exists in the incoming package, not in `tickets/nullforge/` inside the repo.
- ResearchCore docs already contain active engine status and architecture truth; NullForge docs must not overwrite or contradict them.
- Root README/package framing is narrower than current implemented CLI surface; PF-T000 should not fix that drift.
- Generated NullForge volumes are draft inputs until PF-T001 imports reviewed material and an audit accepts it.
- Existing docs contain TODO/partial reference surfaces; NullForge docs should not imply a fully complete engine platform.

## Rollback And Repair Route

If PF-T000 implementation goes out of scope:

1. Stop before further edits.
2. Identify all changed files with `git diff --name-only`.
3. Remove or repair only PF-T000-added files under:

```text
docs/nullforge/import/
reports/nullforge/PF-T000/
plans/nullforge/PF-T000/
```

4. Do not revert unrelated user changes.
5. If an engine doc, code file, dependency file, CI file, or data file was changed, mark PF-T000 as HOLD or REJECT and require human review.

## Human Gate Triggers

Human review is required before any action that would:

- overwrite, move, rename, or materially edit existing ResearchCore Engine docs;
- change root README beyond a later explicitly scoped link/summary;
- rename repo, package, CLI, project, or public identity;
- add dependencies, code, scripts, parsers, sidecar binaries, packaging configs, tests, or CI behavior;
- commit raw/full data, `ES.zip`, ES-derived fixtures, or private/local data;
- mark generated volumes canonical before PF-T001 import and audit;
- broaden into public release, legal/trademark naming, AI strategy activation, broker/live-trading, financial advice, auth, billing, cloud sync, marketplace, or mobile scope;
- skip or parallelize required M0 dependencies without explicit human deferral.

Planner-detected human gates: NONE.
