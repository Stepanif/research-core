# DA-T001 Context Bundle Manifest

Date: `2026-06-17`

Ticket: `DA-T001`

Role: Context Curator

Status: Ready for planner

No NullForge implementation code has started.

## Included Sources

| Source | Type | Use |
|---|---|---|
| `docs/nullforge/CURRENT_STATUS.md` | Active status | Current phase, QA-T005 closeout, gates, no-code claim. |
| `docs/nullforge/SOURCE_INDEX.md` | Active navigation | Repo-local source set and existing artifact links. |
| `docs/nullforge/DECISION_LEDGER.md` | Active decision ledger | Accepted decisions and pending source import note. |
| `docs/nullforge/ARCHIVE_POLICY.md` | Active governance | Archive, quarantine, prompt, and promotion rules. |
| `docs/nullforge/codex/CODEX_ROLE_LOOP.md` | Active workflow | Context/planner/implementor/auditor artifact requirements and stop conditions. |
| `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` | Active ADR | Windows 11 x64, Tauri + React/TypeScript direction, ResearchCore Engine sidecar / scoped command bridge boundary. |
| `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md` | Active ADR | Local-first, no-cloud, no-telemetry, no-broker/live, and no-public-release MVP boundaries. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md` | Imported design memory | Primary source for bridge contract shape, allowlist, workspace, permission, logging, security, and proof gates. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` | Imported roadmap memory | Places DA-T001 in the M1 ticket sequence and defines docs-only ticket discipline. |
| `docs/nullforge/qa/COMMAND_DISCOVERY.md` | Active QA source | Existing command discovery and unsupported command shapes. |
| `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md` | Active QA source | Environment blocker context before repair decisioning. |
| `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md` | Active QA source | Candidate repair/readiness options and human gates. |
| `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md` | Active QA source | Isolated project-local virtual environment path preparation. |
| `docs/nullforge/qa/ENVIRONMENT_REPAIR_EXECUTION.md` | Active QA source | QA-T005 `.venv-qa-t005` readiness proof and limits. |
| `audits/nullforge/PF-T000/AUDIT_REPORT.md` through `audits/nullforge/QA-T005/AUDIT_REPORT.md` | Audit evidence | Prior PASS chain and scope boundaries. |
| `pyproject.toml` | Read-only package fact | Package/source layout context only. |
| `docs/reference/cli/overview.md` | Read-only CLI doc | Current documented CLI module shape. |
| `docs/how-to/run_ci_locally.md` | Read-only command doc | Existing command context only; no commands run by DA-T001 planning. |
| `src/research_core/cli.py` | Read-only source fact | Confirms CLI source shape only; not modified. |
| `plans/nullforge/QA-T005/PLAN.md` | Prior plan style | Local style and gate pattern reference. |
| `plans/nullforge/QA-T005/ACCEPTANCE.md` | Prior acceptance style | Local acceptance criteria style reference. |
| `plans/nullforge/QA-T005/IMPLEMENTOR_PROMPT.md` | Prior implementor prompt style | Local prompt style reference. |

## Excluded Sources

| Excluded Source | Reason |
|---|---|
| External incoming package files | Not repo-local active truth unless later imported through scoped audit. |
| Prompt files and old chats | Workflow history only; not active product/architecture truth. |
| `tickets/`, `milestones/`, `prompts/` | Not part of DA-T001 scope and not currently present as active repo-local truth. |
| Raw/full ES.zip and private/local data | Explicitly gated and irrelevant to bridge contract planning. |
| Generated datasets and ES-derived fixtures | Gated by later data/fixture policy tickets. |
| Tauri/Rust/React/Node package sources | No app scaffold or dependency work is in scope. |
| Broad ResearchCore Engine internals | Existing engine remains authoritative; DA-T001 only needs current CLI/package facts. |
| M2 through M6 feature implementation details | Future milestone context only; not needed for DA-T001 contract finalization. |

## Design Memory Handling

Volumes 3 and 7 are imported planning sources and can inform DA-T001. They do not prove current implementation behavior.

Any bridge command ID copied from Volume 3 must be labeled as planned/candidate unless existing repo evidence proves it exists. DA-T001 must not claim `engine.version`, `engine.doctor`, `workspace.inspect`, `fixture.smoke`, or `artifact.scan` are implemented.

## Refresh Rule

Refresh this context before implementation if any of the following changes:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- ADR-T001 or ADR-T002
- Volume 3 or Volume 7 source files
- QA-T005 execution/audit artifacts
- ResearchCore CLI/package facts
- any prior audit disposition
- working tree status outside `plans/nullforge/DA-T001/`
- human ticket scope

## Context Risks

- Volume 3 includes draft command IDs that may not exist in current ResearchCore Engine behavior.
- QA-T005 proves only isolated `.venv-qa-t005` readiness, not active/global Python environment readiness.
- The bridge contract could accidentally imply Tauri, sidecar, packaging, or permission behavior has been implemented. It must not.
- A docs-only bridge contract can become too broad and start specifying feature behavior beyond M1 proof needs. Keep it narrow.
- Human gates around file access, shell/process execution, dependencies, network, telemetry, cloud, broker/live, AI/model, and public release must remain explicit.

## Curator Verdict

Ready for planner.

The included context is sufficient to plan DA-T001 without broad repo reads, implementation work, or environment mutation.
