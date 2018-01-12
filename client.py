import socket

def connect():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        global_ip = "Lost-and-Found-app.de"
        s.connect((global_ip,5000))
        a = s.recv(1024)
        s.send("Hallo, Niklas")
        s.close
        print a
    except:
        print "Didn't work:/"
