$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$env:RESEARCH_CREATED_UTC = (git show -s --format=%cI HEAD).Trim()

$datasetIdPath = "configs/analysis/_es5m_dataset_id.txt"
$projectPath = "configs/analysis/project.es_5m.json"
$catalogDir = "exec_outputs/catalog"
$runsRoot = "exec_outputs/runs"

if (-not (Test-Path $datasetIdPath -PathType Leaf)) {
    Write-Host "ERROR: Missing dataset_id file '$datasetIdPath'." -ForegroundColor Red
    Write-Host "Next action: run .\docs\scripts\register_es5m_dataset.ps1 first." -ForegroundColor Yellow
    exit 2
}

$datasetId = (Get-Content -Raw $datasetIdPath).Trim()
if ([string]::IsNullOrWhiteSpace($datasetId)) {
    Write-Host "ERROR: dataset_id file is empty: '$datasetIdPath'." -ForegroundColor Red
    Write-Host "Next action: rerun .\docs\scripts\register_es5m_dataset.ps1 to refresh dataset_id." -ForegroundColor Yellow
    exit 2
}

if (-not (Test-Path $projectPath -PathType Leaf)) {
    Write-Host "ERROR: Missing project config '$projectPath'." -ForegroundColor Red
    Write-Host "Next action: restore project config and rerun materialize." -ForegroundColor Yellow
    exit 2
}

$projectPayload = Get-Content -Raw $projectPath | ConvertFrom-Json
if (-not $projectPayload.datasets -or $projectPayload.datasets.Count -eq 0) {
    Write-Host "ERROR: Invalid project datasets block in '$projectPath'." -ForegroundColor Red
    Write-Host "Next action: ensure project.es_5m.json includes datasets[0]." -ForegroundColor Yellow
    exit 2
}
$projectPayload.datasets[0].dataset_id = $datasetId
$projectPayload.datasets[0].instrument = "ES"
$projectPayload.datasets[0].tf = "5m"
$projectPayload | ConvertTo-Json -Depth 12 | Set-Content -Encoding UTF8 $projectPath

$materializeOutput = python -m research_core.cli project materialize --project $projectPath --catalog $catalogDir --runs-root $runsRoot 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: project materialize failed." -ForegroundColor Red
    $materializeOutput | ForEach-Object { Write-Host $_ }
    Write-Host "Next action: verify dataset_id '$datasetId' exists in '$catalogDir' and source data root resolves." -ForegroundColor Yellow
    exit 2
}
$materializeOutput | ForEach-Object { Write-Host $_ }

$runsDir = "exec_outputs/runs/runs"
if (-not (Test-Path $runsDir -PathType Container)) {
    Write-Host "ERROR: Missing runs directory '$runsDir' after materialize." -ForegroundColor Red
    Write-Host "Next action: verify --runs-root exec_outputs/runs is writable and rerun materialize." -ForegroundColor Yellow
    exit 2
}

$todayUtc = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd")
$newHashes = @()

Get-ChildItem -Path $runsDir -Directory | ForEach-Object {
    $manifestPath = Join-Path $_.FullName "canon.manifest.json"
    if (-not (Test-Path $manifestPath -PathType Leaf)) {
        return
    }

    $manifest = Get-Content -Raw $manifestPath | ConvertFrom-Json
    $created = [string]$manifest.created_utc
    $instrument = [string]$manifest.instrument
    $tf = [string]$manifest.tf

    if ($created.StartsWith($todayUtc) -and $instrument -eq "ES" -and $tf -match '^(5m|300s|00:05)$') {
        $newHashes += $_.Name
    }
}

$newHashes = @($newHashes | Sort-Object -Unique)
Write-Host "ES5m run hashes created today ($todayUtc):" -ForegroundColor Green
if ($newHashes.Count -eq 0) {
    Write-Host "- none"
}
else {
    $newHashes | ForEach-Object { Write-Host "- $_" }
}