from scapy.all import * # 10.101.200.28
from random import randint
from colorama import init, Fore, Back
import os, datetime

startTime = datetime.datetime.now()
os.system('cls')

print Fore.GREEN + """          __  ___               ___    ____ 
   ____  /  |/  /___ _____     |__ \  / __ \\
  / __ \/ /|_/ / __ `/ __ \    __/ / / / / /
 / / / / /  / / /_/ / /_/ /   / __/_/ /_/ / 
/_/ /_/_/  /_/\__,_/ .___/   /____(_)____/  
                  /_/                       
                  
            By : H4CK3R_du_44\n\n""" + Fore.RESET

myTarget = raw_input('Enter target IP address : ')
rangeStart = int(input("Enter port range start : "))
rangeStop = int(input("Enter port range stop : "))
fullRange = range(rangeStart, (rangeStop + 1))
closedPorts = []
openPortCnt = 0
closedPortCnt = 0

print("\n--> BEGIN SCAN OF : " + myTarget + " (from port " + str(rangeStart) + " to " + str(rangeStop) + ")\n")

for i in fullRange:
    randSrcPort = randint(40000, 65000)
    scanResult = sr1(IP(dst=myTarget)/TCP(sport=randSrcPort, dport=i, flags="S"), timeout=10, verbose=False)
    if (scanResult.getlayer(TCP).flags == 0x12):
        openPortCnt += 1
        sr1(IP(dst=myTarget)/TCP(sport=randSrcPort, dport=i, flags="AR"), timeout=10, verbose=False)
        print(Fore.GREEN + "[+]" + Fore.RESET + " Port {}:\tOpen".format(i))
    else:
        closedPortCnt += 1
        closedPorts.append(i)

print("\nClosed ports : ")
print(closedPorts)

print "\n" + ("#" * 60)
print "#" + Back.YELLOW + Fore.BLACK + "               ---> DA FCKIN REPORT <---                  " + Fore.RESET + Back.RESET + "#"
print ("#" * 60)
print "Scanned host :\t" + str(myTarget)
print "Port range :\t" + str(rangeStart) + " -> " + str(rangeStop)
print "Open ports :\t" + Fore.GREEN + str(openPortCnt) + Fore.RESET
print "Closed ports :\t" + Fore.RED + str(closedPortCnt) + Fore.RESET

totalTime = str(datetime.datetime.now() - startTime).split(".")[0]
print("\nExec time :\t" + totalTime)

print ("#" * 60)