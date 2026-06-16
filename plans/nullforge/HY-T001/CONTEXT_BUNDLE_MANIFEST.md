# HY-T001 Context Bundle Manifest

Ticket: `HY-T001`

Purpose: Record source files, discovery commands, candidate files, and planner outputs for the local-path hygiene planning ticket.

## Inputs Read

| Path | Role |
| --- | --- |
| `docs/nullforge/CURRENT_STATUS.md` | Current NullForge status, active phase, no-code boundary |
| `docs/nullforge/SOURCE_INDEX.md` | Source index and incoming package provenance |
| `docs/nullforge/ARCHIVE_POLICY.md` | Archive/quarantine/source authority policy |
| `docs/nullforge/codex/CODEX_ROLE_LOOP.md` | Role-loop and artifact rules |
| `docs/nullforge/qa/COMMAND_DISCOVERY.md` | QA-T001 command discovery and local temp path evidence |
| `audits/nullforge/QA-T001/AUDIT_REPORT.md` | QA-T001 audit `PASS` evidence |
| `reports/nullforge/QA-T001/TEST_RESULTS.md` | QA-T001 bounded command output evidence |

## Discovery Commands Run

```powershell
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
git diff --check
rg -n "C:\\Users\\Filip|NullForge_Incoming|research-core-gha-clone|AppData\\Local\\Temp" docs\nullforge plans\nullforge reports\nullforge audits\nullforge
```

## Pre-Planning Candidate Files

- `audits/nullforge/ADR-T001/AUDIT_REPORT.md`
- `audits/nullforge/PF-T002/AUDIT_REPORT.md`
- `audits/nullforge/QA-T001/REPAIR_PROMPT.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/blueprint/volumes/VOLUME_IMPORT_MANIFEST.md`
- `docs/nullforge/import/PF-T000_REPO_INVENTORY.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `plans/nullforge/ADR-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/ADR-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/ADR-T001/IMPLEMENTOR_PROMPT.md`
- `plans/nullforge/ADR-T001/PLAN.md`
- `plans/nullforge/MB-T001/IMPLEMENTOR_PROMPT.md`
- `plans/nullforge/PF-T000/CONTEXT_BUNDLE.md`
- `plans/nullforge/PF-T000/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/PF-T000/IMPLEMENTOR_PROMPT.md`
- `plans/nullforge/PF-T000/PLAN.md`
- `plans/nullforge/PF-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/PF-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/PF-T001/IMPLEMENTOR_PROMPT.md`
- `plans/nullforge/PF-T001/PLAN.md`
- `plans/nullforge/PF-T002/CONTEXT_BUNDLE.md`
- `plans/nullforge/PF-T002/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/PF-T002/IMPLEMENTOR_PROMPT.md`
- `plans/nullforge/PF-T002/PLAN.md`
- `plans/nullforge/QA-T001/IMPLEMENTOR_PROMPT.md`
- `reports/nullforge/ADR-T001/AUDITOR_PROMPT.md`
- `reports/nullforge/ADR-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/ADR-T001/TEST_RESULTS.md`
- `reports/nullforge/MB-T001/AUDITOR_PROMPT.md`
- `reports/nullforge/PF-T000/AUDITOR_PROMPT.md`
- `reports/nullforge/PF-T000/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/PF-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/PF-T002/AUDITOR_PROMPT.md`
- `reports/nullforge/PF-T002/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T001/AUDITOR_PROMPT.md`
- `reports/nullforge/QA-T001/TEST_RESULTS.md`

## Outputs Created

- `plans/nullforge/HY-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/HY-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/HY-T001/PLAN.md`
- `plans/nullforge/HY-T001/ACCEPTANCE.md`
- `plans/nullforge/HY-T001/IMPLEMENTOR_PROMPT.md`

## Deliberately Not Read Or Changed

- `src/`
- `tests/`
- `schemas/`
- `fixtures/`
- `.github/`
- package and dependency files beyond no-change status checks
- generated docs
- raw data and private data
- downstream ticket, milestone, prompt, app, desktop, bridge, sidecar, and implementation artifacts

## Manifest Verdict

The context bundle is complete enough for a bounded implementor prompt. No cleanup implementation was performed.
