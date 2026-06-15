> Import note: This file was imported by PF-T001 from `NullForge_Volume_00_v0_4_Package.zip` / `NullForge_Volume_00_v0_4_Package/artifacts/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md` on `2026-06-15`.
> Authority: repo-managed NullForge planning/workflow source after PF-T001 audit. It is not ResearchCore Engine implementation truth.
> Source package SHA256: `48775665EB1F2EBAA00B2FD513F68B3A5152338AC7EAB800319A4E079672D3B3`

# Volume 0 — NullForge North Star, Doctrine, Naming, Claims, MVP Cutline, Anti-Goals

**Version:** v0.4  
**Artifact type:** Project Factory Volume 0  
**Project:** NullForge  
**Existing repo / engine:** `research-core`  
**Internal engine label:** ResearchCore Engine  
**Status:** Draft canonical source, pending repo promotion  
**Implementation status:** No code authorized by this volume  

---

## 1. Volume purpose

This volume defines the active north star for **NullForge** before implementation begins.

It exists to lock the project’s first doctrine layer:

```text
mission
→ first user
→ first pain
→ first proof loop
→ MVP cutline
→ claims
→ fatal assumptions
→ anti-goals
→ source-of-truth rules
→ promotion / repair / archive / quarantine policy
→ reversal conditions
```

This volume does **not** implement the desktop app. It does **not** generate all future volumes. It does **not** authorize a broad “build the app” prompt.

Its job is to make future build work safe enough to plan.

---

## 2. Project thesis

```text
NullForge is a Windows-first local desktop research workbench that helps a solo research builder import market datasets, map lawful dataset capabilities, compile/generate candidate logic into auditable test specs, run the local ResearchCore Engine, inspect visual trade replays, and decide whether evidence should be promoted, repaired, archived, or quarantined.
```

### Short form

```text
NullForge turns candidate research logic and local datasets into auditable test artifacts, visual explanations, and evidence-backed decisions.
```

### Operating sentence

```text
Every candidate starts untrusted.
Every dataset declares what it can and cannot support.
Every generated idea stays quarantined until compiled.
Every visual replay is explanation, not proof.
Every promotion requires evidence.
```

---

## 3. Working name and naming boundary

## 3.1 Working product name

```text
NullForge
```

NullForge is the working user-facing product name for the desktop app.

The name fits the project doctrine because the product is built around:

```text
nulls
baselines
ablations
evidence gates
claim discipline
promotion only after survival
```

## 3.2 Naming map

| Layer | Name |
|---|---|
| User-facing product | **NullForge** |
| Main product surface | **NullForge Workbench** |
| Existing repo | `research-core` |
| Internal engine label | **ResearchCore Engine** |
| First workspace label | `NullForge_Workspace/` |

## 3.3 Naming boundary

The product name is promoted for planning, but not yet promoted for public release.

```text
NullForge = active working name.
research-core = existing repo and engine identity.
ResearchCore Engine = internal technical engine label.
```

Do **not** rename the existing GitHub repo yet.

Do **not** publish, package publicly, buy domains, create a company identity, or distribute under NullForge until a name availability / conflict check is completed.

## 3.4 Naming status

| Name | Status | Notes |
|---|---:|---|
| NullForge | `ACTIVE_WORKING_NAME` | Use in project docs and planning. |
| ResearchCore Engine | `ACTIVE_INTERNAL_ENGINE_LABEL` | Use for engine boundary docs. |
| research-core | `ACTIVE_REPO_NAME` | Existing repo remains intact. |
| ResearchCore Workbench | `SUPERSEDED_DESIGN_MEMORY` | Old user-facing name; keep only as history. |
| Crucible Workbench | `SUPERSEDED_DESIGN_MEMORY` | Earlier candidate; not active. |

---

## 4. Product identity

NullForge is a **local-first desktop research workbench**.

It is not primarily a trading app, a SaaS app, or an AI strategy generator. It is a controlled environment for taking research ideas through a stricter evidence pipeline.

## 4.1 Product frame

```text
Input:
- local market datasets
- candidate logic ideas
- generated variants
- nulls / ablations
- ResearchCore Engine commands

Process:
- dataset capability mapping
- logic compilation
- test-plan generation
- engine execution
- artifact inspection
- visual replay
- evidence card creation
- audit decision

Output:
- explicit specs
- test artifacts
- visual examples
- aggregate evidence
- null/baseline comparisons
- promote / repair / archive / quarantine decisions
```

## 4.2 Product principles

| Principle | Meaning |
|---|---|
| Local-first | The first useful app runs on the user’s Windows machine against local data and local artifacts. |
| Evidence-first | Claims do not become operating assumptions until tested. |
| Dataset-honest | The app must say what the uploaded data can and cannot support. |
| Compiler-before-generator | Generated logic cannot outrun a deterministic specification boundary. |
| Visuals-explain-only | A chart explains a case; it does not prove a system. |
| Sidecar-not-rewrite | NullForge wraps the existing ResearchCore Engine rather than replacing it. |
| Human-gated | Release, merge, promotion, dependency, security, and naming decisions require human gates. |

---

## 5. First user

## 5.1 Primary user

```text
Solo AI-assisted market research builder testing candidate trading/research logic on local OHLCV datasets.
```

In the first phase, the primary user is effectively the project owner / builder.

## 5.2 User description

The first user:

```text
- has local market data;
- creates or collects candidate research ideas;
- wants to test those ideas without fooling themselves;
- uses AI help but does not want AI-generated mush;
- cares about nulls, baselines, ablations, and audit trails;
- is comfortable with technical concepts but wants a usable desktop cockpit;
- wants visual examples to understand systems;
- needs file/dataset handling to be less scattered;
- wants the ResearchCore Engine to become usable without living in terminal outputs forever.
```

## 5.3 Non-first users

The first user is **not**:

```text
- a retail trader looking for live signals;
- a fund running production execution;
- a multi-user research team;
- a nontechnical consumer;
- a mobile-first user;
- a SaaS customer;
- a broker integration user;
- someone seeking financial advice.
```

These users may matter later, but they do not define the MVP.

---

## 6. First pain / problem

## 6.1 Current painful state

The current workflow is powerful but scattered:

```text
candidate ideas live in chat, notes, scripts, or memory;
datasets live as local files with unclear capability boundaries;
tests produce artifacts that require manual inspection;
visual examples are not consistently tied to evidence;
nulls and ablations are easy to forget or separate from the candidate;
ResearchCore Engine outputs are real but not yet exposed through a cohesive desktop experience;
AI-assisted logic generation risks producing plausible nonsense unless quarantined and compiled;
project planning can drift if chat output becomes hidden source of truth.
```

## 6.2 Pain statement

```text
The user has enough research machinery to generate artifacts, but not yet a governed desktop cockpit that turns data, logic, tests, visuals, evidence, and decisions into one coherent local workflow.
```

## 6.3 Why this matters

Without NullForge, the project risks:

```text
- evidence scattered across folders;
- visual examples becoming cherry-picked proof;
- generated ideas becoming trusted too early;
- impossible dataset transformations sneaking into tests;
- terminal workflows blocking usability;
- Codex implementation drifting without source-of-truth docs;
- research outputs accumulating without promotion/archive discipline.
```

---

## 7. Desired transformation

## 7.1 Before

```text
The user has local datasets, candidate ideas, research scripts, CLI outputs, visual curiosity, and evidence artifacts spread across tools and chats.
```

## 7.2 After

```text
The user opens NullForge, selects a local workspace, imports or selects a dataset, sees what the dataset can lawfully support, compiles candidate logic into test-ready specs, runs the ResearchCore Engine, reviews artifacts, inspects visual replay examples, and records an evidence-backed decision.
```

## 7.3 Transformation map

| Before | NullForge mechanism | After |
|---|---|---|
| Dataset is a file blob | Dataset Studio + manifest | Dataset has identity, schema, capability map, and warnings |
| Candidate is a vague idea | Logic Factory + compiler | Candidate becomes explicit, auditable, and testable |
| Generated variants are risky | Quarantine + compiler gate | Generated logic must earn test eligibility |
| Test artifacts are scattered | Workbench artifact browser | Runs and outputs become navigable |
| Charts are persuasive | Visual Replay trust boundary | Charts explain examples and disclose ambiguity |
| Performance summaries can fool | Evidence Cards | Aggregate evidence, nulls, ablations, and decisions stay linked |
| Chat becomes hidden truth | Source-of-truth doctrine | Repo docs govern; chat becomes scratch unless promoted |

---

## 8. First proof loop

The first proof loop is intentionally narrow.

```text
User opens a Windows 11 x64 desktop app
→ creates/selects a local workspace
→ imports or uses a small ES-derived OHLCV fixture
→ sees a DatasetCapabilityMap
→ runs one ResearchCore Engine smoke command through the desktop bridge
→ views produced artifact metadata
→ opens one visual replay fixture with signal/entry/SL/TP/exit labels
→ sees an audit/decision placeholder.
```

## 8.1 What this proves

The first proof loop tests whether:

```text
- NullForge can exist as a real desktop app, not just a static mockup;
- Tauri can serve as the Windows desktop shell;
- the desktop shell can communicate with the ResearchCore Engine;
- local workspace state can be created and selected;
- a dataset can be represented with a capability map;
- artifact metadata can be shown in the app;
- a visual replay surface can render a governed example;
- the audit/decision layer can be visible from the beginning.
```

## 8.2 What this does not prove

The first proof loop does **not** prove:

```text
- that any trading strategy works;
- that a candidate has edge;
- that users will pay;
- that retention exists;
- that cross-platform packaging is solved;
- that full 10-year datasets are performant;
- that generated logic is useful;
- that public release is safe;
- that NullForge is a legally available public brand.
```

---

## 9. MVP cutline

## 9.1 MVP type

```text
Usable technical prototype / narrow local desktop MVP.
```

This MVP is a test instrument. It exists to test the highest-risk technical/product workflow claim:

```text
Can NullForge become a real local Windows desktop workbench that controls the ResearchCore Engine and presents data/artifact/replay/evidence workflow coherently?
```

## 9.2 Included in MVP

| Included feature | Why included | Claim tested |
|---|---|---|
| Windows desktop launch | Proves product form. | `NF-C004`, `NF-C005` |
| Tauri shell | Tests chosen desktop stack. | `NF-C005` |
| Local workspace create/select | Establishes local-first state. | `NF-C006` |
| Tiny/small ES-derived fixture | Tests real data shape without bloat. | `NF-C007`, `NF-C008` |
| DatasetCapabilityMap display | Tests dataset-honesty layer. | `NF-C009` |
| ResearchCore Engine bridge smoke | Tests highest-risk integration boundary. | `NF-C010` |
| Artifact metadata viewer | Tests cockpit value over raw files. | `NF-C011` |
| Visual replay fixture | Tests chart/explanation surface. | `NF-C012` |
| Audit/decision placeholder | Keeps evidence loop visible. | `NF-C013` |

## 9.3 Excluded from MVP

| Excluded | Why excluded | Reconsider when |
|---|---|---|
| Live trading | High risk and outside first proof. | Only after separate product/legal/risk track. |
| Broker integration | Not needed for research cockpit proof. | Only after strong research workflow evidence. |
| Cloud sync | Violates local-first MVP simplicity. | Multi-device/collaboration need is proven. |
| Accounts/auth | Not needed for single-user local app. | Multi-user or cloud features are promoted. |
| Billing | Premature. | Distribution/business claims become active. |
| Mobile app | Not part of first user workflow. | Clear mobile-specific use case appears. |
| Marketplace | Unrelated to first proof. | Never unless a new product thesis justifies it. |
| AI-generated executable strategy core | Too dangerous before compiler/audit boundary. | Compiler, quarantine, and evidence system are proven. |
| Full optimizer/generator | Too much before bridge + compiler proof. | Logic compiler MVP passes. |
| Full 10-year ES.zip committed to repo | Data bloat/licensing/source risk. | Never by default; local workspace only. |
| Public release under NullForge | Name/legal availability not verified. | Brand/release review passes. |

## 9.4 MVP success threshold

The MVP is successful enough to promote to the next build phase if:

```text
- app launches on Windows 11 x64;
- user can create/select a local workspace;
- fixture dataset appears with a clear capability map;
- app successfully invokes one ResearchCore Engine smoke operation;
- produced artifact metadata is visible;
- visual replay fixture renders labels for signal/entry/SL/TP/exit;
- ambiguity/explanation caveat is visible;
- audit/decision placeholder exists;
- no broad scope, cloud, auth, trading, or AI execution features sneak in;
- the source-of-truth docs and decision ledger are updated.
```

## 9.5 MVP failure threshold

Repair or pivot if:

```text
- Tauri cannot reliably call the ResearchCore Engine;
- Python sidecar packaging blocks the MVP beyond reasonable repair;
- local workspace state becomes confusing or unsafe;
- dataset capability mapping cannot be represented clearly;
- visual replay creates misleading proof pressure;
- implementation requires broad engine rewrites before the bridge is proven;
- the MVP cannot be run by the first user on Windows 11 x64.
```

Kill the current desktop-stack path, not necessarily the project, if:

```text
- the Tauri + Python sidecar strategy is repeatedly blocked;
- Electron or native Python UI becomes clearly superior after spike;
- Windows packaging cannot be made usable enough for the first user.
```

---

## 10. What NullForge is

NullForge is:

```text
- a Windows-first local desktop research workbench;
- a governed shell around the existing ResearchCore Engine;
- a dataset intake and capability mapping tool;
- a logic factory with compiler gates;
- a local artifact cockpit;
- a visual replay viewer for examples;
- an evidence card and decision ledger surface;
- a way to make research workflows inspectable, repeatable, and auditable.
```

## 10.1 Core surfaces

| Surface | Purpose |
|---|---|
| Lab Cockpit | Shows workspace status, latest datasets, runs, warnings, evidence, and next action. |
| Dataset Studio | Imports files, maps schema, slices fixtures, and produces DatasetCapabilityMaps. |
| Logic Factory | Captures candidate ideas and turns them into explicit logic cards/specs. |
| Compiler Gate | Validates logic structure before it can become test-ready. |
| Engine Runner | Invokes ResearchCore Engine commands through a governed bridge. |
| Artifact Browser | Lets the user inspect manifests, metadata, reports, and output paths. |
| Visual Replay | Shows concrete examples with signal/entry/SL/TP/exit/ambiguity labels. |
| Evidence Cards | Summarizes aggregate evidence, nulls, ablations, failures, and decisions. |
| Decision Ledger | Records promote/repair/archive/quarantine decisions and reversals. |

---

## 11. What NullForge is not

NullForge is not:

```text
- a live trading system;
- a broker execution terminal;
- a signal-selling tool;
- a financial advice product;
- a SaaS platform;
- a cloud data warehouse;
- a mobile app;
- a marketplace;
- an AI oracle;
- a magic strategy generator;
- a public brand until name review passes;
- a replacement for the ResearchCore Engine;
- a reason to trust a candidate before evidence exists.
```

---

## 12. Core doctrine

## 12.1 Source doctrine

```text
Repo is source of truth.
Vault is design memory.
Graphify is context/navigation.
Chat is scratch unless promoted.
Archive is memory without authority.
Quarantine is unresolved material without governance power.
```

## 12.2 Research doctrine

```text
Generated logic is not evidence.
Visual replay explains examples; aggregate evidence decides.
DatasetCapabilityMap gates chart/timeframe/test claims.
Compiler before generator.
Nulls and baselines before belief.
Ablations before promotion.
Evidence before roadmap authority.
```

## 12.3 Build doctrine

```text
Blueprint before implementation.
Ticket before branch.
Acceptance before code.
Tests before audit pass.
Audit before merge.
Human approval before release.
No broad “build the app” prompts.
No role grades its own work.
```

## 12.4 AI doctrine

```text
AI may assist drafting, planning, summarizing, or proposing.
AI output is draft until promoted.
AI-generated candidate logic is quarantined until compiled.
AI cannot promote claims.
AI cannot bypass null tests, ablations, audit, or human gates.
AI cannot become the product owner.
```

## 12.5 Dataset doctrine

```text
Dataset first, capability second, testing third.
No data capability may be implied without source support.
5m OHLCV can aggregate upward; it cannot reconstruct true 1m or tick path.
OHLC bars cannot prove exact intrabar SL/TP order without lower-resolution path evidence.
Missing timezone or session rules block session-dependent claims until resolved.
Bad data enters quarantine, not the test pipeline.
```

## 12.6 Visual doctrine

```text
Charts are explanatory witnesses, not judges.
Every replay must show what was known at signal time.
Future-only outcomes must be labeled as future.
Ambiguous intrabar paths must be labeled.
Replay examples must connect back to aggregate evidence, nulls, ablations, and sample size.
```

---

## 13. App Forge readiness summary

| Readiness item | Verdict | Notes |
|---|---:|---|
| Mission sentence | `PASS` | Clear enough for canonical docs. |
| First user/use case | `PASS` | Solo AI-assisted market research builder. |
| Problem/pain | `PASS` | Scattered research, data, tests, visuals, evidence, and decisions. |
| Reality/access dependencies | `PARTIAL/PASS` | Windows, Tauri, ResearchCore Engine, ES data, local filesystem known; formal map still needed. |
| Claim ledger | `PARTIAL` | This volume seeds it; tests still needed. |
| MVP proof loop | `PASS` | Concrete local desktop workflow. |
| Anti-goals | `PASS` | Clear not-now list. |
| Validation/audit plan | `PARTIAL` | General doctrine set; detailed experiments/gates later. |
| Reason for Project Factory | `PASS` | Repo, desktop packaging, engine sidecar, data handling, compiler, replay, evidence, Codex loop. |

## 13.1 Phase decision

```text
APP_FORGE_READY_FOR_PROJECT_FACTORY
→ PROJECT_FACTORY_SETUP
→ VOLUME_GENERATION
```

## 13.2 Current readiness verdict

```text
READY_TO_GENERATE_VOLUME_1_AFTER_VOLUME_0_PROMOTION
```

Not ready for implementation.

---

## 14. Claim ledger seed

Status meanings:

```text
UNTESTED = no useful evidence yet.
WEAK_SIGNAL = opinion/anecdote/weak behavior.
SUPPORTED = meaningful use/test evidence supports it.
CONTRADICTED = evidence pushes against it.
KILLED = kill condition met.
DEFERRED = real but not needed now.
PROMOTED = accepted as next-phase operating assumption after evidence.
```

| ID | Type | Claim | Why it matters | Evidence we have | Evidence needed | Cheapest test | Kill condition | Status |
|---|---|---|---|---|---|---|---|---|
| `NF-C001` | user claim | A solo research builder is a valid first user for NullForge. | Defines first workflow and MVP. | User intent and existing research-core work. | Actual use of MVP loop. | User runs MVP on own machine. | User cannot or will not use local workflow after app exists. | `UNTESTED` |
| `NF-C002` | pain claim | Research workflow pain is caused by scattered datasets, candidates, CLI outputs, visuals, and evidence. | Justifies cockpit. | Observed planning context. | Usage friction log. | Document current workflow pain during first MVP use. | Existing CLI/files are already good enough. | `UNTESTED` |
| `NF-C003` | workflow claim | A desktop cockpit improves research clarity over terminal/artifact-only workflow. | Core product value. | Hypothesis. | Task completion comparison. | Compare task with/without NullForge shell. | Desktop adds friction without clarity. | `UNTESTED` |
| `NF-C004` | product claim | A downloadable Windows app is the right product form for first use. | Drives stack and packaging. | User preference. | Working installed app usage. | Windows-first launch test. | User still prefers terminal/web after trying app. | `UNTESTED` |
| `NF-C005` | technical claim | Tauri + React/TypeScript can provide a strong enough desktop shell. | Stack feasibility. | Stack choice. | Tauri shell + bridge smoke. | Packaging spike. | Tauri cannot support needed local workflow. | `UNTESTED` |
| `NF-C006` | technical claim | ResearchCore Engine can be invoked reliably as a Python sidecar / command bridge. | Highest-risk integration. | Existing engine exists. | Bridge smoke across Windows. | One command invoked from app. | Sidecar packaging/invocation is unstable. | `UNTESTED` |
| `NF-C007` | data claim | ES-derived OHLCV fixtures can support the first Dataset Studio proof. | First data path. | User has ES.zip. | Fixture manifest + import test. | Slice tiny fixture locally. | Data cannot be parsed or used safely. | `UNTESTED` |
| `NF-C008` | data claim | Full 10-year ES.zip can remain outside repo while small fixtures support tests. | Prevents bloat/leakage. | Design decision. | Repo hygiene audit. | Create fixture policy. | Full data must be committed for tests to pass. | `UNTESTED` |
| `NF-C009` | data/workflow claim | DatasetCapabilityMap prevents unlawful chart/timeframe/test assumptions. | Protects validity. | Doctrine. | User sees and understands capability statuses. | Generate DCM for 5m OHLCV. | Users ignore or misunderstand capability warnings. | `UNTESTED` |
| `NF-C010` | research claim | Logic must be compiled before generated variants can be trusted. | Prevents AI/idea mush. | Doctrine. | Compiler contract dry run. | Handwrite one LogicCard and compile spec. | Compiler boundary is too rigid or useless. | `UNTESTED` |
| `NF-C011` | workflow claim | Nulls, baselines, and ablations should be first-class candidate companions. | Prevents fake edge. | Existing validation doctrine. | Evidence Card includes them. | One evidence placeholder with null fields. | Nulls/ablations are too cumbersome to use. | `UNTESTED` |
| `NF-C012` | UX/trust claim | Visual Replay helps understand candidate behavior without replacing evidence. | Important UI surface. | User requested replay examples. | Replay use + comprehension check. | Render one fixture and ask what it proves/doesn’t prove. | Replay creates overconfidence or confusion. | `UNTESTED` |
| `NF-C013` | evidence claim | Evidence Cards can keep aggregate results, nulls, ablations, and decisions together. | Avoids scattered conclusions. | Planning hypothesis. | Evidence Card fixture. | Create one placeholder linked to artifact metadata. | Evidence Card adds clutter without clarity. | `UNTESTED` |
| `NF-C014` | source-of-truth claim | Repo-governed docs prevent chat/context soup from corrupting implementation. | Essential for Codex loop. | Forge doctrine. | Source audit after first milestone. | Generate Volume 1 and enforce locations. | Docs drift immediately or are ignored. | `UNTESTED` |
| `NF-C015` | QA/workflow claim | Context-curator → planner → implementor → auditor loop can keep Codex scoped. | Enables safe implementation. | Role-loop source exists. | First docs milestone through loop. | Execute first milestone with artifacts. | Codex keeps broadening or skipping audit. | `UNTESTED` |
| `NF-C016` | safety claim | Deferring live trading/broker integration materially reduces early risk. | Keeps MVP safe and narrow. | Anti-goal decision. | Scope audit. | Verify no broker/live code in MVP. | MVP requires broker/live flow to be meaningful. | `UNTESTED` |

---

## 15. Fatal claims and kill conditions

Fatal claims do not necessarily kill the whole project. Some kill the current path, stack, or MVP shape.

| Fatal ID | Related claim | Why fatal | Cheapest test | Kill / repair threshold |
|---|---|---|---|---|
| `F001` | `NF-C006` | If the desktop app cannot reliably invoke the ResearchCore Engine, the core bridge fails. | Tauri → engine smoke. | Kill/replace sidecar strategy if repeated bridge spike fails. |
| `F002` | `NF-C005` | If Tauri cannot support the local desktop workflow, the chosen stack is wrong. | Minimal Windows shell + file access + command call. | Pivot to Electron or PySide if Tauri blocks basic MVP. |
| `F003` | `NF-C009` | If dataset capabilities cannot be represented clearly, the app may enable invalid tests. | DCM display for 5m OHLCV. | Repair DCM before any chart/test generation. |
| `F004` | `NF-C010` | If logic cannot be made explicit/compilable, generated logic will become mush. | One hand-written LogicCard compile dry run. | Return to Logic Factory design before generator. |
| `F005` | `NF-C012` | If visual replay creates false confidence, it harms research truth. | Replay comprehension/audit check. | Hide/defer replay until evidence links and warnings are stronger. |
| `F006` | `NF-C014` | If source-of-truth docs are ignored, Codex/project drift returns. | First milestone source audit. | Stop implementation and repair docs/workflow. |
| `F007` | `NF-C008` | If the data policy requires committing full private/raw data, repo hygiene fails. | Fixture policy + repo audit. | Full raw ES.zip must stay outside repo or project pauses. |
| `F008` | `NF-C016` | If live trading pressure enters MVP, risk scope changes completely. | Scope audit. | Quarantine broker/live features and repair roadmap. |

---

## 16. Risk register seed

| Risk ID | Risk | Type | Severity | Likelihood | Detection test | Mitigation | Status |
|---|---|---|---:|---:|---|---|---|
| `R001` | Python sidecar packaging fails or becomes fragile on Windows. | technical | High | Medium | Desktop bridge spike | Keep sidecar contract narrow; consider Electron/PySide fallback. | `OPEN` |
| `R002` | Tauri integration requires unexpected Rust/permissions complexity. | technical | Medium/High | Medium | Tauri shell spike | Document bridge boundary; isolate risk early. | `OPEN` |
| `R003` | Full ES.zip bloats repo or leaks licensed/private data. | data/source | High | Medium | Repo audit | Keep full data local; fixtures only if safe. | `OPEN` |
| `R004` | DatasetCapabilityMap is too abstract for the user. | UX/data | Medium | Medium | DCM fixture review | Use concrete YES/NO/AMBIGUOUS examples. | `OPEN` |
| `R005` | Visual replay makes cherry-picked examples emotionally persuasive. | trust/safety | High | High | Replay audit | Link to aggregate evidence/nulls/ablations; include random/failure examples later. | `OPEN` |
| `R006` | Logic Factory becomes overcomplicated before first compiler proof. | product/scope | Medium/High | Medium | Compiler contract review | Handwritten candidate first; generator later. | `OPEN` |
| `R007` | AI-generated candidates become trusted before evidence. | AI/trust | High | Medium | Quarantine audit | Generated logic status defaults to quarantine. | `OPEN` |
| `R008` | Existing ResearchCore docs/package framing conflict with new app plan. | source/drift | Medium | Medium | Repo/source inventory | Archive/demote old framing; create current status doc. | `OPEN` |
| `R009` | Codex modifies engine internals to satisfy UI needs. | implementation/scope | High | Medium | Ticket audit | Bridge contract; forbidden files; human gate for engine changes. | `OPEN` |
| `R010` | Tests are skipped because desktop packaging is annoying. | QA | High | Medium | Ticket closeout | Require smoke tests or explicit skip reason. | `OPEN` |
| `R011` | Name conflict makes NullForge unsuitable publicly. | legal/brand | Medium | Medium | Name availability check | Working name only until review. | `OPEN` |
| `R012` | User confuses research artifact with financial advice/trading signal. | legal/safety | High | Medium | UX copy audit | Explicit non-advice, no-live-trading, evidence-only framing. | `OPEN` |
| `R013` | Workspace file permissions or deletion behavior risks user data. | data/security | High | Medium | Workspace spec + destructive action review | No destructive actions in MVP; confirm paths. | `OPEN` |
| `R014` | App becomes a feature soup before first bridge proof. | scope | High | Medium | Milestone audit | MVP cutline; no broad build prompt. | `OPEN` |
| `R015` | Large local datasets make UI sluggish. | performance | Medium | Medium | Fixture and later scale tests | Start tiny; index/cache later. | `OPEN` |
| `R016` | Generated chart/timeframe types exceed data support. | data/validity | High | Medium | DCM capability tests | DCM gate before chart generation. | `OPEN` |

---

## 17. Anti-goals and deferred items

## 17.1 Hard anti-goals for MVP

```text
No SaaS.
No cloud sync.
No auth/accounts for MVP.
No billing.
No mobile app.
No marketplace.
No broker/live trading integration.
No live order execution.
No AI-generated executable strategy core.
No public distribution under NullForge until name availability/legal conflict check.
No full 10-year ES.zip committed to repo.
No broad feature soup.
```

## 17.2 Deferred items

| Deferred item | Why deferred | Reconsider when |
|---|---|---|
| SQLite cache/index | Filesystem-first proof comes first. | Artifact/dataset browsing needs speed. |
| Full dataset performance mode | First proof uses fixtures. | Bridge + DCM MVP passes. |
| Rich strategy generator | Compiler must exist first. | Logic compiler and quarantine pass. |
| AI proposer | Generated logic policy must exist first. | AI boundary and eval plan exists. |
| Cross-platform builds | Windows-first chosen. | Windows MVP succeeds. |
| Installer signing/updater | Distribution later. | Public release planning begins. |
| User accounts | Local single-user app first. | Collaboration/cloud features are promoted. |
| Broker integrations | Not a research cockpit requirement. | Separate product/legal/risk pass. |
| Paid product / licensing | No validation yet. | Retention/payment/business claims become active. |

---

## 18. Source-of-truth rules

## 18.1 Authority map

```text
Repo = executable truth + current docs
Vault = design memory
Graphify = context/navigation
Chat = scratch unless promoted
Archive = memory without authority
Quarantine = unresolved/conflicting/risky material without governance power
```

## 18.2 Canonical locations to define in Volume 1

| Object | Proposed canonical location | Status after Volume 0 |
|---|---|---|
| Mission | `docs/MISSION_BRIEF.md` and `docs/blueprint/volumes/VOLUME_00...md` | Needs repo promotion |
| Current status | `docs/CURRENT_STATUS.md` | Missing / to create |
| Claim ledger | `docs/CLAIM_LEDGER.md` | Seeded here; needs canonical copy |
| Risk register | `docs/RISK_REGISTER.md` | Seeded here; needs canonical copy |
| Decision ledger | `docs/DECISION_LEDGER.md` and `docs/adr/` | Needs creation |
| MVP cutline | `docs/MVP_CUTLINE.md` or Volume 0 | Seeded here |
| Roadmap | `docs/ROADMAP.md` | Later volume/tickets |
| Volume docs | `docs/blueprint/volumes/` | Volume 0 starts here |
| Prompts | `prompts/` with archive by ticket/volume | Prompt file should be saved |
| Plans | `plans/` | Not used until Codex tickets |
| Reports | `reports/` | Not used until Codex tickets |
| Audits | `audits/` | Not used until Codex tickets |
| Archive | `docs/ARCHIVE/` | Needs policy |
| Quarantine | `docs/QUARANTINE/` or workspace equivalent | Needs policy |

## 18.3 Promotion rule for chat artifacts

Chat output becomes source of truth only if:

```text
- saved into a canonical repo doc;
- assigned status;
- reviewed for conflicts;
- linked to claims/decisions where relevant;
- not contradicted by newer promoted docs;
- accepted through a human gate or audit gate.
```

## 18.4 Old prompt rule

Old prompts are not source truth. They are generation history.

They should be stored in:

```text
prompts/ARCHIVE/
```

or under the specific volume/ticket that used them.

## 18.5 Generated output rule

AI or Codex output is not truth until accepted through audit.

```text
AI output → draft
Draft → review
Review → promote / repair / archive / quarantine
```

---

## 19. Promotion / repair / archive / quarantine policy

## 19.1 Status taxonomy

| Status | Meaning | Authority |
|---|---|---|
| `RAW` | Captured but unstructured. | None |
| `DRAFT` | Structured but not accepted. | Low |
| `ACTIVE` | Current working object. | Can guide current planning |
| `TESTING` | Under test. | Limited to test scope |
| `SUPPORTED` | Evidence supports it. | Can influence roadmap |
| `PROMOTED` | Accepted as next-phase input. | Active authority until reversed |
| `REPAIR` | Direction kept but defects/missing evidence exist. | No promotion yet |
| `PIVOT` | Direction changes using learning. | Old path loses authority |
| `QUARANTINE` | Risky, conflicting, or untrusted. | No governance power |
| `ARCHIVE` | Preserved history. | No active authority |
| `KILLED` | Kill condition met. | Do not revive without new evidence |
| `DEFERRED` | Real but not now. | Not active |

## 19.2 Promotion policy

Promote an object only when:

```text
- it has an artifact;
- its status is explicit;
- its evidence or rationale is recorded;
- it matches the current mission;
- it does not violate anti-goals;
- risks and reversal conditions are recorded;
- the next action is clearer after promotion.
```

## 19.3 Repair policy

Repair when:

```text
- direction is still valid;
- artifact exists but is incomplete or inconsistent;
- evidence is promising but insufficient;
- scope drift occurred but can be corrected;
- source-of-truth conflict can be resolved without pivot.
```

## 19.4 Archive policy

Archive:

```text
- superseded names;
- static mockups not used as current spec;
- old prompts;
- stale setup drafts;
- outdated ticket names;
- discarded architecture options;
- previous chat outputs not promoted;
- failed or dead-end plans.
```

Archive preserves memory without authority.

## 19.5 Quarantine policy

Quarantine:

```text
- generated candidate logic;
- unverified AI outputs;
- uncertain dataset sources;
- unclear legal/privacy material;
- possible brand conflicts;
- claims with conflicting evidence;
- chart/timeframe transformations not supported by data;
- anything exciting but dangerous to the current MVP scope.
```

Quarantine has no governance power.

## 19.6 Kill policy

Kill a path when:

```text
- a fatal claim fails;
- a required access dependency is impossible or unsafe;
- the MVP cannot test the intended claim;
- the stack blocks the first proof loop after repair attempts;
- scope expands until the project no longer matches the mission;
- evidence shows the workflow is not useful to the first user.
```

---

## 20. Reversal conditions for major decisions

| Decision | Current choice | Reversal condition |
|---|---|---|
| Product name | NullForge as working name | Reverse before public release if name conflict/legal/brand risk is meaningful. |
| Existing repo identity | Keep `research-core` as repo/engine | Reverse only if app/engine split becomes impossible to communicate or maintain. |
| First platform | Windows 11 x64 | Add or switch platform only after Windows MVP proof or if Windows blocks first user. |
| Desktop stack | Tauri + React/TypeScript | Reverse if Tauri cannot support file access, sidecar bridge, packaging, or dev velocity. |
| Engine strategy | ResearchCore Engine as Python sidecar / command bridge | Reverse if sidecar bridge fails repeatedly or requires worse complexity than engine API alternative. |
| Data posture | Full ES.zip stays local/outside repo | Reverse only if legal/license-safe small sample policy requires repo fixture; never commit full raw data by default. |
| Local-first | No cloud/auth for MVP | Reverse only if first proof loop cannot work locally, which is unlikely. |
| Compiler-before-generator | Logic must compile before generated variants are test-eligible | Reverse only if compiler design is proven too rigid and repaired with a better explicit contract. |
| Visual replay boundary | Replay explains; evidence decides | Reverse only if replay can be proven safe and still linked to evidence; never make replay proof by itself. |
| No live trading | No broker/live execution in MVP | Reverse only through separate App Forge/legal/risk/Product Factory pass. |
| No broad Codex prompt | Ticket/role-loop only | Reverse never for implementation. Broad prompts may be used only for brainstorming, not repo changes. |

---

## 21. Volume 0 closeout

## 21.1 What this volume promotes

```text
NullForge as working product name.
Windows 11 x64 as first platform.
Tauri + React/TypeScript as first desktop stack.
ResearchCore Engine as existing internal engine.
Local-first workspace as MVP posture.
Dataset Studio and DatasetCapabilityMap as core tracks.
Logic Factory and compiler boundary as core tracks.
Visual Replay and Evidence Cards as core tracks.
Medium 8-volume Project Factory pattern.
No implementation until Volume 1–2 and bridge contracts exist.
```

## 21.2 What this volume archives or demotes

```text
ResearchCore Workbench as user-facing name → SUPERSEDED_DESIGN_MEMORY.
Crucible Workbench → SUPERSEDED_DESIGN_MEMORY.
Thin local HTML/browser app target → SUPERSEDED.
Static UI mockups → DESIGN_MEMORY, not delivery target.
Unprefixed T000/T001/T002 ticket labels → SUPERSEDED by track prefixes.
```

## 21.3 What remains unresolved

```text
Name availability/legal conflict check.
Exact repo doc layout.
Exact local workspace layout.
Tauri sidecar packaging proof.
Dataset fixture licensing/safety.
DatasetCapabilityMap contract details.
Logic compiler schema.
Visual replay schema and examples.
Evidence Card schema.
Milestone ticket packs.
```

## 21.4 Next artifact

```text
Volume 1 — NullForge Workspace, Repo, Context, Source-of-Truth, Archive, and Quarantine System
```

## 21.5 Volume 0 decision

```text
PROMOTE_TO_VOLUME_1
```

Reason:

```text
The mission, first user, proof loop, MVP cutline, anti-goals, claims, risks, and doctrine are clear enough to define the repo/workspace/source-of-truth system next.
```

---

## 22. Exact next prompt for Volume 1

Save the following as:

```text
NullForge_Prompt_For_Volume_01_v0_4.md
```

````md
# Prompt for Volume 1 — NullForge Workspace, Repo, Context, Source-of-Truth, Archive, and Quarantine System

You are my ForgeIT Project Factory volume writer, source-of-truth librarian, repo/workspace architect, context-curation designer, archive/quarantine policy writer, Codex workflow preparer, and anti-context-soup auditor.

Use the uploaded App Forge + Project Factory + Autonomous Codex Role Loop sources as governing context.

Do not generate implementation code.
Do not generate all volumes.
Do not write Codex implementation tickets yet.
Do not create a broad “build the app” prompt.
Do not treat old chat output as source of truth unless explicitly promoted.
Do not collapse App Forge validation and Project Factory implementation.

## Project

Working product name:

```text
NullForge
```

Existing repo / engine:

```text
research-core
```

Internal engine label:

```text
ResearchCore Engine
```

First platform:

```text
Windows 11 x64
```

Desktop stack:

```text
Tauri + React + TypeScript
```

Engine boundary:

```text
Existing Python ResearchCore Engine as local sidecar / command bridge.
```

Volume 0 decision:

```text
PROMOTE_TO_VOLUME_1
```

Volume 0 summary:

```text
NullForge is a Windows-first local desktop research workbench for importing market datasets, mapping lawful dataset capabilities, compiling/generating candidate logic into auditable specs, running the local ResearchCore Engine, inspecting visual trade replays, and recording promote/repair/archive/quarantine decisions.

The first proof loop is:
User opens a Windows 11 x64 desktop app
→ creates/selects a local workspace
→ imports or uses a small ES-derived OHLCV fixture
→ sees a DatasetCapabilityMap
→ runs one ResearchCore Engine smoke command through the desktop bridge
→ views produced artifact metadata
→ opens one visual replay fixture with signal/entry/SL/TP/exit labels
→ sees an audit/decision placeholder.
```

Core doctrine to preserve:

```text
Repo is source of truth.
Vault is design memory.
Graphify is context/navigation.
Chat is scratch unless promoted.
Archive is memory without authority.
Quarantine is unresolved material without governance power.
Generated logic is not evidence.
Visual replay explains examples; aggregate evidence decides.
DatasetCapabilityMap gates chart/timeframe/test claims.
Compiler before generator.
Evidence before promotion.
Ticket before branch.
Acceptance before code.
Tests before audit pass.
Audit before merge.
Human approval before release.
No broad “build the app” prompts.
No role grades its own work.
```

Known anti-goals:

```text
No SaaS.
No cloud sync.
No auth/accounts for MVP.
No billing.
No mobile app.
No marketplace.
No broker/live trading integration.
No live order execution.
No AI-generated executable strategy core.
No public distribution under NullForge until name availability/legal conflict check.
No full 10-year ES.zip committed to repo.
No broad feature soup.
```

## Mission

Generate Volume 1 only:

```text
Volume 1 — NullForge Workspace, Repo, Context, Source-of-Truth, Archive, and Quarantine System
```

## Required sections

Include:

1. Volume purpose.
2. Relationship to Volume 0.
3. Repo/source-of-truth doctrine.
4. Existing `research-core` repo boundary.
5. Proposed canonical docs map.
6. Proposed repo layout additions without overwriting existing work.
7. Local NullForge workspace layout.
8. Data storage boundary, including ES.zip raw-data policy.
9. Fixture policy.
10. Artifact storage policy.
11. Prompt storage policy.
12. Plans/reports/audits storage policy.
13. Archive policy.
14. Quarantine policy.
15. Context pack types.
16. Minimal active context pack.
17. Codex implementation context pack requirements.
18. Validation context pack requirements.
19. Drift checks.
20. Source promotion rules.
21. Current status document template.
22. Decision ledger / ADR location plan.
23. Human gate triggers for source-of-truth changes.
24. Volume 1 closeout.
25. Exact next prompt for Volume 2.

## Required constraints

Preserve:

```text
Do not overwrite or silently supersede the existing research-core repo.
Do not commit full ES.zip.
Do not treat chat artifacts as active truth unless promoted.
Do not let old prompts govern implementation.
Do not create implementation tickets yet.
Do not generate code.
Do not generate Volume 2.
```

## Response rules

Return Volume 1 as structured Markdown content.
Do not generate Volume 2.
Do not generate implementation code.
Do not create a broad build prompt.
Keep the output detailed enough to become a canonical project source.
End with the exact next prompt for Volume 2.
````
