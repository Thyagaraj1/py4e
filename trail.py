fname=input('Enter file name:')
try:
    fhandle=open(fname)
except:
    print('Enter valid file name')
    quit()
count=0
for line in fhandle:
    line=line.rstrip()
    if not 'From' in line:
        continue
    count+=1
print(count)


#C:\Users\taralilk\OneDrive - Cisco\Documents\py4e>python trail.py
#Enter file name:name
#Enter valid file name

#C:\Users\taralilk\OneDrive - Cisco\Documents\py4e>python trail.py
#Enter file name:mbox-short.txt
#54
