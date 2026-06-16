# CX-T001 Auditor Prompt

You are the independent auditor for NullForge M0 ticket `CX-T001`.

Audit only CX-T001. Do not implement fixes. Do not start MB-T001, ADR-T003, M1, or downstream work.

## Read

```text
plans/nullforge/CX-T001/CONTEXT_BUNDLE.md
plans/nullforge/CX-T001/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/CX-T001/PLAN.md
plans/nullforge/CX-T001/ACCEPTANCE.md
plans/nullforge/CX-T001/IMPLEMENTOR_PROMPT.md
docs/nullforge/codex/CODEX_ROLE_LOOP.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
docs/nullforge/DECISION_LEDGER.md
docs/nullforge/ARCHIVE_POLICY.md
docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md
docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
audits/nullforge/ADR-T002/AUDIT_REPORT.md
reports/nullforge/CX-T001/IMPLEMENTATION_REPORT.md
reports/nullforge/CX-T001/CHANGED_FILES.md
reports/nullforge/CX-T001/TEST_RESULTS.md
```

## Audit Focus

Check that CX-T001:

- stayed docs/workflow-only;
- created `docs/nullforge/codex/CODEX_ROLE_LOOP.md`;
- updated only allowed status/source docs;
- created only required CX-T001 reports;
- did not modify `docs/nullforge/DECISION_LEDGER.md`;
- preserved ADR-T001 and ADR-T002 boundaries;
- recorded role responsibilities for Human / ChatGPT Architect, Context Curator, Planner, Implementor / Codex, Auditor, and Repair Implementor;
- recorded per-ticket artifact paths under `plans/nullforge/`, `reports/nullforge/`, and `audits/nullforge/`;
- recorded PASS / HOLD / REJECT rules;
- recorded human gate triggers and stop conditions;
- recorded source-of-truth, archive, quarantine, and prompt handling rules;
- kept MB-T001, ADR-T003, M1, and downstream work pending;
- avoided claims of implementation proof, Tauri feasibility, packaging feasibility, bridge reliability, workspace safety, telemetry enforcement, cloud-security proof, legal/trademark clearance, public distribution safety, financial advice safety, trading validity, product validation, user validation, market validation, or data licensing safety.

## Required Verification

Run or inspect equivalent evidence for:

```powershell
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
git diff --check
Test-Path -LiteralPath docs\nullforge\codex\CODEX_ROLE_LOOP.md
Test-Path -LiteralPath reports\nullforge\CX-T001\IMPLEMENTATION_REPORT.md
Test-Path -LiteralPath reports\nullforge\CX-T001\CHANGED_FILES.md
Test-Path -LiteralPath reports\nullforge\CX-T001\TEST_RESULTS.md
Test-Path -LiteralPath reports\nullforge\CX-T001\AUDITOR_PROMPT.md
rg -n "Decision: PASS" audits\nullforge\ADR-T002\AUDIT_REPORT.md
rg -n "Context Curator|Planner|Implementor|Auditor|PASS|HOLD|REJECT|human gate|stop condition|No NullForge implementation code has started|CX-T001|MB-T001" docs\nullforge\codex\CODEX_ROLE_LOOP.md
rg -n "CX-T001|CODEX_ROLE_LOOP|MB-T001|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md
```

Manual checks:

- all repo-local Markdown links in `docs/nullforge/SOURCE_INDEX.md` resolve;
- changed files are bounded to CX-T001 plans, allowed NullForge docs, and CX-T001 reports;
- no ResearchCore Engine docs/code, tests, schemas, configs, tools, package files, CI, generated docs, tickets, milestones, prompts, audits, raw data, fixtures, MB-T001, ADR-T003, or M1 files changed.

## Human Gate Triggers

Human review is required if the implementation changed ResearchCore Engine docs/code, repo/package/CLI/product identity, dependencies, code, schemas, tests, generated docs tooling, CI, data, fixtures, cloud/auth/billing/mobile/telemetry/broker/live/AI/release scope, prompt/source promotion, tickets, milestones, MB-T001, ADR-T003, or M1 work.

## Required Outputs

Create only:

```text
audits/nullforge/CX-T001/AUDIT_REPORT.md
audits/nullforge/CX-T001/FINDINGS.md
audits/nullforge/CX-T001/REPAIR_PROMPT.md
```

## Verdict Format

Return exactly one:

```text
PASS
HOLD
REJECT
```

Then include:

```text
Why:
Blocking findings:
Non-blocking findings:
Human decision needed:
Repair prompt path:
```
