#For the startswith used for searching prefix startswith 
with open('mbox-short.txt') as fhandle:
    for line in fhandle:
        line=line.rstrip()
        if line.startswith('From:'):
            print(line)
#From: stephen.marquard@uct.ac.za
#From: louis@media.berkeley.edu
#From: zqian@umich.edu
#From: rjlowe@iupui.edu

#filtering using regular expression 
#import re
#with open('test.txt') as fhanlde:
    #for line in fhanlde:
        #line=line.rstrip()
        #if re.search('From:',line): #^ matching the begining of the line 
            #print(line) #'^From:' --> should be matched at the beginig of line in anywhere in middle same as .startswith 
            #it will not consider anything like 'From' without colon or 'F' anything unless it is 'From:'

#From:
#From: stephen.marquard@uct.ac.za
#From: louis@media.berkeley.edu
#From: zqian@umich.edu
#From: rjlowe@iupui.edu


import re
with open('test.txt') as fhanlde:
    for line in fhandle:
        line=line.rstrip()
        if re.search('^X-\S+:',line):
            print(line)