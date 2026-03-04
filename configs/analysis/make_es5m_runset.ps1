$ErrorActionPreference = "Stop"

$env:RESEARCH_CREATED_UTC = (git show -s --format=%cI HEAD).Trim()

$sourceRunsetId = "9e0fb70c502a553cdfe23a4ecb3d40e1d1e48d009cf70d99e2e2331e3163078e"
$catalogDir = "exec_outputs/catalog"
$runsRoot = "exec_outputs/runs/runs"
$sourceEntryPath = Join-Path $catalogDir "runsets/entries/$sourceRunsetId.json"
$outSpecPath = "configs/analysis/runset.es_5m.json"
$outRunsetsPath = "configs/analysis/runsets.es_5m.json"

if (-not (Test-Path $sourceEntryPath -PathType Leaf)) {
    Write-Host "ERROR: Missing source runset entry '$sourceEntryPath'." -ForegroundColor Red
    Write-Host "Next action: verify the seed runset id ($sourceRunsetId) or update this script to point to an existing runset entry." -ForegroundColor Yellow
    exit 2
}

function Resolve-CanonManifestPath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RunRef
    )

    $candidates = @()

    if (Test-Path $RunRef -PathType Container) {
        $candidates += (Join-Path $RunRef "canon.manifest.json")
    }

    $leaf = Split-Path -Path $RunRef -Leaf
    if ([string]::IsNullOrWhiteSpace($leaf) -eq $false) {
        $candidates += (Join-Path (Join-Path $runsRoot $leaf) "canon.manifest.json")
    }

    foreach ($candidate in $candidates) {
        if (Test-Path $candidate -PathType Leaf) {
            return $candidate
        }
    }

    if ([string]::IsNullOrWhiteSpace($leaf) -eq $false -and (Test-Path $runsRoot -PathType Container)) {
        $recursiveDir = Get-ChildItem $runsRoot -Directory -Recurse | Where-Object { $_.Name -eq $leaf } | Select-Object -First 1
        if ($null -ne $recursiveDir) {
            $recursiveManifest = Join-Path $recursiveDir.FullName "canon.manifest.json"
            if (Test-Path $recursiveManifest -PathType Leaf) {
                return $recursiveManifest
            }
        }
    }

    return $null
}

$sourceEntry = Get-Content -Raw $sourceEntryPath | ConvertFrom-Json
$sourceRuns = @($sourceEntry.runs)

if ($sourceRuns.Count -eq 0) {
    Write-Host "ERROR: Source runset '$sourceRunsetId' has no explicit runs to inspect." -ForegroundColor Red
    Write-Host "Next action: use a source runset entry that includes runs[].run_ref values." -ForegroundColor Yellow
    exit 2
}

$selectedRuns = @()

foreach ($runRow in $sourceRuns) {
    $runRef = [string]$runRow.run_ref
    if ([string]::IsNullOrWhiteSpace($runRef)) {
        continue
    }

    $manifestPath = Resolve-CanonManifestPath -RunRef $runRef
    if ($null -eq $manifestPath) {
        Write-Host "ERROR: Could not locate canon.manifest.json for run_ref '$runRef'." -ForegroundColor Red
        Write-Host "Next action: ensure run artifacts exist under '$runsRoot' and include canon.manifest.json." -ForegroundColor Yellow
        exit 2
    }

    $canonManifest = Get-Content -Raw $manifestPath | ConvertFrom-Json
    $instrument = [string]$canonManifest.instrument
    $tf = [string]$canonManifest.tf

    if ($instrument -eq "ES" -and $tf -match '^(5m|300s|00:05)$') {
        $selectedRuns += [pscustomobject]@{
            dataset_id = [string]$runRow.dataset_id
            run_ref = [string]$runRow.run_ref
            canon_table_sha256 = [string]$runRow.canon_table_sha256
        }
    }
}

if ($selectedRuns.Count -eq 0) {
    Write-Host "ERROR: No ES 5m runs matched from source runset '$sourceRunsetId'." -ForegroundColor Red
    Write-Host "Next action: verify canon manifests for the source runs include instrument='ES' and tf matching one of: 5m, 300s, 00:05." -ForegroundColor Yellow
    exit 2
}

$selectedRuns = @($selectedRuns | Sort-Object dataset_id, run_ref)
$datasetIds = @($selectedRuns | ForEach-Object { $_.dataset_id } | Sort-Object -Unique)
$policy = $sourceEntry.policy
if ($null -eq $policy) {
    $policy = [ordered]@{
        allow_materialize_missing = $false
        require_lineage_links = $true
        require_bidirectional = $true
    }
}

$newSpec = [ordered]@{
    runset_version = "v1"
    name = "ANALYSIS_RUNSET_ES_5M_FROM_MANIFESTS"
    datasets = $datasetIds
    runs = $selectedRuns
    policy = $policy
}

$newSpec | ConvertTo-Json -Depth 8 | Set-Content -Encoding UTF8 $outSpecPath

$createOutput = python -m research_core.cli runset create --catalog $catalogDir --spec $outSpecPath
$createOutput | ForEach-Object { Write-Host $_ }

$newRunsetId = $null
foreach ($line in @($createOutput)) {
    if ($line -match 'runset_id=([0-9a-f]{64})') {
        $newRunsetId = $Matches[1]
        break
    }
}

if ($null -eq $newRunsetId) {
    Write-Host "ERROR: Failed to parse runset_id from runset create output." -ForegroundColor Red
    Write-Host "Next action: run 'python -m research_core.cli runset create --catalog $catalogDir --spec $outSpecPath' manually and verify it prints 'RUNSET_CREATED runset_id=<id>'." -ForegroundColor Yellow
    exit 2
}

([ordered]@{ runset_ids = @($newRunsetId) } | ConvertTo-Json -Compress) | Set-Content -Encoding UTF8 $outRunsetsPath

Write-Host "Created ES5m runset id: $newRunsetId" -ForegroundColor Green
Write-Host "- $outSpecPath"
Write-Host "- $outRunsetsPath"