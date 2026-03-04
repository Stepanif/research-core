$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

function Write-Utf8NoBom {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,
        [Parameter(Mandatory = $true)]
        [string]$Content
    )
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Content, $utf8NoBom)
}

$env:RESEARCH_CREATED_UTC = (git show -s --format=%cI HEAD).Trim()

$catalogDir = "exec_outputs/catalog"
$datasetsTemplatePath = "configs/analysis/datasets.es_5m.json"
$localDir = "configs/analysis/local"
$datasetIdPath = Join-Path $localDir "_es5m_dataset_id.txt"
$generatedDatasetsPath = Join-Path $localDir "datasets.es_5m.generated.json"
$generatedSpecPath = Join-Path $localDir "runset.es_5m.generated.json"
$runsetsPath = Join-Path $localDir "runsets.es_5m.generated.json"
$runsRoot = "exec_outputs/runs/runs"

if (-not (Test-Path $localDir -PathType Container)) {
    New-Item -ItemType Directory -Path $localDir -Force | Out-Null
}

if (-not (Test-Path $datasetsTemplatePath -PathType Leaf)) {
    Write-Host "ERROR: Missing datasets template '$datasetsTemplatePath'." -ForegroundColor Red
    Write-Host "Next action: run .\docs\scripts\register_es5m_dataset.ps1 first." -ForegroundColor Yellow
    exit 2
}

$datasetsPayload = Get-Content -Raw $datasetsTemplatePath | ConvertFrom-Json
if (-not $datasetsPayload.datasets -or $datasetsPayload.datasets.Count -eq 0) {
    Write-Host "ERROR: datasets template has no datasets rows: '$datasetsTemplatePath'." -ForegroundColor Red
    Write-Host "Next action: ensure datasets.es_5m.json has one ES 5m dataset row." -ForegroundColor Yellow
    exit 2
}

if (-not (Test-Path $datasetIdPath -PathType Leaf)) {
    Write-Host "ERROR: Missing dataset_id file '$datasetIdPath'." -ForegroundColor Red
    Write-Host "Next action: run .\docs\scripts\register_es5m_dataset.ps1 first." -ForegroundColor Yellow
    exit 2
}
$datasetId = (Get-Content -Raw $datasetIdPath).Trim()
if ($datasetId -notmatch '^[a-f0-9]{64}$') {
    Write-Host "ERROR: local dataset_id is missing/invalid in '$datasetIdPath': '$datasetId'." -ForegroundColor Red
    Write-Host "Next action: run .\docs\scripts\register_es5m_dataset.ps1 to populate dataset_id." -ForegroundColor Yellow
    exit 2
}

$datasetsPayload.datasets[0].dataset_id = $datasetId
$datasetsPayload.datasets[0].instrument = "ES"
$datasetsPayload.datasets[0].tf = "5m"
Write-Utf8NoBom -Path $generatedDatasetsPath -Content ($datasetsPayload | ConvertTo-Json -Depth 8)

$previousErrorAction = $ErrorActionPreference
$ErrorActionPreference = "Continue"
$genOutput = python docs/scripts/gen_explicit_runset_from_index.py --catalog $catalogDir --datasets $generatedDatasetsPath --out $generatedSpecPath 2>&1
$genExitCode = $LASTEXITCODE
$ErrorActionPreference = $previousErrorAction

if ($genExitCode -ne 0) {
    Write-Host "ERROR: explicit runset generation failed." -ForegroundColor Red
    $genOutput | ForEach-Object { Write-Host $_ }
    Write-Host "Next action: verify dataset_to_runs index exists and dataset_id '$datasetId' has linked runs." -ForegroundColor Yellow
    exit 2
}

function Resolve-CanonManifestPath {
    param([string]$RunRef)

    $leaf = Split-Path -Path $RunRef -Leaf
    $candidates = @(
        (Join-Path $RunRef "canon.manifest.json"),
        (Join-Path (Join-Path $runsRoot $leaf) "canon.manifest.json")
    )

    foreach ($candidate in $candidates) {
        if (Test-Path $candidate -PathType Leaf) {
            return $candidate
        }
    }

    if (Test-Path $runsRoot -PathType Container) {
        $recursive = Get-ChildItem $runsRoot -Directory -Recurse | Where-Object { $_.Name -eq $leaf } | Select-Object -First 1
        if ($null -ne $recursive) {
            $recursiveManifest = Join-Path $recursive.FullName "canon.manifest.json"
            if (Test-Path $recursiveManifest -PathType Leaf) {
                return $recursiveManifest
            }
        }
    }

    return $null
}

$specPayload = Get-Content -Raw $generatedSpecPath | ConvertFrom-Json
$runs = @($specPayload.runs)
if ($runs.Count -eq 0) {
    Write-Host "ERROR: Generated explicit runset has no runs in '$generatedSpecPath'." -ForegroundColor Red
    Write-Host "Next action: run .\docs\scripts\materialize_es5m_project.ps1 and ensure links are registered." -ForegroundColor Yellow
    exit 2
}

foreach ($runRow in $runs) {
    $runRef = [string]$runRow.run_ref
    $manifestPath = Resolve-CanonManifestPath -RunRef $runRef
    if ($null -eq $manifestPath) {
        Write-Host "ERROR: Missing canon.manifest.json for run_ref '$runRef'." -ForegroundColor Red
        Write-Host "Next action: verify run artifacts exist under '$runsRoot'." -ForegroundColor Yellow
        exit 2
    }

    $manifest = Get-Content -Raw $manifestPath | ConvertFrom-Json
    $instrument = [string]$manifest.instrument
    $tf = [string]$manifest.tf
    if ($instrument -ne "ES" -or $tf -notmatch '^(5m|5min|300s|00:05)$') {
        Write-Host "ERROR: Generated runset includes non-ES5m run_ref '$runRef' (instrument='$instrument', tf='$tf')." -ForegroundColor Red
        Write-Host "Next action: rebuild ES5m materialization and dataset links, then regenerate runset." -ForegroundColor Yellow
        exit 2
    }
}

$specPayload.name = "ANALYSIS_RUNSET_ES_5M_EXPLICIT_FROM_INDEX"
Write-Utf8NoBom -Path $generatedSpecPath -Content ($specPayload | ConvertTo-Json -Depth 12)

$previousErrorAction = $ErrorActionPreference
$ErrorActionPreference = "Continue"
$createOutput = python -m research_core.cli runset create --catalog $catalogDir --spec $generatedSpecPath 2>&1
$createExitCode = $LASTEXITCODE
$ErrorActionPreference = $previousErrorAction

if ($createExitCode -ne 0) {
    Write-Host "ERROR: runset create failed." -ForegroundColor Red
    $createOutput | ForEach-Object { Write-Host $_ }
    Write-Host "Next action: inspect '$generatedSpecPath' and catalog consistency, then rerun." -ForegroundColor Yellow
    exit 2
}

$runsetIdLine = @($createOutput | Where-Object { $_ -match '^RUNSET_CREATED runset_id=([a-f0-9]{64})$' } | Select-Object -Last 1)
if ($runsetIdLine.Count -eq 0) {
    Write-Host "ERROR: Could not parse runset_id from runset create output." -ForegroundColor Red
    $createOutput | ForEach-Object { Write-Host $_ }
    Write-Host "Next action: rerun runset create manually and confirm RUNSET_CREATED output." -ForegroundColor Yellow
    exit 2
}

$runsetId = ([regex]::Match([string]$runsetIdLine[0], '^RUNSET_CREATED runset_id=([a-f0-9]{64})$')).Groups[1].Value
Write-Utf8NoBom -Path $runsetsPath -Content (([ordered]@{ runset_ids = @($runsetId) } | ConvertTo-Json -Compress))

$previousErrorAction = $ErrorActionPreference
$ErrorActionPreference = "Continue"
$validateOutput = python -m research_core.cli runset validate --catalog $catalogDir --id $runsetId 2>&1
$validateExitCode = $LASTEXITCODE
$ErrorActionPreference = $previousErrorAction

if ($validateExitCode -ne 0) {
    Write-Host "ERROR: runset validate failed for runset_id '$runsetId'." -ForegroundColor Red
    $validateOutput | ForEach-Object { Write-Host $_ }
    Write-Host "Next action: fix generated runset spec and rerun create_es5m_runset.ps1." -ForegroundColor Yellow
    exit 2
}

Write-Host "Created ES5m runset_id: $runsetId" -ForegroundColor Green
Write-Host "- $generatedSpecPath"
Write-Host "- $runsetsPath"