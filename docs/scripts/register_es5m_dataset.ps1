param(
    [string]$DatasetRoot,
    [string]$PythonExe = "python"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
if ($PSVersionTable.PSVersion.Major -ge 7) {
    $PSNativeCommandUseErrorActionPreference = $false
}

$env:RESEARCH_CREATED_UTC = (git show -s --format=%cI HEAD).Trim()

$catalogDir = "exec_outputs/catalog"
$datasetIdPath = "configs/analysis/_es5m_dataset_id.txt"
$datasetsConfigPath = "configs/analysis/datasets.es_5m.json"
$projectConfigPath = "configs/analysis/project.es_5m.json"

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

function Resolve-Es5mRoot {
    param(
        [string]$DatasetRoot
    )

    if (-not [string]::IsNullOrWhiteSpace($DatasetRoot)) {
        if (-not (Test-Path $DatasetRoot -PathType Container)) {
            Write-Host "ERROR: Provided --DatasetRoot path does not exist: $DatasetRoot" -ForegroundColor Red
            Write-Host "Next action: pass a valid ES 5m dataset directory (contains raw file) via --DatasetRoot." -ForegroundColor Yellow
            exit 2
        }
        return (Resolve-Path $DatasetRoot).Path
    }

    $rawMapJson = $env:RESEARCH_DATA_ROOT_MAP_JSON
    if ([string]::IsNullOrWhiteSpace($rawMapJson)) {
        Write-Host "ERROR: Dataset root not provided and RESEARCH_DATA_ROOT_MAP_JSON is not set." -ForegroundColor Red
        Write-Host "Next action: set RESEARCH_DATA_ROOT_MAP_JSON (e.g. {'Raw CSVs':'G:\\Raw CSVs'}) or pass --DatasetRoot <ES5m folder>." -ForegroundColor Yellow
        exit 2
    }

    try {
        $map = $rawMapJson | ConvertFrom-Json
    }
    catch {
        Write-Host "ERROR: RESEARCH_DATA_ROOT_MAP_JSON is invalid JSON." -ForegroundColor Red
        Write-Host "Next action: set RESEARCH_DATA_ROOT_MAP_JSON to a valid object, e.g. {'Raw CSVs':'G:\\Raw CSVs'}." -ForegroundColor Yellow
        exit 2
    }

    if (-not ($map.PSObject.Properties.Name -contains "Raw CSVs")) {
        Write-Host "ERROR: RESEARCH_DATA_ROOT_MAP_JSON is missing key 'Raw CSVs'." -ForegroundColor Red
        Write-Host "Next action: add key 'Raw CSVs' with an absolute root path or pass --DatasetRoot explicitly." -ForegroundColor Yellow
        exit 2
    }

    $baseRoot = [string]$map."Raw CSVs"
    if ([string]::IsNullOrWhiteSpace($baseRoot) -or -not (Test-Path $baseRoot -PathType Container)) {
        Write-Host "ERROR: 'Raw CSVs' root is missing or not found: $baseRoot" -ForegroundColor Red
        Write-Host "Next action: fix RESEARCH_DATA_ROOT_MAP_JSON['Raw CSVs'] or pass --DatasetRoot explicitly." -ForegroundColor Yellow
        exit 2
    }

    $matches = @(Get-ChildItem -Path $baseRoot -Directory -Recurse | Where-Object {
            $_.Name -match '^ES\s+(5m|5min|300s|00:05)\b'
        } | Sort-Object FullName)

    if ($matches.Count -eq 0) {
        Write-Host "ERROR: No ES 5m dataset directories found under '$baseRoot'." -ForegroundColor Red
        Write-Host "Next action: add an ES 5m raw directory (e.g., 'ES 5min ...') and rerun, or pass --DatasetRoot." -ForegroundColor Yellow
        exit 2
    }

    if ($matches.Count -gt 1) {
        Write-Host "ERROR: Multiple ES 5m dataset directories found under '$baseRoot'." -ForegroundColor Red
        $matches | ForEach-Object { Write-Host "- $($_.FullName)" }
        Write-Host "Next action: rerun with --DatasetRoot <exact-directory> to remove ambiguity." -ForegroundColor Yellow
        exit 2
    }

    return $matches[0].FullName
}

function Update-Es5mConfigs {
    param(
        [string]$DatasetId
    )

    $datasetsPayload = Get-Content -Raw $datasetsConfigPath | ConvertFrom-Json
    if (-not $datasetsPayload.datasets -or $datasetsPayload.datasets.Count -eq 0) {
        Write-Host "ERROR: Invalid datasets config shape in '$datasetsConfigPath'." -ForegroundColor Red
        Write-Host "Next action: restore datasets.es_5m.json to include at least one datasets[] row." -ForegroundColor Yellow
        exit 2
    }
    $datasetsPayload.datasets[0].dataset_id = $DatasetId
    $datasetsPayload.datasets[0].instrument = "ES"
    $datasetsPayload.datasets[0].tf = "5m"
    Write-Utf8NoBom -Path $datasetsConfigPath -Content ($datasetsPayload | ConvertTo-Json -Depth 8)

    $projectPayload = Get-Content -Raw $projectConfigPath | ConvertFrom-Json
    if (-not $projectPayload.datasets -or $projectPayload.datasets.Count -eq 0) {
        Write-Host "ERROR: Invalid project config shape in '$projectConfigPath'." -ForegroundColor Red
        Write-Host "Next action: restore project.es_5m.json to include at least one datasets[] row." -ForegroundColor Yellow
        exit 2
    }
    $projectPayload.datasets[0].dataset_id = $DatasetId
    $projectPayload.datasets[0].instrument = "ES"
    $projectPayload.datasets[0].tf = "5m"
    Write-Utf8NoBom -Path $projectConfigPath -Content ($projectPayload | ConvertTo-Json -Depth 12)
}

function Convert-ToRelativePath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FromPath,
        [Parameter(Mandatory = $true)]
        [string]$ToPath
    )

    $fromUri = New-Object System.Uri((Resolve-Path $FromPath).Path.TrimEnd('\\') + "\\")
    $toUri = New-Object System.Uri((Resolve-Path $ToPath).Path)

    if ($fromUri.Scheme -ne $toUri.Scheme) {
        Write-Host "ERROR: Cannot compute relative path across different schemes/drives." -ForegroundColor Red
        Write-Host "Next action: run from a workspace on the same drive as raw data or supply a relative dataset path." -ForegroundColor Yellow
        exit 2
    }

    $relativeUri = $fromUri.MakeRelativeUri($toUri)
    $relativePath = [System.Uri]::UnescapeDataString($relativeUri.ToString()).Replace('/', '\\')
    if ([string]::IsNullOrWhiteSpace($relativePath)) {
        return "."
    }
    return $relativePath
}

function Find-ExistingEs5mDatasetId {
    param(
        [string]$CatalogRoot
    )

    $entriesDir = Join-Path $CatalogRoot "entries"
    if (-not (Test-Path $entriesDir -PathType Container)) {
        return $null
    }

    $candidateIds = @()
    Get-ChildItem -Path $entriesDir -Filter "*.json" -File | ForEach-Object {
        try {
            $entry = Get-Content -Raw $_.FullName | ConvertFrom-Json
            $kind = [string]$entry.kind
            $root = [string]$entry.source.root
            if ($kind -eq "raw_vendor_v1" -and $root -match 'ES\s+(5m|5min|300s|00:05)') {
                $id = [string]$entry.dataset_id
                if ($id -match '^[a-f0-9]{64}$') {
                    $candidateIds += $id
                }
            }
        }
        catch {
        }
    }

    $candidateIds = @($candidateIds | Sort-Object -Unique)
    if ($candidateIds.Count -eq 1) {
        return $candidateIds[0]
    }
    return $null
}

$es5mRoot = Resolve-Es5mRoot -DatasetRoot $DatasetRoot
$registerRoot = Convert-ToRelativePath -FromPath (Get-Location).Path -ToPath $es5mRoot

$rawFiles = @(Get-ChildItem -Path $es5mRoot -File | Where-Object { $_.Extension -in @('.txt', '.csv') })
if ($rawFiles.Count -eq 0) {
    Write-Host "ERROR: ES5m dataset directory has no .txt/.csv files: $es5mRoot" -ForegroundColor Red
    Write-Host "Next action: point --DatasetRoot to a raw dataset directory containing one source file." -ForegroundColor Yellow
    exit 2
}

$desc = "raw_vendor_v1 ES 5m ANALYSIS_ES_5MIN"
$previousErrorAction = $ErrorActionPreference
$ErrorActionPreference = "Continue"
$registerOutput = & $PythonExe -m research_core.cli dataset register raw --catalog $catalogDir --root $registerRoot --desc $desc 2>&1
$registerExitCode = $LASTEXITCODE
$ErrorActionPreference = $previousErrorAction
$datasetId = $null

if ($registerExitCode -ne 0) {
    $outText = (@($registerOutput) -join "`n")
    if ($outText -match 'Immutable dataset entry conflict') {
        $idCandidates = [regex]::Matches($outText, '([a-f0-9]{64})')
        if ($idCandidates.Count -gt 0) {
            $datasetId = $idCandidates[$idCandidates.Count - 1].Groups[1].Value
        }
        if ([string]::IsNullOrWhiteSpace($datasetId)) {
            $datasetId = Find-ExistingEs5mDatasetId -CatalogRoot $catalogDir
        }
        if (-not [string]::IsNullOrWhiteSpace($datasetId)) {
            Write-Host "Dataset already registered; reusing existing dataset_id: $datasetId" -ForegroundColor Yellow
        }
    }

    if ([string]::IsNullOrWhiteSpace($datasetId)) {
        Write-Host "ERROR: dataset register raw failed." -ForegroundColor Red
        $registerOutput | ForEach-Object { Write-Host $_ }
        Write-Host "Next action: confirm catalog path '$catalogDir' exists and relative root '$registerRoot' resolves to '$es5mRoot'." -ForegroundColor Yellow
        exit 2
    }
}
else {
    $datasetIdLine = @($registerOutput | Where-Object { $_ -match '^REGISTERED dataset_id=([a-f0-9]{64})$' } | Select-Object -Last 1)
    if ($datasetIdLine.Count -eq 0) {
        Write-Host "ERROR: Could not parse dataset_id from dataset register output." -ForegroundColor Red
        $registerOutput | ForEach-Object { Write-Host $_ }
        Write-Host "Next action: rerun command manually and ensure output includes 'REGISTERED dataset_id=<64-hex>'." -ForegroundColor Yellow
        exit 2
    }

    $datasetId = ([regex]::Match([string]$datasetIdLine[0], '^REGISTERED dataset_id=([a-f0-9]{64})$')).Groups[1].Value
}

if ([string]::IsNullOrWhiteSpace($datasetId)) {
    Write-Host "ERROR: Parsed dataset_id was empty." -ForegroundColor Red
    Write-Host "Next action: rerun registration and inspect command output for dataset_id." -ForegroundColor Yellow
    exit 2
}

Write-Utf8NoBom -Path $datasetIdPath -Content $datasetId
Update-Es5mConfigs -DatasetId $datasetId

Write-Host "Registered ES5m dataset_id: $datasetId" -ForegroundColor Green
Write-Host "- dataset_root_rel: $registerRoot"
Write-Host "- $datasetIdPath"
Write-Host "- $datasetsConfigPath"
Write-Host "- $projectConfigPath"

$global:LASTEXITCODE = 0