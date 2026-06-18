# DA-T004 Implementor Prompt

Implement DA-T004 only. Do not commit.

Ticket:
`DA-T004 - Engine command bridge smoke`

Role:
Scoped Implementor.

Mission:
Implement the first bounded desktop bridge smoke in the existing `apps/nullforge-desktop/` launch-only shell. Implement exactly one allowlisted, dev-only bridge command: `engine.cli_help_smoke`. It may invoke only the QA-T005-proven command shape `python -m research_core.cli --help` inside `.venv-qa-t005`, if present, and must return bounded structured output.

Important:
This prompt is for a future implementation turn. Do not use it during the DA-T004 planning-only turn.

Read first:

- `plans/nullforge/DA-T004/CONTEXT_BUNDLE.md`
- `plans/nullforge/DA-T004/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/DA-T004/PLAN.md`
- `plans/nullforge/DA-T004/ACCEPTANCE.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`
- `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md`
- `audits/nullforge/DA-T003-RESUME/AUDIT_REPORT.md`
- `audits/nullforge/QA-T005/AUDIT_REPORT.md`
- `audits/nullforge/DA-T001/AUDIT_REPORT.md`
- `audits/nullforge/DA-T002/AUDIT_REPORT.md`

Before coding:

- Confirm the latest human prompt explicitly authorizes using `engine.cli_help_smoke` as the temporary dev-only first bridge proof.
- If the human asks for `engine.version` or `engine.doctor`, stop and report that a separate source/package or bridge-contract ticket is needed unless existing source support is proven.
- Run `git status --short --untracked-files=all`.
- Inspect current app files before editing.

Allowed future implementation changes, if explicitly authorized:

- `apps/nullforge-desktop/package.json`
- `apps/nullforge-desktop/pnpm-lock.yaml`
- `apps/nullforge-desktop/src/App.tsx`
- `apps/nullforge-desktop/src/styles.css`
- `apps/nullforge-desktop/src-tauri/Cargo.toml`
- `apps/nullforge-desktop/src-tauri/Cargo.lock`
- `apps/nullforge-desktop/src-tauri/capabilities/default.json`
- `apps/nullforge-desktop/src-tauri/src/main.rs`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T004/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T004/CHANGED_FILES.md`
- `reports/nullforge/DA-T004/TEST_RESULTS.md`
- `reports/nullforge/DA-T004/AUDITOR_PROMPT.md`

Required implementation behavior:

- Implement exactly one bridge command equivalent to `engine.cli_help_smoke`.
- Use fixed executable and arguments only.
- Do not accept user-provided command strings, executable paths, or arguments.
- Do not use `cmd.exe`, PowerShell, shell string composition, shell plugins, filesystem plugins, network plugins, or updater/telemetry/release plugins.
- If `.venv-qa-t005` or `research_core.cli` is unavailable, return a structured `BLOCKED` result without installing or repairing anything.
- Use a timeout.
- Bound stdout/stderr excerpts.
- Return a JSON-compatible response with command ID, status, duration, exit code when present, warnings, and errors.
- Add only the smallest UI surface needed to trigger the smoke and show the bounded result.

Forbidden:

- more than one bridge command;
- arbitrary shell execution;
- general process runner behavior;
- source/package changes to ResearchCore Engine;
- package metadata or CLI entrypoint changes outside app-local bridge needs;
- sidecar packaging or launch;
- workspace selection, scanning, reads, or writes;
- artifact metadata behavior;
- dataset import, fixture creation, or raw/full ES.zip handling;
- cloud, external network, telemetry, auth, billing, mobile, marketplace;
- updater, signing, installer, public release;
- broker/live trading, live execution, AI/model calls, legal/trademark, financial advice behavior;
- tests, schemas, docs generation, docs build, CI, or generated references unless separately scoped.

Run and report:

- `git status --short --untracked-files=all`
- exact app-local install command if dependencies changed
- exact app-local build command
- exact bridge smoke evidence for `engine.cli_help_smoke`, or exact `BLOCKED` result
- `git diff --name-only`
- `git diff --check`
- targeted scans for forbidden shell/filesystem/network/plugin/sidecar/unsupported-command behavior
- forbidden-path diff check for non-scoped source/package/test/schema/fixture/generated-doc/CI/root package/root lockfile/docs-reference/tool changes
- final `git status --short --untracked-files=all`

Required reports:

- `reports/nullforge/DA-T004/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T004/CHANGED_FILES.md`
- `reports/nullforge/DA-T004/TEST_RESULTS.md`
- `reports/nullforge/DA-T004/AUDITOR_PROMPT.md`

Stop and ask for human direction if:

- `.venv-qa-t005` is absent and the smoke cannot return a clean `BLOCKED` result;
- app-local dependency additions are needed but not explicitly authorized by the latest human prompt;
- Tauri requires broad permissions or plugins;
- process timeout cannot be implemented safely;
- engine source/package support is needed;
- bridge scope expands beyond `engine.cli_help_smoke`;
- any data, workspace, network, telemetry, release, broker/live, AI/model, or financial-advice scope appears necessary.

Do not commit unless explicitly asked.
