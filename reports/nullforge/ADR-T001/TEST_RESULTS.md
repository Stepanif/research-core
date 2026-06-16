# ADR-T001 Test Results

Ticket: `ADR-T001`
Date: `2026-06-15`

These checks were run after creating the ADR-T001 implementor artifacts.

## Required Checks

| Check | Result | Notes |
|---|---|---|
| `git status --short --branch` | PASS | Branch is `docs/ADR-T001-nullforge-name-platform-stack-engine`; changes are bounded to ADR-T001 plans, allowed NullForge docs, and ADR-T001 reports. |
| `git status --short --untracked-files=all` | PASS | Listed only ADR-T001 plan files, ADR file, ADR-T001 reports, and allowed modified NullForge docs. |
| `git diff --name-only` | PASS | Tracked diffs are limited to `docs/nullforge/CURRENT_STATUS.md`, `docs/nullforge/DECISION_LEDGER.md`, and `docs/nullforge/SOURCE_INDEX.md`. |
| Required ADR-T001 file existence checks | PASS | ADR file and four required report files returned `True`. |
| PF-T002 audit `PASS` confirmation | PASS | `rg -n "Decision: PASS" audits\nullforge\PF-T002\AUDIT_REPORT.md` found the audit decision. |
| ADR required terms search | PASS | Found required name/platform/stack/engine/bridge/gate terms in the ADR. |
| Decision ledger required terms search | PASS | Found `ADR-T001`, `NF-D0004`, and `ADR-T002`; `NF-D0004` references ADR-T001 and ADR-T002 remains pending. |
| Current status required terms search | PASS | Found `ADR-T001`, `ADR-T002`, `REPO_SOURCE_IMPORT_BASELINE`, and the exact no-code sentence. |
| Source index required terms search | PASS | Found `ADR-T001`, `ADR-T002`, and `ADR-T001-name-platform-stack-engine`. |
| Repo-local Markdown links in `SOURCE_INDEX.md` resolve | PASS | Scripted PowerShell check confirmed all repo-local Markdown links resolve. |
| Changed files bounded to ADR-T001 plans, allowed NullForge docs, and reports | PASS | Status output is limited to `plans/nullforge/ADR-T001/`, `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`, `docs/nullforge/CURRENT_STATUS.md`, `docs/nullforge/DECISION_LEDGER.md`, `docs/nullforge/SOURCE_INDEX.md`, and `reports/nullforge/ADR-T001/`. |
| Forbidden files/folders unchanged | PASS | No files under root ResearchCore docs, `docs/STATUS.md`, `docs/index.md`, `docs/ARCHITECTURE.md`, `docs/reference/`, `docs/contributing/`, `src/`, `tests/`, `schemas/`, `configs/`, `tools/`, `.github/`, `tickets/nullforge/`, `milestones/nullforge/`, `prompts/nullforge/`, `docs/adr/`, `docs/architecture/`, or `docs/nullforge/adr/ADR-T002*` appear in status. |
| Optional docs build/generated-doc checks | Skipped | No docs nav, generated-reference, package, schema, or implementation files changed. |

## Command Output

### `git status --short --branch`

```text
## docs/ADR-T001-nullforge-name-platform-stack-engine
 M docs/nullforge/CURRENT_STATUS.md
 M docs/nullforge/DECISION_LEDGER.md
 M docs/nullforge/SOURCE_INDEX.md
?? docs/nullforge/adr/
?? plans/nullforge/ADR-T001/
?? reports/nullforge/ADR-T001/
```

### `git status --short --untracked-files=all`

```text
 M docs/nullforge/CURRENT_STATUS.md
 M docs/nullforge/DECISION_LEDGER.md
 M docs/nullforge/SOURCE_INDEX.md
?? docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md
?? plans/nullforge/ADR-T001/ACCEPTANCE.md
?? plans/nullforge/ADR-T001/CONTEXT_BUNDLE.md
?? plans/nullforge/ADR-T001/CONTEXT_BUNDLE_MANIFEST.md
?? plans/nullforge/ADR-T001/IMPLEMENTOR_PROMPT.md
?? plans/nullforge/ADR-T001/PLAN.md
?? reports/nullforge/ADR-T001/AUDITOR_PROMPT.md
?? reports/nullforge/ADR-T001/CHANGED_FILES.md
?? reports/nullforge/ADR-T001/IMPLEMENTATION_REPORT.md
?? reports/nullforge/ADR-T001/TEST_RESULTS.md
```

### `git diff --name-only`

```text
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/DECISION_LEDGER.md
docs/nullforge/SOURCE_INDEX.md
```

### Required file existence checks

```text
Test-Path -LiteralPath docs\nullforge\adr\ADR-T001-name-platform-stack-engine.md -> True
Test-Path -LiteralPath reports\nullforge\ADR-T001\IMPLEMENTATION_REPORT.md -> True
Test-Path -LiteralPath reports\nullforge\ADR-T001\CHANGED_FILES.md -> True
Test-Path -LiteralPath reports\nullforge\ADR-T001\TEST_RESULTS.md -> True
Test-Path -LiteralPath reports\nullforge\ADR-T001\AUDITOR_PROMPT.md -> True
```

### `rg -n "Decision: PASS" audits\nullforge\PF-T002\AUDIT_REPORT.md`

```text
5:Decision: PASS
```

### `rg -n "NullForge|working product name|research-core|ResearchCore Engine|Windows 11 x64|Tauri|React|TypeScript|sidecar|command bridge|reversal|human gate" docs\nullforge\adr\ADR-T001-name-platform-stack-engine.md`

```text
9:ADR-T001 records the first NullForge architecture/product boundary decisions after PF-T002 established the current status, source index, decision ledger, and archive policy. PF-T002 has audit decision `PASS`.
20:Existing ResearchCore Engine docs, code, package metadata, schemas, tests, and generated references remain separate engine truth. ADR-T001 does not rename or rewrite the engine.
22:No NullForge implementation code has started.
28:| Product name | `NullForge` | Working product name only. Not legally/trademark cleared and not approved for public distribution. |
29:| Repo identity | `research-core` | Existing repo name remains unchanged. |
30:| Engine label | `ResearchCore Engine` | Existing internal engine label remains unchanged. |
31:| First platform | Windows 11 x64 | First future desktop proof target. Not a cross-platform claim. |
32:| Desktop stack | Tauri + React/TypeScript | Accepted default desktop stack direction pending bridge and packaging spikes. |
33:| Engine boundary | Python ResearchCore Engine sidecar / scoped command bridge | Intended future boundary. Narrow, allowlisted, structured command protocol; not arbitrary shell execution. |
39:Use `NullForge` as the working product name for planning docs and future app-facing language.
45:Keep the repository name `research-core`.
47:Keep the internal engine label `ResearchCore Engine`.
53:Use Windows 11 x64 as the first platform for future desktop proof work.
59:Use Tauri + React/TypeScript as the accepted default desktop stack direction pending bridge and packaging spikes.
65:Treat the existing Python ResearchCore Engine as a separate engine controlled by a future Python sidecar / scoped command bridge.
83:| `NullForge` as working product name | Chosen | Matches imported planning docs and separates future product/workbench language from the existing engine repo. |
91:| Windows 11 x64 first | Chosen | Matches first-user environment and M1 proof path. |
99:| Tauri + React/TypeScript | Chosen as default direction pending spikes | Matches imported planning docs and supports a local desktop shell direction with explicit permission/bridge boundaries. |
108:| Dev command bridge to local Python environment | Chosen as early proof path | Fastest way to test a narrow bridge without packaging claims. |
109:| Packaged Python sidecar | Chosen as later spike target | Needed before stronger desktop distribution claims. |
118:- ResearchCore Engine remains the engine truth and can continue evolving separately.
148:- name conflict, legal risk, brand risk, or public release review invalidates `NullForge`;
149:- Windows 11 x64 blocks first-user proof or a later audited decision changes platform priority;
150:- Tauri cannot support required filesystem, process, permission, packaging, or dev-velocity needs;
151:- the sidecar / command bridge repeatedly fails;
155:- a human gate requires deferral or repair.
```

The full command output included additional matches for source file paths, risks, human gates, and non-decisions.

### `rg -n "ADR-T001|NF-D0004|ADR-T002" docs\nullforge\DECISION_LEDGER.md`

```text
14:| `NF-D0004` | `2026-06-15` | Accepted by ADR-T001 | Record `NullForge` as working product name only, keep repo `research-core`, keep internal engine label `ResearchCore Engine`, set Windows 11 x64 as first platform, set Tauri + React/TypeScript as default desktop stack direction pending bridge/packaging spikes, and define the intended engine boundary as a Python ResearchCore Engine sidecar / scoped command bridge. | [ADR-T001 name/platform/stack/engine](adr/ADR-T001-name-platform-stack-engine.md), Volume 00, Volume 03, PF-T000 conflict/gate context. | Reverse or repair by scoped ADR if name conflict/legal/brand risk blocks use, Windows proof fails, Tauri/packaging/bridge proof fails, arbitrary shell execution is required, or app/engine split becomes impossible to communicate or maintain. | `ADR-T001` |
15:| `NF-D0005` | `2026-06-15` | Pending ADR | Decide local-first/no-cloud MVP boundary. | Volume 00, Volume 03, Volume 07 roadmap context. | Must be resolved by scoped ADR ticket; do not treat as accepted in PF-T002. | `ADR-T002` |
```

### `rg -n "ADR-T001|ADR-T002|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\CURRENT_STATUS.md`

```text
5:Active phase: `REPO_SOURCE_IMPORT_BASELINE`
7:Active ticket: `ADR-T001`
9:Next action: `ADR-T002` after ADR-T001 independent audit disposition.
13:No NullForge implementation code has started.
15:NullForge is in M0 repo source import and canonical baseline work. The current repo-local NullForge source set contains the PF-T000 import planning docs, the PF-T001 imported Volume 00-07 planning artifacts, and the PF-T002 status/source baseline. ADR-T001 records the working name, first platform, default desktop stack direction, and ResearchCore Engine boundary as a docs-only decision record.
26:| `ADR-T001` | In progress until independent audit disposition | [ADR-T001 plan](../../plans/nullforge/ADR-T001/PLAN.md) | Records working name, first platform, default desktop stack direction, and ResearchCore Engine boundary. |
27:| `ADR-T002` | Pending downstream ticket | `ADR-T002` | Must not start until ADR-T001 has an audit disposition. |
31:- ADR-T001 must receive independent audit disposition before it is complete.
39:- ADR-T001 records planning/source-of-truth decisions only; it does not prove Tauri feasibility, packaging feasibility, bridge reliability, product validation, user validation, market claims, trading validity, financial advice safety, legal clearance, or public distribution safety.
```

### `rg -n "ADR-T001|ADR-T002|ADR-T001-name-platform-stack-engine" docs\nullforge\SOURCE_INDEX.md`

```text
18:| [ADR-T001 - Name/platform/stack/engine](adr/ADR-T001-name-platform-stack-engine.md) | Records working product name, first platform, default desktop stack direction, and ResearchCore Engine boundary. | Active NullForge decision record after ADR-T001 audit disposition; not implementation proof. |
42:| [ADR-T001 Context Bundle](../../plans/nullforge/ADR-T001/CONTEXT_BUNDLE.md) | Curated active context for ADR-T001. | Repo-local plan artifact. |
43:| [ADR-T001 Context Bundle Manifest](../../plans/nullforge/ADR-T001/CONTEXT_BUNDLE_MANIFEST.md) | Context source list and exclusions. | Repo-local plan artifact. |
44:| [ADR-T001 Plan](../../plans/nullforge/ADR-T001/PLAN.md) | Bounded implementation plan. | Repo-local plan artifact. |
45:| [ADR-T001 Acceptance](../../plans/nullforge/ADR-T001/ACCEPTANCE.md) | Acceptance criteria and checks. | Repo-local plan artifact. |
46:| [ADR-T001 Implementor Prompt](../../plans/nullforge/ADR-T001/IMPLEMENTOR_PROMPT.md) | Implementor instructions. | Repo-local plan artifact. |
47:| [ADR-T001 Implementation Report](../../reports/nullforge/ADR-T001/IMPLEMENTATION_REPORT.md) | Implementor report. | Created by ADR-T001 implementor. |
48:| [ADR-T001 Changed Files](../../reports/nullforge/ADR-T001/CHANGED_FILES.md) | Changed-file inventory. | Created by ADR-T001 implementor. |
49:| [ADR-T001 Test Results](../../reports/nullforge/ADR-T001/TEST_RESULTS.md) | Required check results. | Created by ADR-T001 implementor. |
50:| [ADR-T001 Auditor Prompt](../../reports/nullforge/ADR-T001/AUDITOR_PROMPT.md) | Independent auditor prompt. | Created by ADR-T001 implementor. |
57:<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\ADR-T001-name-platform-stack-engine-adr.md
66:tickets/nullforge/ADR-T001-name-platform-stack-engine-adr.md
70:docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
93:| `ADR-T002` | Decide local-first/no-cloud MVP boundary after ADR-T001 audit disposition. | Pending downstream; not created in ADR-T001. |
```

### `git diff --check`

```text
```

### `SOURCE_INDEX.md` Markdown link resolution

```text
All SOURCE_INDEX.md repo-local Markdown links resolve.
```

Note: the first sandboxed run of the read-only link-resolution script failed because the Windows sandbox helper could not launch. The same read-only check was rerun with escalation and passed.
