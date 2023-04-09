fname=input('Please enter file name: ')
if len(fname)<1:
    fname='Trial.txt'
try:
    fhandle=open(fname)
except:
    print('please enter valid file name')
count = 0
for line in fhandle:
    line = line.rstrip()
    #if line == "": continue
    #if not line.startswith('From:'):continue #skipping those lines not starting with From
    #print(line) # wrong method as startswith filters all lines with From including From: colon so not specific so need to break this into words using split to filter again From only
    #From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    #From: stephen.marquard@uct.ac.za
    words = line.split()
    #print('words: ',words)
    #words:  ['Return-Path:', '<postmaster@collab.sakaiproject.org>']
    #words:  ['Received:', 'from', 'murder', '(mail.umich.edu', '[141.211.14.90])']
    #words:  ['----------------------']
    #words:  ['[]']
    #words:  ['From:', 'stephen.marquard@uct.ac.za']
    if words[0] !="From": continue #if word[0] is not equal to From then skip those lines
    #if not line.startswith('From'):continue, will not apply to lists
    #['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
    print(words[1]) #gives the same output without using
    #stephen.marquard@uct.ac.za
    #IndexError: list index out of range, we get this error when their is only index value having 0
    count = count+1

print ("There were", count, "lines in the file with From as the first word")
