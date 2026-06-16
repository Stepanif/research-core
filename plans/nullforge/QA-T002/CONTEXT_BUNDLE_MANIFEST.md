# QA-T002 Context Bundle Manifest

## Bundle

- Ticket ID: `QA-T002`
- Bundle path: `plans/nullforge/QA-T002/CONTEXT_BUNDLE.md`
- Manifest path: `plans/nullforge/QA-T002/CONTEXT_BUNDLE_MANIFEST.md`
- Curator role: Context Curator
- Verdict: Ready for planner

## Required Inputs Read

| Path | Role |
| --- | --- |
| `docs/nullforge/CURRENT_STATUS.md` | Current NullForge phase, active status, no-code sentence, baseline marker. |
| `docs/nullforge/SOURCE_INDEX.md` | Repo-local source index and current NullForge artifact map. |
| `docs/nullforge/ARCHIVE_POLICY.md` | Archive, quarantine, and source-of-truth rules. |
| `docs/nullforge/codex/CODEX_ROLE_LOOP.md` | Role boundaries and artifact rules for context/planning/implementation/audit. |
| `docs/nullforge/qa/COMMAND_DISCOVERY.md` | `QA-T001` command discovery findings and CLI/runtime blocker evidence. |
| `docs/nullforge/M0_HANDOFF.md` | M0 completion context and M1 readiness transition. |
| `audits/nullforge/QA-T001/AUDIT_REPORT.md` | `QA-T001` audit `PASS` evidence. |
| `reports/nullforge/QA-T001/TEST_RESULTS.md` | Detailed local command results and blocker evidence from `QA-T001`. |
| `audits/nullforge/HY-T001/AUDIT_REPORT.md` | `HY-T001` audit `PASS` evidence. |
| `reports/nullforge/HY-T001/TEST_RESULTS.md` | Confirmation of local-path hygiene checks and remaining known hits. |
| `pyproject.toml` | Package metadata, package discovery, pytest config, dependency declarations. |
| `README.md` | Existing repo verification and command references. |
| `docs/how-to/run_ci_locally.md` | Current local CI and CLI command guidance. |
| `docs/reference/cli/overview.md` | Generated CLI invocation reference. |
| `docs/reference/cli/index.md` | Generated CLI reference index. |

## Supplemental Read-Only Discovery

These read-only discovery checks informed the bundle:

- `git status --short --branch`
- `rg --files src\research_core`
- `rg -n "research_core\.cli|typer|app =|def main|__main__|\[project\.scripts\]|console_scripts" pyproject.toml src docs\reference\cli docs\how-to README.md .github`
- `Test-Path -LiteralPath src\research_core\cli.py`
- `Test-Path -LiteralPath src\research_core\__main__.py`
- `Test-Path -LiteralPath package.json`

No install, test, docs generation, docs build, quickstart, CI smoke, or environment-changing command was run.

## Key Evidence Captured

- `QA-T001` audit decision is `PASS`.
- `HY-T001` audit decision is `PASS`.
- `QA-T001` recorded local environment blocker evidence:
  - editable install from `<local-temp-editable-install>`
  - `python -m research_core.cli --help` failed with `No module named research_core.cli`
  - `python -m research_core --help` failed because `research_core` has no `__main__`
  - `research-core --help` was not recognized
- `pyproject.toml` has Python package metadata and no console script entry point.
- `src/research_core/cli.py` exists.
- `src/research_core/__main__.py` is absent.
- CI and docs reference `python -m research_core.cli`.
- `No NullForge implementation code has started.`

## Included Scope

The context bundle includes:

- Ticket summary and M1 readiness purpose.
- Completed prerequisite audit evidence.
- Local environment blocker summary from `QA-T001`.
- Existing package and CLI metadata relevant to triage.
- Likely relevant files for later planning.
- Explicit exclusions, gates, stop conditions, and required later checks.
- Open questions for planner/human disposition.

## Excluded Scope

The context bundle excludes:

- Implementation plan artifacts.
- Reports and audits for `QA-T002`.
- Source, package, dependency, test, schema, fixture, CI, generated-doc, raw-data, or private-data changes.
- Environment mutation commands.
- `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, or downstream work.

## Current Repo State At Curation Start

```text
git status --short --branch
## main...origin/main
```

## Refresh Triggers

Refresh this bundle before planning if:

- `pyproject.toml`, `src/research_core/cli.py`, `.github/workflows/research-ci.yml`, or CLI docs change.
- A human changes the local Python environment or editable install state.
- `QA-T001` or `HY-T001` audit disposition changes.
- New untracked or modified files appear outside `plans/nullforge/QA-T002/`.

## Output Files

- `plans/nullforge/QA-T002/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T002/CONTEXT_BUNDLE_MANIFEST.md`
