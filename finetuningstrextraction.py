import re 
x='From thyagaraj@gmail.com Sat Jan 5 09:14:16 2008'
y=re.findall('\S+@\S+',x)
print(y)
#['thyagaraj@gmail.com']
y=x.split()[1]
print(y)
#thyagaraj@gmail.com
#Non-greedy would give us different result 
y=re.findall('\S@\S?',x)
print(y)
#['j@g']

#Fine tuning using Parenthesis ()
#Parenthesis ()--> Not a part of match -but they tell us where to start and stop to extract 
y=re.findall('^From (\S+@\S+)',x) #'^From(\S+@\S+)'-->It won't work as it needs space after From 
print(y)
#['thyagaraj@gmail.com']

import re
with open('mbox-short.txt') as fhandle:
    for line in fhandle:
        line=line.rstrip()
        if re.findall('^From (\S+@\S+)',line): #Not considering the From: colon 
            print(line)
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008
#From zqian@umich.edu Fri Jan  4 16:10:39 2008
#From rjlowe@iupui.edu Fri Jan  4 15:46:24 2008

import re
with open('mbox-short.txt') as fhandle:
    for line in fhandle:
        line=line.rstrip()
        if re.findall('^From: (\S+@\S+)',line): #here it will consider only From: with colon 
            print(line)
#From: stephen.marquard@uct.ac.za
#From: louis@media.berkeley.edu
#From: zqian@umich.edu

#conventional method
with open('mbox-short.txt') as fhandle:
    for line in fhandle:
        #line=line.rstrip()
        #if not line.startswith('From'):continue #won't work for From 
        #print(line)
#From cwen@iupui.edu Thu Jan  3 16:23:48 2008
#From: cwen@iupui.edu
        #if not line.startswith('From:'):continue #it works for From:
        #print(line)
#From: louis@media.berkeley.edu
#From: ray@media.berkeley.edu
        #if line=='':continue
        words=line.split()
        if len(words)<2 or words[0]!='From':continue
        email=words[1]
        print(email)
        ray@media.berkeley.edu
#cwen@iupui.edu
#cwen@iupui.edu
#cwen@iupui.edu