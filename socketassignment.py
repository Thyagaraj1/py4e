#socket
#connect
#send
#recv
import socket
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0/n/n'.encode() #unicode to UFT-8 encoding 
socket.send(cmd)

while True:
    data=socket.recv(512)
    if (len(data)<1):
        break 
    print(data.decode())#UFT-8 to Unicode decoding 
socket.close()