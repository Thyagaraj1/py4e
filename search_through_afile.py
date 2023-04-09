#we can put an if statement in our for loop to only print lines that meet some criteria
fhand=open('mailbox.txt')
count=0
for line in fhand:
    if line.startswith('From:'):
        count+=1
        print(count,line)

#1 From: Vivek Ranjan (viveranj) <viveranj@cisco.com>\n--It will added by the text from the file, print statement adds this one more line
#\n These are from the for loop it adds new line
#2 From: Sourajit Hazra (souhazra) <souhazra@cisco.com>\n
#\n
#3 From: Janaka PERERA <janakaperera@hsbc.co.nz>\n
#\n
#4 From: Lisa Castillo -X (liscasti) <liscasti@cisco.com>\n


#Searaching through a file fixed
fhandle=open('mailbox.txt')
count=0
for line in fhandle:
    line=line.rstrip() #It considers the newlines as whitespace and elimates it as per rightstrip function from string library
    if line.startswith('From:'):
        count+=1
        print(count,line)
print(count)
#1 From: Vivek Ranjan (viveranj) <viveranj@cisco.com> \n--This is added by print statement as text from the file
#2 From: Sourajit Hazra (souhazra) <souhazra@cisco.com>\n
#3 From: Janaka PERERA <janakaperera@hsbc.co.nz>\n
#4 From: Lisa Castillo -X (liscasti) <liscasti@cisco.com>\n
#4

fhandle=open('mailbox.txt')
inp=fhandle.read()
print(inp[0:500])


#Hi Vodafone Team,

#We have checked the config from our side and no issues were found. We also compared with another working Vodafone PRI at Auckland site and the configuration was the same. I also checked for recent changes on our side and there arenâ€™t any.

#Please let us know the following :
#-       Do you see any issues at your end ?
#-       Can we have a joint tâ€™shooting session during business hours tomorrow ? We will need help with cable checks, local VF device and cables, etcâ€¦.
#-       We would als
