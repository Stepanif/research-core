$ErrorActionPreference = "Stop"

$env:RESEARCH_CREATED_UTC = (git show -s --format=%cI HEAD).Trim()

# Optional data-root override (delete this line if not needed in your environment).
$env:RESEARCH_DATA_ROOT_MAP_JSON = '{"Raw CSVs":"G:\\Raw CSVs"}'

$runsetsPath = "configs/analysis/runsets.es_5m.json"
$runsetsPayload = Get-Content -Raw $runsetsPath | ConvertFrom-Json
$runsetIds = @($runsetsPayload.runset_ids)

if ($runsetIds.Count -eq 0) {
    Write-Host "ERROR: No ES 5m runset IDs found in '$runsetsPath'." -ForegroundColor Red
    Write-Host "Next action: update '$runsetsPath' with ES 5m runset IDs (scan exec_outputs/catalog/runsets/runsets.index.json and matching entries/<runset_id>.json where runs[].run_ref contains 'ES' and '5m' or 'run_ES_5m')." -ForegroundColor Yellow
    exit 2
}

python -m research_core.cli ci doctor --config configs/analysis/doctor.es_5m.json

python -m research_core.cli risk dashboard --catalog exec_outputs/catalog --root baselines/prod --runsets configs/analysis/runsets.es_5m.json --out exec_outputs/analysis/es_5m/dashboard --label prod

foreach ($runsetId in $runsetIds) {
    python -m research_core.cli risk runset --catalog exec_outputs/catalog --id $runsetId --out exec_outputs/analysis/es_5m/risk_runset
}

Write-Host ""
Write-Host "Analysis outputs:" -ForegroundColor Green
Write-Host "- exec_outputs/analysis/es_5m/doctor/ci.doctor.summary.json"
Write-Host "- exec_outputs/analysis/es_5m/dashboard/dashboard.summary.json"
foreach ($runsetId in $runsetIds) {
    Write-Host "- exec_outputs/analysis/es_5m/risk_runset/$runsetId/risk.runset.summary.json"
}