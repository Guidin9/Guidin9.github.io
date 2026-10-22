# Rebuilds assets/Cv/*.pdf: cv.py writes the HTML into a temp folder, then headless
# Chrome prints it with a throwaway profile. Needs Python and Google Chrome.
# Run from anywhere: powershell -ExecutionPolicy Bypass -File _cv\build.ps1
$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
$chrome = Join-Path $env:ProgramFiles 'Google\Chrome\Application\chrome.exe'
$tmp = Join-Path ([IO.Path]::GetTempPath()) ('cv-build-' + [guid]::NewGuid())
New-Item -ItemType Directory $tmp | Out-Null
$out = [ordered]@{ tr = 'Mert_Demirdoven_CV.pdf'; en = 'Mert_Demirdoven_CV_EN.pdf' }

try {
  Push-Location $tmp
  try { python (Join-Path $PSScriptRoot 'cv.py') } finally { Pop-Location }
  if ($LASTEXITCODE -ne 0) { throw "cv.py failed ($LASTEXITCODE)" }

  foreach ($lang in $out.Keys) {
    $html = 'file:///' + ((Join-Path $tmp "cv-$lang.html") -replace '\\', '/')
    $pdf = Join-Path $root "assets\Cv\$($out[$lang])"
    # Start-Process joins arguments with spaces, so quote the paths ourselves.
    Start-Process $chrome -Wait -WindowStyle Hidden -ArgumentList @(
      '--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
      "--user-data-dir=`"$tmp\profile`"", '--no-pdf-header-footer',
      '--virtual-time-budget=15000', "--print-to-pdf=`"$pdf`"", "`"$html`"")
    "{0}: {1:N0} bytes" -f $out[$lang], (Get-Item $pdf).Length
  }
} finally {
  Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
}
