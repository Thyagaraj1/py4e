#Conventional method 
fname=input('Enter file name: ')
if len(fname)<1:
    fname='mbox-short.txt'
try:
    fhandle=open(fname)
except:
    print('Enter valid file name')
    quit()
count=0
total=0
for line in fhandle:
    line=line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):continue 
    digits=line.split()[1]
    #t = line.find("0") #find method instead of split 
    #value =float(line[t:])
    value=float(digits)
    count+=1
    total+=value
print(total/count)
#0.7507185185185187

#using list 
with open('mbox-short.txt') as fhandle:
    numlist=list()
    for line in fhandle:
        if not line.startswith('X-DSPAM-Confidence:'):continue
        value=float(line.split()[1])
        numlist.append(value)
print(sum(numlist)/len(numlist))
#0.7507185185185187

#Using Regex method 
import re
numlist=list()
#count=0
#total=0
with open('mbox-short.txt') as fhandle:
    for line in fhandle:
        line=line.rstrip()
        stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
        #print(stuff)
        #[] #coz it has empty lines as well
        #['0.9846']
        if len(stuff)!=1:continue # if len(stuff)<1:continue
        #print(stuff)
        #['0.8475']
        #['0.6178']
        num=float(stuff[0])
        #count+=1
        #total+=num
        numlist.append(num)
print(numlist)
print(sum(numlist))
print(sum(numlist)/len(numlist))
#0.7507185185185187



