$edgePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
$files = Get-ChildItem -Path . -Filter *.html

foreach ($file in $files) {
    $inputPath = $file.FullName
    $outputPath = $inputPath.Replace(".html", ".pdf")
    Write-Host "Exporting $inputPath to $outputPath"
    
    Start-Process -FilePath $edgePath -ArgumentList "--headless", "--print-to-pdf=`"$outputPath`"", "--disable-gpu", "`"$inputPath`"" -Wait
}
