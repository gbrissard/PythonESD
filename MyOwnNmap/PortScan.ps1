cls ; Write-Host "
          __  ___               ___    ____ 
   ____  /  |/  /___ _____     |__ \  / __ \
  / __ \/ /|_/ / __ ``/ __ \    __/ / / / / /
 / / / / /  / / /_/ / /_/ /   / __/_/ /_/ / 
/_/ /_/_/  /_/\__,_/ .___/   /____(_)____/  
                  /_/                       
                  
                  By : HUNT3R `n`n"

$Target = Read-Host "Enter target IP address"
$RanStart = Read-Host "Enter port range start"
$RanStop = Read-Host "Enter port range stop"
$Range = $RanStart..$RanStop

function Test-Port {
    param (
        [parameter(Mandatory = $true)][string]$TargetIP,
        [parameter(Mandatory = $true)][string[]]$Ports
    )

    foreach ($Port in $Ports) {
        Start-Job -Name "port($($Port))" -ScriptBlock {
            Test-NetConnection -ComputerName $args[0] -Port $args[1] -WarningAction SilentlyContinue
        } -ArgumentList $TargetIP, $Port
    }

    $r = Get-Job | ? {$_.Name -like "port*"} | Receive-Job -Wait
    return $r
}

$Result = Test-Port -TargetIP $Target -Ports $Range
$Result | ?{$_.TcpTestSucceeded} | Select-Object RemoteAddress, RemotePort, TcpTestSucceeded | Sort-Object -Property RemotePort | ft -AutoSize