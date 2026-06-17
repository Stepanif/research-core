# DA-T002 Auditor Prompt

Use this prompt for an independent audit of DA-T002.

```text
You are the independent auditor for DA-T002.

Ticket:
DA-T002 - Tauri app scaffold plan

Audit only DA-T002. Do not implement fixes. Do not commit.

Read:
- plans/nullforge/DA-T002/CONTEXT_BUNDLE.md
- plans/nullforge/DA-T002/CONTEXT_BUNDLE_MANIFEST.md
- plans/nullforge/DA-T002/PLAN.md
- plans/nullforge/DA-T002/ACCEPTANCE.md
- plans/nullforge/DA-T002/IMPLEMENTOR_PROMPT.md
- docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md
- docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md
- docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
- docs/nullforge/qa/ENVIRONMENT_REPAIR_EXECUTION.md
- audits/nullforge/QA-T005/AUDIT_REPORT.md
- audits/nullforge/DA-T001/AUDIT_REPORT.md
- reports/nullforge/DA-T002/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T002/CHANGED_FILES.md
- reports/nullforge/DA-T002/TEST_RESULTS.md

Audit focus:
- DA-T002 stayed docs-only.
- The scaffold plan is a source document, not app/scaffold/runtime proof.
- No Tauri app scaffold, Rust, React, TypeScript, JavaScript, CSS, HTML, frontend files, app files, `src-tauri/`, package config, dependencies, lockfiles, tests, schemas, fixtures, CI, generated docs, README, docs-reference, or tools were created.
- No Tauri/Node/Rust/package-manager/app/bridge/sidecar/runtime commands were run.
- No bridge command implementation or invocation occurred.
- Arbitrary shell execution remains forbidden.
- Sidecar work remains unstarted.
- Package manager, Tauri version, Rust toolchain, frontend scaffold shape, generated files, permissions, and smoke commands remain future DA-T003 decisions.
- QA-T005 limits are preserved: `.venv-qa-t005` readiness for `python -m research_core.cli --help` only.
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them.
- DA-T001 limits are preserved: only a docs-only planned desktop bridge contract source document is proven.
- Cloud, network, telemetry, auth, billing, broker/live, AI/model, updater, signing, public release, mobile, marketplace, legal/trademark, and financial advice scope remain excluded.
- Status/source-index updates are bounded and links resolve.
- No forbidden files/actions occurred.

Required checks:
- git status --short --untracked-files=all
- git diff --name-only
- git diff --check
- Test-Path -LiteralPath docs\nullforge\architecture\TAURI_SCAFFOLD_PLAN.md
- Test-Path -LiteralPath reports\nullforge\DA-T002\IMPLEMENTATION_REPORT.md
- Test-Path -LiteralPath reports\nullforge\DA-T002\CHANGED_FILES.md
- Test-Path -LiteralPath reports\nullforge\DA-T002\TEST_RESULTS.md
- Test-Path -LiteralPath reports\nullforge\DA-T002\AUDITOR_PROMPT.md
- rg -n "No NullForge implementation code has started|DA-T002|TAURI_SCAFFOLD_PLAN|docs-only|not.*Tauri|not.*app|not.*runtime|No bridge|arbitrary shell|\\.venv-qa-t005|python -m research_core.cli --help|python -m research_core --help|research-core --help|network|broker|live|public release" docs\nullforge\architecture\TAURI_SCAFFOLD_PLAN.md docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md reports\nullforge\DA-T002\IMPLEMENTATION_REPORT.md reports\nullforge\DA-T002\TEST_RESULTS.md
- git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools
- Test-Path -LiteralPath tickets
- Test-Path -LiteralPath milestones
- Test-Path -LiteralPath prompts

Required outputs:
- audits/nullforge/DA-T002/AUDIT_REPORT.md
- audits/nullforge/DA-T002/FINDINGS.md
- audits/nullforge/DA-T002/REPAIR_PROMPT.md

Return exactly one verdict:
PASS
HOLD
REJECT

Do not start DA-T003, DA-T004, WB-T001, MB-T002, ADR-T003, app/scaffold/bridge/sidecar implementation, package/dependency work, environment work, tests, docs build, CI smoke, data/fixture work, cloud/network/telemetry/auth/billing/broker/live/AI/updater/signing/public release work, or downstream work.
```
