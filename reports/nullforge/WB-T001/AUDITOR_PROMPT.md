# WB-T001 Auditor Prompt

Act as the independent auditor for `WB-T001 - Artifact metadata read-only viewer`.

Do not commit.

## Read First

- `plans/nullforge/WB-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/WB-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/WB-T001/PLAN.md`
- `plans/nullforge/WB-T001/ACCEPTANCE.md`
- `plans/nullforge/WB-T001/IMPLEMENTOR_PROMPT.md`
- `reports/nullforge/WB-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/WB-T001/CHANGED_FILES.md`
- `reports/nullforge/WB-T001/TEST_RESULTS.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `audits/nullforge/DA-T004/AUDIT_REPORT.md`
- `reports/nullforge/DA-T004/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T004/TEST_RESULTS.md`
- `apps/nullforge-desktop/src/App.tsx`
- `apps/nullforge-desktop/src/styles.css`
- `apps/nullforge-desktop/src-tauri/src/main.rs`
- `apps/nullforge-desktop/src-tauri/capabilities/default.json`
- `apps/nullforge-desktop/package.json`
- `apps/nullforge-desktop/src-tauri/Cargo.toml`

## Audit Scope

Audit only WB-T001.

Verify:

- DA-T004 audit `PASS` remains the bridge-smoke authority.
- WB-T001 displays only the existing bridge response `artifacts` field.
- Empty artifact arrays render an honest empty state.
- No artifact files are created, scanned, read, written, deleted, or mutated.
- No workspace selection, filesystem access, or artifact scan behavior was added.
- No new bridge command was added.
- DA-T004 Rust process execution was not changed by WB-T001.
- No app-local or root dependency was added by WB-T001.
- Tauri capabilities remain minimal and no shell/filesystem/network/updater/telemetry/release plugin was added.
- No ResearchCore Engine source/package metadata was changed.
- No sidecar, dataset, fixture, raw/private data, cloud/network, telemetry, updater, signing, public release, broker/live, AI/model, legal/trademark, or financial-advice behavior was introduced.
- Reports honestly state no screenshot-level visual UI proof and no button-click/UI invocation proof were captured.

## Required Auditor Checks

Run safe checks needed to verify scope and evidence, including:

- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- path checks for required WB-T001 plan/report files
- app-local frontend build if available, or record why skipped
- targeted scans for forbidden new bridge commands, filesystem/workspace/artifact scan behavior, plugins, dependencies, network/release behavior, sidecar behavior, data/fixture scope, broker/live scope, AI/model scope, and financial advice scope
- forbidden tracked-path diff check for non-scoped ResearchCore Engine source/package/test/schema/fixture/generated-doc/CI/root package/root lockfile/docs-reference/tool changes
- generated-output/ignored-state check for `node_modules`, `dist`, `src-tauri/target`, and `src-tauri/gen`

Do not run cleanup beyond auditor-safe verification.

## Known Evidence Limits

- `pnpm --dir apps/nullforge-desktop build` passed after an approved outside-sandbox rerun.
- WB-T001 did not run `tauri dev`.
- WB-T001 did not click the UI.
- WB-T001 did not capture screenshots.
- WB-T001 did not test a runtime non-empty artifact array.
- The current DA-T004 bridge returns `artifacts: []`.

## Disposition Rules

Return exactly one disposition:

- `PASS` if WB-T001 satisfies the read-only returned-artifact metadata display scope and the evidence limits are acceptable.
- `HOLD` if report clarification, stronger UI proof, or bounded repair is required before closeout.
- `REJECT` if there are forbidden files, proof inflation, behavior beyond scope, new bridge commands, Rust process changes, arbitrary shell execution, broad permissions/plugins, dependency/root changes beyond scope, artifact scanning or file access, workspace/data/cloud/network/telemetry/release/broker/live/AI/model/financial-advice scope, or ResearchCore Engine source/package boundary violations.

If writing audit artifacts, write them under:

```text
audits/nullforge/WB-T001/
```

Use the existing NullForge audit style.
