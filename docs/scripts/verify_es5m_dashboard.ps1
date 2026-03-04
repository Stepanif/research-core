param(
    [string]$Runsets
)

$ErrorActionPreference = "Stop"

$env:RESEARCH_CREATED_UTC = (git show -s --format=%cI HEAD).Trim()

$localGeneratedRunsetsPath = "configs/analysis/local/runsets.es_5m.generated.json"
$runsetsPath = $Runsets
if ([string]::IsNullOrWhiteSpace($runsetsPath)) {
    if (Test-Path $localGeneratedRunsetsPath -PathType Leaf) {
        $runsetsPath = $localGeneratedRunsetsPath
    }
    else {
        Write-Host "ERROR: No runsets path supplied and local generated runsets file is missing." -ForegroundColor Red
        Write-Host "Expected generated file: $localGeneratedRunsetsPath" -ForegroundColor Yellow
        Write-Host "Next action: run .\docs\scripts\create_es5m_runset.ps1, or create a runsets file containing proven runset_id 4980bb092de3d6ae8996b6e935987ca8701bf530714ba5a8226658e2a1790aa9 and pass -Runsets <path>." -ForegroundColor Yellow
        exit 2
    }
}

if (-not (Test-Path $runsetsPath -PathType Leaf)) {
    Write-Host "ERROR: Runsets file not found: '$runsetsPath'." -ForegroundColor Red
    Write-Host "Next action: pass a valid -Runsets path or run .\docs\scripts\create_es5m_runset.ps1." -ForegroundColor Yellow
    exit 2
}

$payload = Get-Content -Raw $runsetsPath | ConvertFrom-Json
if (-not $payload.PSObject.Properties.Name.Contains("runset_ids") -or @($payload.runset_ids).Count -eq 0) {
    Write-Host "runsets file contains no runset_ids" -ForegroundColor Red
    Write-Host "Path: $runsetsPath" -ForegroundColor Yellow
    exit 2
}

$dashboardOutDir = "exec_outputs/analysis/es_5m/dashboard"
$dashboardSummaryPath = "$dashboardOutDir/dashboard.summary.json"
$dashboardCommand = "python -m research_core.cli risk dashboard --catalog exec_outputs/catalog --root baselines/prod --runsets `"$runsetsPath`" --out $dashboardOutDir --label prod"

Write-Host "Runsets path: $runsetsPath"
Write-Host "Dashboard out dir: $dashboardOutDir"

python -m research_core.cli risk dashboard --catalog exec_outputs/catalog --root baselines/prod --runsets "$runsetsPath" --out $dashboardOutDir --label prod

if (-not (Test-Path $dashboardSummaryPath -PathType Leaf)) {
    Write-Host "dashboard.summary.json not found" -ForegroundColor Red
    Write-Host "Expected path: $dashboardSummaryPath" -ForegroundColor Yellow
    Write-Host "Dashboard command executed:" -ForegroundColor Yellow
    Write-Host $dashboardCommand -ForegroundColor Yellow
    Write-Host "Directory listing: $dashboardOutDir" -ForegroundColor Yellow
    if (Test-Path $dashboardOutDir -PathType Container) {
        Get-ChildItem $dashboardOutDir | ForEach-Object { Write-Host "- $($_.Name)" }
    }
    else {
        Write-Host "- (directory missing)"
    }
    exit 2
}

Write-Host "DASHBOARD OK: $dashboardSummaryPath" -ForegroundColor Green
exit 0
