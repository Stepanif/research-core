# DA-T001 Auditor Prompt

Use this prompt for an independent audit of DA-T001.

```text
You are the independent auditor for DA-T001.

Ticket:
DA-T001 - Desktop bridge contract finalization

Audit only DA-T001. Do not implement fixes. Do not commit.

Read:
- plans/nullforge/DA-T001/CONTEXT_BUNDLE.md
- plans/nullforge/DA-T001/CONTEXT_BUNDLE_MANIFEST.md
- plans/nullforge/DA-T001/PLAN.md
- plans/nullforge/DA-T001/ACCEPTANCE.md
- plans/nullforge/DA-T001/IMPLEMENTOR_PROMPT.md
- docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md
- docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
- docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md
- docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md
- docs/nullforge/qa/ENVIRONMENT_REPAIR_EXECUTION.md
- audits/nullforge/QA-T005/AUDIT_REPORT.md
- reports/nullforge/DA-T001/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T001/CHANGED_FILES.md
- reports/nullforge/DA-T001/TEST_RESULTS.md

Audit focus:
- DA-T001 stayed docs-only.
- The bridge contract is a source document, not implementation proof.
- The contract defines allowlisted structured command IDs only.
- Arbitrary shell execution is forbidden.
- Volume 3 command IDs are marked planned/candidate unless proven.
- QA-T005 limits are preserved: `.venv-qa-t005` readiness for `python -m research_core.cli --help` only.
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them.
- Cloud, network, telemetry, auth, billing, broker/live, AI/model, updater, signing, public release, and financial advice scope remain excluded.
- No forbidden files/actions occurred.
- Status/source-index updates are bounded and links resolve.

Required checks:
- git status --short --untracked-files=all
- git diff --name-only
- git diff --check
- Test-Path -LiteralPath docs\nullforge\architecture\ENGINE_BRIDGE_CONTRACT.md
- Test-Path -LiteralPath reports\nullforge\DA-T001\IMPLEMENTATION_REPORT.md
- Test-Path -LiteralPath reports\nullforge\DA-T001\CHANGED_FILES.md
- Test-Path -LiteralPath reports\nullforge\DA-T001\TEST_RESULTS.md
- Test-Path -LiteralPath reports\nullforge\DA-T001\AUDITOR_PROMPT.md
- rg -n "Decision: PASS" audits\nullforge\PF-T000\AUDIT_REPORT.md audits\nullforge\PF-T001\AUDIT_REPORT.md audits\nullforge\PF-T002\AUDIT_REPORT.md audits\nullforge\ADR-T001\AUDIT_REPORT.md audits\nullforge\ADR-T002\AUDIT_REPORT.md audits\nullforge\CX-T001\AUDIT_REPORT.md audits\nullforge\MB-T001\AUDIT_REPORT.md audits\nullforge\QA-T001\AUDIT_REPORT.md audits\nullforge\HY-T001\AUDIT_REPORT.md audits\nullforge\QA-T002\AUDIT_REPORT.md audits\nullforge\QA-T003\AUDIT_REPORT.md audits\nullforge\QA-T004\AUDIT_REPORT.md audits\nullforge\QA-T005\AUDIT_REPORT.md
- rg -n "DA-T001|ENGINE_BRIDGE_CONTRACT|No NullForge implementation code has started|allowlist|arbitrary shell|\\.venv-qa-t005|python -m research_core.cli --help|network|broker|live" docs\nullforge\architecture\ENGINE_BRIDGE_CONTRACT.md docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md reports\nullforge\DA-T001\IMPLEMENTATION_REPORT.md reports\nullforge\DA-T001\TEST_RESULTS.md
- git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools
- Test-Path -LiteralPath tickets
- Test-Path -LiteralPath milestones
- Test-Path -LiteralPath prompts

Required outputs:
- audits/nullforge/DA-T001/AUDIT_REPORT.md
- audits/nullforge/DA-T001/FINDINGS.md
- audits/nullforge/DA-T001/REPAIR_PROMPT.md

Return exactly one verdict:
PASS
HOLD
REJECT

Do not start DA-T002, DA-T003, DA-T004, WB-T001, MB-T002, ADR-T003, app/bridge/sidecar implementation, package/dependency work, environment work, tests, docs build, CI smoke, data/fixture work, cloud/network/telemetry/auth/billing/broker/live/AI/updater/signing/public release work, or downstream work.
```
