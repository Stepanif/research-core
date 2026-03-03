# Pilot Cohort v1 (First Real Cohort)

## Cohort Definition

- Instrument: `ES`
- Timeframe: `1min`
- Session policy: `rth`
- Years: `2019-2025`
- Data source: `RAW_VENDOR_V1` (ingested as immutable raw dataset root)

## Deterministic Directory Conventions

Use this layout consistently for the pilot:

- `CATALOG_DIR = exec_outputs/catalog`
- `BASELINE_ROOT = baselines/prod`
- `RUNS_ROOT = exec_outputs/pilot/runs_root`
- `OUT_DIR = exec_outputs/pilot`

Config files in repo:

- `configs/pilot/project.pilot.json`
- `configs/pilot/runset.pilot.json`
- `configs/pilot/runsets.pilot.json`
- `configs/pilot/ci.pilot.json`
- `configs/pilot/doctor.pilot.json`

## End-to-End Operator Flow

All commands below are deterministic when `RESEARCH_CREATED_UTC` is pinned.

## Data Lake (Option A)

- External raw data lake root: `G:\Raw CSVs`
- Raw files must remain outside the repository.
- Do not copy raw CSVs into repo paths.
- Do not commit CSVs or raw archives.

Recommended path pattern:

- `G:\Raw CSVs\<INSTRUMENT>\<TF>\...`

Registration procedure:

1. Select instrument/timeframe directory in the external data lake.
2. Register that root with `dataset register raw`.
3. Use returned `dataset_id` in project/runset pilot configs.

Deterministic bulk registration script (writes to `catalog_dir=exec_outputs/catalog`):

```powershell
pwsh -File docs/scripts/register_g_raw_datasets.ps1
```

### 0) Pin deterministic build timestamp

```powershell
$env:RESEARCH_CREATED_UTC = "2026-03-02T00:00:00+00:00"
```

### 1) Register raw dataset

```powershell
python -m research_core.cli dataset register raw --catalog exec_outputs/catalog --root "G:\Raw CSVs\ES\1min" --desc "pilot ES 1min rth 2019-2025"
```

Capture printed `dataset_id` and replace `DATASET_ID` in `configs/pilot/project.pilot.json` and `configs/pilot/runset.pilot.json`.

### 2) Materialize project runs (datasets mode)

```powershell
python -m research_core.cli project materialize --project configs/pilot/project.pilot.json --catalog exec_outputs/catalog --runs-root exec_outputs/pilot/runs_root
```

### 3) Create and validate runset

```powershell
python -m research_core.cli runset create --catalog exec_outputs/catalog --spec configs/pilot/runset.pilot.json
python -m research_core.cli runset validate --catalog exec_outputs/catalog --id RUNSET_ID
```

Capture printed `RUNSET_ID` and replace it in `configs/pilot/runsets.pilot.json`.

### 4) Generate baseline card from runset

```powershell
python -m research_core.cli risk sweep --catalog exec_outputs/catalog --runset RUNSET_ID --out exec_outputs/pilot/risk
```

### 5) Refresh baseline index and promote to prod

```powershell
python -m research_core.cli baseline index refresh --root baselines/prod
python -m research_core.cli baseline promote --root baselines/prod --runset RUNSET_ID --baseline-id BASELINE_ID --label prod
```

`BASELINE_ID` is the baseline checksum emitted by sweep/baseline card checksums.

### 6) Drift and dashboard checks

```powershell
python -m research_core.cli risk drift --catalog exec_outputs/catalog --root baselines/prod --runset RUNSET_ID --label prod --out exec_outputs/pilot/drift
python -m research_core.cli risk dashboard --catalog exec_outputs/catalog --root baselines/prod --runsets configs/pilot/runsets.pilot.json --out exec_outputs/pilot/dashboard --label prod
```

### 7) CI pipeline gate

```powershell
python -m research_core.cli ci run --config configs/pilot/ci.pilot.json
```

### 8) Read-only CI doctor gate

```powershell
python -m research_core.cli ci doctor --config configs/pilot/doctor.pilot.json
```

## Promotion Policy (`label=prod`)

Promote a runset to `prod` only when all conditions hold:

1. `runset validate` passes for the exact `RUNSET_ID`.
2. `risk sweep` produced baseline card + manifest without errors.
3. `risk drift` is acceptable for pilot policy (target: no unexplained drift).
4. `risk dashboard` status is acceptable for the full pilot runset list.
5. `ci run` passes under `configs/pilot/ci.pilot.json`.
6. `ci doctor` passes under `configs/pilot/doctor.pilot.json`.

If any gate fails, do not move `prod`; investigate and regenerate artifacts deterministically from corrected inputs.

## Appendix: Locked Pilot Dataset Mapping

- Authoritative pilot dataset mapping: `configs/pilot/datasets.pilot.json`
- Catalog target for mapping: `exec_outputs/catalog`
- Pilot dataset IDs are locked as metadata in Git; raw files remain external (`G:\Raw CSVs`).
