from scapy.all import *

def testAlive(s,d):
    a = IP()
    b = ICMP()

    a.dst = d
    a.src = s
    ping = a/b
    res = sr1(ping)
    if res.code == 0:
        print "host is up"

print testAlive("10.101.200.27", "10.101.200.28")