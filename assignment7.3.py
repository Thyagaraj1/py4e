#7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
#looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and
#compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname=input('Enter file name: ')
try:
    fhandle=open(fname)
except:
    print('Enter valid file name')
    quit()
count=0
total=0

for line in fhandle:
    if line.startswith('X-DSPAM-Confidence'):
        count+=1
        value=float(line.split()[1]) #float is compulsory to convert the string to integer
        total=total+value

avg=total/count  #exit from the for loop
print('Avg spam Confidence',avg)

#C:\Users\taralilk\OneDrive - Cisco\Documents\py4e>python assignment7.3.py
#Enter file name: mbox-short.txt
#Avg spam Confidence 0.7507185185185187
