import socket # 10.101.200.28
import os, datetime

startTime = datetime.datetime.now()
os.system('cls')

print """          __  ___               ___    ____ 
   ____  /  |/  /___ _____     |__ \  / __ \\
  / __ \/ /|_/ / __ `/ __ \    __/ / / / / /
 / / / / /  / / /_/ / /_/ /   / __/_/ /_/ / 
/_/ /_/_/  /_/\__,_/ .___/   /____(_)____/  
                  /_/                       
                  
            By : H4CK3R_du_44\n\n"""

myTarget = raw_input('Enter target IP address : ')
rangeStart = int(input("Enter port range start : "))
rangeStop = int(input("Enter port range stop : "))
fullRange = range(rangeStart, rangeStop)
closedPorts = []

print("\n--> BEGIN SCAN OF : " + myTarget + " (from port " + str(rangeStart) + " to " + str(rangeStop) + ")\n")

for i in fullRange:
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanResult = mySocket.connect_ex((str(myTarget), int(i)))
    if scanResult == 0:
        print "[+] Port {}: 	 Open".format(i)
    else:
        closedPorts.append(i)
    mySocket.close()

print("\nClosed ports : ")
print(closedPorts)

totalTime = str(datetime.datetime.now() - startTime)

print("\nTotal time taken : " + totalTime)