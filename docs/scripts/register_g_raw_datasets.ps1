<#
Usage (run from repository root):

  $env:RESEARCH_CREATED_UTC = "2026-03-02T00:00:00+00:00"
  .\docs\scripts\register_g_raw_datasets.ps1

Notes:
- This script is deterministic and fail-loud.
- It uses the current Research CLI contract:
  dataset register raw --catalog <path> --root <dataset_dir>
- Each dataset is expected as a directory named like:
  "<INSTR> <TF> 2015-2025" where TF is e.g. 1min/5min/15min/60min.
#>

[CmdletBinding()]
param(
    [string]$DataLakeRoot = "G:\Raw CSVs\Futures",
    [string]$CatalogDir = "exec_outputs/catalog",
    [string]$PythonExe = "python"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($env:RESEARCH_CREATED_UTC)) {
    throw "RESEARCH_CREATED_UTC is required for deterministic dataset registration"
}

$targets = @(
    @{ Category = "Indicies"; Instruments = @("ES", "NQ", "YM") },
    @{ Category = "Crypto"; Instruments = @("BTC", "ETH") },
    @{ Category = "Commodity"; Instruments = @("GC", "CL") }
)

$namePattern = '^(?<instr>[A-Za-z0-9]+)\s+(?<tf>\d+min)\s+'
$registeredIds = New-Object System.Collections.Generic.List[string]

foreach ($group in $targets) {
    $category = [string]$group.Category
    foreach ($instrument in $group.Instruments) {
        $instrumentDir = Join-Path -Path (Join-Path -Path $DataLakeRoot -ChildPath $category) -ChildPath $instrument
        if (-not (Test-Path -LiteralPath $instrumentDir -PathType Container)) {
            throw "Missing instrument directory: $instrumentDir"
        }

        $datasetDirs = @(Get-ChildItem -LiteralPath $instrumentDir -Directory | Sort-Object Name)
        if ($datasetDirs.Count -eq 0) {
            throw "No dataset directories found under: $instrumentDir"
        }

        foreach ($datasetDir in $datasetDirs) {
            $name = [string]$datasetDir.Name
            $match = [regex]::Match($name, $namePattern)
            if (-not $match.Success) {
                throw "Dataset directory name does not match required pattern '<INSTR> <TF> ...': $($datasetDir.FullName)"
            }

            $parsedInstr = $match.Groups['instr'].Value.ToUpperInvariant()
            $parsedTf = $match.Groups['tf'].Value
            if ($parsedInstr -ne $instrument.ToUpperInvariant()) {
                throw "Instrument mismatch in directory name '$name': expected $instrument, found $parsedInstr"
            }

            $desc = "raw_vendor_v1 $parsedInstr $parsedTf $name"
            $args = @(
                "-m", "research_core.cli",
                "dataset", "register", "raw",
                "--catalog", $CatalogDir,
                "--root", $datasetDir.FullName,
                "--desc", $desc
            )

            $output = & $PythonExe @args 2>&1
            if ($LASTEXITCODE -ne 0) {
                throw "dataset register raw failed for '$($datasetDir.FullName)'. Output:`n$output"
            }

            $idLine = $output | Where-Object { $_ -match '^REGISTERED dataset_id=(?<id>[a-f0-9]{64})$' } | Select-Object -Last 1
            if (-not $idLine) {
                throw "Unable to parse dataset_id from output for '$($datasetDir.FullName)'. Output:`n$output"
            }

            $datasetId = ([regex]::Match([string]$idLine, '^REGISTERED dataset_id=(?<id>[a-f0-9]{64})$')).Groups['id'].Value
            if ([string]::IsNullOrWhiteSpace($datasetId)) {
                throw "Parsed empty dataset_id for '$($datasetDir.FullName)'"
            }

            $registeredIds.Add($datasetId)
            Write-Host "REGISTERED instr=$parsedInstr tf=$parsedTf id=$datasetId root=$($datasetDir.FullName)"
        }
    }
}

$uniqueIds = @($registeredIds | Sort-Object -Unique)
if ($uniqueIds.Count -ne 28) {
    throw "Expected 28 unique dataset registrations, got $($uniqueIds.Count)"
}

foreach ($datasetId in $uniqueIds) {
    $validateArgs = @(
        "-m", "research_core.cli",
        "dataset", "validate",
        "--catalog", $CatalogDir,
        "--id", $datasetId
    )
    $validateOutput = & $PythonExe @validateArgs 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "dataset validate failed for id=$datasetId. Output:`n$validateOutput"
    }
}

$listArgs = @("-m", "research_core.cli", "dataset", "list", "--catalog", $CatalogDir)
$listOutput = & $PythonExe @listArgs 2>&1
if ($LASTEXITCODE -ne 0) {
    throw "dataset list failed. Output:`n$listOutput"
}

Write-Host ""
Write-Host "Registration complete. Unique dataset count=$($uniqueIds.Count)"
Write-Output $listOutput
