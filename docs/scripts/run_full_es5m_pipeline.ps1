param(
    [string]$DatasetRoot
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$env:RESEARCH_CREATED_UTC = (git show -s --format=%cI HEAD).Trim()

function Assert-PathExists {
    param(
        [string]$Path,
        [string]$PathType,
        [string]$Hint
    )

    if (-not (Test-Path $Path -PathType $PathType)) {
        throw "Preflight failed: missing $PathType '$Path'. Next action: $Hint"
    }
}

function Test-CanReusePinnedEs5mDataset {
    $datasetsTemplatePath = "configs/analysis/datasets.es_5m.json"
    $catalogEntriesDir = "exec_outputs/catalog/entries"
    if (-not (Test-Path $datasetsTemplatePath -PathType Leaf)) {
        return $false
    }
    if (-not (Test-Path $catalogEntriesDir -PathType Container)) {
        return $false
    }

    try {
        $payload = Get-Content -Raw $datasetsTemplatePath | ConvertFrom-Json
        if (-not $payload.datasets -or $payload.datasets.Count -eq 0) {
            return $false
        }
        $pinnedId = [string]$payload.datasets[0].dataset_id
        if ($pinnedId -notmatch '^[a-f0-9]{64}$') {
            return $false
        }
        return (Test-Path (Join-Path $catalogEntriesDir "$pinnedId.json") -PathType Leaf)
    }
    catch {
        return $false
    }
}

Assert-PathExists -Path "docs/scripts/register_es5m_dataset.ps1" -PathType Leaf -Hint "restore repository docs/scripts files"
Assert-PathExists -Path "docs/scripts/materialize_es5m_project.ps1" -PathType Leaf -Hint "restore repository docs/scripts files"
Assert-PathExists -Path "docs/scripts/create_es5m_runset.ps1" -PathType Leaf -Hint "restore repository docs/scripts files"
Assert-PathExists -Path "docs/scripts/promote_es5m_baseline.ps1" -PathType Leaf -Hint "restore repository docs/scripts files"
Assert-PathExists -Path "docs/scripts/run_analysis_es_5m.ps1" -PathType Leaf -Hint "restore repository docs/scripts files"
Assert-PathExists -Path "configs/analysis/datasets.es_5m.json" -PathType Leaf -Hint "restore configs/analysis/datasets.es_5m.json"
Assert-PathExists -Path "configs/analysis/project.es_5m.json" -PathType Leaf -Hint "restore configs/analysis/project.es_5m.json"
Assert-PathExists -Path "configs/analysis/specs" -PathType Container -Hint "restore configs/analysis/specs (canonical ES5m spec_dir)"
Assert-PathExists -Path "exec_outputs/catalog" -PathType Container -Hint "create catalog by running bootstrap or ensure exec_outputs/catalog exists"

if ([string]::IsNullOrWhiteSpace($env:RESEARCH_DATA_ROOT_MAP_JSON)) {
    $rawCsvsRoot = $null
    if (-not [string]::IsNullOrWhiteSpace($env:RESEARCH_DATA_LAKE_ROOT)) {
        $candidate = Join-Path $env:RESEARCH_DATA_LAKE_ROOT "Raw CSVs"
        if (Test-Path $candidate -PathType Container) {
            $rawCsvsRoot = (Resolve-Path $candidate).Path
        }
    }
    if ($null -eq $rawCsvsRoot -and (Test-Path "G:\Raw CSVs" -PathType Container)) {
        $rawCsvsRoot = (Resolve-Path "G:\Raw CSVs").Path
    }
    if ($null -ne $rawCsvsRoot) {
        $env:RESEARCH_DATA_ROOT_MAP_JSON = (@{ "Raw CSVs" = $rawCsvsRoot } | ConvertTo-Json -Compress)
        Write-Host "NOTE: set RESEARCH_DATA_ROOT_MAP_JSON for ES5m materialize using '$rawCsvsRoot'." -ForegroundColor Yellow
    }
}

if ([string]::IsNullOrWhiteSpace($DatasetRoot) -and [string]::IsNullOrWhiteSpace($env:RESEARCH_DATA_ROOT_MAP_JSON) -and -not (Test-CanReusePinnedEs5mDataset)) {
    throw "Preflight failed: step [1/5] needs either --DatasetRoot, RESEARCH_DATA_ROOT_MAP_JSON, or a reusable pinned ES5m dataset entry in exec_outputs/catalog/entries. Next action: set RESEARCH_DATA_ROOT_MAP_JSON (e.g. {'Raw CSVs':'G:\Raw CSVs'}) or pass -DatasetRoot <ES5m folder>."
}

$generatedProjectPath = "configs/analysis/local/project.es_5m.generated.json"
if (Test-Path $generatedProjectPath -PathType Leaf) {
    $generatedProjectContent = Get-Content -Raw $generatedProjectPath
    if ($generatedProjectContent -match [regex]::Escape("configs/analysis/local/specs")) {
        $generatedProjectContent = $generatedProjectContent.Replace("configs/analysis/local/specs", "configs/analysis/specs")
        [System.IO.File]::WriteAllText($generatedProjectPath, $generatedProjectContent, [System.Text.UTF8Encoding]::new($false))
        Write-Host "NOTE: replaced stale 'configs/analysis/local/specs' with canonical 'configs/analysis/specs' (local/specs is invalid for ES5m)." -ForegroundColor Yellow
    }
}

function Invoke-Step {
    param(
        [string]$StepLabel,
        [scriptblock]$Step
    )

    Write-Host $StepLabel
    & $Step
    if ($LASTEXITCODE -ne 0) {
        throw "Pipeline step failed with exit code ${LASTEXITCODE}: $StepLabel"
    }
}

Invoke-Step "[1/5] Register ES5m dataset" {
    if ([string]::IsNullOrWhiteSpace($DatasetRoot)) {
        & "./docs/scripts/register_es5m_dataset.ps1"
    }
    else {
        & "./docs/scripts/register_es5m_dataset.ps1" -DatasetRoot $DatasetRoot
    }
}

Write-Host "NOTE: ES5m materialize uses canonical spec_dir 'configs/analysis/specs' (local/specs is invalid)." -ForegroundColor Yellow

Invoke-Step "[2/5] Materialize ES5m project" {
    & "./docs/scripts/materialize_es5m_project.ps1"
}

Invoke-Step "[3/5] Create ES5m runset" {
    & "./docs/scripts/create_es5m_runset.ps1"
}

Invoke-Step "[4/5] Promote ES5m baseline" {
    & "./docs/scripts/promote_es5m_baseline.ps1"
}

Invoke-Step "[5/5] Run ES5m analysis gates" {
    & "./docs/scripts/run_analysis_es_5m.ps1" -Runsets "configs/analysis/local/runsets.es_5m.generated.json"
}

$runsetsPayload = Get-Content -Raw "configs/analysis/local/runsets.es_5m.generated.json" | ConvertFrom-Json
$runsetIds = @($runsetsPayload.runset_ids)

Write-Host ""
Write-Host "Final output paths:" -ForegroundColor Green
Write-Host "- exec_outputs/analysis/es_5m/doctor/ci.doctor.summary.json"
Write-Host "- exec_outputs/analysis/es_5m/dashboard/dashboard.summary.json"
foreach ($runsetId in $runsetIds) {
    Write-Host "- exec_outputs/analysis/es_5m/risk_runset/$runsetId/risk.runset.summary.json"
    Write-Host "- baselines/prod/$runsetId/baseline.card.json"
}