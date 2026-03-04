param(
    [string]$DatasetRoot
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$env:RESEARCH_CREATED_UTC = (git show -s --format=%cI HEAD).Trim()

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