> Import note: This file was imported by PF-T001 from `NullForge_Volume_06_v0_4_Package.zip` / `NullForge_Volume_06_v0_4_Package/artifacts/NullForge_Volume_06_Visual_Replay_Evidence_Cards_Audit_Decision_UX_Result_Interpretation_Boundaries_v0_4.md` on `2026-06-15`.
> Authority: repo-managed NullForge planning/workflow source after PF-T001 audit. It is not ResearchCore Engine implementation truth.
> Source package SHA256: `C5B1609C022992194F8082F2050CE9BA97A6A71B81A0AFAE5D904952C5D0CAC2`

# Volume 6 — NullForge Visual Replay, Evidence Cards, Audit Decision UX, and Result Interpretation Boundaries v0.4

```text
Project: NullForge
Existing repo / engine: research-core
Internal engine label: ResearchCore Engine
First platform: Windows 11 x64
Desktop stack: Tauri + React + TypeScript
Engine boundary: Existing Python ResearchCore Engine as local sidecar / command bridge
Volume status: Draft canonical project source
```

---

## 1. Volume purpose

Volume 6 defines how NullForge presents run results, visual examples, trade/path replays, aggregate evidence, nulls, ablations, failures, ambiguity, and audit decisions.

The purpose is not to make charts look impressive.

The purpose is to make evidence interpretable without letting beautiful examples become fake proof.

Core rule:

```text
Visual replay explains examples.
Evidence Cards summarize evidence.
Audit decides what survives.
```

This volume exists because NullForge will be especially vulnerable to chart theater:

```text
one perfect replay
one clean entry
one dramatic profit target
one cherry-picked case
```

can emotionally overpower:

```text
sample size
null tests
ablations
failure modes
intrabar ambiguity
data limitations
out-of-sample behavior
```

Volume 6 prevents that by making every replay subordinate to an Evidence Card and every Evidence Card subordinate to an audit decision.

---

## 2. Relationship to Volumes 0, 1, 2, 3, 4, and 5

| Prior volume | What it established | Volume 6 dependency |
|---|---|---|
| Volume 0 | Mission, doctrine, claims, MVP cutline, anti-goals | Result screens must preserve the claim/evidence/audit doctrine. |
| Volume 1 | Repo/workspace/source-of-truth/archive/quarantine | Replay and Evidence Card artifacts must have canonical locations and archive rules. |
| Volume 2 | Planner / Implementor / Auditor loop and QA gates | Replay/evidence implementation later must go through scoped tickets and independent audit. |
| Volume 3 | Windows + Tauri desktop architecture and ResearchCore Engine bridge | Replay/evidence surfaces must read scoped engine artifacts through safe local access. |
| Volume 4 | Dataset Studio and DatasetCapabilityMap | Replay/evidence surfaces must display dataset capability limitations and ambiguity. |
| Volume 5 | Logic Factory, compiler, generator/null/ablation boundary | Evidence Cards must connect LogicCard → CompiledLogicSpec → TestPlan → run artifacts → decision. |

Volume 6 is the interpretation boundary.

It does not define dataset import, candidate compilation, or engine execution. It defines how the user sees and judges the outputs after those upstream stages produce artifacts.

---

## 3. Visual Replay product role

Visual Replay is the NullForge surface for inspecting specific examples from a tested candidate.

It answers:

```text
What happened in this case?
Where did the signal occur?
What was known at signal time?
When would entry have occurred?
Where were SL / TP levels?
What exit rule applied?
Was the path ambiguous?
How does this example relate to aggregate evidence?
```

Visual Replay is useful for:

```text
debugging candidate logic
explaining signal timing
finding leakage
spotting execution-rule misunderstandings
showing ambiguous intrabar paths
illustrating failures
reviewing outliers
building intuition after evidence exists
```

Visual Replay is not useful for:

```text
proving market edge
promoting a candidate by visual taste
replacing null tests
hiding ambiguous or failed examples
making financial claims
```

Visual Replay should feel like a forensic replay tool, not a hype reel.

---

## 4. Evidence Card product role

Evidence Cards are the NullForge surface for summarizing what a test produced and what decision is allowed.

An Evidence Card answers:

```text
What was tested?
On what dataset and capability map?
Using which compiled logic spec and test plan?
What aggregate metrics resulted?
What happened against nulls and baselines?
Which ablations mattered?
What limitations or failures are known?
Which replay examples are available?
What audit decision is allowed now?
```

Evidence Cards exist because users should not have to chase evidence across raw logs, chart screenshots, JSON artifacts, notebook outputs, CLI summaries, and memory.

Evidence Cards are not marketing cards. They are audit cards.

---

## 5. Result interpretation doctrine

NullForge result interpretation must preserve these rules:

```text
A beautiful chart is not proof.
One replay example is not validation.
Visual replay explains examples; aggregate evidence decides.
Aggregate evidence without nulls is weak.
Aggregate evidence without ablations is incomplete.
Aggregate evidence without sample size is suspicious.
Aggregate evidence without limitations is unsafe.
A compile pass is not market edge.
A test pass is not production readiness.
A candidate promoted for further testing is not a trading recommendation.
No screen may imply financial advice, guaranteed edge, or live-trading readiness.
```

### Evidence hierarchy inside NullForge

| Level | Artifact | What it can do | What it cannot do |
|---|---|---|---|
| Example | Visual Replay | Explain one case. | Prove candidate validity. |
| Run summary | ResearchCore artifact metadata | Show what was produced. | Decide promotion alone. |
| Evidence Card | Aggregated result + nulls + ablations + limitations | Support audit review. | Replace audit. |
| Audit report | PASS / HOLD / REJECT or promote/repair/archive decision | Govern next action. | Guarantee market performance. |

### Interpretation sentence

Every result screen should be compatible with this sentence:

```text
This result describes a historical research test under stated data, logic, and execution assumptions. It is not financial advice, live-trading readiness, or evidence of future performance.
```

---

## 6. Visual replay object model

Visual Replay should be modeled as a structured artifact, not just a rendered chart.

### Core objects

| Object | Meaning |
|---|---|
| `VisualReplayExample` | One selected replay case attached to a tested candidate/run. |
| `ReplayContext` | Metadata linking the example to dataset, capability map, logic spec, test plan, and run. |
| `PriceSeriesSlice` | The bounded OHLCV/time-series window displayed around the example. |
| `ReplayAnnotation` | A labeled marker or region: signal, known_at, entry, SL, TP, exit, hold window, ambiguity. |
| `PathAssessment` | Whether the displayed path is determinate, approximate, ambiguous, or unsupported. |
| `SelectionReason` | Why this example was selected: random, median, best, worst, failure, ambiguous, edge case. |
| `InterpretationBoundary` | Required disclaimers and constraints for the example. |

### Replay object lifecycle

```text
candidate tested
→ ResearchCore Engine emits run artifacts
→ Evidence Card indexes run outputs
→ replay examples are selected by policy
→ VisualReplayExample artifacts are created or referenced
→ UI renders the example
→ audit checks whether examples are honest and sufficiently diverse
```

### Replay object authority

```text
VisualReplayExample = explanatory artifact.
EvidenceCard = evidence summary artifact.
Audit report = decision artifact.
```

---

## 7. Required visual replay fields

Each `VisualReplayExample` should include at least:

| Field | Required? | Meaning |
|---|---:|---|
| `replay_id` | Yes | Stable replay identifier. |
| `candidate_id` | Yes | Candidate / logic identity. |
| `logic_card_id` | Yes if available | Source LogicCard. |
| `compiled_spec_id` | Yes | Compiled logic spec used. |
| `test_plan_id` | Yes | Test plan that produced the example. |
| `run_id` | Yes | ResearchCore Engine run. |
| `dataset_id` | Yes | Dataset used. |
| `dataset_manifest_id` | Yes | Dataset manifest used. |
| `capability_map_id` | Yes | DatasetCapabilityMap used. |
| `instrument` | Yes | Example: ES. |
| `timeframe` | Yes | Example: 5m. |
| `session_rule` | Required if session-aware | Session/calendar assumptions. |
| `timezone` | Required if time-based | Timezone applied to timestamps. |
| `window_start` | Yes | Display window start. |
| `window_end` | Yes | Display window end. |
| `signal_time` | Yes | Timestamp where the signal fires. |
| `known_at` | Yes | Latest timestamp whose data was available to the logic. |
| `entry_time` | Required if entry exists | Entry timestamp. |
| `entry_price` | Required if entry exists | Entry price assumption. |
| `stop_rule` | Required if used | Stop-loss rule. |
| `stop_price` | Required if used and determinate | Stop-loss level. |
| `take_profit_rule` | Required if used | Take-profit rule. |
| `take_profit_price` | Required if used and determinate | Take-profit level. |
| `exit_rule` | Yes | Exit logic. |
| `exit_time` | Required if exited | Exit timestamp. |
| `exit_price` | Required if exited | Exit price assumption. |
| `outcome_label` | Yes | Win/loss/flat/timeout/no-fill/ambiguous/etc. |
| `path_status` | Yes | `DETERMINATE`, `AMBIGUOUS`, `APPROXIMATE`, `UNSUPPORTED`. |
| `selection_reason` | Yes | Why this example is shown. |
| `limitations` | Yes | Known limits for the example. |
| `artifact_paths` | Yes | Source artifact references. |
| `created_at` | Yes | Artifact creation timestamp. |

### Optional but useful fields

| Field | Meaning |
|---|---|
| `split_label` | Train/validation/test/OOS/walk-forward split label. |
| `bar_index` | Index of signal/entry bar in canonical data. |
| `entry_assumption` | Next open, close, limit, stop, midpoint, etc. |
| `slippage_assumption` | Slippage model used, if any. |
| `cost_assumption` | Commission/spread/cost model used, if any. |
| `risk_unit` | R-multiple or configured risk model. |
| `mfe` / `mae` | Only if causally calculated and allowed by test plan. |
| `notes` | Human notes, if audited. |

---

## 8. Signal / entry / SL / TP / exit labeling rules

Visual labels must be explicit and time-aware.

### Required labels

| Label | Must show | Rule |
|---|---|---|
| `Signal` | `signal_time`, signal rule summary | Marks when the candidate condition became true. |
| `Known at` | `known_at` | Marks the latest data available to the logic. |
| `Entry` | `entry_time`, `entry_price`, entry assumption | Must not be earlier than allowed by the compiled spec. |
| `SL` | stop rule and level | Must show whether it is fixed, trailing, dynamic, or unavailable. |
| `TP` | take-profit rule and level | Must show whether it is fixed, partial, dynamic, or unavailable. |
| `Exit` | exit rule, `exit_time`, `exit_price` | Must distinguish rule exit, stop, TP, timeout, no-fill, forced close. |
| `Hold window` | duration or bars held | Must match the compiled test plan. |
| `Ambiguity` | ambiguity status | Must be visible if the path cannot be resolved. |

### Label clarity rules

```text
Labels must not imply the system knew future outcomes.
Labels must separate signal time from entry time.
Labels must separate entry assumption from observed bar data.
Labels must distinguish stop/take-profit levels from actual fills.
Labels must show when an exit is simulated, inferred, unsupported, or ambiguous.
Labels must show if the replay is based on approximate/derived data.
```

### Good label example

```text
Signal: 2024-03-14 10:15 ET
Known at: bar close 10:15 ET
Entry assumption: next bar open, 10:20 ET
Stop rule: 1.0R fixed from entry
Take-profit rule: 2.0R fixed from entry
Exit: TP reached, but first-hit path AMBIGUOUS on 5m OHLC
```

### Bad label example

```text
Perfect long entry before breakout.
```

Reason:

```text
It hides timing, known-at boundary, entry assumption, and ambiguity.
```

---

## 9. Known-at-time and no-leakage display rules

Every replay must show the difference between:

```text
what the chart shows now
what the logic knew then
what the test assumed for execution
what happened after entry
```

### Required no-leakage markers

| Marker | Purpose |
|---|---|
| `known_at` vertical marker | Prevents future bars from being interpreted as decision inputs. |
| `future path region` shading/label | Makes post-signal/post-entry outcome visibly separate. |
| `entry assumption` label | Shows whether entry was next open, close, limit, etc. |
| `feature window` optional overlay | Shows lookback window used by the signal. |
| `target/label availability` warning | Shows that outcomes are not inputs. |

### No-leakage display policy

```text
Feature values may be displayed only if they were available at known_at.
Future outcome labels must be visually separated from decision inputs.
Performance overlays must not appear as if known at signal time.
Trade management levels must distinguish pre-declared rules from hindsight annotations.
```

### Required warning when relevant

```text
Post-entry movement is shown for review only. It was not available to the candidate at signal time.
```

---

## 10. Intrabar ambiguity display policy

OHLC bars can hide the order of price movement inside a bar.

If a stop-loss and take-profit are both within the same bar range, the exact first-hit path may be unknown without lower-timeframe or tick data.

### Ambiguity statuses

| Status | Meaning | UI behavior |
|---|---|---|
| `DETERMINATE` | Available data supports the path/fill sequence under stated rules. | Render normally with source note. |
| `AMBIGUOUS` | OHLC/order information cannot determine first hit or sequence. | Show visible ambiguity badge and explanation. |
| `APPROXIMATE` | Result uses approximation or assumption. | Show assumption label and confidence limitation. |
| `UNSUPPORTED` | Dataset cannot support the replay/fill claim. | Block or render as non-authoritative explanatory sketch. |
| `REQUIRES_LOWER_TIMEFRAME` | Lower-timeframe/tick data needed. | Link to DatasetCapabilityMap limitation. |

### Required ambiguity notes

When ambiguity exists, the replay should show:

```text
which bar is ambiguous
which levels were touched
which outcomes are possible
what assumption was applied, if any
whether the aggregate test counted the case
where to find the DatasetCapabilityMap limitation
```

### Ambiguity handling examples

| Situation | Required handling |
|---|---|
| SL and TP both inside same 5m bar | Mark `AMBIGUOUS`; do not silently choose favorable fill. |
| Entry and stop both inside same OHLC bar | Mark `AMBIGUOUS` or `UNSUPPORTED` depending on rule. |
| Session close exit after unambiguous sequence | Mark determinate if timestamps/rules support it. |
| Derived Renko from 5m OHLC | Mark `APPROXIMATE` or block depending on capability map. |

---

## 11. Replay example selection policy

Replay examples must be selected by policy, not cherry-picked by emotional appeal.

### Required example set for non-trivial tests

When enough cases exist, each Evidence Card should link to a balanced replay set:

| Example class | Purpose |
|---|---|
| `RANDOM_SEEDED` | Shows ordinary cases without cherry picking. |
| `MEDIAN_OUTCOME` | Shows representative result. |
| `BEST_OUTCOME` | Shows upside example, clearly labeled. |
| `WORST_OUTCOME` | Shows downside example, clearly labeled. |
| `FAILURE_CASE` | Shows no-fill, invalid, timeout, or rule failure. |
| `AMBIGUOUS_CASE` | Shows first-hit/path ambiguity where relevant. |
| `EDGE_CASE` | Shows boundary condition such as session edge, missing data, extreme volatility. |

### Selection rules

```text
Use deterministic seeded selection for random examples.
Record selection reason for every replay.
Do not hide losing or ambiguous cases.
Do not let the default example be only best outcome.
Prefer representative and failure examples before showcase examples.
If only one example exists, label it as insufficient for validation.
```

### MVP replay fixture exception

For the MVP, a single hand-selected fixture is allowed only if it is labeled:

```text
Fixture / explanation only.
Not evidence.
Not validation.
Not candidate promotion basis.
```

---

## 12. Forbidden visual replay claims

Replay screens must not say or imply:

```text
This strategy works.
This is a profitable edge.
This setup is guaranteed.
This is ready to trade live.
This is financial advice.
This proves future performance.
This example represents the whole distribution.
This candidate is promoted because this chart looks good.
This stop or target was definitely hit first when data is ambiguous.
This entry was available before the signal/known_at boundary.
```

### Forbidden UI patterns

| Pattern | Why forbidden |
|---|---|
| Green profit badges without context | Creates fake certainty and encourages outcome-chasing. |
| Defaulting to best trade example | Encourages cherry-picking. |
| Hiding null/baseline links | Separates examples from evidence. |
| Hiding ambiguity labels behind hover-only text | Users may miss critical limitations. |
| Showing future indicators as if known at signal time | Leakage confusion. |
| Using “validated” for compile-only artifacts | Compile is not validation. |
| Export/share button before review | Data/legal/privacy risk. |

---

## 13. EvidenceCard draft schema

Evidence Cards should be structured artifacts.

This is a draft field contract, not implementation code.

```text
EvidenceCard
  card_id
  version
  created_at
  status
  candidate
    candidate_id
    logic_card_id
    compiled_spec_id
    candidate_state
  dataset
    dataset_id
    dataset_manifest_id
    capability_map_id
    instrument
    timeframe
    timezone
    session_rule
    split_policy
  test
    test_plan_id
    run_id
    engine_version
    command_label
    artifact_paths
  metrics
    summary
    sample_size
    coverage
    costs_slippage_assumptions
    split_results
    uncertainty_notes
  nulls_and_baselines
    random_baseline
    shuffled_baseline
    naive_baseline
    no_signal_baseline
    other_controls
  ablations
    parent_logic
    removed_conditions
    weakened_conditions
    inverted_conditions
    results
  replay_examples
    replay_id
    selection_reason
    path_status
    artifact_path
  failures_and_limitations
    data_limitations
    logic_limitations
    execution_limitations
    test_limitations
    known_failures
  audit
    recommended_decision
    auditor_status
    human_gate_required
    decision_record_path
```

---

## 14. Required EvidenceCard fields

| Field group | Required fields |
|---|---|
| Identity | `card_id`, `version`, `created_at`, `status` |
| Candidate | `candidate_id`, `logic_card_id`, `compiled_spec_id`, `candidate_state` |
| Dataset | `dataset_id`, `dataset_manifest_id`, `capability_map_id`, `instrument`, `timeframe`, `timezone`, `session_rule` |
| Test | `test_plan_id`, `run_id`, `engine_version`, `artifact_paths` |
| Metrics | `sample_size`, `metric_definitions`, `aggregate_results`, `split_results` if applicable |
| Nulls/baselines | At least one baseline status or explicit reason missing |
| Ablations | Ablation status or explicit reason deferred |
| Replays | Replay list with selection reasons |
| Limitations | Data, logic, execution, and test limitations |
| Audit | Decision status, reviewer, date, next action |

### Evidence Card statuses

```text
DRAFT
RUN_INDEXED
EVIDENCE_READY
AUDIT_PENDING
PROMOTED_FOR_NEXT_TEST
REPAIR_REQUIRED
ARCHIVED
QUARANTINED
KILLED
```

### Evidence Card non-claim

Every Evidence Card must include:

```text
This card summarizes a historical research test under stated assumptions. It is not financial advice, live-trading readiness, or a guarantee of future performance.
```

---

## 15. Aggregate metrics display boundary

Aggregate metrics must be displayed with enough context to prevent over-reading.

### Required context near metrics

| Context | Why |
|---|---|
| Sample size | Prevents tiny-N excitement. |
| Split policy | Shows train/validation/test/OOS context. |
| Dataset ID and timeframe | Prevents data/source confusion. |
| Cost/slippage assumptions | Prevents frictionless fantasy. |
| Null/baseline comparison | Avoids fake improvement. |
| Ablation summary | Shows which component mattered. |
| Ambiguous path rate | Reveals execution uncertainty. |
| Failure count | Shows what did not work. |
| Limitation summary | Prevents overclaiming. |

### Metrics that need caution labels

| Metric family | Caution |
|---|---|
| Win rate | Needs payoff and costs context. |
| Average return | Sensitive to outliers. |
| Profit factor | Can be unstable at small sample sizes. |
| Max drawdown | Historical only; future may differ. |
| Sharpe-like metrics | Sensitive to assumptions and sample regime. |
| First-hit SL/TP stats | Requires intrabar path policy. |
| MFE/MAE | Must not be used as future input; display only as outcome analysis if allowed. |

### Display rule

No aggregate metric should be shown alone. It must be near:

```text
sample size
dataset/split
null/baseline
limitations
decision status
```

---

## 16. Null and baseline result display rules

Nulls and baselines are first-class evidence, not optional decoration.

### Required baseline/null panel

Each Evidence Card should include a panel showing:

| Control | Purpose | Display |
|---|---|---|
| Random baseline | Avoid fake improvement from noise. | Result + comparison status. |
| Shuffled/timing null | Test timing dependency. | Result + comparison status. |
| Naive baseline | Compare simple alternative. | Result + comparison status. |
| No-signal baseline | Compare doing nothing / unconditional exposure where applicable. | Result + comparison status. |
| Existing parent baseline | Compare prior candidate/spec. | Result + comparison status. |

### Null display statuses

```text
PASSED_AGAINST_NULL
FAILED_AGAINST_NULL
INCONCLUSIVE
NOT_RUN
NOT_APPLICABLE
BLOCKED_BY_DATA
```

### Null display rule

If nulls are not run, the Evidence Card cannot say:

```text
validated
supported edge
promoted
```

It may say:

```text
aggregate run complete, null evidence missing
```

or:

```text
audit pending / continue testing
```

---

## 17. Ablation result display rules

Ablations show whether candidate parts matter.

### Required ablation categories

| Ablation | Purpose |
|---|---|
| Remove one condition | Tests whether a condition is load-bearing. |
| Weaken threshold | Tests whether exact thresholds are overfit. |
| Invert direction | Tests directional dependence. |
| Remove context filter | Tests whether regime filter matters. |
| Parent-only baseline | Tests whether added feature improved parent. |

### Ablation display statuses

```text
SUPPORTS_COMPONENT
COMPONENT_NOT_LOAD_BEARING
CONTRADICTS_COMPONENT
INCONCLUSIVE
NOT_RUN
BLOCKED
```

### Ablation display policy

```text
Ablations must be summarized near the main result.
Ablations must not be hidden in raw artifact links only.
If ablations contradict the main interpretation, the decision defaults to HOLD or CONTINUE_TESTING.
```

---

## 18. Failure mode and limitation display rules

Failures are part of evidence.

### Required failure classes

| Failure class | Examples |
|---|---|
| Data failure | Missing timestamps, gaps, bad schema, unknown timezone, unsupported chart type. |
| Logic failure | Compile reject, future-looking input, undefined exit rule, invalid stop rule. |
| Execution failure | No fill, ambiguous fill, session conflict, unsupported order assumption. |
| Test failure | Too few cases, nulls missing, ablations missing, split leakage, command error. |
| UI/interpretation failure | Replay label missing, metric shown without context, misleading copy. |
| Source-of-truth failure | Artifact missing, stale docs, unpromoted output used as truth. |

### Limitation display rules

Each Evidence Card must show:

```text
data limitations
candidate logic limitations
test design limitations
execution/fill assumptions
interpretation limitations
next evidence needed
```

### Failure transparency rule

A result screen that hides failures is treated as an audit failure.

---

## 19. Audit decision UX

Audit decision UX should make the allowed next action obvious.

### Decision panel fields

| Field | Meaning |
|---|---|
| `current_status` | Draft, evidence ready, audit pending, promoted for next test, repair required, archived, killed. |
| `recommended_decision` | System/human/auditor recommendation, if available. |
| `decision_basis` | Main evidence used. |
| `blocking_issues` | Items preventing promotion. |
| `human_gate_required` | Whether user approval is required. |
| `next_action` | Specific next artifact/ticket/test. |
| `decision_record_path` | Link to decision/audit record. |
| `reversal_condition` | When to undo or revisit. |

### Audit decision copy

Use language like:

```text
PROMOTE_FOR_NEXT_TEST
REPAIR_REQUIRED
CONTINUE_TESTING
ARCHIVE
QUARANTINE
KILL
```

Avoid language like:

```text
WINNER
EDGE CONFIRMED
READY TO TRADE
PROFITABLE SYSTEM
```

### Decision hierarchy

```text
Replay can suggest questions.
Evidence Card can recommend review.
Audit can decide next status.
Human gate can approve promotion/release/scope expansion.
```

---

## 20. Promotion / repair / archive / quarantine / kill decision rules

### `PROMOTE_FOR_NEXT_TEST`

Allowed only when:

```text
compiled spec matches tested logic
dataset/capability constraints are recorded
aggregate result is present
null/baseline result is present or explicitly justified
ablation result is present or explicitly deferred with reason
sample size is sufficient for the next phase
limitations are visible
audit finds no blocking issue
```

Promotion here does **not** mean market edge. It means the candidate may guide the next research step.

### `REPAIR_REQUIRED`

Use when:

```text
direction is plausible but replay labels are missing
dataset capability status is unclear
nulls/ablations are missing
metric context is insufficient
ambiguity is hidden
artifact references are broken
copy overclaims result
```

### `CONTINUE_TESTING`

Use when:

```text
evidence is insufficient
sample size is too small
results are mixed
nulls/ablations are inconclusive
additional dataset/split/regime test is needed
```

### `ARCHIVE`

Use when:

```text
candidate is not active now
artifact is useful as history
result is weak but not dangerous
better candidates supersede it
```

### `QUARANTINE`

Use when:

```text
data source is unverified
logic may contain leakage
artifact references conflict
name/source/licensing/legal/privacy review is needed
generated logic is untrusted
result interpretation is risky
```

### `KILL`

Use when:

```text
fatal claim failed
leakage cannot be repaired
dataset cannot support the test
candidate fails meaningful nulls/ablations
result depends on impossible execution assumptions
strategy interpretation is materially misleading
```

---

## 21. ResearchCore Engine artifact boundary

ResearchCore Engine artifacts remain canonical run outputs.

NullForge may:

```text
read allowed artifact metadata
index artifact paths in the local workspace
render derived Evidence Cards
render replay examples from allowed data slices
link back to source artifacts
```

NullForge must not:

```text
silently mutate engine artifacts
rewrite ResearchCore Engine run outputs for UI convenience
treat UI state as canonical run evidence
hide source artifact paths
promote a result whose source artifacts are missing
```

### Artifact reference rule

Every Evidence Card and replay must be able to answer:

```text
Which ResearchCore Engine run produced this?
Which dataset/capability map was used?
Which compiled logic spec was tested?
Which test plan governed the run?
Where are the source artifacts?
```

---

## 22. UI states for Visual Replay and Evidence Cards

### Visual Replay UI states

| State | Meaning | User-facing behavior |
|---|---|---|
| `NO_REPLAY_AVAILABLE` | No examples indexed. | Show why and link to Evidence Card/test plan. |
| `LOADING_REPLAY` | Loading bounded data slice. | Show source artifact and window. |
| `REPLAY_READY` | Example can render. | Show chart, labels, source, limitation panel. |
| `AMBIGUITY_PRESENT` | Intrabar/path ambiguity exists. | Show visible badge and explanation. |
| `UNSUPPORTED_REPLAY` | Dataset cannot support displayed claim. | Block or show non-authoritative sketch. |
| `SOURCE_MISSING` | Required artifact missing. | Block promotion and trigger repair. |
| `QUARANTINED_REPLAY` | Replay exists but cannot govern. | Show quarantine reason. |

### Evidence Card UI states

| State | Meaning | User-facing behavior |
|---|---|---|
| `DRAFT` | Card not complete. | Show missing fields. |
| `RUN_INDEXED` | Run artifacts found. | Show metadata, not evidence decision. |
| `EVIDENCE_READY` | Required result sections populated. | Show audit-ready status. |
| `AUDIT_PENDING` | Evidence ready but not audited. | Disable promotion language. |
| `REPAIR_REQUIRED` | Audit or validation found defects. | Show repair list. |
| `PROMOTED_FOR_NEXT_TEST` | Audit passed for next research step. | Show next test/ticket, not trading claim. |
| `CONTINUE_TESTING` | Evidence insufficient. | Show next evidence needed. |
| `ARCHIVED` | Preserved without active authority. | Read-only view. |
| `QUARANTINED` | Risk/conflict unresolved. | Block promotion and show review need. |
| `KILLED` | Fatal condition met. | Preserve record, remove from active flow. |

---

## 23. Validation/test strategy for replay/evidence surfaces

Volume 6 enables later validation tests. It does not implement them.

### Replay surface tests

| Test | Purpose |
|---|---|
| Label completeness test | Every replay shows signal, known_at, entry, SL/TP, exit, and path status if relevant. |
| No-leakage display test | Future outcome region is visually/textually separated from known-at information. |
| Ambiguity badge test | Ambiguous first-hit cases are visibly marked. |
| Source artifact link test | Replay links back to run/dataset/spec/test artifacts. |
| Selection reason test | Every example has a recorded selection reason. |
| Non-overclaim copy test | Replay copy does not imply proof/edge/advice. |

### Evidence Card tests

| Test | Purpose |
|---|---|
| Required field validation | Card cannot become evidence-ready with missing core fields. |
| Null/baseline panel test | Evidence card shows nulls or missing-null warning. |
| Ablation panel test | Evidence card shows ablations or missing-ablation warning. |
| Limitation panel test | Data, execution, logic, and test limitations are visible. |
| Decision gating test | Promotion is blocked if audit pending or blocking evidence missing. |
| Artifact traceability test | Card links back to ResearchCore Engine artifacts. |

### User interpretation test

Manual test:

```text
Show the Evidence Card and replay to the first user.
Ask:
- What was known at signal time?
- Does this one chart prove the candidate works?
- What are the main limitations?
- What null/baseline did it beat or fail?
- What is the allowed next decision?

Pass if the user correctly understands that replay explains one case and the Evidence Card/audit controls promotion.
```

---

## 24. QA/security/human gates for result presentation

Human gate required before:

```text
public result export/share feature
financial-performance wording
candidate promotion wording
live-trading or broker wording
changing null/baseline display requirements
hiding ambiguity or limitations
changing EvidenceCard decision rules
publishing screenshots from proprietary datasets
using full ES.zip-derived examples in docs
external upload/cloud sharing of results
AI-generated interpretation copy
```

Security/privacy gate required before:

```text
exporting result bundles
sharing chart images
including dataset paths in screenshots
embedding raw data rows in reports
opening external links from artifacts
adding file watchers over arbitrary directories
```

QA gate required before:

```text
EvidenceCard status can move to EVIDENCE_READY
VisualReplay can display trade labels
audit decision can display PROMOTED_FOR_NEXT_TEST
result summary can be exported
```

---

## 25. Risks and reversal conditions

| Risk | Severity | Mitigation | Reversal condition |
|---|---:|---|---|
| Replay creates false confidence | High | Replay subordinate to Evidence Card; balanced examples; no promotion from replay. | Remove or hide replay until evidence card gating works. |
| Ambiguity hidden or misunderstood | High | Visible ambiguity badge, explanation, and DatasetCapabilityMap link. | Block first-hit replay claims without lower-timeframe/tick data. |
| Evidence Cards overclaim results | High | Required limitations, nulls, ablations, decision status. | Revert to raw artifact browser until copy/gating repaired. |
| Metrics become leaderboard/hype UI | Medium/High | Avoid winner language; require sample/null/limitation context. | Remove ranking/comparison UI until audit doctrine is implemented. |
| Source artifacts drift or disappear | Medium | Artifact traceability required. | Mark cards `SOURCE_MISSING` and block promotion. |
| Proprietary data leaks through screenshots | Medium/High | Export/share gates and local-only defaults. | Disable export until data policy and review exist. |
| User confuses research with financial advice | High | Explicit non-advice copy and no live-trading readiness language. | Remove performance-focused language and require safety review. |

---

## 26. ADRs to create later

Volume 6 recommends these ADRs later:

| ADR | Decision |
|---|---|
| `ADR-VR-001` | Visual Replay is explanatory and cannot promote candidates. |
| `ADR-EV-001` | Evidence Card is required before audit decision UX. |
| `ADR-EV-002` | Nulls and ablations are first-class display requirements. |
| `ADR-VR-002` | Intrabar ambiguity must be visible on replay surfaces. |
| `ADR-RI-001` | Result interpretation copy must avoid financial advice/live-trading claims. |
| `ADR-EXPORT-001` | Result export/share is deferred until data/legal/privacy review. |

---

## 27. First milestone category enabled by this volume

Volume 6 enables this future milestone category:

```text
M6 — Visual Replay + Evidence Card Specification and Fixture Proof
```

Purpose:

```text
Create the first non-production replay/evidence fixture flow that can show one bounded example and one evidence card placeholder without making strategy-validity claims.
```

Expected future milestone shape:

```text
docs/specs/visual_replay_contract.md
docs/specs/evidence_card_contract.md
docs/specs/result_interpretation_boundary.md
design/replay_fixture_notes.md
tests/fixtures/replay_fixture_manifest.md
```

Do not generate implementation tickets yet.

Volume 7 will decide how this milestone fits into the overall roadmap.

---

## 28. What must not be built yet

Do not build yet:

```text
production charting engine
real trade replay renderer
performance leaderboard
candidate ranking UI
export/share system
public report generator
AI result interpreter
broker/live trading bridge
portfolio/risk management system
social sharing
paid reports
cloud storage of results
full EvidenceCard database
```

Do not create a screen that visually suggests:

```text
candidate approved for trading
live execution ready
future profit expected
financial advice
```

Do not build replay before the upstream contracts exist:

```text
DatasetCapabilityMap
LogicCard
CompiledLogicSpec
TestPlan
ResearchCore Engine run artifact boundary
EvidenceCard schema
audit decision rules
```

---

## 29. Volume 6 closeout

### Decisions promoted by this volume

```text
Visual Replay is an explanation surface, not a proof surface.
Evidence Card is the required evidence summary surface.
Replay examples must show known-at-time, signal, entry, SL, TP, exit, and ambiguity labels.
Evidence Cards must show nulls, baselines, ablations, sample size, failures, limitations, and audit status.
No candidate can be promoted from replay alone.
No result screen may imply financial advice, guaranteed edge, or live-trading readiness.
ResearchCore Engine artifacts remain canonical run output.
```

### Open items for Volume 7

```text
Roadmap and milestone sequencing.
First ticket/milestone batch design.
Where Visual Replay and Evidence Card contracts enter the ticket backlog.
How to order desktop bridge, dataset fixture, logic compiler, replay fixture, and evidence card proof.
Which docs-only setup tickets must happen before implementation.
```

### Status

```text
Decision:
PROMOTE_TO_VOLUME_7_AFTER_REVIEW
```

---

## 30. Prompt for Volume 7

Use the following prompt next.

```md
# Prompt for Volume 7 — NullForge Roadmap, Milestones, Ticket Backlog, Codex Prompt Packs, and First Execution Batch

You are my ForgeIT Project Factory volume writer, roadmap architect, milestone-batch planner, ticket backlog designer, Codex prompt-pack generator, source-of-truth guardian, QA/human gate designer, and anti-context-soup auditor.

Use the uploaded App Forge + Project Factory + Autonomous Codex Role Loop sources as governing context.

Do not generate implementation code.
Do not start implementation.
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

Volume 6 status:

```text
Volume 6 — NullForge Visual Replay, Evidence Cards, Audit Decision UX, and Result Interpretation Boundaries has been generated as draft canonical project source.
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

Key boundaries from Volumes 3–6:

```text
Windows 11 x64 first.
Tauri + React + TypeScript.
ResearchCore Engine is a scoped Python sidecar / command bridge.
No arbitrary shell execution.
DatasetCapabilityMap before timeframe/chart/test generation.
5m OHLCV can aggregate upward but cannot reconstruct true 1m/tick data.
Generated logic is not evidence.
A LogicCard is not runnable until compiled.
A passing compile is not market edge.
Visual replay explains examples; aggregate evidence decides.
EvidenceCard must show nulls, ablations, sample size, failure modes, and limitations.
No result screen may imply financial advice, guaranteed edge, or live-trading readiness.
```

## Mission

Generate Volume 7 only:

```text
Volume 7 — NullForge Roadmap, Milestones, Ticket Backlog, Codex Prompt Packs, and First Execution Batch
```

This volume should convert Volumes 0–6 into an implementation-ready roadmap and milestone system without generating implementation code.

## Required sections

Include:

1. Volume purpose.
2. Relationship to Volumes 0–6.
3. Roadmap philosophy.
4. MVP vertical slice recap.
5. Active source-of-truth docs to create in repo.
6. Recommended milestone map.
7. Milestone dependency order.
8. Ticket namespace policy recap.
9. First 30–40 ticket backlog.
10. Ticket acceptance template.
11. Milestone batching policy.
12. M0 first milestone package plan.
13. M1 desktop bridge proof package plan.
14. M2 Dataset Studio fixture/capability proof package plan.
15. M3 Logic Factory compiler proof package plan.
16. M4 Visual Replay fixture proof package plan.
17. M5 Evidence Card/audit placeholder proof package plan.
18. M6 Windows packaging spike package plan.
19. Context Curator prompt pattern for NullForge tickets.
20. Planner prompt pattern for NullForge tickets.
21. Implementor prompt pattern for NullForge tickets.
22. Auditor prompt pattern for NullForge tickets.
23. Human gate and stop-condition matrix.
24. QA/test command discovery plan.
25. First milestone handoff template.
26. What should happen before Codex implementation begins.
27. What should not be automated.
28. Volume 7 closeout.
29. Exact next prompt for the first milestone batch or repo-source import pass.

## Required boundaries

Preserve these boundaries:

```text
No implementation code.
No broad “build the app” prompt.
No all-at-once autonomous build.
Milestone prompts may be batched, but tickets execute serially.
Each ticket needs scope, acceptance, tests, report, audit, and gate handling.
Do not generate live trading, AI strategy generation, cloud sync, auth, billing, marketplace, mobile, or public release tickets as MVP implementation.
Do not commit full ES.zip.
Do not treat generated volumes as repo truth until promoted into the repo through a setup/import ticket.
```

## Response rules

Return Volume 7 as structured Markdown content or downloadable Markdown files if files are requested.
Do not generate implementation code.
Do not start Codex execution.
Do not create a broad build prompt.
Keep the output detailed enough to become a canonical project source.
End with the exact next prompt for the first milestone batch or repo-source import pass.
```
