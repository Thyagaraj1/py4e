#Here instead of using socket we use urllib as it's does all the socket work for us
#Python Parse through URL
#It's gonna figure out which server to talk to 
#what document to retreive 
#what HTTP version , that GET request all that stuff all is inside as it turns out it's same 
#everytime we make web request 

import urllib.request, urllib.parse, urllib.error
fhandle=urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #data written into fhandle 
for line in fhandle:#I'm reading the data which being written into fhandle 
    print(line.decode().strip()) #We are talking to external server or external world, we receive data 
    # in the form of byte or UFT-8, we need to convert(decode()) it into Unicode or string by using decode()
    #for line in fhandle[:30]:# slicing method can be used 
    #for line in fhanlde[30:]: 

#But soft what light through yonder window breaks
#It is the east and Juliet is the sun
#Arise fair sun and kill the envious moon
#Who is already sick and pale with grief




import urllib.request, urllib.parse,urllib.error
fhandle=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhandle:
    print(line.decode().strip())

#But soft what light through yonder window breaks
#It is the east and Juliet is the sun
#Arise fair sun and kill the envious moon
#Who is already sick and pale with grief



import socket
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creating a socket 
socket.connect(('data.or4e.org',80)) #connecting the socket to web 
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0/n/n'.encode() #encoding from string or Unicode to UFT-8 to byte 
socket.send(cmd) #sending the request using socket port 

while True:
    data=socket.recv(512) #getting the data via socket ,#data will be in byte or UTF-8 formate 
    if (len(data)<1): #if I'm not getting anydata, end of seesion I will be breaking out and close the socket
        break
    print(data.decode()) #decoding the received data from byte or UTF-8 to Unicode or string 
socket.close()

#Traceback (most recent call last):
  #File "c:\Users\taralilk\OneDrive - Cisco\Documents\py4e\retrievingwebpages.py", line 25, in <module>
    #socket.connect(('data.or4e.org',80)) #connecting the socket to web
#socket.gaierror: [Errno 11001] getaddrinfo failed



