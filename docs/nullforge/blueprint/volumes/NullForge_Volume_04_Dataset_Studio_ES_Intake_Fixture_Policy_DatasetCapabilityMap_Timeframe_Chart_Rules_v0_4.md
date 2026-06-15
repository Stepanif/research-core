> Import note: This file was imported by PF-T001 from `NullForge_Volume_04_v0_4_Package.zip` / `NullForge_Volume_04_v0_4_Package/artifacts/NullForge_Volume_04_Dataset_Studio_ES_Intake_Fixture_Policy_DatasetCapabilityMap_Timeframe_Chart_Rules_v0_4.md` on `2026-06-15`.
> Authority: repo-managed NullForge planning/workflow source after PF-T001 audit. It is not ResearchCore Engine implementation truth.
> Source package SHA256: `2C2783429B77016199B2F515C5CB95F6432C78CF12982DAA77557ACC9312715A`

# Volume 4 — NullForge Dataset Studio, ES.zip Intake Boundary, Fixture Policy, DatasetCapabilityMap, Timeframe/Chart Capability Rules v0.4

```text
Project: NullForge
Existing repo / engine: research-core
Internal engine label: ResearchCore Engine
Platform target: Windows 11 x64
Desktop stack: Tauri + React + TypeScript
Engine boundary: Existing Python ResearchCore Engine as local sidecar / command bridge
Volume status: Draft canonical project source
```

---

## 1. Volume purpose

Volume 4 defines how NullForge handles local dataset intake before any dataset import implementation begins.

It exists to prevent a dangerous product drift:

```text
user uploads data
→ app pretends all chart types / timeframes / tests are lawful
→ visual outputs look convincing
→ weak or impossible evidence gets trusted
```

The correct NullForge path is:

```text
dataset selected
→ source preserved
→ schema detected
→ user confirms timestamp / timezone / session assumptions
→ data quality checked
→ DatasetCapabilityMap generated
→ only lawful transformations and tests become selectable
```

Volume 4 is not a data parser implementation. It is the governing boundary for Dataset Studio, fixture policy, and capability mapping.

---

## 2. Relationship to Volumes 0, 1, 2, and 3

| Prior volume | What it established | How Volume 4 uses it |
|---|---|---|
| Volume 0 | NullForge mission, doctrine, claims, MVP cutline, anti-goals | Dataset Studio serves the first proof loop and enforces “DatasetCapabilityMap gates chart/timeframe/test claims.” |
| Volume 1 | Repo/workspace/source-of-truth/archive/quarantine policy | Full raw data stays local/outside repo; fixtures and manifests follow source-of-truth rules. |
| Volume 2 | Planner / Implementor / Auditor loop, QA gates, human gates | Dataset work must be ticketed, scoped, audited, and human-gated when file access/data boundaries change. |
| Volume 3 | Windows + Tauri desktop architecture and ResearchCore Engine bridge | Dataset Studio must respect Tauri file permissions, local workspace boundaries, and engine bridge constraints. |

Volume 4 is the data/access volume. It turns “upload datasets and generate timeframes/charts” into an explicit access-governed workflow.

---

## 3. Dataset Studio product role

Dataset Studio is the NullForge surface for making local data usable without pretending the data can do things it cannot do.

Dataset Studio owns:

```text
file selection
dataset registration
schema detection
column mapping
timestamp/timezone/session confirmation
data quality checks
fixture slicing
dataset manifest generation
DatasetCapabilityMap generation
quarantine of unsafe/ambiguous data
presentation of lawful next actions
```

Dataset Studio does not own:

```text
market edge claims
candidate validity
ResearchCore Engine internals
live data feeds
broker connections
cloud storage
data licensing judgment beyond project-level flags
public dataset redistribution decisions
```

## 3.1 Product principle

```text
Dataset Studio tells the truth about the data before NullForge asks the data to prove anything.
```

---

## 4. First data domain and ES.zip boundary

The first data domain is local OHLCV market data, with ES as the first realistic test domain.

The user may provide:

```text
ES.zip
```

expected to contain multi-year ES OHLCV data. This is not yet a committed project asset. It is a local source input.

## 4.1 ES.zip boundary

| Object | Location | Authority | Repo policy |
|---|---|---|---|
| Full `ES.zip` | User local machine or local NullForge workspace raw-data area | Source input only | Do not commit |
| Extracted full raw ES files | User workspace only | Raw local data | Do not commit |
| Imported/canonical ES data | User workspace only unless intentionally sampled | Derived local working data | Do not commit by default |
| Tiny fixture derived from ES | `data/fixtures/` or equivalent only if license-safe | Test fixture | Commit only after human approval |
| Synthetic OHLCV fixture | Repo test data | Safe deterministic fixture | Preferred for public tests |
| Manifest / capability map | Repo docs or workspace depending on source | Evidence/control artifact | Commit docs only if no restricted data leaks |

## 4.2 Working policy

```text
Full ES.zip is allowed as local test input.
Full ES.zip is not repo truth.
Full ES.zip is not public fixture material.
Any ES-derived fixture must pass a human license-safety gate before commit.
Synthetic fixtures should be preferred for repo tests.
```

---

## 5. Raw data, imported data, canonical data, fixture data, and derived data definitions

| Data class | Meaning | Mutability | Example | Source-of-truth status |
|---|---|---:|---|---|
| Raw data | User-provided file exactly as selected/imported | Immutable | `ES.zip`, raw CSV export | Preserve; never silently mutate |
| Imported data | Local workspace copy or registered reference with import metadata | Append-only metadata | Extracted CSV in workspace | Local working object |
| Canonical data | Normalized data with explicit schema, timezone/session assumptions, hashes, and checks | Regenerated from raw/imported | normalized OHLCV parquet/csv | Engine/workspace artifact |
| Fixture data | Small, intentional sample for tests or UI/demo | Versioned and audited | `synthetic_ohlcv_tiny.csv`, `es_5m_tiny_fixture.csv` | Commit only if safe |
| Derived data | Timeframes/chart inputs/features generated from canonical data | Regenerated, not edited | 15m candles, Heikin-Ashi, capability report | Artifact, not raw source |
| Quarantined data | Data blocked from normal use due to ambiguity/risk | Locked until reviewed | missing timestamps, unknown timezone | No active authority |

## 5.1 Mutation rule

```text
Raw source files are never mutated.
Derived/canonical artifacts are regenerated, not hand-edited.
Quarantined data cannot drive tests until reviewed and promoted.
```

---

## 6. Full ES.zip policy

## 6.1 Full ES.zip may be used for

```text
local import tests
local fixture slicing
local schema inspection
local performance/load checks
local ResearchCore Engine compatibility tests
private manual analysis
```

## 6.2 Full ES.zip must not be used for

```text
repo commits
public package assets
screenshots containing licensed/proprietary raw rows unless approved
automatic cloud upload
default test suite dependency
benchmark claims without manifest and provenance
```

## 6.3 Full ES.zip import options

NullForge may support two local modes later:

| Mode | Meaning | MVP preference |
|---|---|---|
| Reference-only | User selects file; app stores path + hash + metadata | Good for very large files |
| Workspace copy | App copies selected file into `NullForge_Workspace/datasets/raw/` | Good for smaller fixtures |

MVP should prefer explicit user choice. The app must tell the user whether it is copying data or referencing an external path.

## 6.4 Deletion boundary

NullForge may delete its own generated derived artifacts after user confirmation.

NullForge must not delete, overwrite, or mutate the original `ES.zip`.

---

## 7. Fixture policy and license-safety rule

## 7.1 Fixture ladder

| Fixture | Preferred source | Purpose | Commit to repo? |
|---|---|---|---|
| `synthetic_ohlcv_tiny` | Generated deterministic synthetic data | Unit tests, UI smoke, capability logic | Yes |
| `synthetic_ohlcv_bad_rows` | Generated invalid rows | Quarantine/error-state tests | Yes |
| `synthetic_ohlcv_gaps_duplicates` | Generated synthetic edge cases | Quality checks | Yes |
| `es_ohlcv_tiny_private` | Local slice from ES.zip | Real-schema smoke on user machine | No by default |
| `es_ohlcv_public_fixture` | ES-derived sample only if license-safe | Optional integration fixture | Human approval required |

## 7.2 License-safety rule

An ES-derived fixture may be committed only if:

```text
- source rights allow redistribution or internal repo use;
- fixture contains the minimum number of rows needed;
- raw source vendor/license terms are recorded;
- no restricted metadata is leaked;
- human gate approves the commit;
- manifest records source, slice rule, hash, and reason.
```

If license status is unknown, the fixture is treated as:

```text
LOCAL_ONLY
```

## 7.3 Preferred public fixtures

For public or portable tests, use deterministic synthetic OHLCV fixtures that are generated or committed with clear provenance.

---

## 8. Dataset import workflow

## 8.1 MVP import workflow

```text
1. User opens Dataset Studio.
2. User chooses “Import dataset” or “Use sample fixture.”
3. App prompts user to select a file/folder.
4. App records selected path, file name, size, modified time, and hash.
5. App detects file type: zip/csv/parquet/json/folder/unknown.
6. If zip: app lists contained files without extracting all by default.
7. User selects intended data file if multiple are present.
8. App previews first safe sample rows.
9. App detects likely columns.
10. User confirms column mapping.
11. User confirms timestamp/timezone/session assumptions.
12. App runs data quality checks.
13. App writes dataset manifest.
14. App writes DatasetCapabilityMap.
15. App unlocks only lawful next actions.
```

## 8.2 Import states

```text
EMPTY
SELECTING_FILE
SCANNING
FILE_TYPE_DETECTED
MULTI_FILE_SELECTION_REQUIRED
SCHEMA_DETECTED
MAPPING_REQUIRED
TIMEZONE_CONFIRMATION_REQUIRED
SESSION_CONFIRMATION_REQUIRED
QUALITY_CHECK_RUNNING
QUALITY_WARNINGS
QUARANTINED
MANIFEST_READY
CAPABILITY_MAP_READY
IMPORTED
ERROR
```

## 8.3 Import must preserve

```text
source path or imported workspace path
source file hash
detected schema
user-confirmed mapping
timezone/session assumptions
quality check results
capability map version
engine/tool version if used
```

---

## 9. Schema detection workflow

## 9.1 Detection inputs

Dataset Studio should inspect:

```text
file extension
delimiter
header row
row count estimate
column names
sample rows
date/time fields
numeric fields
compression/container type
encoding
```

## 9.2 Detection outputs

```text
detected_file_type
detected_columns
candidate_timestamp_columns
candidate_ohlcv_columns
candidate_instrument_column
candidate_timezone_source
confidence_by_field
warnings
required_user_confirmations
```

## 9.3 Detection confidence

| Confidence | Meaning | Action |
|---|---|---|
| `HIGH` | Column is obvious and sample values match expected type | Preselect but allow override |
| `MEDIUM` | Likely match but name/type is ambiguous | Ask confirmation |
| `LOW` | Possible match only | Do not auto-accept |
| `NONE` | No suitable field found | Block or quarantine |

## 9.4 Schema detection cannot infer everything

Dataset Studio must not silently infer:

```text
timezone
session calendar
instrument identity
exchange holiday handling
intrabar sequence
data vendor rights
tick/trade source quality
```

These require explicit metadata, user confirmation, or quarantine.

---

## 10. Required OHLCV fields and optional fields

## 10.1 Minimum fields for OHLCV candles

| Field | Required? | Notes |
|---|---:|---|
| `timestamp` | Yes | May be single datetime or date+time pair. |
| `open` | Yes | Numeric. |
| `high` | Yes | Numeric. |
| `low` | Yes | Numeric. |
| `close` | Yes | Numeric. |
| `volume` | Preferred / conditional | Required for volume features, VWAP approximations, volume charts. |

## 10.2 Acceptable aliases

| Canonical field | Common aliases |
|---|---|
| `timestamp` | `datetime`, `date_time`, `time`, `DateTime`, `Date Time` |
| `date` | `Date`, `trade_date`, `session_date` |
| `time` | `Time`, `bar_time` |
| `open` | `Open`, `O`, `open_price` |
| `high` | `High`, `H`, `high_price` |
| `low` | `Low`, `L`, `low_price` |
| `close` | `Close`, `C`, `last`, `close_price` |
| `volume` | `Volume`, `Vol`, `V`, `total_volume` |
| `up_volume` | `Up`, `up`, `up_vol` |
| `down_volume` | `Down`, `down`, `down_vol` |

## 10.3 Optional fields

| Field | Why useful | Capability unlocked |
|---|---|---|
| `instrument` | Disambiguates symbol/source | Multi-instrument import |
| `timezone` | Removes ambiguity | Session-aware aggregation |
| `session_id` | Already-labeled sessions | Session tests |
| `bid` / `ask` | Spread/order analysis | Limited bid/ask features |
| `tick_count` | Activity proxy | Tick count features, not true tick bars |
| `open_interest` | Futures context | OI features |
| `up_volume` / `down_volume` | Directional volume proxy | Up/down volume features |
| `trade_id` / per-trade records | Tick/trade data | Tick/volume/range bars, more exact path |

## 10.4 Field invariant rules

At minimum:

```text
high >= open
high >= close
low <= open
low <= close
high >= low
timestamp not null
open/high/low/close numeric and finite
volume numeric and nonnegative if present
```

Violation of these invariants triggers warning or quarantine depending on severity.

---

## 11. Timestamp, timezone, session, and calendar confirmation rules

## 11.1 Timestamp rules

Dataset Studio must determine:

```text
whether timestamps are timezone-aware
whether timestamps are bar open or bar close
whether date and time are separate columns
whether timestamps are sorted
whether duplicate timestamps exist
whether timestamps match expected interval
```

## 11.2 Timezone rules

| Timezone state | Action |
|---|---|
| Explicit timezone in data/metadata | Record and use after confirmation |
| Known source convention | Ask user to confirm |
| User-supplied timezone | Record assumption |
| Unknown timezone | Block session-specific capabilities until confirmed |
| Conflicting timezone evidence | Quarantine |

For ES, the project may commonly use `America/New_York` for RTH workflow assumptions, but Dataset Studio must not silently impose it on imported data.

## 11.3 Session rules

Dataset Studio must distinguish:

```text
RTH
ETH
24h
custom session
unknown session
```

Session-dependent capabilities require a confirmed session policy.

## 11.4 Calendar rules

Session-aware daily candles, holidays, partial days, and RTH filters require a calendar policy.

MVP may support simple user-confirmed session windows before a full exchange calendar engine.

## 11.5 Bar timestamp convention

Dataset Studio must record whether the timestamp means:

```text
bar_open_time
bar_close_time
unknown
```

If unknown, visual replay and signal timing must label it.

---

## 12. Dataset manifest draft

Each imported/canonical dataset should have a manifest.

```yaml
dataset_id: "ds_YYYYMMDD_hash_short"
manifest_version: "0.1"
created_at: "YYYY-MM-DDTHH:MM:SS"
created_by: "NullForge Dataset Studio"
source:
  mode: "reference_only | workspace_copy | synthetic_fixture"
  original_filename: "ES.zip"
  original_path_recorded: true
  source_hash_sha256: "<hash>"
  source_size_bytes: 0
  source_modified_time: "YYYY-MM-DDTHH:MM:SS"
  license_status: "unknown | local_only | redistributable | restricted"
  provenance_notes: ""
container:
  type: "zip | csv | parquet | folder | unknown"
  selected_member: ""
schema:
  data_kind: "ohlcv_candles | tick_trades | unknown"
  instrument: "ES"
  timeframe_detected: "5m | 1m | unknown"
  timestamp_column: ""
  timestamp_timezone: "unknown"
  timestamp_convention: "bar_open_time | bar_close_time | unknown"
  open_column: ""
  high_column: ""
  low_column: ""
  close_column: ""
  volume_column: ""
  optional_columns: []
session:
  session_type: "RTH | ETH | 24h | custom | unknown"
  timezone: "America/New_York | unknown | other"
  session_window: ""
  calendar_policy: "simple | exchange_calendar | unknown"
quality:
  row_count: 0
  duplicate_timestamps: 0
  missing_timestamps: 0
  gap_count: 0
  ohlc_invariant_violations: 0
  null_count_by_field: {}
  warnings: []
  quarantine_status: "CLEAR | WARNING | QUARANTINE"
capability_map:
  path: "capability_maps/<dataset_id>.capability.json"
  version: "0.1"
derived_outputs:
  canonical_path: ""
  fixtures: []
  generated_timeframes: []
audit:
  human_confirmations:
    timezone: false
    session: false
    license_status: false
  notes: ""
```

## 12.1 Manifest rule

```text
No canonical dataset without a manifest.
No capability map without a manifest.
No fixture without source and slice rule.
```

---

## 13. DatasetCapabilityMap purpose

The DatasetCapabilityMap is the authoritative answer to:

```text
What can this dataset lawfully support?
What is approximate?
What is ambiguous?
What is blocked?
What requires confirmation?
```

It gates:

```text
timeframe generation
chart type selection
feature availability
test-plan eligibility
visual replay labels
SL/TP path certainty
logic compiler inputs
```

It does not prove:

```text
strategy validity
market edge
profitability
data vendor accuracy
future performance
```

---

## 14. DatasetCapabilityMap statuses

| Status | Meaning | UI behavior |
|---|---|---|
| `YES` | Supported by available fields and confirmed assumptions | Enable |
| `NO` | Not supported by available data | Disable |
| `APPROXIMATE` | Can be generated but with known distortion | Enable only with warning |
| `AMBIGUOUS` | Data cannot determine the result uniquely | Disable for hard claims; allow labeled exploratory view |
| `REQUIRES_CONFIRMATION` | Needs user-confirmed metadata first | Prompt confirmation |
| `QUARANTINE` | Dataset issue blocks normal use | Block until repaired/reviewed |
| `DEFERRED` | Plausible later, not in MVP | Hide or show as not built |
| `UNKNOWN` | Detection inconclusive | Require review |

## 14.1 Capability map draft shape

```json
{
  "dataset_id": "ds_...",
  "capability_map_version": "0.1",
  "source_manifest": "datasets/manifests/ds_....yaml",
  "data_kind": "ohlcv_candles",
  "base_timeframe": "5m",
  "confirmed": {
    "timezone": false,
    "session": false,
    "timestamp_convention": false
  },
  "capabilities": {
    "timeframes": [],
    "chart_types": [],
    "features": [],
    "path_resolution": []
  },
  "warnings": [],
  "blocked_reasons": []
}
```

---

## 15. Capability rules for OHLCV timeframes

## 15.1 Timeframe principle

```text
Candle data can aggregate upward.
Candle data cannot reconstruct truthful lower-timeframe or tick-level data.
```

## 15.2 Upward aggregation

| Source | Target | Status | Conditions |
|---|---|---|---|
| 1m OHLCV | 5m / 15m / 30m / 60m | `YES` | Timestamps sorted, no blocking gaps, timezone confirmed if session-aware |
| 5m OHLCV | 15m / 30m / 60m | `YES` | Target is integer multiple; alignment confirmed |
| 5m OHLCV | Daily session candles | `REQUIRES_CONFIRMATION` | Timezone + session/calendar confirmed |
| 15m OHLCV | 30m / 60m | `YES` | Alignment confirmed |
| Any intraday OHLCV | Weekly/monthly | `DEFERRED` for MVP | Later if calendar policy exists |

## 15.3 Downward reconstruction

| Source | Target | Status | Reason |
|---|---|---|---|
| 5m OHLCV | 1m candles | `NO` | Lower-timeframe path is not present |
| 60m OHLCV | 5m candles | `NO` | Lower-timeframe path is not present |
| Daily OHLCV | Intraday candles | `NO` | Intraday path is not present |
| OHLCV candles | Tick data | `NO` | Trades are not present |

## 15.4 Non-integer / irregular target timeframes

| Case | Status |
|---|---|
| Target timeframe is integer multiple of base and aligned | `YES` |
| Target timeframe is integer multiple but alignment unknown | `REQUIRES_CONFIRMATION` |
| Target timeframe is non-integer or session-crossing | `AMBIGUOUS` or `DEFERRED` |
| Target requires exchange calendar not configured | `REQUIRES_CONFIRMATION` |

## 15.5 Aggregation formulas

For upward OHLCV aggregation:

```text
open = first open in group
high = max high in group
low = min low in group
close = last close in group
volume = sum volume, if available
timestamp = group open or close time according to chosen convention
```

The timestamp convention must be recorded.

---

## 16. Capability rules for chart types

## 16.1 Time-based charts

| Chart type | Required data | Status from 5m OHLCV | Notes |
|---|---|---|---|
| Candlestick | OHLC | `YES` | Base timeframe only or lawful upward aggregates |
| OHLC bars | OHLC | `YES` | Same as candlestick |
| Line chart | Close | `YES` | Close-only display |
| Area chart | Close | `YES` | Display-only |
| Volume bars under candles | Volume | `YES` if volume present | Not volume-bar chart generation |

## 16.2 Derived candle transforms

| Chart type | Required data | Status from 5m OHLCV | Notes |
|---|---|---|---|
| Heikin-Ashi | OHLC | `YES` | Derived from candle OHLC; label as transformed |
| Typical price / HLC3 | HLC | `YES` | Derived display/feature |
| Median price / HL2 | HL | `YES` | Derived display/feature |
| Session VWAP approximation | OHLCV + session | `APPROXIMATE` | Uses candle price proxy, not true trade VWAP |
| True VWAP | Tick/trade price+volume | `NO` from candles | Requires trade-level data |

## 16.3 Event/path-dependent charts

| Chart type | Required data | Status from 5m OHLCV | Notes |
|---|---|---|---|
| Tick chart | Tick/trade records | `NO` | Candle rows are not trades |
| True volume bars | Tick/trade records with volume | `NO` | Candle volume lacks event ordering |
| Range bars | Intrabar path/ticks | `NO` or `APPROXIMATE` only with warning | OHLC high/low lacks sequence |
| Renko | Tick/lower timeframe path preferred | `APPROXIMATE` from closes; `NO` for exact | Must label approximation |
| Point-and-Figure | Path/order assumptions | `APPROXIMATE` | Close/high-low method must be declared |
| Footprint / bid-ask delta | Bid/ask trade classification | `NO` | Requires orderflow data |
| Volume profile by price | Price-level volume | `NO` from OHLCV | Candle volume lacks price distribution |
| Market profile / TPO | Time-at-price or lower granularity | `APPROXIMATE` / `DEFERRED` | Not MVP |

## 16.4 Chart rule

```text
A chart can be shown only if its capability status is visible or implied by the selected view.
Approximate charts must carry an approximation badge.
Ambiguous charts must not be used as hard evidence.
```

---

## 17. Intrabar ambiguity and SL/TP first-hit boundary

## 17.1 Core issue

An OHLC candle tells:

```text
open
high
low
close
```

It does not tell the sequence inside the bar.

If both a stop-loss and take-profit are inside the same candle range, OHLC alone cannot determine which was hit first.

## 17.2 First-hit statuses

| Data available | SL/TP first-hit status |
|---|---|
| Tick/trade path | `YES`, if clean and ordered |
| Lower-timeframe bars where only one level hit per lower bar | `SUPPORTED_WITH_RESOLUTION_LIMIT` |
| 5m OHLC only, both SL and TP inside same bar | `AMBIGUOUS` |
| 5m OHLC only, only one level touched | `YES_WITH_BAR_GRANULARITY` |
| Gap through entry/exit level | `AMBIGUOUS` or rule-dependent |
| Missing bars around event | `QUARANTINE` for exact path claims |

## 17.3 Visual Replay labels

Visual Replay must label:

```text
entry_bar
exit_bar
known_at_signal
known_at_entry
sl_tp_same_bar_ambiguity
gap_ambiguity
bar_granularity_limit
requires_lower_timeframe
```

## 17.4 Test-plan boundary

If a candidate requires exact intrabar first-hit ordering, the compiler/test plan must reject or label it unless the dataset supports required path resolution.

---

## 18. Data quality checks

## 18.1 Required MVP checks

| Check | Severity if failed | Notes |
|---|---|---|
| File readable | Blocking | Cannot import otherwise |
| Expected columns present | Blocking | Missing OHLC blocks OHLCV dataset |
| Numeric OHLC | Blocking | Invalid schema |
| Timestamp parseable | Blocking | Cannot order bars |
| Duplicate timestamps | Warning/blocking depending count | Must report |
| Sort order | Repairable | Can sort derived canonical copy, not raw |
| OHLC invariants | Blocking if severe | high/low/open/close consistency |
| Null OHLC values | Blocking | Invalid bars |
| Null volume | Warning if volume optional; blocking for volume features | |
| Negative volume | Blocking for volume features | |
| Gaps vs expected interval | Warning/blocking based on size | Affects tests and timeframes |
| Timezone unknown | Blocks session-aware features | Confirm required |
| Session unknown | Blocks RTH/ETH/daily session features | Confirm required |
| Compression member ambiguity | Requires selection | Multiple CSVs in zip |
| Encoding/delimiter ambiguity | Requires confirmation | |

## 18.2 Later checks

```text
outlier detection
holiday/partial day handling
rollover/contract continuity
duplicate session labels
vendor/source drift
split/adjustment metadata if equities added later
bid/ask consistency if tick data added later
```

## 18.3 Quality report summary

Each import should produce:

```text
PASS / WARNING / QUARANTINE
row count
date range
detected timeframe
missing field summary
gap summary
duplicate summary
OHLC invariant summary
confirmation requirements
blocked capabilities
```

---

## 19. Quarantine conditions

A dataset or derived artifact must enter quarantine when:

```text
required OHLC fields are missing
timestamps cannot be parsed
timezone/session is required but unresolved
data has severe OHLC invariant violations
row order cannot be safely interpreted
file contents do not match claimed format
multiple files conflict and no user selection was made
source/license status blocks fixture publication
data appears corrupted or truncated
hash changed unexpectedly
import process cannot verify source identity
capability map cannot be produced
```

## 19.1 Quarantine record

```yaml
quarantine_id: "q_..."
dataset_id: "ds_..."
created_at: "YYYY-MM-DDTHH:MM:SS"
reason: ""
severity: "warning | blocking | fatal"
blocked_capabilities: []
repair_options: []
human_review_required: true
promotion_blocked_until: ""
```

## 19.2 Quarantine rule

```text
Quarantined data cannot drive tests, evidence cards, or promotion decisions.
```

---

## 20. Allowed MVP data operations

MVP may include:

```text
select local file
inspect zip contents safely
preview sample rows
detect columns
ask user to confirm mapping
ask user to confirm timezone/session/timestamp convention
copy or reference file with explicit choice
compute file hash
write manifest
run quality checks
generate synthetic fixture
slice a small local fixture for private testing
aggregate upward to lawful timeframes
generate DatasetCapabilityMap
show capability map in UI
block unsupported charts/timeframes
```

MVP may call ResearchCore Engine only through approved bridge commands or scoped additions created through the ticket loop.

---

## 21. Forbidden MVP data operations

MVP must not:

```text
commit full ES.zip
silently upload data to cloud
silently mutate source files
scan arbitrary drives
infer timezone/session without disclosure
generate lower timeframe data from higher timeframe candles
claim exact intrabar SL/TP order from OHLC alone
generate tick/volume/orderflow charts from candle data
treat visual replay examples as proof
redistribute ES-derived data without license review
delete user source data
auto-run heavy tests on full data without user confirmation
activate broker/live trading or live market data feed behavior
```

---

## 22. UI states for Dataset Studio

## 22.1 Main screens

| Screen | Purpose |
|---|---|
| Dataset Studio Home | List datasets, status, warnings, and next actions |
| Import Wizard | Select file/folder, inspect, map, confirm |
| Schema Mapper | Show detected columns and confidence |
| Time/Session Confirmation | Confirm timezone, session, timestamp convention |
| Quality Report | Show pass/warning/quarantine results |
| Capability Map | Show what the data can/cannot support |
| Fixture Manager | Create/list tiny fixtures with source/manifest |
| Quarantine Review | Explain blocked data and repair options |

## 22.2 Dataset status badges

```text
NEW
SCANNING
MAPPING_REQUIRED
CONFIRMATION_REQUIRED
QUALITY_WARNING
CAPABILITY_READY
QUARANTINED
LOCAL_ONLY
FIXTURE_READY
ERROR
```

## 22.3 User language

Use direct labels:

```text
Supported
Not supported
Approximate
Ambiguous
Needs confirmation
Quarantined
```

Avoid language like:

```text
Probably fine
AI inferred
Should work
Trust me
```

## 22.4 Capability map UI example

| Capability | Status | Why | Next action |
|---|---|---|---|
| 15m candles | `YES` | 5m bars aggregate upward cleanly | Enable |
| 1m candles | `NO` | 5m bars cannot reconstruct 1m bars | Disable |
| Session daily candles | `REQUIRES_CONFIRMATION` | Timezone/session not confirmed | Ask user |
| True VWAP | `NO` | Trade-level data unavailable | Disable |
| Renko from closes | `APPROXIMATE` | Uses close-only transform | Show warning |
| SL/TP first-hit same-bar | `AMBIGUOUS` | OHLC sequence unknown | Require lower timeframe |

---

## 23. ResearchCore Engine boundary for dataset operations

## 23.1 Engine owns or may own

```text
canonicalization
schema validation
quality checks
manifest generation
fixture slicing
capability map generation
artifact hashing
report writing
```

## 23.2 NullForge owns

```text
user file selection
workspace selection
display of import states
confirmation prompts
showing quality/capability results
calling approved engine commands
recording UI-side audit metadata
```

## 23.3 Bridge rule

NullForge should call the ResearchCore Engine through a narrow command bridge, not through arbitrary shell execution.

Desired command families may include later:

```text
research-core --version
research-core dataset inspect
research-core dataset manifest
research-core dataset quality-check
research-core dataset capability-map
research-core dataset slice-fixture
```

These command names are design targets, not claims that the existing engine already supports them.

If the current `research-core` CLI lacks a needed command, implementation tickets must either:

```text
adapt to an existing command safely; or
create a scoped engine-side command through the role-loop; or
defer the feature.
```

## 23.4 No silent engine rewrite

```text
Do not rewrite ResearchCore Engine internals just to make Dataset Studio convenient.
```

---

## 24. Validation/test strategy for Dataset Studio

## 24.1 First test ladder

| Test | Claim tested | Input | Expected result |
|---|---|---|---|
| Synthetic valid OHLCV import | Dataset Studio can detect clean data | tiny synthetic CSV | Manifest + capability map |
| Missing timestamp fixture | Quarantine works | synthetic bad CSV | Quarantine with reason |
| Duplicate timestamp fixture | Quality warnings work | synthetic duplicate CSV | Warning or quarantine |
| 5m → 15m capability | Upward aggregation capability is lawful | 5m fixture | 15m `YES` |
| 5m → 1m capability | Downward reconstruction is blocked | 5m fixture | 1m `NO` |
| Missing timezone | Confirmation gate works | fixture with naive timestamps | session daily `REQUIRES_CONFIRMATION` |
| Same-bar SL/TP ambiguity fixture | Intrabar ambiguity is labeled | OHLC fixture with both levels touched | `AMBIGUOUS` label |
| Full ES.zip private smoke | Real local file can be inspected without repo bloat | local ES.zip | local manifest only |

## 24.2 Success criteria

Dataset Studio planning is ready for implementation when:

```text
manifest contract exists
capability statuses are defined
MVP allowed/forbidden operations are clear
quarantine conditions are explicit
fixture policy is defined
human gates for data/license/file access are clear
```

## 24.3 What this validation does not prove

```text
It does not prove market edge.
It does not prove strategy validity.
It does not prove vendor data accuracy.
It does not prove full-data performance.
It does not prove user retention.
```

---

## 25. QA/security/human gates for data work

Human approval required before:

```text
committing any ES-derived fixture
changing file access scope
adding cloud upload/sync
adding external data APIs
adding background scanning
adding deletion behavior
adding full ES.zip processing by default
adding new dependency for parsing/compression/storage
changing manifest/capability map contract
publishing screenshots or examples from licensed data
using imported data in public demos
claiming exact path resolution from candle data
```

Security/data review required before:

```text
broad filesystem permissions
recursive folder import
external connectors
compressed archive extraction changes
automatic deletion/cleanup
large file memory-mapping behavior
user data export/import behavior
```

QA gate requires:

```text
fixtures for valid and invalid data
tests for capability status rules
tests for quarantine reasons
tests for manifest creation
tests for no source mutation
tests for path handling and workspace boundaries
```

---

## 26. Risks and reversal conditions

| Risk | Severity | Mitigation | Reversal / repair condition |
|---|---:|---|---|
| Data import becomes too complex before MVP | High | Synthetic fixtures first, ES private smoke second | Defer full import wizard; use fixture selector |
| ES.zip license ambiguity blocks fixtures | High | Keep local-only; use synthetic repo fixtures | Do not commit ES-derived samples |
| Timezone/session assumptions contaminate tests | High | Require confirmation and manifest recording | Quarantine ambiguous datasets |
| Users overtrust approximate charts | High | Status badges and warnings | Disable approximate views from evidence by default |
| Intrabar ambiguity creates false winners | High | Label ambiguity and require lower-timeframe data for exact first-hit | Reject exact first-hit claims on OHLC-only data |
| Full data processing is slow | Medium | Tiny fixture MVP; performance spike later | Defer full dataset operations |
| File permissions too broad | High | Tauri scoped file selection only | Rework desktop permissions before build |
| Engine lacks needed dataset command | Medium | Bridge contract and scoped engine tickets | Adapt/defer instead of rewrite |
| User source file is accidentally changed | High | Read-only import and hash checks | Block release until no-source-mutation test passes |

---

## 27. ADRs to create later

| ADR | Decision |
|---|---|
| `ADR-DS-001` | Dataset Studio local import model: reference-only vs workspace copy |
| `ADR-DS-002` | Dataset manifest v0.1 contract |
| `ADR-DS-003` | DatasetCapabilityMap status taxonomy |
| `ADR-DS-004` | ES.zip local-only and fixture license-safety policy |
| `ADR-DS-005` | Timezone/session confirmation policy |
| `ADR-DS-006` | Intrabar ambiguity policy for SL/TP and visual replay |
| `ADR-DS-007` | Synthetic fixtures as default public test data |

---

## 28. First milestone category enabled by this volume

Volume 4 enables a future milestone category:

```text
M2 — Dataset Studio MVP Planning and Capability Map Proof
```

The first implementation milestone should not start until:

```text
Volume 0 reviewed
Volume 1 reviewed
Volume 2 reviewed
Volume 3 reviewed
Volume 4 reviewed
desktop bridge contract accepted
dataset fixture policy accepted
human gate decisions recorded
```

Possible future planning tickets, not generated here:

```text
DS-T001 — Dataset manifest contract
DS-T002 — DatasetCapabilityMap contract
DS-T003 — Synthetic OHLCV fixture policy
DS-T004 — ES.zip local-only intake policy
DS-T005 — Dataset Studio UI state map
```

These are placeholders for Volume 7 roadmap generation, not implementation prompts.

---

## 29. What must not be built yet

Do not build yet:

```text
full import wizard
full ES.zip ingestion
ResearchCore Engine dataset parser changes
automatic fixture slicing
timeframe generation code
chart rendering
visual replay engine
evidence card integration
data cache/index
cloud sync
external data connectors
broker/live feed integrations
public sample package
performance optimizer
AI-assisted data cleaning
```

Volume 4 is a boundary/spec volume only.

---

## 30. Volume 4 closeout

## 30.1 Decisions promoted

```text
Dataset Studio is a governed product track.
DatasetCapabilityMap must gate timeframe/chart/test generation.
Full ES.zip is local-only and outside repo.
Synthetic fixtures are preferred for repo tests.
ES-derived fixtures require human license-safety approval.
5m OHLCV may aggregate upward but cannot reconstruct true 1m/tick data.
OHLC bars cannot prove exact intrabar SL/TP order when both levels occur inside the same bar.
Missing timezone/session information triggers confirmation or quarantine.
Dataset Studio does not prove strategy validity.
```

## 30.2 Open decisions

```text
Whether MVP imports by reference-only, workspace copy, or both.
Exact dataset manifest file format: YAML vs JSON.
Exact ResearchCore Engine commands available vs needed.
Whether ES-derived private fixtures can ever be committed.
Which session calendar policy is acceptable for MVP.
```

## 30.3 Volume 4 verdict

```text
PROMOTE_TO_VOLUME_5_AFTER_REVIEW
```

## 30.4 Next volume

```text
Volume 5 — NullForge Logic Factory, LogicCard Lifecycle, Compiler Contract, Generator/Null/Ablation Boundary, and Test-Plan Bridge
```

---

## 31. Prompt for Volume 5

See:

```text
prompts/NullForge_Prompt_For_Volume_05_v0_4.md
```
