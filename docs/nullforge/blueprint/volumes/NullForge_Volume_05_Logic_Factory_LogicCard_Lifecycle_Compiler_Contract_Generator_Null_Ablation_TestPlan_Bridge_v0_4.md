> Import note: This file was imported by PF-T001 from `NullForge_Volume_05_v0_4_Package.zip` / `NullForge_Volume_05_v0_4_Package/artifacts/NullForge_Volume_05_Logic_Factory_LogicCard_Lifecycle_Compiler_Contract_Generator_Null_Ablation_TestPlan_Bridge_v0_4.md` on `2026-06-15`.
> Authority: repo-managed NullForge planning/workflow source after PF-T001 audit. It is not ResearchCore Engine implementation truth.
> Source package SHA256: `218387F5177999ED838A6985C35F18EC866C17AB21F957D5BB8557EDDCC17D45`

# Volume 5 — NullForge Logic Factory, LogicCard Lifecycle, Compiler Contract, Generator/Null/Ablation Boundary, and Test-Plan Bridge v0.4

```text
Project: NullForge
Existing repo / engine: research-core
Internal engine label: ResearchCore Engine
First platform: Windows 11 x64
Desktop stack: Tauri + React + TypeScript
Volume status: DRAFT_CANONICAL_SOURCE
Generated for: ForgeIT Project Factory workflow
Implementation status: NO IMPLEMENTATION CODE GENERATED
```

---

## 1. Volume purpose

This volume defines the **Logic Factory** layer for NullForge before implementation begins.

The goal is to make candidate trading/research logic explicit, auditable, compilable, test-plan-ready, and evidence-gated.

Volume 5 answers:

```text
How does a raw idea become a LogicCard?
How does a LogicCard become a CompiledLogicSpec?
What does the compiler check?
What must fail compilation?
How are nulls, ablations, and variants generated without becoming fake evidence?
How does a compiled spec become a ResearchCore Engine TestPlan?
What does NullForge show in the UI at each state?
What must stay quarantined until tested and audited?
```

This volume does **not** define implementation code. It defines contracts, states, boundaries, schemas, failure modes, and gate logic.

---

## 2. Relationship to Volumes 0, 1, 2, 3, and 4

| Prior volume | What it contributes to Volume 5 |
|---|---|
| **Volume 0 — North Star / Doctrine** | Establishes the doctrine that generated logic is not evidence, compiler before generator, evidence before promotion, visual replay explains examples, and DatasetCapabilityMap gates claims. |
| **Volume 1 — Workspace / Source-of-Truth** | Defines where logic drafts, compiled specs, generated variants, nulls, ablations, reports, archives, and quarantine records should live. |
| **Volume 2 — Planner / Implementor / Auditor Loop** | Prevents Codex or any implementation agent from inventing product strategy, generating unbounded logic, skipping acceptance, or grading its own work. |
| **Volume 3 — Desktop / Tauri / Engine Bridge** | Defines how the desktop shell may call the ResearchCore Engine through a scoped bridge rather than arbitrary shell execution. |
| **Volume 4 — Dataset Studio / DatasetCapabilityMap** | Defines the dataset capability gate that must pass before candidate logic can be compiled or tested against a dataset. |

Volume 5 sits between **Dataset Studio** and **Evidence/Replay**:

```text
Dataset Studio
→ DatasetCapabilityMap
→ Logic Factory
→ Compiler
→ Nulls / ablations / variants
→ TestPlan bridge
→ ResearchCore Engine run
→ Evidence Cards
→ Visual Replay
→ Audit decision
```

---

## 3. Logic Factory product role

Logic Factory is the NullForge surface where the user turns candidate research ideas into explicit, testable, auditable logic objects.

It is not a magic strategy generator. It is a disciplined conversion layer:

```text
raw idea / hypothesis / setup / operator / pattern
→ structured LogicCard
→ compiler checks
→ CompiledLogicSpec
→ generated nulls / ablations / bounded variants
→ TestPlan
→ ResearchCore Engine artifacts
→ EvidenceCard
→ promote / repair / archive / quarantine
```

### Logic Factory exists because

| Pain | Logic Factory response |
|---|---|
| Candidate ideas are often vague. | Require LogicCard fields before compilation. |
| Testing can accidentally leak future information. | Compiler enforces timing, known-at, and causality fields. |
| Generated variants can become fake confidence. | Generator output stays quarantined until compiled/tested/audited. |
| Nulls and ablations are often afterthoughts. | Nulls and ablations are first-class outputs. |
| Visual examples can trick the user. | Visual replay is linked to compiled specs and EvidenceCards, not treated as proof. |
| ResearchCore Engine needs runnable structure. | TestPlan bridge translates compiled logic into engine-ready work without arbitrary execution. |

---

## 4. Raw idea vs LogicCard vs CompiledLogicSpec vs TestPlan vs EvidenceCard

| Object | Meaning | Authority | Can run? | Can be promoted? |
|---|---|---:|---:|---:|
| **Raw idea** | A sentence, sketch, intuition, operator idea, or setup description. | None | No | No |
| **LogicCard** | Structured candidate definition with required fields for hypothesis, inputs, timing, rules, exits, and test intent. | Draft authority only | No | No |
| **CompiledLogicSpec** | Compiler-accepted, hashable, causality-checked, dataset-compatible candidate spec. | Test-ready authority | Not directly; via TestPlan | No, compile alone is not evidence |
| **Generated variant** | Bounded mutation of a parent LogicCard or CompiledLogicSpec. | Quarantined until compiled/tested | No until compiled | No |
| **Null spec** | Control spec designed to test whether apparent signal exceeds baseline/random/structural expectations. | Test control authority | Via TestPlan | No; supports or weakens evidence |
| **Ablation spec** | Parent logic with one component removed/neutralized to test what matters. | Test control authority | Via TestPlan | No; supports or weakens evidence |
| **TestPlan** | Engine-ready run plan binding compiled specs, datasets, targets, splits, cost assumptions, and output expectations. | Run authority | Yes, through scoped engine bridge | No |
| **EvidenceCard** | Summary of test results, nulls, ablations, failures, examples, and audit decision. | Evidence summary | No | Can support promotion after audit |

### Core distinction

```text
LogicCard = explicit hypothesis.
CompiledLogicSpec = legal-to-test object.
TestPlan = legal-to-run object.
EvidenceCard = legal-to-decide object.
```

---

## 5. Candidate lifecycle states

### State diagram

```text
RAW_IDEA
  ↓
LOGICCARD_DRAFT
  ↓
READY_FOR_COMPILE
  ↓
COMPILE_RUNNING
  ↓
COMPILE_PASS ───────────────┐
  ↓                         │
COMPILED_SPEC               │
  ↓                         │
NULLS_ABLATIONS_VARIANTS    │
  ↓                         │
TESTPLAN_READY              │
  ↓                         │
QUEUED_FOR_RUN              │
  ↓                         │
RUN_COMPLETE                │
  ↓                         │
EVIDENCE_LINKED             │
  ↓                         │
AUDIT_PENDING               │
  ↓                         │
PROMOTED / REPAIR / ARCHIVE / QUARANTINE / KILLED / CONTINUE_TESTING

Failure branches:
READY_FOR_COMPILE → COMPILE_HOLD / COMPILE_REJECT
COMPILED_SPEC → TESTPLAN_HOLD
QUEUED_FOR_RUN → RUN_FAILED
EVIDENCE_LINKED → AUDIT_HOLD / AUDIT_REJECT
```

### State table

| State | Meaning | Allowed next state | Forbidden action |
|---|---|---|---|
| `RAW_IDEA` | Unstructured thought. | `LOGICCARD_DRAFT` | Testing directly. |
| `LOGICCARD_DRAFT` | Structured but incomplete. | `READY_FOR_COMPILE`, `ARCHIVE`, `QUARANTINE` | Running engine. |
| `READY_FOR_COMPILE` | Required fields complete. | `COMPILE_RUNNING` | Treating as validated. |
| `COMPILE_RUNNING` | Compiler checks active. | `COMPILE_PASS`, `COMPILE_HOLD`, `COMPILE_REJECT` | User edits without version bump. |
| `COMPILE_HOLD` | Missing/ambiguous/repairable issues. | `LOGICCARD_DRAFT`, `READY_FOR_COMPILE` | Run anyway. |
| `COMPILE_REJECT` | Fatal compile violation. | `REPAIR`, `ARCHIVE`, `KILLED` | Test anyway. |
| `COMPILED_SPEC` | Hashable, test-ready spec. | `TESTPLAN_READY`, `NULLS_ABLATIONS_VARIANTS` | Claim market edge. |
| `NULLS_ABLATIONS_VARIANTS` | Controls and bounded variants attached. | `TESTPLAN_READY` | Skip controls silently. |
| `TESTPLAN_READY` | Engine-bound run plan exists. | `QUEUED_FOR_RUN` | Change test after seeing results. |
| `RUN_COMPLETE` | ResearchCore Engine produced artifacts. | `EVIDENCE_LINKED` | Promote without EvidenceCard. |
| `EVIDENCE_LINKED` | Results tied to candidate, controls, datasets, examples. | `AUDIT_PENDING` | Cherry-pick visual examples. |
| `AUDIT_PENDING` | Needs independent audit. | `PROMOTED`, `REPAIR`, `ARCHIVE`, `QUARANTINE`, `KILLED`, `CONTINUE_TESTING` | Self-promotion. |
| `PROMOTED` | Strong enough as next-phase input. | `RETEST`, `SUPERSEDE`, `ARCHIVE` | Treat as permanent truth. |
| `QUARANTINE` | Unresolved/risky/conflicting. | `REPAIR`, `ARCHIVE`, `KILLED` | Govern roadmap. |

---

## 6. LogicCard draft schema

This is a **conceptual schema**, not implementation code.

### LogicCard top-level sections

| Section | Purpose | Required for compile? |
|---|---|---:|
| `identity` | Names, IDs, version, owner, status. | Yes |
| `hypothesis` | Plain-language reason this candidate might matter. | Yes |
| `dataset_requirements` | Required fields, timeframe, session, instrument, capability dependencies. | Yes |
| `feature_inputs` | Inputs used by the signal and when they are known. | Yes |
| `signal_rule` | Boolean or scored rule that creates a signal. | Yes |
| `timing_model` | signal_time, known_at, entry_time, exit horizon or exit rules. | Yes |
| `direction_model` | Long, short, both, neutral, classification, or observation-only. | Yes |
| `risk_model` | Stop, take profit, sizing assumption, ambiguity policy. | Required if trade-like |
| `target_model` | What is being measured and over what horizon. | Yes |
| `filters` | Regime/session/context filters. | Optional but explicit |
| `nulls` | Required null/control families. | Yes for test-ready status |
| `ablations` | Components to remove/neutralize for attribution. | Yes for test-ready status |
| `variant_policy` | Bounded parameter/logic variations allowed. | Optional for first pass |
| `provenance` | Source of idea, notes, parent ID, prompt/manual origin. | Yes |
| `review` | Human notes, warnings, open questions. | Yes |

### LogicCard identity fields

| Field | Meaning | Required |
|---|---|---:|
| `logic_id` | Stable candidate identifier. | Yes |
| `title` | Human-readable name. | Yes |
| `version` | Version of this LogicCard. | Yes |
| `status` | Lifecycle state. | Yes |
| `created_by` | Human, assistant, generator, imported. | Yes |
| `created_at` | Timestamp. | Yes |
| `parent_logic_id` | Parent if generated/derived. | Conditional |
| `source_type` | Manual, AI-assisted draft, imported, generated variant, null, ablation. | Yes |
| `promotion_status` | Draft, quarantined, compiled, tested, promoted, archived, killed. | Yes |

### LogicCard hypothesis fields

| Field | Meaning | Required |
|---|---|---:|
| `hypothesis_text` | Plain-language claim. | Yes |
| `mechanism_claim` | Why the pattern may exist. | Yes |
| `expected_behavior` | What should happen if the claim is true. | Yes |
| `kill_condition` | What would make the idea fail. | Yes |
| `non_claims` | What this candidate does not prove. | Yes |

### LogicCard data fields

| Field | Meaning | Required |
|---|---|---:|
| `dataset_id` | Dataset or dataset class intended for test. | Yes |
| `required_columns` | OHLCV, session, instrument, etc. | Yes |
| `source_timeframe` | Required input timeframe. | Yes |
| `derived_timeframes` | Any requested aggregation. | Conditional |
| `session_requirements` | RTH/ETH/24h/custom session. | Conditional |
| `timezone_requirement` | Required timezone confirmation. | Yes |
| `capability_dependencies` | DatasetCapabilityMap statuses needed. | Yes |
| `unsupported_if` | Conditions that must block compilation. | Yes |

### LogicCard signal fields

| Field | Meaning | Required |
|---|---|---:|
| `feature_definitions` | Inputs, formulas, lookbacks, transformations. | Yes |
| `lookback_windows` | Past-only windows used by features. | Yes |
| `thresholds` | Fixed/trailing/train-only thresholds. | Conditional |
| `signal_rule` | Rule for signal creation. | Yes |
| `signal_type` | Boolean, score, ranking, classification, observation. | Yes |
| `signal_time` | Bar/event when signal is evaluated. | Yes |
| `known_at` | Exact time information is known. | Yes |
| `entry_time` | When simulated entry would occur, if trade-like. | Required if trade-like |
| `direction` | Long/short/both/observe-only. | Yes |

### LogicCard risk / exit fields

| Field | Meaning | Required |
|---|---|---:|
| `exit_rule` | Time exit, signal reversal, SL/TP, first-hit, end-of-session, etc. | Required if trade-like |
| `stop_rule` | Stop-loss definition, if any. | Conditional |
| `take_profit_rule` | Take-profit definition, if any. | Conditional |
| `hold_window` | Max holding period or evaluation horizon. | Conditional |
| `intrabar_policy` | How ambiguous OHLC first-hit cases are handled. | Required if SL/TP on OHLC |
| `cost_model` | Commission/slippage assumptions or placeholder. | Required for trade-like tests |
| `position_model` | One-entry, re-entry, overlapping positions, or observation-only. | Required if trade-like |

### LogicCard provenance fields

| Field | Meaning | Required |
|---|---|---:|
| `idea_source` | Manual note, research report, generated suggestion, prior candidate, etc. | Yes |
| `source_artifact` | Path/link/ref to source artifact if any. | Conditional |
| `author_notes` | Human notes. | Optional |
| `generator_notes` | Required if AI/generated. | Conditional |
| `quarantine_reason` | Required if generated or unresolved. | Conditional |
| `review_required` | Human review required before compile/test. | Yes |

---

## 7. Required fields for a candidate logic card

A LogicCard may not become `READY_FOR_COMPILE` until these fields exist:

```text
logic_id
title
version
status
source_type
hypothesis_text
mechanism_claim
expected_behavior
kill_condition
dataset_id or dataset_class
required_columns
source_timeframe
timezone_requirement
capability_dependencies
feature_definitions
lookback_windows
signal_rule
signal_type
signal_time
known_at
direction
target_model
validation_intent
null_policy
ablation_policy
provenance
review_required
```

For trade-like candidates, also require:

```text
entry_time
exit_rule
hold_window or exit trigger
cost_model
position_model
intrabar_policy
stop_rule, if stop is claimed
take_profit_rule, if take profit is claimed
```

For generated candidates, also require:

```text
parent_logic_id or generation_seed_id
generation_method
generation_bounds
quarantine_reason
human_review_required = true
```

---

## 8. Signal timing and no-leakage rules

### Timing doctrine

```text
Features at time t may use only information available at or before t.
A signal emitted at bar close t cannot enter before the next legal execution time unless explicitly modeled.
Any threshold, scaler, quantile, or ranking must be fixed, trailing, or train-only.
No centered windows.
No future returns as features.
No MFE/MAE, TP/SL outcomes, EOD labels, or holdout statistics as inputs.
No post-hoc test changes after seeing results.
```

### Required timing fields

| Field | Meaning | Example |
|---|---|---|
| `feature_time` | Time index used to compute features. | `bar_close_t` |
| `known_at` | When feature values become known. | `bar_close_t_after_bar_finalized` |
| `signal_time` | When the signal is evaluated. | `bar_close_t` |
| `entry_time` | Earliest modeled action time. | `next_bar_open_t_plus_1` |
| `exit_eligibility_time` | Earliest legal exit evaluation. | `bar_t_plus_1_or_later` |
| `target_window` | Future window being evaluated, never used as input. | `next_18_bars` |
| `training_window` | Past-only / train split window for thresholds. | `prior_N_bars` or `train_split_only` |

### No-leakage rejection examples

| Candidate behavior | Compiler response |
|---|---|
| Uses next-bar return in signal. | `REJECT_FUTURE_LOOKING_INPUT` |
| Uses full-sample quantile for threshold. | `REJECT_FULL_SAMPLE_THRESHOLD` |
| Uses centered moving average. | `REJECT_CENTERED_WINDOW` |
| Uses EOD result as intraday feature. | `REJECT_TARGET_AS_FEATURE` |
| Uses MFE/MAE to decide entry. | `REJECT_OUTCOME_DERIVED_FEATURE` |
| Uses lower timeframe assumption not present in DatasetCapabilityMap. | `HOLD_UNSUPPORTED_DATA_CAPABILITY` |
| Has signal at close but entry at same bar open. | `REJECT_IMPOSSIBLE_EXECUTION_TIME` |

---

## 9. DatasetCapabilityMap dependency rules

Logic Factory cannot compile a LogicCard against a dataset until DatasetCapabilityMap has established what the dataset supports.

### Required dependency checks

| Dependency | Compiler check |
|---|---|
| Required columns | Dataset manifest contains all required columns or declared substitutes. |
| Required timeframe | Source timeframe or lawful derived timeframe exists. |
| Derived timeframe | DatasetCapabilityMap marks derivation as `YES` or accepted `APPROXIMATE`. |
| Timezone | Confirmed or compile holds for confirmation. |
| Session calendar | Confirmed or compile holds for session-sensitive logic. |
| Chart type | Capability status supports requested chart. |
| Intrabar path | Candidate has ambiguity policy if SL/TP first-hit cannot be known. |
| Volume features | Volume exists and passes quality checks. |
| Tick/range/volume bars | Supported only from data that can lawfully produce them. |

### Capability status handling

| DatasetCapabilityMap status | Compiler action |
|---|---|
| `YES` | May compile if all other checks pass. |
| `NO` | Reject or require changing candidate/data. |
| `APPROXIMATE` | Hold unless candidate explicitly accepts approximation and labels limitation. |
| `AMBIGUOUS` | Hold unless ambiguity policy is explicit and safe. |
| `REQUIRES_CONFIRMATION` | Hold until user confirms. |
| `QUARANTINE` | Reject compile for that dataset. |

### ES / OHLCV boundary reminders

```text
5m OHLCV can aggregate upward.
5m OHLCV cannot reconstruct true 1m/tick data.
OHLC bars cannot prove exact intrabar SL/TP first-hit order without lower-timeframe/tick data.
Missing timezone/session information must trigger confirmation or quarantine.
Dataset Studio does not prove strategy validity.
```

---

## 10. Compiler purpose

The compiler is a gatekeeper, not a profitability engine.

Compiler purpose:

```text
Turn explicit LogicCards into hashable, causally valid, dataset-compatible, test-plan-ready CompiledLogicSpecs.
```

Compiler does not decide:

```text
whether the strategy works;
whether the user should trade it;
whether the candidate is profitable;
whether a chart example is impressive;
whether the idea deserves promotion.
```

### Compiler responsibilities

| Responsibility | Description |
|---|---|
| Structure validation | Required fields exist and have valid statuses. |
| Timing validation | known_at, signal_time, entry_time, and exit rules are causal. |
| Data validation | Candidate requirements match DatasetCapabilityMap. |
| Formula validation | Feature and signal definitions are explicit enough to materialize. |
| Bounds validation | Parameters/search/generation are bounded. |
| Risk/exit validation | Stops, TPs, exits, and ambiguity are defined. |
| Control validation | Required nulls and ablations are declared. |
| Provenance validation | Source and generated/quarantine status are recorded. |
| Determinism validation | Spec can be hashed and reproduced. |
| TestPlan readiness | Candidate can be bound into a test plan. |

---

## 11. Compiler validation checks

### Check matrix

| Check | Pass condition | HOLD condition | REJECT condition |
|---|---|---|---|
| Required fields | All required fields present. | Repairable missing optional/review fields. | Missing required timing/data/signal fields. |
| Dataset capability | DCM supports required inputs. | Requires confirmation/ambiguity policy. | DCM says `NO` or `QUARANTINE`. |
| Causality | Inputs are known at/before signal time. | Timing needs clarification. | Future-looking input. |
| Entry timing | Entry is possible after signal. | Entry convention unclear. | Entry before signal/known_at. |
| Exit timing | Exit logic is explicit. | Some exit fields ambiguous. | Exit depends on future outcome. |
| Intrabar ambiguity | Policy explicit. | Needs lower timeframe or conservative mode. | Pretends OHLC first-hit path is known when it is not. |
| Thresholds/scalers | Fixed, trailing, or train-only. | Fit method unclear. | Full-sample/holdout-informed. |
| Parameter bounds | Bounded and declared. | Bounds too wide/unclear. | Unbounded search/optimizer. |
| Nulls | Required nulls declared. | Null family incomplete. | Nulls intentionally bypassed. |
| Ablations | Parent components named. | Attribution plan incomplete. | No ablation where candidate has multiple components. |
| Provenance | Source recorded. | Source vague but recoverable. | Unknown generated origin. |
| ResearchCore bridge | Uses allowed engine command class. | Bridge mapping unresolved. | Requires arbitrary shell execution. |

### Compile output statuses

```text
COMPILE_PASS
COMPILE_HOLD
COMPILE_REJECT
```

A compile pass means:

```text
This candidate is legal to test under the stated constraints.
```

A compile pass does **not** mean:

```text
This candidate works.
This candidate has edge.
This candidate should be traded.
This candidate should be promoted.
```

---

## 12. Compiler failure modes

| Failure code | Severity | Meaning | Repair route |
|---|---:|---|---|
| `MISSING_REQUIRED_FIELD` | HOLD | LogicCard lacks required field. | Fill missing field. |
| `AMBIGUOUS_HYPOTHESIS` | HOLD | Hypothesis not testable. | Rewrite claim/expected behavior. |
| `MISSING_DATASET_BINDING` | HOLD | Dataset/class not declared. | Bind dataset or dataset class. |
| `UNSUPPORTED_DATA_CAPABILITY` | REJECT/HOLD | DCM does not support requested input/chart/timeframe. | Change dataset, transform, or candidate. |
| `TIMEZONE_UNCONFIRMED` | HOLD | Timezone needed but not confirmed. | Confirm timezone/session. |
| `SESSION_UNCONFIRMED` | HOLD | Session-sensitive logic lacks calendar/session confirmation. | Confirm session or remove dependency. |
| `FUTURE_LOOKING_INPUT` | REJECT | Feature uses future outcome/data. | Redesign signal. |
| `TARGET_AS_FEATURE` | REJECT | Candidate uses label/target as input. | Remove target from inputs. |
| `CENTERED_WINDOW` | REJECT | Feature uses future bars via centered window. | Use trailing window. |
| `FULL_SAMPLE_SCALER` | REJECT | Threshold/scaler uses full sample/holdout. | Use train-only/trailing rule. |
| `IMPOSSIBLE_ENTRY_TIME` | REJECT | Entry occurs before signal information is known. | Change entry rule. |
| `AMBIGUOUS_INTRABAR_PATH` | HOLD | SL/TP first-hit path not knowable from data. | Add policy/lower-timeframe data/conservative label. |
| `UNBOUNDED_SEARCH` | REJECT | Candidate asks for unbounded optimization. | Define finite bounds. |
| `NO_NULL_POLICY` | HOLD | No null/control declared. | Add null policy. |
| `NO_ABLATION_POLICY` | HOLD | Multi-component candidate lacks attribution tests. | Add ablations. |
| `ARBITRARY_SHELL_REQUIRED` | REJECT | Requires unsafe engine/OS execution. | Use bridge-approved command. |
| `GENERATED_UNREVIEWED` | HOLD | Generated candidate has not been human-reviewed. | Human review/quarantine decision. |
| `PROVENANCE_MISSING` | HOLD | Source unknown. | Record source or quarantine. |
| `TESTPLAN_INCOMPLETE` | HOLD | Compiled spec cannot bind to run plan. | Complete TestPlan fields. |

---

## 13. CompiledLogicSpec draft

A CompiledLogicSpec is the compiler output. It should be deterministic, hashable, and reproducible.

### Top-level sections

| Section | Purpose |
|---|---|
| `compiled_identity` | ID, version, hash, parent LogicCard ID, compiler version. |
| `compile_context` | DatasetCapabilityMap, dataset manifest, assumptions, warnings. |
| `feature_graph` | Materialized feature dependencies and lookbacks. |
| `signal_graph` | Materialized signal logic. |
| `timing_contract` | known_at, signal_time, entry_time, exit eligibility. |
| `execution_contract` | Direction, position model, costs, exits, SL/TP rules. |
| `target_contract` | What is measured, horizon, labels, metrics. |
| `controls_contract` | Required nulls, ablations, variants. |
| `testplan_requirements` | Required split policy, dataset binding, engine command class. |
| `warnings` | Limitations, approximations, ambiguity labels. |
| `provenance` | Source LogicCard, generated origin, review status. |

### Compiled identity fields

| Field | Meaning |
|---|---|
| `compiled_spec_id` | Stable ID for this compiled object. |
| `logic_id` | Parent LogicCard. |
| `logic_version` | Parent version. |
| `compiler_version` | Compiler contract version. |
| `compiled_at` | Timestamp. |
| `compiled_hash` | Deterministic hash of compile-relevant contents. |
| `compile_status` | `COMPILE_PASS`, `COMPILE_HOLD`, or `COMPILE_REJECT`. |
| `compile_warnings` | Non-blocking issues/limitations. |
| `compile_blockers` | Blocking issues if any. |

### Timing contract fields

| Field | Required? | Notes |
|---|---:|---|
| `known_at` | Yes | Must be at/before signal_time. |
| `signal_time` | Yes | Bar/event where signal is evaluated. |
| `entry_time` | Required if trade-like | Must be legal after signal/known_at. |
| `exit_rule` | Required if trade-like | Must be explicit. |
| `stop_rule` | Conditional | Required if stop is claimed. |
| `take_profit_rule` | Conditional | Required if TP is claimed. |
| `ambiguity_handling` | Conditional | Required for OHLC first-hit ambiguity. |

### Compile warnings are not evidence

Warnings may allow testing with limitations, but the limitations must follow the artifact into the TestPlan, EvidenceCard, and Visual Replay.

---

## 14. TestPlan bridge draft

The TestPlan bridge binds CompiledLogicSpecs to ResearchCore Engine runs.

### TestPlan purpose

```text
Create a run-ready plan that specifies exactly what will be tested, on which dataset, with which controls, over which splits, with which metrics, and where artifacts will be written.
```

### TestPlan sections

| Section | Purpose |
|---|---|
| `testplan_identity` | ID, version, creation time, owner. |
| `compiled_specs` | Candidate, null, ablation, and variant spec IDs. |
| `dataset_binding` | Dataset manifest, DCM ID, fixture/full local path policy. |
| `split_policy` | Train/validation/test/walk-forward or smoke-only. |
| `metrics_policy` | Metrics to compute and what they do not prove. |
| `cost_policy` | Commission/slippage/latency assumptions if trade-like. |
| `execution_policy` | Entry/exit, overlapping positions, ambiguous path policy. |
| `artifact_policy` | Required output manifests/reports/logs. |
| `evidence_policy` | EvidenceCard fields expected after run. |
| `engine_command_class` | Allowed ResearchCore Engine command category. |
| `pre_run_checks` | Assertions before run. |
| `post_run_checks` | Assertions after run. |

### TestPlan required fields

```text
testplan_id
created_at
candidate_compiled_spec_id
control_spec_ids
dataset_manifest_id
dataset_capability_map_id
allowed_engine_command_class
split_policy
metrics_policy
artifact_output_dir
pre_run_checks
post_run_checks
audit_required = true
```

### TestPlan statuses

| Status | Meaning |
|---|---|
| `DRAFT` | Not ready to run. |
| `READY_FOR_REVIEW` | Human/planner review needed. |
| `READY_FOR_RUN` | Can be queued through scoped bridge. |
| `RUNNING` | Engine run active. |
| `RUN_COMPLETE` | Engine artifacts produced. |
| `RUN_FAILED` | Engine run failed. |
| `EVIDENCE_READY` | EvidenceCard can be assembled. |
| `AUDIT_PENDING` | Needs audit decision. |

---

## 15. ResearchCore Engine boundary for logic/testing

NullForge calls ResearchCore Engine through the scoped desktop bridge defined in Volume 3.

### ResearchCore Engine owns

```text
actual data processing;
canonicalization;
feature materialization if supported;
run execution;
validation checks;
artifact writing;
reports/manifests/logs;
existing CLI/test behavior.
```

### NullForge owns

```text
LogicCard creation UI;
compile status display;
compiler contract presentation;
TestPlan assembly UI;
run queue display;
artifact browsing;
EvidenceCard and Visual Replay linkage;
audit decision UX.
```

### Boundary rules

```text
NullForge may request approved engine command classes.
NullForge must not issue arbitrary shell commands.
NullForge must not mutate engine internals to bypass compile checks.
NullForge must not run uncompiled LogicCards.
NullForge must not treat engine output as promoted evidence without EvidenceCard + audit.
ResearchCore Engine artifacts remain canonical run output.
```

### First proof allowed command class

For MVP planning, the first allowed command class should be:

```text
ENGINE_SMOKE_OR_DRY_RUN_WITH_FIXTURE
```

Later command classes may include:

```text
DATASET_CANONICALIZATION
CAPABILITY_MAP_GENERATION
LOGIC_COMPILE_DRY_RUN
TESTPLAN_DRY_RUN
CANDIDATE_RUN_WITH_FIXTURE
EVIDENCE_SUMMARY_BUILD
```

Each command class requires a bridge contract and human-approved ticket before implementation.

---

## 16. Generator boundary

The generator is an assistant to propose structured drafts. It is not an evidence engine.

### Generator may

```text
create LogicCard drafts from human prompts;
suggest bounded variants from a parent LogicCard;
suggest null families;
suggest ablation families;
identify missing fields;
translate raw notes into candidate fields;
propose repair text for compiler HOLD statuses.
```

### Generator may not

```text
generate executable strategy code;
run tests;
promote candidates;
edit compiled specs after results;
bypass compiler checks;
choose best variants after seeing holdout results without explicit validation protocol;
make financial claims;
activate live trading or broker behavior;
call arbitrary shell commands;
commit to repo without ticket/audit.
```

### Generator output status

All generator outputs start as:

```text
GENERATED_DRAFT
QUARANTINE_REVIEW_REQUIRED
NO_EVIDENCE
```

The generator must attach:

```text
parent or prompt source;
method description;
bounds used;
fields changed;
reason for generation;
human review requirement;
quarantine reason.
```

---

## 17. Null generation policy

Nulls are first-class test controls. They are not optional decoration.

### Null purpose

```text
Determine whether candidate behavior exceeds what could be produced by random timing, shuffled labels, naive baselines, simple parent rules, or structurally similar but meaningless controls.
```

### Required null families

| Null family | Purpose | Example |
|---|---|---|
| `random_time_null` | Tests whether timing matters. | Randomly sample eligible bars with same count/session distribution. |
| `direction_flip_null` | Tests direction specificity. | Long candidate becomes short or vice versa. |
| `label_shuffle_null` | Tests relation to target labels where appropriate. | Shuffle labels within train/split constraints. |
| `feature_shuffle_null` | Tests feature/target relation while preserving distribution. | Shuffle feature values within session/regime constraints. |
| `threshold_random_null` | Tests whether selected thresholds are special. | Sample thresholds from declared bounded range. |
| `simple_baseline_null` | Compares against simpler obvious rule. | Always next-bar, session baseline, open-to-close baseline. |
| `parent_rule_null` | Tests whether child adds value over parent. | Parent candidate without added filter. |

### Null constraints

```text
Nulls must preserve no-leakage rules.
Nulls must respect split boundaries.
Nulls must be declared before the run.
Nulls must be tied to candidate ID and TestPlan ID.
Null results must appear on EvidenceCards.
Null generation cannot inspect holdout performance to choose favorable controls.
```

### Null output object

| Field | Meaning |
|---|---|
| `null_id` | Stable null identifier. |
| `parent_logic_id` | Candidate controlled by this null. |
| `null_family` | Null type. |
| `preserved_structure` | What stays the same. |
| `randomized_structure` | What changes. |
| `seed_policy` | Deterministic seed rules. |
| `split_policy` | How splits are respected. |
| `expected_meaning` | What pass/fail means. |

---

## 18. Ablation policy

Ablations identify which parts of the candidate matter.

### Ablation purpose

```text
Remove, neutralize, or simplify one component at a time to learn whether the parent candidate's behavior depends on that component.
```

### Ablation types

| Ablation type | What it removes/changes | Example |
|---|---|---|
| `filter_removed` | Removes a context/regime filter. | Run signal without PSA/state filter. |
| `feature_removed` | Removes one feature. | Remove open-position feature. |
| `threshold_neutralized` | Replaces threshold with neutral/default. | Replace high threshold with median/none. |
| `exit_simplified` | Simplifies exit logic. | Time exit only, no TP/SL. |
| `risk_rule_removed` | Removes stop/TP/risk component. | No stop version for attribution only. |
| `direction_isolated` | Tests long and short separately. | Long-only / short-only ablations. |
| `session_filter_removed` | Removes RTH/ETH/session filter. | All-session version. |
| `parent_only` | Retains parent logic before new component. | Parent candidate without generated modifier. |

### Ablation constraints

```text
Ablations must be named before testing.
Ablations must preserve causal timing.
Ablations must be linked to parent candidate.
Ablations must not become new promoted candidates without their own audit.
Ablation results must appear near aggregate evidence.
```

---

## 19. Variant generation policy

Variants explore bounded candidate changes. Variants are not an optimizer free-for-all.

### Variant generation may change

```text
fixed thresholds within declared bounds;
lookback windows within declared bounds;
session filters from a predefined set;
entry delay conventions from a predefined set;
exit horizons from a predefined set;
feature combinations from a declared component list;
direction split long/short/both;
conservative ambiguity policy variants.
```

### Variant generation may not change

```text
target labels after seeing results;
split definitions after seeing results;
full-sample thresholds;
holdout-selected parameters;
data source assumptions;
timezone/session assumptions;
core hypothesis without creating a new parent LogicCard;
execution model in a way that invalidates comparison;
results or EvidenceCard content.
```

### Variant budget

Every generator ticket should define:

```text
maximum number of variants;
allowed fields to vary;
parameter bounds;
random seed policy;
parent candidate link;
selection rule;
holdout protection;
archive/quarantine route.
```

### Variant lifecycle

```text
PARENT_COMPILED_SPEC
→ VARIANT_DRAFT
→ HUMAN_REVIEW
→ VARIANT_COMPILE
→ VARIANT_TESTPLAN
→ VARIANT_RUN
→ VARIANT_EVIDENCE
→ AUDIT_DECISION
```

No variant skips compile/test/audit because its parent passed.

---

## 20. Quarantine policy for generated logic

Generated logic is quarantined by default.

### Quarantine reasons

| Reason | Meaning |
|---|---|
| `AI_GENERATED_UNREVIEWED` | Produced by assistant/model; human has not reviewed. |
| `PROVENANCE_WEAK` | Source or parent unclear. |
| `TIMING_UNCLEAR` | known_at/signal_time/entry_time ambiguous. |
| `DATA_CAPABILITY_UNCONFIRMED` | DCM dependency unresolved. |
| `GENERATION_BOUNDS_UNCLEAR` | Variant space too open. |
| `NULLS_MISSING` | No control plan. |
| `ABLATIONS_MISSING` | Attribution missing. |
| `RISKY_FINANCIAL_CLAIM` | Language implies trading validity/profit. |
| `SCOPE_DRIFT` | Candidate expands beyond current milestone. |

### Quarantine exit conditions

A generated candidate may leave quarantine only if:

```text
human review completed;
required fields filled;
provenance recorded;
DatasetCapabilityMap dependency resolved;
compiler pass achieved;
nulls and ablations declared;
TestPlan defined;
no audit/human gate blocks it.
```

Quarantine is not failure. It is containment.

---

## 21. Promotion policy for compiled/tested logic

A candidate cannot be promoted because it is interesting, compiled, visually impressive, or generated from a clever idea.

### Promotion prerequisites

```text
LogicCard exists.
CompiledLogicSpec exists.
TestPlan exists.
DatasetCapabilityMap supports the test.
ResearchCore Engine run artifacts exist.
EvidenceCard exists.
Nulls and ablations are visible.
Failures/limitations are recorded.
Audit returns PROMOTE or CONTINUE_TESTING with clear status.
Decision ledger updated.
Reversal condition recorded.
```

### Promotion levels

| Level | Meaning | Authority |
|---|---|---|
| `COMPILE_PROMOTED` | Candidate is legal to test. | May enter TestPlan. |
| `TEST_PROMOTED` | Candidate produced complete run artifacts. | May enter EvidenceCard. |
| `EVIDENCE_PROMOTED` | Evidence strong enough for next research pass. | May guide next candidate/milestone. |
| `PRODUCT_PROMOTED` | UX/workflow feature proved valuable. | May enter roadmap. |
| `ENGINE_PROMOTED` | Engine/bridge capability proved reliable. | May become operating assumption. |

### Non-promotion examples

| Situation | Correct status |
|---|---|
| Compiles but not tested. | `COMPILE_PASS`, not promoted evidence. |
| One good chart example. | `VISUAL_EXAMPLE`, not proof. |
| Beats no nulls. | `INCOMPLETE_EVIDENCE`. |
| Beats random null but fails ablation. | `CONTINUE_TESTING` or `REPAIR`. |
| Generated 100 variants, one looks good. | `QUARANTINE_REVIEW`, likely multiple-comparison risk. |
| User likes the idea. | `OPINION`, not validation. |

---

## 22. UI states for Logic Factory

### Main surfaces

| Surface | User goal | Core state shown |
|---|---|---|
| Logic Library | Browse ideas/cards/specs by status. | Draft, compile, test, evidence, audit state. |
| LogicCard Editor | Convert idea into explicit fields. | Required fields, missing fields, timing map. |
| Compiler Panel | See pass/hold/reject. | Checks, blockers, warnings, repair suggestions. |
| Controls Panel | Attach nulls, ablations, variants. | Coverage of controls, parent-child links. |
| TestPlan Bridge | Prepare engine run. | Dataset binding, split policy, allowed command class. |
| Quarantine Review | Review generated/untrusted logic. | Reason, required repair, promotion blockers. |
| Lineage View | Inspect parent/child/generated trees. | Parent, variants, nulls, ablations, evidence links. |

### UI state language

Use direct labels:

```text
Draft — not runnable
Ready for compile
Compile hold — repair needed
Compile reject — cannot test as written
Compiled — legal to test, not evidence
Controls missing
TestPlan ready
Run queued
Evidence ready
Audit pending
Promoted
Quarantined
Archived
Killed
```

Avoid labels that imply proof:

```text
Winner
Profitable
Validated strategy
Best setup
Guaranteed
Edge found
Production ready
```

### Required user warnings

Logic Factory should repeatedly show:

```text
Compile pass is not evidence.
Generated logic is not evidence.
Visual replay is not aggregate proof.
Nulls and ablations are required for serious interpretation.
DatasetCapabilityMap controls what can be lawfully tested.
```

---

## 23. Validation/test strategy for Logic Factory

This volume enables later test planning. It does not implement tests.

### Validation targets

| Target | Test idea | Success criterion |
|---|---|---|
| LogicCard completeness | Draft fixture with missing fields. | Compiler returns HOLD with exact missing fields. |
| No-leakage rejection | Future-looking feature fixture. | Compiler returns REJECT. |
| Timing correctness | Signal at close, entry next open. | Compiler accepts legal timing. |
| DCM gate | Candidate requests unsupported chart/timeframe. | Compiler rejects or holds. |
| Intrabar ambiguity | OHLC SL/TP first-hit candidate. | Compiler requires ambiguity policy. |
| Null policy | Candidate without nulls. | Compiler holds before TestPlan readiness. |
| Ablation policy | Multi-component candidate without ablations. | Compiler holds before TestPlan readiness. |
| Generated quarantine | Generated candidate draft. | Starts quarantined and requires review. |
| TestPlan bridge | Compiled fixture to dry-run TestPlan. | TestPlan includes candidate/control IDs and allowed engine command class. |

### MVP test fixtures

Use small deterministic fixtures:

```text
valid_logiccard_minimal_observation
valid_logiccard_trade_like_next_bar_entry
invalid_future_return_feature
invalid_centered_window
invalid_full_sample_threshold
invalid_unsupported_timeframe
hold_missing_timezone
hold_ambiguous_intrabar_sl_tp
hold_missing_null_policy
hold_generated_unreviewed
```

### Evidence boundary test

A test should explicitly verify:

```text
CompiledLogicSpec cannot be marked promoted evidence without run artifacts and EvidenceCard.
```

---

## 24. QA/security/human gates for logic/generator work

### Human gate triggers

Stop for human approval before:

```text
activating any generator that creates candidate logic automatically;
allowing generated candidates to leave quarantine;
adding AI/model/API dependency;
adding broker/live-trading behavior;
adding arbitrary code execution or formula execution beyond approved compiler model;
changing no-leakage rules;
changing DatasetCapabilityMap gate behavior;
changing promotion rules;
changing null/ablation requirements;
running large optimization/variant sweeps;
committing full ES.zip or other large/private datasets;
claiming market edge/profitability;
publicly distributing candidate results.
```

### Security/privacy/data gates

| Gate | Required review |
|---|---|
| Arbitrary formulas | Ensure no unsafe eval/shell behavior. |
| File paths in LogicCards | Ensure scoped workspace-only access. |
| Generated content | Ensure prompt/model output is quarantined and provenance-recorded. |
| Dataset references | Ensure no private/full data committed. |
| Engine bridge | Ensure only allowed command classes. |
| Exporting results | Ensure no sensitive raw data leaves workspace unexpectedly. |
| AI activation | Ensure model/API keys, data boundaries, and audit trail exist. |

### QA requirements

Every Logic Factory implementation ticket later needs:

```text
acceptance criteria;
compiler fixture tests;
negative tests;
source-of-truth doc update if contract changes;
implementation report;
auditor pass;
human gate handling if generation/AI/security/data access changes.
```

---

## 25. Risks and reversal conditions

| Risk | Severity | Mitigation | Reversal condition |
|---|---:|---|---|
| LogicCard schema becomes too heavy to use. | Medium | Start with minimal required fields and progressive disclosure. | If user cannot create first card without excessive friction. |
| Compiler is too strict and blocks exploration. | Medium | Separate draft, compile-ready, and test-ready states. | If useful manual candidates cannot be represented without unsafe shortcuts. |
| Compiler is too loose and permits leakage. | High | Negative tests for future-looking features and full-sample thresholds. | If any leakage passes compile, tighten before testing. |
| Generator floods project with low-quality variants. | High | Variant budget, quarantine, parent lineage, human review. | Disable generator until compiler/quarantine policy is repaired. |
| Nulls/ablations feel like overhead. | Medium | UI explains why each control exists. | If users bypass controls, make TestPlan gate stricter. |
| Visual replay overpowers aggregate evidence. | High | EvidenceCard must sit beside replay; replay cannot promote. | If decisions are made from chart examples alone, change UI. |
| ResearchCore Engine does not map cleanly to TestPlan needs. | High | Bridge dry run and contract spike before feature build. | If mapping requires engine rewrite, split into engine roadmap or reduce MVP. |
| Generated strategies imply financial advice. | High | Copy/UX labels avoid advice/profit claims. | If users interpret output as trade recommendation, restrict language/features. |

---

## 26. ADRs to create later

| ADR | Decision |
|---|---|
| `ADR-LF-001` | LogicCard object model and lifecycle states. |
| `ADR-LF-002` | Compiler before generator policy. |
| `ADR-LF-003` | No-leakage timing contract. |
| `ADR-LF-004` | DatasetCapabilityMap as compile gate. |
| `ADR-LF-005` | Nulls and ablations as first-class controls. |
| `ADR-LF-006` | Generated logic quarantine policy. |
| `ADR-LF-007` | ResearchCore Engine TestPlan bridge boundary. |
| `ADR-LF-008` | No arbitrary shell/code execution for logic evaluation. |

---

## 27. First milestone category enabled by this volume

This volume enables a future milestone category:

```text
M3 — Logic Factory Compiler Contract Proof
```

M3 should prove, later and through tickets, that NullForge can:

```text
represent one manual LogicCard;
reject one future-looking invalid LogicCard;
hold one ambiguous dataset/timing LogicCard;
compile one valid minimal LogicCard into a deterministic CompiledLogicSpec;
attach at least one null and one ablation;
produce a dry-run TestPlan bridge object;
show all states in the UI or fixture output;
avoid running uncompiled logic.
```

Do not generate M3 implementation tickets yet. They belong after Volume 7 roadmap generation.

---

## 28. What must not be built yet

Do not build yet:

```text
LogicCard editor implementation;
compiler implementation;
generator implementation;
AI proposer;
large variant search;
optimizer;
broker/live trading integration;
public strategy library;
paid signals;
real-time engine execution;
full ES.zip test runs;
visual replay proof claims;
EvidenceCard promotion automation;
public distribution;
anything that requires arbitrary shell execution.
```

Also do not generate broad implementation prompts such as:

```text
Build the Logic Factory.
Implement the compiler.
Generate strategies and test them.
```

Those are not tickets. They are scope traps.

---

## 29. Volume 5 closeout

### Artifacts defined

```text
Logic Factory product role
LogicCard lifecycle
LogicCard draft schema
required candidate fields
no-leakage timing rules
DatasetCapabilityMap dependency rules
compiler purpose and validation checks
compiler failure modes
CompiledLogicSpec draft
TestPlan bridge draft
ResearchCore Engine boundary
generator boundary
null policy
ablation policy
variant policy
generated logic quarantine policy
promotion policy
Logic Factory UI states
validation/test strategy
QA/security/human gates
risks and reversal conditions
ADRs to create later
first milestone category enabled
prompt for Volume 6
```

### Decision

```text
PROMOTE_TO_VOLUME_6_AFTER_REVIEW
```

### Why

Volume 5 defines the boundary that makes “compile/generate logic to test” safe enough to plan without turning NullForge into an unbounded strategy generator.

### Next volume

```text
Volume 6 — NullForge Visual Replay, Evidence Cards, Audit Decision UX, and Result Interpretation Boundaries
```

---

## 30. Prompt for Volume 6

Use this exact prompt next.

```md
# Prompt for Volume 6 — NullForge Visual Replay, Evidence Cards, Audit Decision UX, and Result Interpretation Boundaries

You are my ForgeIT Project Factory volume writer, Visual Replay architect, Evidence Card designer, audit-decision UX planner, result-interpretation boundary auditor, market-research safety reviewer, source-of-truth guardian, and anti-context-soup auditor.

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

Volume 0 status:

```text
Volume 0 — NullForge North Star, Doctrine, Naming, Claims, MVP Cutline, Anti-Goals has been generated as draft canonical project source.
```

Volume 1 status:

```text
Volume 1 — NullForge Workspace, Repo, Context, Source-of-Truth, Archive, and Quarantine System has been generated as draft canonical project source.
```

Volume 2 status:

```text
Volume 2 — NullForge Planner / Implementor / Auditor Loop, QA Gates, Human Gates, and Codex Execution System has been generated as draft canonical project source.
```

Volume 3 status:

```text
Volume 3 — NullForge Windows + Tauri Desktop Architecture, ResearchCore Engine Bridge, Sidecar Contract, and Packaging Spike Plan has been generated as draft canonical project source.
```

Volume 4 status:

```text
Volume 4 — NullForge Dataset Studio, ES.zip Intake Boundary, Fixture Policy, DatasetCapabilityMap, Timeframe/Chart Capability Rules has been generated as draft canonical project source.
```

Volume 5 status:

```text
Volume 5 — NullForge Logic Factory, LogicCard Lifecycle, Compiler Contract, Generator/Null/Ablation Boundary, and Test-Plan Bridge has been generated as draft canonical project source.
```

One-sentence thesis:

```text
NullForge is a Windows-first local desktop research workbench that helps a solo research builder import market datasets, map lawful dataset capabilities, compile/generate candidate logic into auditable test specs, run the local ResearchCore Engine, inspect visual trade replays, and decide whether evidence should be promoted, repaired, archived, or quarantined.
```

First proof loop:

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

Volume 4 data doctrine to preserve:

```text
DatasetCapabilityMap must happen before timeframe/chart/test generation.
5m OHLCV can aggregate upward but cannot reconstruct true 1m/tick data.
OHLC bars cannot prove exact intrabar SL/TP first-hit order without lower-timeframe/tick data.
Missing or ambiguous timezone/session information must trigger confirmation or quarantine.
Dataset Studio does not prove strategy validity.
```

Volume 5 logic doctrine to preserve:

```text
Generated logic is not evidence.
A LogicCard is not runnable until compiled.
A compiled spec is not validated until tested.
A passing compile is not market edge.
A visual replay is not aggregate proof.
DatasetCapabilityMap gates test eligibility.
Compiler must reject future-looking inputs.
Compiler must record signal_time, known_at, entry_time, exit_rule, stop_rule, take_profit_rule, and ambiguity handling.
Generator must not create executable strategy code without compiler/audit boundary.
Nulls and ablations must be first-class, not optional decoration.
ResearchCore Engine is called through a scoped bridge; no arbitrary shell execution.
Codex does not invent strategy or promote candidates.
```

## Mission

Generate Volume 6 only:

```text
Volume 6 — NullForge Visual Replay, Evidence Cards, Audit Decision UX, and Result Interpretation Boundaries
```

This volume should define how NullForge presents run results, visual examples, trade/path replays, aggregate evidence, nulls, ablations, failures, ambiguity, and audit decisions without letting charts or cherry-picked examples masquerade as proof.

## Required sections

Include:

1. Volume purpose.
2. Relationship to Volumes 0, 1, 2, 3, 4, and 5.
3. Visual Replay product role.
4. Evidence Card product role.
5. Result interpretation doctrine.
6. Visual replay object model.
7. Required visual replay fields.
8. Signal / entry / SL / TP / exit labeling rules.
9. Known-at-time and no-leakage display rules.
10. Intrabar ambiguity display policy.
11. Replay example selection policy.
12. Forbidden visual replay claims.
13. EvidenceCard draft schema.
14. Required EvidenceCard fields.
15. Aggregate metrics display boundary.
16. Null and baseline result display rules.
17. Ablation result display rules.
18. Failure mode and limitation display rules.
19. Audit decision UX.
20. Promotion / repair / archive / quarantine / kill decision rules.
21. ResearchCore Engine artifact boundary.
22. UI states for Visual Replay and Evidence Cards.
23. Validation/test strategy for replay/evidence surfaces.
24. QA/security/human gates for result presentation.
25. Risks and reversal conditions.
26. ADRs to create later.
27. First milestone category enabled by this volume, without generating implementation tickets.
28. What must not be built yet.
29. Volume 6 closeout.
30. Prompt for Volume 7.

## Required boundaries

Preserve these boundaries:

```text
Visual replay explains examples; aggregate evidence decides.
A beautiful chart is not proof.
One replay example is not validation.
EvidenceCard must show nulls, ablations, sample size, failure modes, and limitations.
Intrabar ambiguity must be visible, not hidden.
Known-at-time labels must prevent future-data confusion.
No result screen may imply financial advice, guaranteed edge, or live-trading readiness.
No candidate can be promoted from replay alone.
No aggregate result can be promoted without audit.
No public sharing/export of results before data/source/legal/privacy review.
ResearchCore Engine artifacts remain canonical run output.
```

## Response rules

Return Volume 6 as structured Markdown content or downloadable Markdown files if files are requested.
Do not generate Volume 7.
Do not generate implementation code.
Do not create a broad build prompt.
Keep the output detailed enough to become a canonical project source.
End with the exact next prompt for Volume 7.
```
