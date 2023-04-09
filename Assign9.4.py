fname=input('Enter file name: ')
if len(fname)<1:
    fname='mbox-short.txt'
try:
    fhandle=open(fname)
except:
    print('Enter valid file name')
    quit()
dict=dict()
for line in fhandle:
    #if line=='':continue
    words=line.split()
    #Guardian 
    if len(words)<2 or words[0]!='From:':continue #[0] index zero #it filters by written order
    email=words[1]
    dict[email]=dict.get(email,0)+1 #instead of appending to list and taking from their we are directly proceeding 
#print(dict)
#{'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3, 'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5, 'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1, 'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1, 'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}
Bigcount=None
Bigword=None
for x, y in dict.items():
    if Bigcount is None or y>Bigcount: 
        Bigword=x 
        Bigcount=y 
print(Bigword,Bigcount)
#cwen@iupui.edu 5



