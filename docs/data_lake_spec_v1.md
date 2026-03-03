# Data Lake Spec v1 (Option A)

## Purpose

Option A keeps raw market files outside Git and registers them into the dataset catalog for deterministic lineage-driven workflows.

## External Data Lake Root

- `G:\Raw CSVs`

Recommended folder convention:

- `G:\Raw CSVs\Futures\<CATEGORY>\<INSTRUMENT>\<DATASET_DIR>`

Registration contract:

- Each dataset must be a directory named:
	- `"<INSTR> <TF> 2015-2025"`
- Each dataset directory contains raw file(s) (`.csv`/`.txt`) for that dataset.
- The registration script reads instrument/timeframe from the dataset directory name.

Examples:

- `G:\Raw CSVs\Futures\Indicies\ES\ES 1min 2015-2025\...`
- `G:\Raw CSVs\Futures\Crypto\BTC\BTC 5min 2015-2025\...`

## Rules

1. Raw datasets never go into the repository.
2. Dataset catalog metadata lives in the repository workspace path (for example `exec_outputs/catalog`).
3. Registration is performed per `(instrument, tf)` root directory.
4. Git tracks only metadata and contracts: schemas/specs/catalog entries/indexes/manifests, not raw files.

## If You Currently Have Files Only

If files are directly under each instrument folder, do a one-time folderization so each file is wrapped in a dataset directory named after its file basename.

```powershell
$roots = @(
	"G:\Raw CSVs\Futures\Indicies\ES",
	"G:\Raw CSVs\Futures\Indicies\NQ",
	"G:\Raw CSVs\Futures\Indicies\YM",
	"G:\Raw CSVs\Futures\Crypto\BTC",
	"G:\Raw CSVs\Futures\Crypto\ETH",
	"G:\Raw CSVs\Futures\Commodity\GC",
	"G:\Raw CSVs\Futures\Commodity\CL"
)

foreach ($root in $roots) {
	Get-ChildItem -LiteralPath $root -File | Sort-Object Name | ForEach-Object {
		$targetDir = Join-Path $root $_.BaseName
		if (-not (Test-Path -LiteralPath $targetDir -PathType Container)) {
			New-Item -ItemType Directory -Path $targetDir | Out-Null
		}
		Move-Item -LiteralPath $_.FullName -Destination (Join-Path $targetDir $_.Name)
	}
}
```

After folderization, run the deterministic registration script:

```powershell
pwsh -File docs/scripts/register_g_raw_datasets.ps1
```

## Example Commands

### Register raw dataset

```powershell
python -m research_core.cli dataset register raw --catalog exec_outputs/catalog --root "G:\Raw CSVs\Futures\Indicies\ES\ES 1min 2015-2025" --desc "ES 1min external data lake"
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
