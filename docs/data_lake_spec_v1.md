# Data Lake Spec v1 (Option A)

## Purpose

Option A keeps raw market files outside Git and registers them into the dataset catalog for deterministic lineage-driven workflows.

## External Data Lake Root

- `G:\Raw CSVs`

Recommended folder convention:

- `G:\Raw CSVs\<INSTRUMENT>\<TF>\...`

Examples:

- `G:\Raw CSVs\ES\1min\...`
- `G:\Raw CSVs\NQ\5min\...`

## Rules

1. Raw datasets never go into the repository.
2. Dataset catalog metadata lives in the repository workspace path (for example `exec_outputs/catalog`).
3. Registration is performed per `(instrument, tf)` root directory.
4. Git tracks only metadata and contracts: schemas/specs/catalog entries/indexes/manifests, not raw files.

## Example Commands

### Register raw dataset

```powershell
python -m research_core.cli dataset register raw --catalog exec_outputs/catalog --root "G:\Raw CSVs\ES\1min" --desc "ES 1min external data lake"
```

### List and validate datasets

```powershell
python -m research_core.cli dataset list --catalog exec_outputs/catalog
python -m research_core.cli dataset validate --catalog exec_outputs/catalog --id DATASET_ID
```

### Materialize project (datasets mode)

```powershell
python -m research_core.cli project materialize --project configs/pilot/project.pilot.json --catalog exec_outputs/catalog --runs-root exec_outputs/pilot/runs_root
```

`project materialize` consumes registered `dataset_id` references and does not require raw files to be copied into the repository.
