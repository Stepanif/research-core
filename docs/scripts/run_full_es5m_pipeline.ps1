$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$env:RESEARCH_CREATED_UTC = (git show -s --format=%cI HEAD).Trim()

Write-Host "[1/5] Register ES5m dataset"
& "./docs/scripts/register_es5m_dataset.ps1"

Write-Host "[2/5] Materialize ES5m project"
& "./docs/scripts/materialize_es5m_project.ps1"

Write-Host "[3/5] Create ES5m runset"
& "./docs/scripts/create_es5m_runset.ps1"

Write-Host "[4/5] Promote ES5m baseline"
& "./docs/scripts/promote_es5m_baseline.ps1"

Write-Host "[5/5] Run ES5m analysis gates"
& "./docs/scripts/run_analysis_es_5m.ps1"

$runsetsPayload = Get-Content -Raw "configs/analysis/runsets.es_5m.json" | ConvertFrom-Json
$runsetIds = @($runsetsPayload.runset_ids)

Write-Host ""
Write-Host "Final output paths:" -ForegroundColor Green
Write-Host "- exec_outputs/analysis/es_5m/doctor/ci.doctor.summary.json"
Write-Host "- exec_outputs/analysis/es_5m/dashboard/dashboard.summary.json"
foreach ($runsetId in $runsetIds) {
    Write-Host "- exec_outputs/analysis/es_5m/risk_runset/$runsetId/risk.runset.summary.json"
    Write-Host "- baselines/prod/$runsetId/baseline.card.json"
}