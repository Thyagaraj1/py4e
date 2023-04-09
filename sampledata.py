import re
with open('sampledata.txt') as fhandle:
    sum=0
    for line in fhandle:
        line=line.rstrip()
        stuff=re.findall('[0-9]+',line)
        #print(stuff)
        #[]
        #['1004', '9258', '4183']
        if len(stuff)<1:continue #if len(stuff)!=1:continue, is a wrong method as we have more index here 
        #print(stuff)
        #['1004', '9258', '4183']
        for number in stuff:
            sum+=int(number)
print(sum)
        
import re
fname=input('Enter file name: ')
if len(fname)<1:
    fname='actualdata.txt'
try:
    fhandle=open(fname)
except:
    print('Enter valid file name')
    quit()
sum=0
for line in fhandle:
    line=line.rstrip()
    stuff=re.findall('[0-9]+',line)
    if len(stuff)<1:continue 
    for number in stuff:
        sum+=int(number)
print(sum)
#509151 
    

#print( sum( [ int(i) for i in re.findall('[0-9]+',(open("sampledata.txt")).read()) ] ) )  #should have been ' ,open("regex... ' 

#import re
#print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )

#Python 3:
#import re
#print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
