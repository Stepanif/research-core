$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$env:RESEARCH_CREATED_UTC = (git show -s --format=%cI HEAD).Trim()

$catalogDir = "exec_outputs/catalog"
$datasetsPath = "configs/analysis/datasets.es_5m.json"
$generatedSpecPath = "configs/analysis/runset.es_5m.generated.json"
$finalSpecPath = "configs/analysis/runset.es_5m.json"
$runsetsPath = "configs/analysis/runsets.es_5m.json"
$runsRoot = "exec_outputs/runs/runs"

if (-not (Test-Path $datasetsPath -PathType Leaf)) {
    Write-Host "ERROR: Missing datasets file '$datasetsPath'." -ForegroundColor Red
    Write-Host "Next action: run .\docs\scripts\register_es5m_dataset.ps1 first." -ForegroundColor Yellow
    exit 2
}

$datasetsPayload = Get-Content -Raw $datasetsPath | ConvertFrom-Json
if (-not $datasetsPayload.datasets -or $datasetsPayload.datasets.Count -eq 0) {
    Write-Host "ERROR: datasets file has no datasets rows: '$datasetsPath'." -ForegroundColor Red
    Write-Host "Next action: ensure datasets.es_5m.json has one ES 5m dataset row with dataset_id." -ForegroundColor Yellow
    exit 2
}
$datasetId = [string]$datasetsPayload.datasets[0].dataset_id
if ($datasetId -notmatch '^[a-f0-9]{64}$') {
    Write-Host "ERROR: datasets.es_5m.json dataset_id is missing/invalid: '$datasetId'." -ForegroundColor Red
    Write-Host "Next action: run .\docs\scripts\register_es5m_dataset.ps1 to populate dataset_id." -ForegroundColor Yellow
    exit 2
}

$genOutput = python docs/scripts/gen_explicit_runset_from_index.py --catalog $catalogDir --datasets $datasetsPath --out $generatedSpecPath 2>&1
if ($LASTEXITCODE -ne 0) {
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
    if ($instrument -ne "ES" -or $tf -notmatch '^(5m|300s|00:05)$') {
        Write-Host "ERROR: Generated runset includes non-ES5m run_ref '$runRef' (instrument='$instrument', tf='$tf')." -ForegroundColor Red
        Write-Host "Next action: rebuild ES5m materialization and dataset links, then regenerate runset." -ForegroundColor Yellow
        exit 2
    }
}

$specPayload.name = "ANALYSIS_RUNSET_ES_5M_EXPLICIT_FROM_INDEX"
$specPayload | ConvertTo-Json -Depth 12 | Set-Content -Encoding UTF8 $finalSpecPath

$createOutput = python -m research_core.cli runset create --catalog $catalogDir --spec $finalSpecPath 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: runset create failed." -ForegroundColor Red
    $createOutput | ForEach-Object { Write-Host $_ }
    Write-Host "Next action: inspect '$finalSpecPath' and catalog consistency, then rerun." -ForegroundColor Yellow
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
([ordered]@{ runset_ids = @($runsetId) } | ConvertTo-Json -Compress) | Set-Content -Encoding UTF8 $runsetsPath

$validateOutput = python -m research_core.cli runset validate --catalog $catalogDir --id $runsetId 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: runset validate failed for runset_id '$runsetId'." -ForegroundColor Red
    $validateOutput | ForEach-Object { Write-Host $_ }
    Write-Host "Next action: fix generated runset spec and rerun create_es5m_runset.ps1." -ForegroundColor Yellow
    exit 2
}

Write-Host "Created ES5m runset_id: $runsetId" -ForegroundColor Green
Write-Host "- $finalSpecPath"
Write-Host "- $runsetsPath"