fname=input('Enter file name: ')
if len(fname)<1:
    fname='mbox-short.txt'
try:
    fhandle=open(fname)
except:
    print('Enter valid name')
    quit()
#list=list() #using here to save all the lines starts with From
list=list()
for line in fhandle:
    #if not line.startswith('From'): #wrong method
       # continue
    #list.append(line) #where.append(what), I'm appending the lines after filtering the lines starts with From
    #which won't work as I need to filter only mail where I don't know how much space is there to use find funtion
    # and each and every line with mail has different space so ignoring using slice method.
    words=line.split() # can be writter email=line.split()[1]
    #print('words:',words) #debug
    if len(words)<2 or words[0]!='From:':continue
    email=words[1] #index value
    #print('email:',email) #debug
    #email=line.split()[1]
    list.append(email)
#print('list:',list), #understanding below is the sample output
#list: ['stephen.marquard@uct.ac.za', 'stephen.marquard@uct.ac.za', 'louis@media.berkeley.edu']
#Now I have to find how many of times the mail has been repeated in the list and all the list counts at one place
#Basically we need dict with key-value pair
    #convetional method
dict=dict() # if we use dict() we will get traceback saying dict not collable
for email in list:
    #print('email:',email)
    #email: zqian@umich.edu #example
    #email: rjlowe@iupui.edu
    #email: cwen@iupui.edu
    #if email not in dict:
        #dict[email]=1
    #else:
        #dict[email]=dict[email]+1
    # or latest method
    dict[email]=dict.get(email,0)+1
    #print('0:   ',dict) # example
#0:    {'stephen.marquard@uct.ac.za': 1}
#0:    {'stephen.marquard@uct.ac.za': 2}
#0:    {'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 1}
#0:    {'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 2}
#print('1:  ',dict)
#1:   {'stephen.marquard@uct.ac.za': 4, 'louis@media.berkeley.edu': 6, 'zqian@umich.edu': 8, 'rjlowe@iupui.edu': 4, 'cwen@iupui.edu': 10, 'gsilver@umich.edu': 6, 'wagnermr@iupui.edu': 2, 'antranig@caret.cam.ac.uk': 2, 'gopal.ramasammycook@gmail.com': 2, 'david.horwitz@uct.ac.za': 8, 'ray@media.berkeley.edu': 2}
# Now we have arrived at the collection of key-value pair with exact time the mail sent for each mail
# we need the maximum mail sent from a single mail
Bigcount=None
Bigword=None
for Key, value in dict.items(): #items makes sure it converts into the tuples
    if Bigcount is None or value>Bigcount:
        Bigword=Key
        Bigcount=value
print(Bigword,Bigcount)
#cwen@iupui.edu 5
 #From the below program
        #if Bigcount in None:
            #Bigcount=value
        #elif value>Bigcount:
            #Bigcount=value
            
#from using .startswith('From')
#cwen@iupui.edu 10
           
