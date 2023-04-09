#Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

#You can download the sample data at
#http://www.py4e.com/code3/mbox-short.txt
fname=input('Enter file name: ')
if len(fname)<1:
    fname='mbox-short.txt'
try:
    fhandle=open(fname)
except:
    print('Please Enter valid file name')
    quit()
count=0
for line in fhandle:
    line=line.rstrip()
    #print('line:',line)
    #Guardian --> we can write to skip the lines without any words
    #if line=='':
        #print('Skip Blank') #debugging method
        #Skip Blank
        #Skip Blank
        #continue
    word=line.split()
    #print('word:',word) #Using for debugging
    #Guardian
    #if len(word)<1:
        #print('skip')
        #[]
        #skip
        #continue
    if len(word)<3 or word[0] !='From': #skipping words not including From
    #if word[0] !='From' or len(word)<3: # it will consider the order and will not ignore [] gives IndexError: list index out of range
        #print('Ignore')
        #['You', 'can', 'modify', 'how', 'you', 'receive', 'notifications', 'at', 'My', 'Workspace', '>', 'Preferences.']
        #Ignore
        continue
    print(word[1])
    count+=1
print("There were", count, "lines in the file with From as the first word")

#Sample output for if line=='': method
#line: Course grade does not appear on "All Grades" page if no categories in gb
#word: ['Course', 'grade', 'does', 'not', 'appear', 'on', '"All', 'Grades"', 'page', 'if', 'no', 'categories', 'in', 'gb']
#Ignore
#line: ------------------------------------------------------------------------
#word: ['------------------------------------------------------------------------']
#Ignore
#line:
#Skip Blank
#line:
#Skip Blank
#line: ----------------------
#word: ['----------------------']
#Ignore
#line: This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
#word: ['This', 'automatic', 'notification', 'message', 'was', 'sent', 'by', 'Sakai', 'Collab', '(https://collab.sakaiproject.org/portal)', 'from', 'the', 'Source', 'site.']
#Ignore
#line: You can modify how you receive notifications at My Workspace > Preferences.
#word: ['You', 'can', 'modify', 'how', 'you', 'receive', 'notifications', 'at', 'My', 'Workspace', '>', 'Preferences.']
#Ignore
#There were 27 lines in the file with From as the first word


















fname=input('Please enter file name: ')
if len(fname)<1:
    fname='mbox-short.txt'
try:
    fhandle=open(fname)
except:
    print('please enter valid file name')
count=0
for line in fhandle:
    line=line.rstrip()
    #print(line)
    word=line.split()
    if word[0]=='From:':
        count+=1
        print(word)

    #print(word)
print(count)

#stephen.marquard@uct.ac.za
#<postmaster@collab.sakaiproject.org>
#from
#frankenstein.mail.umich.edu
#05
#CMU
#from
#mail.umich.edu
#05
#from
#flawless.mail.umich.edu
#5
#FROM
#holes.mr.itd.umich.edu
#Jan
#from
#paploo.uhi.ac.uk
#5
#<200801051412.m05ECIaH010327@nakamura.uits.iupui.edu>
#1.0
#7bit
#from
#paploo.uhi.ac.uk
#<source@collab.sakaiproject.org>;
#5
#from
#shmi.uhi.ac.uk
#<source@collab.sakaiproject.org>;
#from
#nakamura.uits.iupui.edu
#<source@collab.sakaiproject.org>;
#(from
#nakamura.uits.iupui.edu
#source@collab.sakaiproject.org;
#Sat,
#nakamura.uits.iupui.edu:
#source@collab.sakaiproject.org
#stephen.marquard@uct.ac.za
#[sakai]
#text/plain;
#text/plain;
#text/plain;
#Innocent
#Sat
#0.8475
#0.0000
#Traceback (most recent call last):
  #File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\assignment8.5.py", line 21, in <module>
    #word=line.split()[1]

#IndexError: list index out of range





































fname=input('Enter file name: ')
if len(fname)<1:
    fname='mbox-short.txt'
try:
    fhandle=open(fname)
except:
    print('Please enter valid fie name')
    quit()
count=0
for line in fhandle:
    line=line.rstrip()
    if line.startswith('From'):
        continue
    last=line.split()[1]
    count+=1
    print(last)
    #for text in last:
        #if '@' in text:
            #count+=1
            #print(text)
print("There were", count, "lines in the file with From as the first word")

#stephen.marquard@uct.ac.za
#stephen.marquard@uct.ac.za
#louis@media.berkeley.edu
#louis@media.berkeley.edu
#zqian@umich.edu
#zqian@umich.edu
#rjlowe@iupui.edu
#rjlowe@iupui.edu
#zqian@umich.edu
#zqian@umich.edu
#rjlowe@iupui.edu
#rjlowe@iupui.edu
#cwen@iupui.edu
#cwen@iupui.edu
#cwen@iupui.edu
#cwen@iupui.edu
#gsilver@umich.edu
#gsilver@umich.edu
#gsilver@umich.edu
#gsilver@umich.edu
#zqian@umich.edu
#zqian@umich.edu
#gsilver@umich.edu
#gsilver@umich.edu
#wagnermr@iupui.edu
#wagnermr@iupui.edu
#zqian@umich.edu
#zqian@umich.edu
#antranig@caret.cam.ac.uk
#antranig@caret.cam.ac.uk
#gopal.ramasammycook@gmail.com
#gopal.ramasammycook@gmail.com
#david.horwitz@uct.ac.za
#david.horwitz@uct.ac.za
#david.horwitz@uct.ac.za
#david.horwitz@uct.ac.za
#david.horwitz@uct.ac.za
#david.horwitz@uct.ac.za
#david.horwitz@uct.ac.za
#stephen.marquard@uct.ac.za
#stephen.marquard@uct.ac.za
#louis@media.berkeley.edu
#louis@media.berkeley.edu
#louis@media.berkeley.edu
#louis@media.berkeley.edu
#ray@media.berkeley.edu
#ray@media.berkeley.edu
#cwen@iupui.edu
#cwen@iupui.edu
#wen@iupui.edu
#cwen@iupui.edu
#cwen@iupui.edu
#cwen@iupui.edu
#There were 54 lines in the file with From as the first word
