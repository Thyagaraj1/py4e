fhandle=open('mailbox.txt') #Make sure the file name is in mailbox not mailbox.txt which will be mailbox.txt.txt finally
count=0 #fhanlde is not a data, it's just a way to get to the data
for lines in fhandle:#we can open, read, write and close fhandle it's variable
    count+=1
print('Line count:',count)

#Line count: 15

fhandle=open('mailbox.txt') #Make sure the file name is in mailbox not mailbox.txt which will be mailbox.txt.txt finally
count=0 #fhanlde is not a data, it's just a way to get to the data
for lines in fhandle:#we can open, read, write and close fhandle it's variable
    count+=1
    inp=len(lines)
print('Line count:',count,inp)
#Line count: 15 12  # which is wrong


fhandle=open('mailbox.txt') #Make sure the file name is in mailbox not mailbox.txt which will be mailbox.txt.txt finally
count=0 #fhanlde is not a data, it's just a way to get to the data
for lines in fhandle:#we can open, read, write and close fhandle it's variable
    count+=1
    inp=len(fhandle)
print('Line count:',count,inp)

#TypeError: object of type '_io.TextIOWrapper' has no len()



fhandle=open('Password.txt') #the file name should be proper with including the .txt and it should be in the same folder as the programm where we've stored
count=0
for lines in fhandle:
    count+=1
print('Line count:',count)

#Line count: 1

fhandle=open('mailbox.txt')
for line in fhandle:
    host=fhandle.replace('a','z')
print(host)

#Traceback (most recent call last):
#  File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\files.py", line 18, in <module>
    #for line in fhandle:
#io.UnsupportedOperation: not readable

fhandle=open('mailbox.txt','w')
for line in fhandle:
    print(fhandle)
#Traceback (most recent call last):
 # File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\files.py", line 18, in <module>
    #for line in fhandle:
#io.UnsupportedOperation: not readable
