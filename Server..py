#!/usr/bin/python

#IMPORTS
import socket

#DEFINE FILES
datei = "Senden.jpg"
log = "log.txt"

while True:
    try:
        ##ESTABLISHING SOCKET SERVER
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #BIND SOCKETSERVER TO LOCAL IP AND PORT 5000
        s.bind(('',5000))
        #ALLOW ONLY ONE CONNECTION TO THE SERVER
        s.listen(1)
        #WAIT FOR CONNECTION
        con,addr = s.accept()
        con.send("Connected, will open files")
        #OBENING AND SENDING IMAGE
        try:
            with open(datei, 'rb') as f, open(log, 'wb') as l:
                con.send("Opened files!")
                l.write("Files Opened")
                #SENDING FILES IN 1024 BIT PACKAGES
                while True:
                    l.write("1,")
                    data = f.read(1024)
                    l.write("2|")
                    con.send(data)
                    #WAITING FOR MESSAGE FROM SERVER
                    con.recv(1024)
                    #BREAK OUT OF LOOP ON END OF FILE
                    if not data:
                        break
                f.close()
                l.close()
        except Exception as fail:
            con.send(fail)
        con.close()
        s.close()
        break
        
    except Exception as ex:
        print "Did not work!"
        print ex
        try:
            con.close()
        except:
            break
        break
        
