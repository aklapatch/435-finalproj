$srcdir = "ALOTDDS"
$files = Get-ChildItem $srcdir
$dds = $files | where {$_.extension -eq ".dds"}
$paths = New-Object System.Collections.Generic.List[System.Object]
$dds | ForEach-Object { $paths.Add($_.FullName + ".jpg" )}
For ($i=0; $i -le $dds.Length; $i++){
    $path = $dds[$i].FullName
    $destpath = $paths[$i]
    $compress =Test-Path $destpath
    if (-not $compress) {
        iex "CompressonatorCLI.exe -DecodeWith OpenGL -NumThreads 2 $path $destpath"
    }
}


