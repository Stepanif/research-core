param(
    [string]$Runsets
)

$ErrorActionPreference = "Stop"

$env:RESEARCH_CREATED_UTC = (git show -s --format=%cI HEAD).Trim()

# Optional data-root override (delete this line if not needed in your environment).
$env:RESEARCH_DATA_ROOT_MAP_JSON = '{"Raw CSVs":"G:\\Raw CSVs"}'

$localGeneratedRunsetsPath = "configs/analysis/local/runsets.es_5m.generated.json"
$runsetsPath = $Runsets
if ([string]::IsNullOrWhiteSpace($runsetsPath)) {
    if (Test-Path $localGeneratedRunsetsPath -PathType Leaf) {
        $runsetsPath = $localGeneratedRunsetsPath
    }
    else {
        Write-Host "ERROR: No runsets path supplied and local generated runsets file is missing." -ForegroundColor Red
        Write-Host "Next action: run .\docs\scripts\create_es5m_runset.ps1 (or pass --Runsets <path>) before running analysis." -ForegroundColor Yellow
        exit 2
    }
}

if (-not (Test-Path $runsetsPath -PathType Leaf)) {
    Write-Host "ERROR: Runsets file not found: '$runsetsPath'." -ForegroundColor Red
    Write-Host "Next action: pass a valid --Runsets path or run .\docs\scripts\create_es5m_runset.ps1." -ForegroundColor Yellow
    exit 2
}

$runsetsPayload = Get-Content -Raw $runsetsPath | ConvertFrom-Json
$runsetIds = @($runsetsPayload.runset_ids)

if ($runsetIds.Count -eq 0) {
    Write-Host "ERROR: No ES 5m runset IDs found in '$runsetsPath'." -ForegroundColor Red
    Write-Host "Next action: run .\docs\scripts\create_es5m_runset.ps1 to generate and validate an ES5m runset via canon.manifest.json filtering, then rerun this script." -ForegroundColor Yellow
    exit 2
}

$doctorTemplatePath = "configs/analysis/doctor.es_5m.json"
$doctorResolvedPath = "configs/analysis/local/doctor.es_5m.generated.json"
$doctorPayload = Get-Content -Raw $doctorTemplatePath | ConvertFrom-Json
$doctorPayload.runsets_path = $runsetsPath

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($doctorResolvedPath, ($doctorPayload | ConvertTo-Json -Depth 8), $utf8NoBom)

python -m research_core.cli ci doctor --config $doctorResolvedPath

python -m research_core.cli risk dashboard --catalog exec_outputs/catalog --root baselines/prod --runsets $runsetsPath --out exec_outputs/analysis/es_5m/dashboard --label prod

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