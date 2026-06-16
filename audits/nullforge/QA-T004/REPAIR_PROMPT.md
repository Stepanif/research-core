# QA-T004 Repair Prompt

QA-T004 audit decision is `PASS`.

No repair is required.

Use this prompt only if a later review invalidates the QA-T004 audit evidence or discovers drift in the QA-T004 artifacts.

```text
You are Codex working in C:\Users\Filip\Desktop\Repos\research-core.

Task: repair QA-T004 audit findings only.

Context:
- QA-T004 is docs-only local Python environment repair/readiness path preparation.
- No NullForge implementation code has started.
- Do not run install, uninstall, editable install, dependency sync, package build, virtual-environment creation/activation, environment repair, full tests, docs generation, docs build, quickstart, CI smoke, or post-repair CLI validation commands.
- Do not start ADR-T003, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, package changes, dependency changes, or downstream work.

Read first:
- audits/nullforge/QA-T004/AUDIT_REPORT.md
- audits/nullforge/QA-T004/FINDINGS.md
- plans/nullforge/QA-T004/PLAN.md
- plans/nullforge/QA-T004/ACCEPTANCE.md
- docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md

Allowed files:
- docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- reports/nullforge/QA-T004/IMPLEMENTATION_REPORT.md
- reports/nullforge/QA-T004/CHANGED_FILES.md
- reports/nullforge/QA-T004/TEST_RESULTS.md
- reports/nullforge/QA-T004/AUDITOR_PROMPT.md

Forbidden:
- Do not modify plans/nullforge/QA-T004/.
- Do not modify audits/nullforge/QA-T004/ unless a later explicit audit-repair instruction permits it.
- Do not modify source, tests, schemas, fixtures, package files, dependencies, CI, generated docs, README, docs/reference, tools, ResearchCore Engine docs/code, or downstream artifacts.

Required work:
1. Verify the specific QA-T004 finding.
2. Apply the smallest docs-only correction needed.
3. Preserve the exact sentence: No NullForge implementation code has started.
4. Preserve QA-T004 as path preparation only, not environment repair or CLI readiness proof.
5. Run bounded checks from plans/nullforge/QA-T004/ACCEPTANCE.md that do not mutate the environment.
6. Report changed files, checks, remaining findings, and whether QA-T004 is ready for re-audit.

Do not commit.
```
