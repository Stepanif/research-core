# Auditor Prompt: PF-T000 - Repo Inventory And NullForge Import Plan

You are the independent Auditor for NullForge M0 ticket `PF-T000`.

Audit only PF-T000. Do not implement fixes unless explicitly asked after the audit. Do not run PF-T001 or any downstream ticket.

## Read

Read these PF-T000 artifacts:

```text
plans/nullforge/PF-T000/CONTEXT_BUNDLE.md
plans/nullforge/PF-T000/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/PF-T000/PLAN.md
plans/nullforge/PF-T000/ACCEPTANCE.md
plans/nullforge/PF-T000/IMPLEMENTOR_PROMPT.md
docs/nullforge/import/PF-T000_REPO_INVENTORY.md
docs/nullforge/import/PF-T000_IMPORT_PLAN.md
docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md
reports/nullforge/PF-T000/IMPLEMENTATION_REPORT.md
reports/nullforge/PF-T000/CHANGED_FILES.md
reports/nullforge/PF-T000/TEST_RESULTS.md
```

Active incoming package ticket source, if needed:

```text
<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\PF-T000-repo-inventory-and-nullforge-import-plan.md
```

## Audit Scope

Verify:

- PF-T000 stayed docs/source-of-truth only.
- Required outputs exist.
- Inventory identifies likely ResearchCore host/conflict docs and configs.
- Import plan names exact target folders for volumes, ADRs, current status, prompts, tickets, milestone docs, role-loop artifacts, reports, and audits.
- Conflict/gates doc separates ResearchCore Engine truth from NullForge product truth.
- Human gates are listed for overwrite, rename, dependency/code, data, source-of-truth, and public-branding concerns.
- Implementation report, changed files, and test results are present and accurate.
- Changed files are limited to PF-T000 docs/plans/reports paths.
- No generated NullForge Volume 0-7 content was imported or marked canonical.
- No root README, package, CI, engine code, tests, schemas, generated reference docs, raw data, or existing ResearchCore Engine docs were modified.
- PF-T001 remains blocked until audit disposition.

## Required Checks

Run and inspect:

```powershell
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
```

Run `Test-Path -LiteralPath` checks for:

```text
docs/nullforge/import/PF-T000_REPO_INVENTORY.md
docs/nullforge/import/PF-T000_IMPORT_PLAN.md
docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md
reports/nullforge/PF-T000/IMPLEMENTATION_REPORT.md
reports/nullforge/PF-T000/CHANGED_FILES.md
reports/nullforge/PF-T000/TEST_RESULTS.md
reports/nullforge/PF-T000/AUDITOR_PROMPT.md
```

Optional: inspect source docs named in the PF-T000 inventory if needed to validate claims.

Do not install dependencies. Do not run broad tests unless you decide a docs-only scope violation requires additional verification.

## Return

Create audit artifacts under:

```text
audits/nullforge/PF-T000/
```

Required audit outputs:

```text
audits/nullforge/PF-T000/AUDIT_REPORT.md
audits/nullforge/PF-T000/FINDINGS.md
audits/nullforge/PF-T000/REPAIR_PROMPT.md
```

Return:

```text
Audit report path:
Findings path:
Repair prompt path:
Decision: PASS/HOLD/REJECT
Human gates:
Ready for PF-T001? YES/NO
```

Use HOLD or REJECT if scope was exceeded, required outputs are missing, checks are absent without explanation, source-of-truth boundaries are unclear, or a human gate was triggered without approval.
