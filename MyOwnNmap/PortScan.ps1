Write-Host "
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

$Range | % {
    Test-NetConnection -ComputerName $Target -Port $_
}