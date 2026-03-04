$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$env:RESEARCH_CREATED_UTC = (git show -s --format=%cI HEAD).Trim()

$catalogDir = "exec_outputs/catalog"
$datasetIdPath = "configs/analysis/_es5m_dataset_id.txt"
$datasetsConfigPath = "configs/analysis/datasets.es_5m.json"
$projectConfigPath = "configs/analysis/project.es_5m.json"

function Resolve-Es5mRoot {
    param(
        [string]$DatasetRoot
    )

    if (-not [string]::IsNullOrWhiteSpace($DatasetRoot)) {
        if (-not (Test-Path $DatasetRoot -PathType Container)) {
            Write-Host "ERROR: Provided --DatasetRoot path does not exist: $DatasetRoot" -ForegroundColor Red
            Write-Host "Next action: pass a valid ES 5m dataset directory (contains raw file) via --DatasetRoot." -ForegroundColor Yellow
            exit 2
        }
        return (Resolve-Path $DatasetRoot).Path
    }

    $rawMapJson = $env:RESEARCH_DATA_ROOT_MAP_JSON
    if ([string]::IsNullOrWhiteSpace($rawMapJson)) {
        Write-Host "ERROR: Dataset root not provided and RESEARCH_DATA_ROOT_MAP_JSON is not set." -ForegroundColor Red
        Write-Host "Next action: set RESEARCH_DATA_ROOT_MAP_JSON (e.g. {'Raw CSVs':'G:\\Raw CSVs'}) or pass --DatasetRoot <ES5m folder>." -ForegroundColor Yellow
        exit 2
    }

    try {
        $map = $rawMapJson | ConvertFrom-Json
    }
    catch {
        Write-Host "ERROR: RESEARCH_DATA_ROOT_MAP_JSON is invalid JSON." -ForegroundColor Red
        Write-Host "Next action: set RESEARCH_DATA_ROOT_MAP_JSON to a valid object, e.g. {'Raw CSVs':'G:\\Raw CSVs'}." -ForegroundColor Yellow
        exit 2
    }

    if (-not ($map.PSObject.Properties.Name -contains "Raw CSVs")) {
        Write-Host "ERROR: RESEARCH_DATA_ROOT_MAP_JSON is missing key 'Raw CSVs'." -ForegroundColor Red
        Write-Host "Next action: add key 'Raw CSVs' with an absolute root path or pass --DatasetRoot explicitly." -ForegroundColor Yellow
        exit 2
    }

    $baseRoot = [string]$map."Raw CSVs"
    if ([string]::IsNullOrWhiteSpace($baseRoot) -or -not (Test-Path $baseRoot -PathType Container)) {
        Write-Host "ERROR: 'Raw CSVs' root is missing or not found: $baseRoot" -ForegroundColor Red
        Write-Host "Next action: fix RESEARCH_DATA_ROOT_MAP_JSON['Raw CSVs'] or pass --DatasetRoot explicitly." -ForegroundColor Yellow
        exit 2
    }

    $matches = @(Get-ChildItem -Path $baseRoot -Directory -Recurse | Where-Object {
            $_.Name -match '^ES\s+(5m|5min|300s|00:05)\b'
        } | Sort-Object FullName)

    if ($matches.Count -eq 0) {
        Write-Host "ERROR: No ES 5m dataset directories found under '$baseRoot'." -ForegroundColor Red
        Write-Host "Next action: add an ES 5m raw directory (e.g., 'ES 5min ...') and rerun, or pass --DatasetRoot." -ForegroundColor Yellow
        exit 2
    }

    if ($matches.Count -gt 1) {
        Write-Host "ERROR: Multiple ES 5m dataset directories found under '$baseRoot'." -ForegroundColor Red
        $matches | ForEach-Object { Write-Host "- $($_.FullName)" }
        Write-Host "Next action: rerun with --DatasetRoot <exact-directory> to remove ambiguity." -ForegroundColor Yellow
        exit 2
    }

    return $matches[0].FullName
}

function Update-Es5mConfigs {
    param(
        [string]$DatasetId
    )

    $datasetsPayload = Get-Content -Raw $datasetsConfigPath | ConvertFrom-Json
    if (-not $datasetsPayload.datasets -or $datasetsPayload.datasets.Count -eq 0) {
        Write-Host "ERROR: Invalid datasets config shape in '$datasetsConfigPath'." -ForegroundColor Red
        Write-Host "Next action: restore datasets.es_5m.json to include at least one datasets[] row." -ForegroundColor Yellow
        exit 2
    }
    $datasetsPayload.datasets[0].dataset_id = $DatasetId
    $datasetsPayload.datasets[0].instrument = "ES"
    $datasetsPayload.datasets[0].tf = "5m"
    $datasetsPayload | ConvertTo-Json -Depth 8 | Set-Content -Encoding UTF8 $datasetsConfigPath

    $projectPayload = Get-Content -Raw $projectConfigPath | ConvertFrom-Json
    if (-not $projectPayload.datasets -or $projectPayload.datasets.Count -eq 0) {
        Write-Host "ERROR: Invalid project config shape in '$projectConfigPath'." -ForegroundColor Red
        Write-Host "Next action: restore project.es_5m.json to include at least one datasets[] row." -ForegroundColor Yellow
        exit 2
    }
    $projectPayload.datasets[0].dataset_id = $DatasetId
    $projectPayload.datasets[0].instrument = "ES"
    $projectPayload.datasets[0].tf = "5m"
    $projectPayload | ConvertTo-Json -Depth 12 | Set-Content -Encoding UTF8 $projectConfigPath
}

param(
    [string]$DatasetRoot,
    [string]$PythonExe = "python"
)

$es5mRoot = Resolve-Es5mRoot -DatasetRoot $DatasetRoot

$rawFiles = @(Get-ChildItem -Path $es5mRoot -File | Where-Object { $_.Extension -in @('.txt', '.csv') })
if ($rawFiles.Count -eq 0) {
    Write-Host "ERROR: ES5m dataset directory has no .txt/.csv files: $es5mRoot" -ForegroundColor Red
    Write-Host "Next action: point --DatasetRoot to a raw dataset directory containing one source file." -ForegroundColor Yellow
    exit 2
}

$desc = "raw_vendor_v1 ES 5m ANALYSIS_ES_5MIN"
$registerOutput = & $PythonExe -m research_core.cli dataset register raw --catalog $catalogDir --root $es5mRoot --desc $desc 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: dataset register raw failed." -ForegroundColor Red
    $registerOutput | ForEach-Object { Write-Host $_ }
    Write-Host "Next action: confirm catalog path '$catalogDir' exists and '$es5mRoot' is readable." -ForegroundColor Yellow
    exit 2
}

$datasetIdLine = @($registerOutput | Where-Object { $_ -match '^REGISTERED dataset_id=([a-f0-9]{64})$' } | Select-Object -Last 1)
if ($datasetIdLine.Count -eq 0) {
    Write-Host "ERROR: Could not parse dataset_id from dataset register output." -ForegroundColor Red
    $registerOutput | ForEach-Object { Write-Host $_ }
    Write-Host "Next action: rerun command manually and ensure output includes 'REGISTERED dataset_id=<64-hex>'." -ForegroundColor Yellow
    exit 2
}

$datasetId = ([regex]::Match([string]$datasetIdLine[0], '^REGISTERED dataset_id=([a-f0-9]{64})$')).Groups[1].Value
if ([string]::IsNullOrWhiteSpace($datasetId)) {
    Write-Host "ERROR: Parsed dataset_id was empty." -ForegroundColor Red
    Write-Host "Next action: rerun registration and inspect command output for dataset_id." -ForegroundColor Yellow
    exit 2
}

Set-Content -Encoding UTF8 $datasetIdPath $datasetId
Update-Es5mConfigs -DatasetId $datasetId

Write-Host "Registered ES5m dataset_id: $datasetId" -ForegroundColor Green
Write-Host "- $datasetIdPath"
Write-Host "- $datasetsConfigPath"
Write-Host "- $projectConfigPath"