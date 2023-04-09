fname=input('Enter file name: ')
if len(fname)<1:
    fname='mbox-short.txt'
try:
    fhandle=open(fname)
except:
    print('Enter valid name')
    quit()
list=list()
for line in fhandle:
    #print('Line:',line)
    words=line.split() 
    #Words:  ['From', 'cwen@iupui.edu', 'Thu', 'Jan', '3', '16:34:40', '2008']
    #print('Words: ',words)
    if len(words)<2 or words[0]!='From:':continue# len(words)<3 which was skipping 
    #print('Filtering only : ',words)
    #Filtering only :  ['From:', 'stephen.marquard@uct.ac.za']
    email=words[1] 
    #print('Email: ',email)
    list.append(email)
#print('List: ',list)
dict=dict() 
for email in list:
    dict[email]=dict.get(email,0)+1
Bigcount=None
Bigword=None
for Key, value in dict.items(): #items makes sure it converts into the tuples
    if Bigcount is None or value>Bigcount:
        Bigword=Key
        Bigcount=value
print(Bigword,Bigcount)
#cwen@iupui.edu 5
