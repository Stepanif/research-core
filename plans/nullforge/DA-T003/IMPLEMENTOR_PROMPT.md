# DA-T003 Implementor Prompt

Use this prompt to implement DA-T003 only.

```text
Implement DA-T003 only. Do not commit.

Ticket:
DA-T003 - Minimal Tauri shell scaffold

Role:
Scoped Implementor.

Mission:
Create the minimal launch-only local Windows/Tauri shell scaffold planned by DA-T003. This is the first implementation ticket and may create app-local Tauri, Rust, React, TypeScript, JavaScript, CSS, HTML, package, dependency, and lockfile artifacts only under the bounded allowed paths. Do not implement bridge commands, invoke bridge commands, invoke ResearchCore Engine, package or launch a sidecar, create workspace behavior, create artifact metadata behavior, create dataset/fixture behavior, run full tests, run docs builds, run CI smoke, create schemas, create generated docs, modify ResearchCore Engine files, or start downstream work.

Read first:
- plans/nullforge/DA-T003/CONTEXT_BUNDLE.md
- plans/nullforge/DA-T003/CONTEXT_BUNDLE_MANIFEST.md
- plans/nullforge/DA-T003/PLAN.md
- plans/nullforge/DA-T003/ACCEPTANCE.md
- plans/nullforge/DA-T003/IMPLEMENTOR_PROMPT.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md
- docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md
- audits/nullforge/QA-T005/AUDIT_REPORT.md
- audits/nullforge/DA-T001/AUDIT_REPORT.md
- audits/nullforge/DA-T002/AUDIT_REPORT.md

Allowed changes:
- apps/nullforge-desktop/.gitignore
- apps/nullforge-desktop/index.html
- apps/nullforge-desktop/package.json
- apps/nullforge-desktop/pnpm-lock.yaml
- apps/nullforge-desktop/tsconfig.json
- apps/nullforge-desktop/vite.config.ts
- apps/nullforge-desktop/src/App.tsx
- apps/nullforge-desktop/src/main.tsx
- apps/nullforge-desktop/src/styles.css
- apps/nullforge-desktop/src-tauri/Cargo.toml
- apps/nullforge-desktop/src-tauri/Cargo.lock
- apps/nullforge-desktop/src-tauri/build.rs
- apps/nullforge-desktop/src-tauri/tauri.conf.json
- apps/nullforge-desktop/src-tauri/capabilities/default.json
- apps/nullforge-desktop/src-tauri/src/main.rs
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- reports/nullforge/DA-T003/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T003/CHANGED_FILES.md
- reports/nullforge/DA-T003/TEST_RESULTS.md
- reports/nullforge/DA-T003/AUDITOR_PROMPT.md

Implementation requirements:
- Create a manually bounded scaffold under `apps/nullforge-desktop/`; do not use `create-tauri-app`, `pnpm create`, `pnpm dlx`, `npx`, or interactive generator commands.
- Use `pnpm` only inside `apps/nullforge-desktop/`.
- Use Tauri 2 major-version dependencies and record exact resolved versions in lockfiles and reports.
- Use React + TypeScript + Vite for a static launch-only shell.
- Use the local Rust toolchain only if already available.
- Display static status content only.
- Include an app-local `.gitignore` for `node_modules/`, `dist/`, `src-tauri/target/`, and optional `src-tauri/gen/`.
- Keep Tauri capabilities empty/minimal.
- Do not add filesystem, shell/process, network, updater, telemetry, credential, bridge, sidecar, auth, billing, broker/live, AI/model, signing, public release, mobile, marketplace, legal/trademark, or financial advice behavior.
- Do not implement or invoke bridge commands.
- Do not invoke ResearchCore Engine.
- Do not invoke `.venv-qa-t005`.
- Do not run `python -m research_core.cli --help` as a bridge action.
- Keep `python -m research_core --help` and `research-core --help` unsupported unless a later source/package ticket changes them.
- Preserve QA-T005 limits: only `.venv-qa-t005` readiness for `python -m research_core.cli --help` is proven.
- Preserve DA-T001 limits: only a docs-only planned desktop bridge contract source document is proven.
- Preserve DA-T002 limits: only a docs-only Tauri scaffold plan source document is proven.
- Update status/source navigation only to DA-T003 implementation pending independent audit.
- Because DA-T003 creates the first bounded app scaffold, do not keep claiming globally that no NullForge implementation code has started after scaffold files are created. Replace that claim with the bounded DA-T003 implementation claim from `plans/nullforge/DA-T003/PLAN.md`.

Run:
- `git status --short --untracked-files=all`
- `node --version`
- `pnpm --version`
- `rustc --version`
- `cargo --version`
- `pnpm --dir apps/nullforge-desktop install`
- `pnpm --dir apps/nullforge-desktop build`
- `pnpm --dir apps/nullforge-desktop tauri dev`
- `git diff --name-only`
- `git diff --check`
- required path/content/forbidden-path checks from `plans/nullforge/DA-T003/ACCEPTANCE.md`
- final `git status --short --untracked-files=all`

If `node`, `pnpm`, `rustc`, or `cargo` is missing, stop and report a blocker. Do not install or repair tools.

If `pnpm --dir apps/nullforge-desktop tauri dev` cannot be run or observed, record the exact reason and do not claim launch proof. A compile-only result should be treated as blocked or audit-pending HOLD unless a human explicitly accepts it.

Forbidden:
- root package files, root lockfiles, root Cargo files, `pnpm-workspace.yaml`, source/package/test/schema/fixture/CI/generated-doc/docs-reference/tool/README changes, ResearchCore Engine files
- `create-tauri-app`, `pnpm create`, `pnpm dlx`, `npx`, interactive generators, `rustup`, `cargo install`, global installs, environment repair, package/dependency changes outside `apps/nullforge-desktop/`
- bridge command implementation, bridge command invocation, ResearchCore Engine invocation, Python sidecar packaging, workspace behavior, artifact metadata behavior, dataset import, fixture creation, tests, schemas, CI, generated docs, docs build, quickstart, package/public release commands
- arbitrary shell execution, process-spawn adapters, raw shell strings, filesystem plugins, shell plugins, network plugins, updater/signing/public release behavior, telemetry/auth/billing/broker/live/AI/model/mobile/marketplace/legal/trademark/financial advice scope
- creating audits, tickets, milestones, prompt packs, or standalone prompt files outside the allowed DA-T003 report `AUDITOR_PROMPT.md`
- starting DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work

Do not commit unless explicitly asked.
```
