# DA-T004 Context Bundle Manifest

Ticket: `DA-T004 - Engine command bridge smoke`

Date: `2026-06-17`

Role: Context Curator + Planner only

## Included Sources

| Source | Role |
|---|---|
| `docs/nullforge/CURRENT_STATUS.md` | Confirms DA-T003-RESUME is closed with audit `PASS`, downstream work remains separately scoped, and DA-T004 is not started. |
| `docs/nullforge/SOURCE_INDEX.md` | Confirms repo-local source navigation and pending downstream `DA-T004`, `WB-T001`, `MB-T002` sequence. |
| `docs/nullforge/codex/CODEX_ROLE_LOOP.md` | Defines required context/planner artifact shapes, role boundaries, audit loop, and human gates. |
| `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md` | Primary bridge contract authority, allowlist principles, candidate command IDs, first-proof selection rule, and forbidden bridge behaviors. |
| `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md` | Confirms bridge command smoke belongs to DA-T004 or later after launch-only shell audit. |
| `audits/nullforge/DA-T003-RESUME/AUDIT_REPORT.md` | Audit authority for DA-T003-RESUME `PASS`, launch-only scaffold proof, accepted process-level launch evidence, and excluded downstream scope. |
| `audits/nullforge/DA-T003-RESUME/FINDINGS.md` | Confirms no blocking findings and stale wording cleanup. |
| `audits/nullforge/QA-T005/AUDIT_REPORT.md` | Readiness proof authority for `.venv-qa-t005` and `python -m research_core.cli --help` only. |
| `audits/nullforge/DA-T001/AUDIT_REPORT.md` | Audit authority for docs-only bridge contract, planned candidate command IDs, and first-proof boundaries. |
| `audits/nullforge/DA-T002/AUDIT_REPORT.md` | Audit authority for docs-only scaffold plan and deferred bridge behavior. |

## Supporting Design Memory

| Source | Role |
|---|---|
| `docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md` | Design memory for first-proof engine command ideas. Not implementation authority. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` | Design memory naming DA-T004 as `Engine command bridge smoke`. Not implementation authority. |

## Excluded Sources

- Raw/full ES.zip.
- Private/local data.
- Incoming ticket, milestone, and prompt files not promoted to repo-local active truth.
- Old chats, archived prompts, and unreviewed package material.
- External package registry or network state.
- Generated local outputs such as `node_modules/`, `dist/`, `src-tauri/target/`, and `src-tauri/gen/`.

## Planned Artifact Set

This planner ticket creates only:

- `plans/nullforge/DA-T004/CONTEXT_BUNDLE.md`
- `plans/nullforge/DA-T004/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/DA-T004/PLAN.md`
- `plans/nullforge/DA-T004/ACCEPTANCE.md`
- `plans/nullforge/DA-T004/IMPLEMENTOR_PROMPT.md`

## Explicitly Uncreated By This Planner

This planner does not create or modify:

- app files;
- source files;
- package files;
- dependency files;
- lockfiles;
- reports;
- audits;
- status/source docs;
- tests;
- schemas;
- fixtures;
- generated docs;
- CI;
- ticket, milestone, or prompt folders.

## Expiry And Refresh Rule

Refresh this context before implementation if any of these change:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`
- `apps/nullforge-desktop/`
- `pyproject.toml`
- `src/research_core/cli.py`
- `.venv-qa-t005` readiness state

## Context Risks

- `engine.version` and `engine.doctor` are planned candidates only, not known implemented ResearchCore Engine commands.
- `engine.cli_help_smoke` is not structured engine output and must remain a temporary dev-only proof if used.
- Invoking a process from Tauri is a security-sensitive bridge step and must stay allowlisted, fixed-argument, bounded, and audited.
- Any dependency addition or Tauri permission change requires explicit future implementation scope and human gate handling.
- DA-T004 must not silently become sidecar packaging, workspace behavior, artifact metadata display, fixture handling, or engine source work.

## Manifest Verdict

Context is sufficient for DA-T004 planning only.

Implementation must not start from this planner packet without a later scoped implementation prompt.
