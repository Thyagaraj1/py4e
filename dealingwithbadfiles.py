fname=input('Enter file name: ')
try:
    fhandle=open(fname)
except:
    print("File can't be opened:",fname)
    quit()
count=0
for line in fhandle:
    if line.startswith('To:'):
        count+=1
print('There are',count,'To lines in',fname)

#There are 4 To lines in mailbox.txt

###
fname=input('Enter file name: ')
try:
    fhandle=open(fname)
except:
    print("File can't be opened:", fname)
    quit()
count=0
for line in fhandle:
    count+=1
    print('There are', count,'lines in', fname)
#Enter file name: mailbox
#File can't be opened: mailbox

#C:\Users\taralilk\OneDrive - Cisco\Documents\py4e>python dealingwithbadfiles.py
#Enter file name: mailbox.txt
#There are 1 lines in mailbox.txt
#There are 2 lines in mailbox.txt
#There are 3 lines in mailbox.txt
#There are 4 lines in mailbox.txt
#..
#There are 169 lines in mailbox.txt
