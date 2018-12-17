import socket # 10.101.200.28
import os

os.system('cls')

print """          __  ___               ___    ____ 
   ____  /  |/  /___ _____     |__ \  / __ \\
  / __ \/ /|_/ / __ `/ __ \    __/ / / / / /
 / / / / /  / / /_/ / /_/ /   / __/_/ /_/ / 
/_/ /_/_/  /_/\__,_/ .___/   /____(_)____/  
                  /_/                       
                  
                  By : HUNT3R\n\n"""

myTarget = raw_input('Enter target IP address : ')

print("\n--> BEGIN SCAN OF : " + myTarget + "\n")

for i in range(0,1000):
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print myTarget
    scanResult = mySocket.connect((str(myTarget), int(i)))
    if scanResult == 0:
        print "Port {}: 	 Open".format(i)
    else:
        print "Port {}: 	 Closed".format(i)
    mySocket.close()