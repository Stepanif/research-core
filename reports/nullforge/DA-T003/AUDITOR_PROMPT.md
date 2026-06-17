# DA-T003 Auditor Prompt

Use this prompt to independently audit the blocked DA-T003 implementation attempt. Do not implement fixes. Do not commit.

```text
Independently audit DA-T003. Do not implement fixes. Do not commit.

Ticket:
DA-T003 - Minimal Tauri shell scaffold

Role:
Independent Auditor.

Scope:
Audit only the DA-T003 implementation attempt against its planner artifacts, acceptance criteria, implementation report, changed-file report, test results, and active NullForge source docs.

Read:
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
- reports/nullforge/DA-T003/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T003/CHANGED_FILES.md
- reports/nullforge/DA-T003/TEST_RESULTS.md
- reports/nullforge/DA-T003/AUDITOR_PROMPT.md

Audit focus:
- DA-T003 stopped at the required toolchain blocker because `rustc` and `cargo` are unavailable.
- No app scaffold was created.
- No `apps/nullforge-desktop/`, `src-tauri/`, package file, lockfile, Rust, React, TypeScript, JavaScript, CSS, or HTML app file was created.
- No dependency install, Tauri command, package-manager install, app launch, bridge command, sidecar command, ResearchCore Engine command, environment repair, or downstream work occurred.
- `docs/nullforge/CURRENT_STATUS.md` and `docs/nullforge/SOURCE_INDEX.md` were not changed because no scaffold was created.
- The global `No NullForge implementation code has started.` claim remains valid for this blocked attempt.
- QA-T005 limits remain preserved: only `.venv-qa-t005` readiness for `python -m research_core.cli --help` is proven.
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them.
- DA-T001 limits remain preserved: only a docs-only planned desktop bridge contract source document is proven.
- DA-T002 limits remain preserved: only a docs-only Tauri scaffold plan source document is proven.
- No cloud/network/telemetry/auth/billing/broker/live/AI/model/updater/signing/public release/mobile/marketplace/legal/trademark/financial advice scope was introduced.
- No forbidden files/actions occurred.

Required outputs:
- audits/nullforge/DA-T003/AUDIT_REPORT.md
- audits/nullforge/DA-T003/FINDINGS.md
- audits/nullforge/DA-T003/REPAIR_PROMPT.md

Required checks:
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- path checks for DA-T003 reports
- checks that `apps`, `apps/nullforge-desktop`, and `src-tauri` are absent
- prior audit `Decision: PASS` checks through DA-T002
- forbidden-path diff check for source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool files
- `Test-Path` checks for absent `tickets`, `milestones`, and `prompts`

Verdict:
Return exactly one: `PASS`, `HOLD`, or `REJECT`.

Expected verdict:
HOLD, unless the auditor finds forbidden changes or false claims that require `REJECT`.

Forbidden:
- implementing fixes
- installing Rust/Cargo or repairing environment
- creating app/package/Tauri/Rust/React/TypeScript/JavaScript/CSS/HTML files
- creating code/tests/schemas/fixtures/dependencies/package files/lockfiles/config files/CI/generated docs
- creating bridge commands, sidecar behavior, runtime behavior, tickets, milestones, prompt packs, or standalone prompt files
- starting DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work
- committing
```
