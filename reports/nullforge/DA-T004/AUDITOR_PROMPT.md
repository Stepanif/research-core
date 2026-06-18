# DA-T004 Auditor Prompt

Act as the independent auditor for `DA-T004 - Engine command bridge smoke`.

Do not commit.

## Read First

- `plans/nullforge/DA-T004/CONTEXT_BUNDLE.md`
- `plans/nullforge/DA-T004/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/DA-T004/PLAN.md`
- `plans/nullforge/DA-T004/ACCEPTANCE.md`
- `plans/nullforge/DA-T004/IMPLEMENTOR_PROMPT.md`
- `reports/nullforge/DA-T004/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T004/CHANGED_FILES.md`
- `reports/nullforge/DA-T004/TEST_RESULTS.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`
- `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md`
- `audits/nullforge/DA-T003-RESUME/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003-RESUME/FINDINGS.md`
- `audits/nullforge/QA-T005/AUDIT_REPORT.md`
- `audits/nullforge/DA-T001/AUDIT_REPORT.md`
- `audits/nullforge/DA-T002/AUDIT_REPORT.md`

## Audit Scope

Audit only DA-T004.

Verify:

- DA-T003-RESUME remains closed with audit `PASS`.
- DA-T003-RESUME process-level launch evidence remains accepted only for the launch-only scaffold.
- No screenshot-level visual UI proof is claimed for DA-T003-RESUME or DA-T004.
- DA-T004 implements exactly one temporary dev-only bridge command: `engine.cli_help_smoke`.
- The command uses only fixed app-owned executable/arguments equivalent to `.venv-qa-t005\Scripts\python.exe -m research_core.cli --help`.
- The command accepts no user-provided command strings, executable paths, command IDs, workspace paths, or arguments.
- Missing `.venv-qa-t005` or missing `research_core.cli` returns `BLOCKED` without install, repair, or mutation.
- The response is JSON-compatible and bounded.
- The UI adds only one small trigger/result surface.
- App-local dependencies are limited to `@tauri-apps/api` and `serde`.
- Tauri capabilities remain minimal and no shell/filesystem/network/updater/telemetry/release plugin is added.
- No sidecar implementation or launch exists.
- No ResearchCore Engine source/package metadata was changed.
- No workspace, artifact metadata, dataset, fixture, cloud/network, telemetry, updater, signing, public release, broker/live, AI/model, legal/trademark, or financial advice behavior was introduced.
- Reports honestly distinguish fixed command target evidence, Rust compile evidence, app process-level launch evidence, and absence of screenshot/UI-click proof.

## Files To Inspect

Implementation files:

- `apps/nullforge-desktop/package.json`
- `apps/nullforge-desktop/pnpm-lock.yaml`
- `apps/nullforge-desktop/src/App.tsx`
- `apps/nullforge-desktop/src/styles.css`
- `apps/nullforge-desktop/src-tauri/Cargo.toml`
- `apps/nullforge-desktop/src-tauri/Cargo.lock`
- `apps/nullforge-desktop/src-tauri/capabilities/default.json`
- `apps/nullforge-desktop/src-tauri/src/main.rs`

Status/source files:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`

Reports:

- `reports/nullforge/DA-T004/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T004/CHANGED_FILES.md`
- `reports/nullforge/DA-T004/TEST_RESULTS.md`
- `reports/nullforge/DA-T004/AUDITOR_PROMPT.md`

## Required Auditor Checks

Run the auditor-safe checks needed to verify scope and evidence, including:

- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- path checks for required DA-T004 files
- scans for forbidden shell strings, broad process runners, shell/fs/network plugins, sidecar behavior, unsupported command IDs, workspace/data/artifact scope, telemetry/updater/release scope, broker/live scope, AI/model scope, and financial advice scope
- forbidden-path diff check for non-scoped source/package/test/schema/fixture/generated-doc/CI/root package/root lockfile/docs-reference/tool changes
- generated-output/ignored-state check for `node_modules`, `dist`, `src-tauri/target`, and `src-tauri/gen`
- process cleanup check for remaining `nullforge-desktop.exe` app processes

Do not run cleanup beyond auditor-safe verification.

## Known Evidence Limits

- Exact fixed command target `.venv-qa-t005\Scripts\python.exe -m research_core.cli --help` returned exit code `0`.
- `cargo check --manifest-path apps\nullforge-desktop\src-tauri\Cargo.toml` passed on rerun after an initial compile timeout.
- `pnpm --dir apps/nullforge-desktop build` passed.
- `pnpm --dir apps/nullforge-desktop tauri dev` launched far enough to observe `nullforge-desktop.exe`, then cleanup stopped DA-T004 app/dev processes.
- No screenshot-level visual UI proof was captured.
- No button-click/UI invocation proof was captured.

## Disposition Rules

Return exactly one disposition:

- `PASS` if DA-T004 satisfies the single-command bridge-smoke scope and the evidence limits are acceptable.
- `HOLD` if screenshot-level UI proof, button-click proof, stronger bridge invocation proof, report clarification, or bounded repair is required before closeout.
- `REJECT` if there are forbidden files, proof inflation, behavior beyond scope, arbitrary shell execution, broad permissions/plugins, dependency/root changes beyond scope, sidecar/workspace/data/cloud/network/telemetry/release/broker/live/AI/model/financial-advice scope, or ResearchCore Engine source/package boundary violations.

Write the audit result under:

```text
audits/nullforge/DA-T004/
```

Use the existing NullForge audit style.
