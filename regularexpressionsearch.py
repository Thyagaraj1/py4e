#finding using find() method
with open('mbox-short.txt') as fhandle:
    for line in fhandle:
        line=line.rstrip()
        if line.find('From:')>=0:
            print(line)
#From: stephen.marquard@uct.ac.za
#From: louis@media.berkeley.edu
#From: zqian@umich.edu
#From: rjlowe@iupui.edu
#From: zqian@umich.edu
#From: rjlowe@iupui.edu
#etc

import re #import regular expression 
with open('mbox-short.txt') as fhandle:
    for line in fhandle:
        line=line.rstrip()
        if re.search('From:',line): #regular expression search 'From:' from each line
            print(line)
#From: stephen.marquard@uct.ac.za
#From: louis@media.berkeley.edu
#From: zqian@umich.edu
#From: rjlowe@iupui.edu
#From: zqian@umich.edu
#From: rjlowe@iupui.edu
#etc