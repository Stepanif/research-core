> Import note: This file was imported by PF-T001 from `NullForge_Volume_03_v0_4_Package.zip` / `artifacts/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md` on `2026-06-15`.
> Authority: repo-managed NullForge planning/workflow source after PF-T001 audit. It is not ResearchCore Engine implementation truth.
> Source package SHA256: `0C8E5730CBBAB35E5F80B496D291F2E34204A3363D218C8980DC2254B8AD297B`

# Volume 3 — NullForge Windows + Tauri Desktop Architecture, ResearchCore Engine Bridge, Sidecar Contract, and Packaging Spike Plan

```text
Project: NullForge
Version: v0.4
Volume: 03
Status: DRAFT_CANONICAL_PROJECT_SOURCE
Date: 2026-06-14
```

---

## 1. Volume purpose

This volume defines the **desktop architecture and first technical proof path** for NullForge.

It answers:

```text
How should NullForge become a real Windows 11 x64 desktop app?
How should the Tauri shell talk to the existing ResearchCore Engine?
What can the desktop bridge do during the MVP?
What must it never do?
What packaging spike proves the direction before feature buildout?
```

This volume does **not** implement code. It creates the architecture boundary that future tickets must obey.

---

## 2. Relationship to Volumes 0, 1, and 2

### Volume 0 established

```text
NullForge mission
first user
first proof loop
MVP cutline
claim ledger seed
anti-goals
promotion / repair / archive / quarantine policy
```

### Volume 1 established

```text
repo/source-of-truth doctrine
local workspace boundaries
archive/quarantine system
data boundary for ES.zip and fixtures
prompt/volume/ADR storage policy
context-pack rules
drift checks
```

### Volume 2 established

```text
context-curator → planner → implementor → auditor role loop
ticket artifact tree
PASS / HOLD / REJECT audit rules
QA/security/human gates
milestone batching discipline
Codex boundaries
```

### Volume 3 adds

```text
Windows 11 x64 desktop architecture
Tauri + React + TypeScript boundary
ResearchCore Engine bridge model
Python sidecar / command bridge strategy
permission and filesystem access model
packaging spike plan
desktop-specific QA/security gates
```

Volume 3 is the bridge between project doctrine and the first serious technical proof.

---

## 3. Desktop-first product decision

```text
Decision:
NullForge is a downloadable Windows desktop application first, not a thin browser/localhost dashboard.
```

The intended user experience is:

```text
download / install
→ double-click NullForge
→ create/select local workspace
→ import/use fixture dataset
→ run local ResearchCore Engine smoke
→ inspect artifact metadata
→ open visual replay fixture
→ see audit/decision placeholder
```

### Why desktop-first

| Reason | Meaning |
|---|---|
| Local-first data | Market datasets and artifacts should remain on the user machine by default. |
| Serious app feel | Double-click desktop app matches the desired product form better than loose HTML files or a dev server. |
| File access | Dataset import, workspace selection, artifacts, logs, and exports are natural desktop workflows. |
| Engine wrapping | The existing ResearchCore Engine is Python-based and should be controlled locally. |
| Offline-friendly path | MVP should not depend on cloud accounts, server uptime, or auth. |

### What this decision does not prove

```text
It does not prove market edge.
It does not prove user retention.
It does not prove public packaging/distribution.
It does not prove name/legal availability.
It does not prove cross-platform viability.
```

---

## 4. Windows 11 x64 first-platform boundary

```text
First platform:
Windows 11 x64 on the project owner's system.
```

### Included

```text
Windows 11 x64 development and smoke execution.
Local install/build on the owner's machine.
Tauri desktop shell.
ResearchCore Engine local sidecar / command bridge.
Local workspace folder.
Local logs and artifacts.
```

### Excluded for MVP

```text
macOS packaging
Linux packaging
Microsoft Store distribution
auto-updater
code signing requirement
public release
enterprise installer management
multi-user workstation policy
```

### Platform expansion rule

Only expand beyond Windows 11 x64 after:

```text
- Windows bridge proof passes;
- packaged local app can call the engine safely;
- workspace/data boundary is audited;
- Volume 7 roadmap explicitly promotes cross-platform work.
```

---

## 5. Tauri + React + TypeScript architecture

### Recommended shell architecture

```text
NullForge Desktop App
├── Tauri shell
│   ├── Rust command layer
│   ├── permission/capability boundary
│   ├── sidecar process launcher
│   ├── workspace/file access adapter
│   └── app logging/error bridge
│
├── React + TypeScript UI
│   ├── Lab Cockpit
│   ├── Dataset Studio
│   ├── Logic Factory
│   ├── Visual Replay
│   ├── Evidence Cards
│   └── Settings / Workspace
│
└── ResearchCore Engine bridge
    ├── packaged Python sidecar or dev command adapter
    ├── command allowlist
    ├── structured request/response contract
    ├── artifact path contract
    └── logs/errors/exit-code contract
```

### Responsibilities by layer

| Layer | Owns | Must not own |
|---|---|---|
| React/TypeScript UI | Screens, interactions, status display, user confirmation flows | Raw shell execution, engine internals, file permission bypass |
| Tauri/Rust layer | Desktop permissions, filesystem boundary, process spawning, command adapter | Product strategy, engine logic, candidate validity |
| ResearchCore Engine | Canonicalization, validation, artifact production, existing CLI logic | Desktop UI state, broad OS file access, public release policy |
| Workspace filesystem | Durable local datasets, manifests, runs, artifacts, evidence | Repo source-of-truth docs, unreviewed strategy authority |
| Repo docs | Canonical project truth and implementation governance | User runtime data, full private datasets |

### UI is not source of truth

The desktop shell displays and orchestrates. It does not become the source of truth.

```text
Repo docs govern project truth.
ResearchCore Engine artifacts govern run truth.
Workspace manifests govern local user/runtime state.
UI state is temporary and recoverable.
```

---

## 6. Existing ResearchCore Engine boundary

The existing `research-core` repo / engine is treated as a real prior asset.

### ResearchCore Engine owns

```text
existing Python CLI
existing canonicalization / validation / artifact commands
existing schema/report patterns
existing tests
existing ResearchCore docs
core research logic
```

### NullForge owns

```text
desktop shell
workspace selection
dataset import UI
capability map display
logic factory UI
engine orchestration
artifact browsing
visual replay UI
evidence card UI
audit/decision UX
```

### Boundary rule

```text
Do not rewrite the ResearchCore Engine just to make the UI easier.
```

If the engine needs a new command or output contract, the change must be introduced through a scoped ticket, acceptance criteria, tests, and audit.

---

## 7. Python sidecar / command bridge options

### Option A — Tauri external binary sidecar wrapping ResearchCore Engine

```text
Tauri packages a local executable sidecar.
The sidecar exposes a narrow JSON-oriented command surface.
The desktop app invokes only allowlisted bridge commands.
```

**Pros**

```text
Best product feel.
User does not need to install Python manually.
Works with double-click desktop app goal.
Supports packaged proof.
```

**Cons**

```text
Packaging Python dependencies may be difficult.
Binary size may be large.
PyArrow/scientific dependencies may complicate packaging.
Antivirus/SmartScreen warnings may appear during early unsigned builds.
```

### Option B — Development bridge to local Python environment

```text
During early development, Tauri calls the existing Python CLI through a configured local venv/command.
```

**Pros**

```text
Fastest way to prove command contract.
Avoids packaging complexity at first.
Good for local developer smoke tests.
```

**Cons**

```text
Not enough for user-grade desktop app.
Requires local Python environment.
Can mask packaging failures.
```

### Option C — Embedded Python distribution

```text
Bundle a minimal Python runtime and ResearchCore package resources with the desktop app.
```

**Pros**

```text
Potentially more controllable than relying on system Python.
May support more transparent dependency layout.
```

**Cons**

```text
More custom packaging complexity.
Harder to validate quickly.
May create brittle path/import behavior.
```

### Option D — Local HTTP server

```text
Tauri launches a local ResearchCore service and UI communicates over localhost.
```

**Pros**

```text
Clear API boundary.
Good long-term if background jobs become complex.
```

**Cons**

```text
Feels closer to the browser/server model the product is trying to avoid.
Adds port/firewall/process-lifecycle complexity.
Too much for MVP bridge proof.
```

---

## 8. Recommended bridge strategy for MVP

```text
Recommended MVP bridge:
Start with a strict command bridge that can operate in dev mode against a local Python environment, then prove a packaged sidecar path in a dedicated packaging spike.
```

### Phase A — dev command bridge

Goal:

```text
Prove the UI/Rust bridge can invoke a narrow ResearchCore Engine command and parse structured output.
```

Allowed for Phase A:

```text
local configured engine command
fixture workspace
strict command allowlist
structured JSON response
no arbitrary shell strings
no broad file access
```

### Phase B — packaged sidecar spike

Goal:

```text
Prove the same bridge contract can run when the engine is packaged as a Windows x64 sidecar.
```

Allowed for Phase B:

```text
sidecar executable
fixture command only
one packaged local build
workspace-scoped output
logs and error report
```

### Promotion rule

Promote the bridge only if:

```text
- command allowlist works;
- workspace path restrictions work;
- stdout/stderr/error behavior is predictable;
- artifact metadata can be displayed;
- packaged or packaging-spike behavior is documented;
- no human gate is bypassed.
```

---

## 9. Bridge contract draft

The bridge contract is a **structured command protocol**, not a raw shell interface.

### Request object

```json
{
  "request_id": "uuid-or-ticket-run-id",
  "bridge_version": "0.1",
  "command_id": "engine.doctor",
  "workspace_path": "C:/Users/<user>/NullForge_Workspace",
  "inputs": {
    "fixture_id": "synthetic_ohlcv_tiny"
  },
  "output_mode": "json",
  "timeout_ms": 30000,
  "dry_run": false
}
```

### Response object

```json
{
  "request_id": "same-as-request",
  "status": "OK",
  "command_id": "engine.doctor",
  "exit_code": 0,
  "duration_ms": 523,
  "engine": {
    "name": "ResearchCore Engine",
    "version": "unknown-until-read",
    "mode": "dev-or-sidecar"
  },
  "artifacts": [
    {
      "artifact_id": "artifact-or-run-id",
      "kind": "doctor_report",
      "path": "workspace-relative/path/to/artifact.json",
      "sha256": "optional"
    }
  ],
  "warnings": [],
  "errors": []
}
```

### Error response object

```json
{
  "request_id": "same-as-request",
  "status": "ERROR",
  "command_id": "engine.smoke",
  "exit_code": 2,
  "duration_ms": 812,
  "error": {
    "code": "ENGINE_COMMAND_FAILED",
    "message": "Human-readable summary.",
    "stderr_excerpt": "bounded stderr excerpt",
    "repair_hint": "Check engine install or fixture path."
  },
  "artifacts": [],
  "warnings": [
    "Full stderr stored in workspace logs."
  ]
}
```

### Required bridge fields

| Field | Required? | Purpose |
|---|---:|---|
| `request_id` | Yes | Correlates UI event, engine run, logs, artifacts. |
| `bridge_version` | Yes | Allows contract evolution. |
| `command_id` | Yes | Uses allowlist; prevents raw shell. |
| `workspace_path` | Yes | Scopes read/write behavior. |
| `inputs` | Yes | Structured parameters only. |
| `timeout_ms` | Yes | Prevents hung commands. |
| `status` | Yes | `OK`, `ERROR`, `TIMEOUT`, `CANCELLED`, `BLOCKED`. |
| `exit_code` | Yes when process ran | Debug/audit field. |
| `artifacts` | Yes, can be empty | Lets UI show evidence links. |
| `warnings/errors` | Yes, can be empty | Keeps failures explicit. |

---

## 10. Allowed engine commands for first proof

The first proof should use only a tiny command allowlist.

| Bridge command ID | Purpose | Mutates workspace? | Notes |
|---|---|---:|---|
| `engine.version` | Return engine/version/environment metadata. | No | Read-only smoke. |
| `engine.doctor` | Check engine can run and report basic health. | Optional report only | No dataset required. |
| `workspace.inspect` | Confirm workspace manifest and expected folders. | No | App/bridge command, not necessarily engine-owned. |
| `fixture.smoke` | Run one tiny fixture smoke command. | Yes, writes a run/artifact report | Must use committed synthetic or approved small fixture. |
| `artifact.scan` | Return workspace-relative artifact metadata. | No | Must not scan outside workspace. |

### First proof command sequence

```text
engine.version
→ workspace.inspect
→ engine.doctor
→ fixture.smoke
→ artifact.scan
```

### Commands explicitly deferred

```text
full dataset import
full ES.zip processing
logic generation
logic compiler execution
optimizer runs
large backtests
AI proposal
broker integration
network calls
public release packaging
```

---

## 11. Forbidden bridge behaviors

The bridge must not:

```text
accept arbitrary shell strings from the UI
execute user-provided scripts
run commands outside an allowlist
scan arbitrary folders or drives
delete files outside workspace
mutate the repo unless a scoped dev ticket says so
commit full ES.zip
send datasets to cloud
install dependencies silently
modify environment variables/secrets silently
launch broker/live trading
activate AI/model calls
hide stderr/test failures
promote claims automatically
```

### Shell command rule

```text
Never concatenate a shell string from UI inputs.
Use structured command IDs and structured arguments.
```

### Path rule

```text
User-selected paths must be normalized, validated, recorded in a manifest, and constrained by explicit import/copy/reference policies.
```

---

## 12. Tauri permission boundary

Tauri permissions should be treated as an architecture surface, not as a convenience setting.

### Default stance

```text
Deny by default.
Allow only the commands and filesystem scopes needed for the current ticket.
Expand permissions only through ADR/ticket/audit.
```

### Initial permissions should support only

```text
open app window
select workspace folder
read/write workspace-owned files
read selected imported fixture file
call allowlisted bridge commands
write app logs
display artifact metadata
```

### Initial permissions should not support

```text
arbitrary shell
arbitrary filesystem traversal
network access
auto-updater
global file scanning
background startup
clipboard scraping
credential storage
broker connectivity
```

### Capability policy

| Capability area | MVP default | Expansion gate |
|---|---|---|
| Filesystem | Workspace-scoped read/write only | Human gate for broader import/reference behavior |
| Shell/process | Allowlisted sidecar commands only | Human gate for any new command |
| Network | Off / not required | Human gate + privacy/security review |
| Updater | Off | Post-MVP release decision |
| Notifications | Off | UX/product decision later |
| Store/settings | Minimal app settings only | Human gate if sensitive data stored |

---

## 13. Local workspace access model

The app should work against one selected local workspace at a time.

### Workspace selection

```text
User creates/selects NullForge_Workspace.
App writes/reads workspace manifest.
App does not silently scan parent directories.
App does not assume repo location equals workspace location.
```

### Workspace manifest draft

```json
{
  "workspace_schema_version": "0.1",
  "workspace_id": "uuid",
  "created_at": "timestamp",
  "last_opened_at": "timestamp",
  "app_name": "NullForge",
  "engine_label": "ResearchCore Engine",
  "paths": {
    "datasets": "datasets/",
    "fixtures": "datasets/fixtures/",
    "runs": "runs/",
    "artifacts": "artifacts/",
    "logs": "logs/",
    "evidence": "evidence/",
    "visual_replay": "visual_replay/"
  },
  "data_policy": {
    "raw_full_datasets_committed_to_repo": false,
    "external_dataset_references_allowed": "later",
    "fixture_policy": "small-license-safe-only"
  }
}
```

### Workspace write policy

| Area | Write allowed in MVP? | Notes |
|---|---:|---|
| `logs/` | Yes | App and engine logs. |
| `runs/` | Yes | Engine smoke output. |
| `artifacts/` | Yes | Artifact metadata/read-only output index. |
| `datasets/fixtures/` | Yes | Tiny approved fixture only. |
| `datasets/raw/` | No or manual only | Full ES.zip import later. |
| `logic/` | No | Volume 5 later. |
| `evidence/` | Placeholder only | Volume 6 later. |

---

## 14. Data/file-access security model

### Security posture

```text
Local-first does not mean careless.
Local file access is a permission boundary.
```

### Allowed for MVP

```text
read app config
read/write selected NullForge workspace
read tiny fixture dataset
write smoke run artifacts
write bounded logs
display workspace-relative paths
```

### Not allowed for MVP

```text
recursive drive scan
automatic import of huge raw datasets
deleting external user files
modifying repo files from app runtime
network upload
untrusted script execution
loading plugins
reading secrets
```

### ES.zip boundary

```text
Full 10-year ES.zip stays outside repo.
Full ES.zip is not imported in Volume 3.
Small ES-derived fixtures are allowed later only if license-safe and intentionally selected.
Dataset Studio governs real import policy in Volume 4.
```

### Path and filename rules

```text
Use workspace-relative artifact paths in UI.
Store absolute paths only in local workspace manifest/settings when needed.
Never display or log sensitive full paths unnecessarily.
Reject path traversal.
Reject executable/script imports as datasets.
Record dataset source/import decisions.
```

---

## 15. Process/logging/error-handling model

### Process model

```text
React UI event
→ Tauri command invocation
→ Rust bridge validates command_id and inputs
→ Rust bridge constructs safe process call
→ ResearchCore Engine sidecar/dev command runs
→ stdout/stderr/exit code captured
→ artifacts written to workspace
→ structured response returned to UI
→ UI displays status/artifact metadata
```

### Logging model

| Log | Location | Contents | Exclusions |
|---|---|---|---|
| App log | `workspace/logs/nullforge-app.log` | UI/bridge lifecycle, non-sensitive errors | raw dataset contents, secrets |
| Engine log | `workspace/logs/researchcore-engine.log` | engine command, run ID, bounded stderr | full private paths unless needed |
| Run log | `workspace/runs/<run_id>/run.log` | specific smoke/run result | secrets, full ES data dump |
| Audit/event log | later Volume 6 | decision events | automated promotion |

### Error handling requirements

| Failure | User sees | Artifact/log |
|---|---|---|
| Engine not found | “ResearchCore Engine is not available.” | bridge error report |
| Command not allowlisted | “Command blocked by bridge policy.” | security event |
| Timeout | “Engine command timed out.” | timeout report |
| Bad workspace | “Workspace is missing or invalid.” | workspace inspection report |
| Bad fixture path | “Fixture unavailable or invalid.” | data error report |
| Engine exception | bounded human-readable summary | stderr excerpt + full local log |
| Permission denied | “NullForge lacks permission for this workspace path.” | permission report |

### Stderr rule

```text
Never dump unbounded stderr into the UI.
Show bounded excerpts and store full local logs only when safe.
```

---

## 16. Packaging spike plan

### Spike name

```text
DA-SPIKE-001 — Windows Tauri + ResearchCore Engine Bridge Packaging Spike
```

### Spike purpose

Prove the highest-risk desktop technical claim:

```text
A Windows 11 x64 Tauri app can launch locally, access a selected workspace, invoke a narrow ResearchCore Engine command through a safe bridge, receive structured output, and display artifact metadata.
```

### Inputs

```text
Volumes 0–3
existing research-core repo
tiny synthetic OHLCV fixture or no-data engine doctor command
Windows 11 x64 dev system
Tauri development environment
local Python ResearchCore Engine environment
```

### Spike sequence

```text
1. Confirm Windows 11 x64 dev prerequisites.
2. Confirm existing ResearchCore Engine can run a minimal local command outside Tauri.
3. Define bridge command allowlist for first proof.
4. Create a minimal Tauri shell only after ticket approval.
5. Add a dev bridge path to call engine.version / engine.doctor.
6. Add workspace create/select smoke.
7. Add fixture.smoke if fixture exists and is approved.
8. Capture structured JSON output and bounded error behavior.
9. Display artifact metadata in a simple read-only UI.
10. Attempt packaged sidecar build or document precise blocker.
11. Run audit against bridge, permissions, data, and packaging acceptance.
```

### Spike acceptance criteria

```text
- App launches on Windows 11 x64.
- User can select/create local workspace.
- Bridge command allowlist is explicit.
- No arbitrary shell execution exists.
- engine.version or engine.doctor succeeds through the bridge.
- At least one command failure path is shown cleanly.
- Artifact metadata can be read from workspace.
- Logs are written locally.
- Full ES.zip is not used or committed.
- No network/cloud/broker/AI behavior exists.
- Packaging path is either proven or blocked with specific evidence.
```

### Spike failure thresholds

```text
- Tauri cannot invoke a safe command bridge on the target system.
- ResearchCore Engine cannot run locally in a predictable way.
- Packaging requires broad unsafe permissions.
- Python dependency packaging is not viable without major engine refactor.
- The bridge requires arbitrary shell execution to function.
- Workspace path restrictions cannot be enforced.
```

### Spike output artifacts

```text
DA-SPIKE-001_REPORT.md
DA-SPIKE-001_CHANGED_FILES.md
DA-SPIKE-001_TEST_RESULTS.md
DA-SPIKE-001_BRIDGE_FINDINGS.md
DA-SPIKE-001_PACKAGING_FINDINGS.md
DA-SPIKE-001_AUDIT_REPORT.md
```

---

## 17. Installer/signing/update deferrals

### Installer

MVP may produce a local dev build or installer artifact for the owner's machine.

It does not require:

```text
polished installer UX
Microsoft Store package
enterprise MSI policy
auto-update
cross-machine testing
public release notes
```

### Signing

Code signing is deferred.

```text
Unsigned builds may trigger Windows trust warnings.
This is acceptable for owner-only development.
Public distribution requires a separate signing/release decision.
```

### Updates

Auto-update is deferred.

```text
No updater plugin is required for MVP.
No update server.
No static update manifest.
No release channel.
```

### Public distribution

```text
Do not publicly package or distribute under NullForge before name availability/legal conflict review.
```

---

## 18. Development environment assumptions

### First development environment

```text
OS: Windows 11 x64
Repo: existing research-core
Desktop stack: Tauri + React + TypeScript
Engine: existing Python ResearchCore Engine
Data: tiny fixture first; full ES.zip outside repo
```

### Expected tools to verify during DA-SPIKE-001

```text
Git
Node package manager selected by repo decision
Rust toolchain
Tauri CLI/tooling
Microsoft C++ Build Tools
Microsoft Edge WebView2
Python version compatible with research-core
ResearchCore Engine dependencies
test runner for existing repo
packaging tool candidate for Python sidecar
```

### Version pinning rule

```text
Do not guess final versions in Volume 3.
Record actual versions during the packaging spike and promote them through ADR/update.
```

---

## 19. Test strategy for desktop bridge proof

### Test categories

| Test | Purpose |
|---|---|
| Engine direct smoke | Confirm ResearchCore Engine runs outside desktop app. |
| Bridge allowlist test | Confirm only approved command IDs run. |
| Workspace path test | Confirm app uses only selected workspace. |
| Error handling test | Confirm missing engine/bad command/timeouts are visible and logged. |
| Artifact metadata test | Confirm produced artifacts can be indexed/displayed. |
| Negative shell test | Confirm arbitrary shell strings cannot run. |
| Full ES.zip exclusion test | Confirm full data is not committed/used in MVP spike. |
| Permission review | Confirm no broad filesystem/network/updater permissions. |
| Packaging smoke | Confirm build or document precise blocker. |

### Minimum test command expectations

Future implementation tickets should define exact commands, but Volume 3 expects at least:

```text
existing ResearchCore Engine tests or smoke command
desktop bridge smoke
workspace selection/create smoke
allowlist negative test
artifact metadata read smoke
```

### Test result rule

```text
Tests skipped without precise reason cannot pass audit.
```

---

## 20. QA/security/human gates specific to desktop/sidecar work

Human gate required before:

```text
adding Tauri plugins
expanding filesystem permissions
adding shell/process permissions
adding network access
changing sidecar packaging method
adding dependencies
changing Python version
changing ResearchCore Engine command behavior
using real ES.zip
committing any data fixture derived from ES.zip
adding updater
adding installer signing/public release
adding telemetry/analytics
activating AI/model calls
adding broker/live trading hooks
changing workspace deletion behavior
```

### Security review required before

```text
arbitrary file import
external binary execution beyond allowlist
large dataset import
workspace cleanup/delete features
credential/token storage
network access
auto-update
plugin system
```

### Audit must check

```text
- no arbitrary shell execution;
- bridge command IDs are allowlisted;
- workspace scope is enforced;
- logs do not leak sensitive data;
- full ES.zip was not committed;
- no network/cloud/broker/AI behavior was added;
- tests ran or skips are justified;
- docs/ADRs updated for architecture changes.
```

---

## 21. Risks and reversal conditions

| Risk | Severity | Mitigation | Reversal / repair condition |
|---|---:|---|---|
| Python sidecar packaging fails | High | Run packaging spike before feature build | Switch to dev-engine bridge for MVP or evaluate embedded Python/Electron fallback |
| Tauri permission model becomes awkward | Medium/High | Keep MVP command surface tiny | Reassess shell stack if safe file/process model cannot be expressed |
| Scientific deps create huge/fragile sidecar | High | Start with doctor/smoke only | Split engine packaging or require local engine install for early internal build |
| Bridge accidentally enables arbitrary shell | High | Command IDs only, no raw shell | HOLD/REJECT ticket until removed |
| Workspace access too broad | High | Workspace-scoped permissions | HOLD/REJECT ticket; repair permission model |
| Visual UI pressures engine changes | Medium | Engine boundary doctrine | New engine change must be scoped and tested |
| Unsigned installer warnings | Medium | Owner-only build first | Public distribution deferred until signing plan |
| Name conflict | Medium | Working name only | Rename before public release if conflict matters |
| Full ES.zip leaks into repo | High | Data boundary and audit checks | Immediate REJECT, purge/remediation plan |
| App drifts toward live trading | High | Anti-goal and human gate | Quarantine/reject any broker/live order feature |

---

## 22. ADRs to create later

| ADR | Decision |
|---|---|
| `ADR-001` | NullForge working name and ResearchCore Engine naming boundary |
| `ADR-002` | Windows 11 x64 first-platform decision |
| `ADR-003` | Tauri + React + TypeScript desktop shell decision |
| `ADR-004` | ResearchCore Engine sidecar / command bridge strategy |
| `ADR-005` | Local workspace and filesystem permission model |
| `ADR-006` | No cloud/auth/updater/signing/public release for MVP |
| `ADR-007` | Full ES.zip remains outside repo; fixtures only if license-safe |
| `ADR-008` | No AI/broker/live trading in MVP |

Each ADR must include:

```text
context
options considered
chosen option
why
evidence
risks
reversal condition
human owner
review date
```

---

## 23. First milestone category enabled by this volume

Volume 3 enables the future milestone category:

```text
M1 — Windows Tauri Shell + ResearchCore Engine Bridge Smoke
```

This milestone should not be generated yet as implementation prompts until:

```text
Volume 4 Dataset Studio boundary exists.
Volume 5 Logic Factory boundary exists.
Volume 6 Visual Replay / Evidence Card boundary exists.
Volume 7 roadmap/ticket system exists.
M0 docs/source-of-truth baseline is accepted.
```

However, Volume 3 allows planning of the future `DA` ticket family.

---

## 24. What must not be built yet

Do not build yet:

```text
full Tauri app
production installer
auto-updater
signed release
dataset import system
full ES.zip processor
timeframe generator
chart-type generator
logic compiler
logic generator
visual replay engine
evidence card system
AI proposal layer
optimizer/backtest UI
broker integration
live trading
plugin system
account/auth/cloud
marketplace/billing
```

Also do not ask Codex to:

```text
“build NullForge”
“make the app”
“add the dashboard”
“wire everything together”
```

Future implementation must start from a scoped ticket, not from a broad app-building prompt.

---

## 25. Volume 3 closeout

### Volume 3 decision

```text
PROMOTE_TO_VOLUME_4_AFTER_REVIEW
```

### What Volume 3 promotes

```text
Windows 11 x64 as first platform.
Tauri + React + TypeScript as desktop shell direction.
ResearchCore Engine remains existing internal Python engine.
Strict sidecar / command bridge as MVP strategy.
Workspace-scoped filesystem model.
No arbitrary shell execution.
No full ES.zip in repo.
Packaging spike before feature-heavy desktop build.
```

### What remains unproven

```text
Tauri bridge feasibility on the actual system.
ResearchCore Engine packaging feasibility.
Python sidecar size/stability.
Workspace permission implementation.
Packaged Windows installer behavior.
Artifact metadata bridge behavior.
```

### Next volume

```text
Volume 4 — NullForge Dataset Studio, ES.zip Intake Boundary, Fixture Policy, DatasetCapabilityMap, Timeframe/Chart Capability Rules
```

---

## 26. Prompt for Volume 4

See:

```text
NullForge_Prompt_For_Volume_04_v0_4.md
```
