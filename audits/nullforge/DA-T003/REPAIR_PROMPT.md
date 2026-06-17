# DA-T003 Repair Prompt

Use this prompt only after a separate human-approved action makes `rustc` and `cargo` available on PATH, or after a separate scoped planning change replaces that prerequisite. Do not use this prompt to install Rust/Cargo, repair the environment, or broaden DA-T003 scope.

```text
Resume DA-T003 only after the independent audit HOLD.

Ticket:
DA-T003 - Minimal Tauri shell scaffold

Role:
Scoped Implementor.

Audit authority:
- audits/nullforge/DA-T003/AUDIT_REPORT.md
- audits/nullforge/DA-T003/FINDINGS.md

Mission:
Resolve the DA-T003 HOLD only if `rustc` and `cargo` are already available on PATH. Create the minimal launch-only local Windows/Tauri shell scaffold exactly as scoped by the existing DA-T003 planner artifacts. Do not implement bridge commands, invoke bridge commands, invoke ResearchCore Engine, package or launch a sidecar, create workspace behavior, create artifact metadata behavior, create dataset/fixture behavior, run full tests, run docs builds, run CI smoke, create schemas, create generated docs, modify ResearchCore Engine files, or start downstream work.

Read first:
- plans/nullforge/DA-T003/CONTEXT_BUNDLE.md
- plans/nullforge/DA-T003/CONTEXT_BUNDLE_MANIFEST.md
- plans/nullforge/DA-T003/PLAN.md
- plans/nullforge/DA-T003/ACCEPTANCE.md
- plans/nullforge/DA-T003/IMPLEMENTOR_PROMPT.md
- reports/nullforge/DA-T003/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T003/CHANGED_FILES.md
- reports/nullforge/DA-T003/TEST_RESULTS.md
- audits/nullforge/DA-T003/AUDIT_REPORT.md
- audits/nullforge/DA-T003/FINDINGS.md

Required first checks:
- `git status --short --untracked-files=all`
- `node --version`
- `pnpm --version`
- `rustc --version`
- `cargo --version`

If `rustc` or `cargo` is still unavailable, stop again and update only DA-T003 reports with the renewed blocker evidence. Do not install or repair tools.

If all required tools are available, continue only within the allowed DA-T003 implementation paths from `plans/nullforge/DA-T003/IMPLEMENTOR_PROMPT.md`.

Preserve:
- QA-T005 proves only `.venv-qa-t005` readiness for `python -m research_core.cli --help`.
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them.
- DA-T001 proves only a docs-only planned desktop bridge contract source document.
- DA-T002 proves only a docs-only Tauri scaffold plan source document.

Forbidden:
- Rust/Cargo install or environment repair.
- Root package/workspace/Cargo files.
- Bridge command implementation or invocation.
- ResearchCore Engine invocation.
- Sidecar behavior.
- Source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool changes outside the DA-T003 allowed file list.
- Cloud/network/telemetry/auth/billing/broker/live/AI/model/updater/signing/public release/mobile/marketplace/legal/trademark/financial advice scope.
- DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work.
- Commit, unless explicitly asked.
```
