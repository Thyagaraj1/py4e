#We will establish the socket connectivity between two ports 
#80-->web server port number 
#Http(80)
#We will make sure connection happens between transport to transport layer
#Stream-->set of characters that keep coming back
#TCP(Transmission control protocol) socket connection 
#import socket
#mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #This return us the object
#mysocket.connect(('data.pr4e.org',80)) #(hostname,port) #Actual connection happens here 


#socket
#connect
#send
#recv

import socket #importing socket library 
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket object method #port hole in computer,not open and not connected 
mysocket.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0/n/n'.encode()
mysocket.send(cmd) #In HTTP-application layer we will send the request data first 

while True:
    data=mysocket.recv(512)   #recv mthod using mysocket object, recv using the socket, recv only 512 characters
    if (len(data)<1): #if length of data is zero then no data receiving end of transmission or session ,end of file
        break # we will break out of the loop and close the socket as session ended
    print(data.decode()) # we will print out the all the data received onto our screen by decoding it 
mysocket.close()

#writing the dataoutput to the output_file 
#with open('dataoutput.txt','w') as output_file:
    #output_file.write(data)
#TypeError: write() argument must be str, not bytes
#PS C:\Users\taralilk\OneDrive - Cisco\Documents\py4e> & C:/Users/taralilk/AppData/Local/Programs/odule>
    #output_file.write(data)
#TypeError: write() argument must be str, not bytes
#output_file.close()
