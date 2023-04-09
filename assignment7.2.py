#7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
#looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and
#compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
#count+=1
#linespos=line.find('0')
#print(linespos)
#lineepos=line.find('5')
#print(lineepos)
#host=line[linespos:lineepos+1]
#print(count)

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        t = line.find("0")
        number =float(line[t:])
        count = count + 1
        total = total + number

average = total/count
print("Average spam confidence:",average)

#C:\Users\taralilk\OneDrive - Cisco\Documents\py4e>python assignment7.2.py
#Enter file name: mbox-short.txt
#Average spam confidence: 0.7507185185185187

#fname=input('Enter file name: ')
#try:
    #fhandle=open(fname)
#except:
    #print("File can't be opened",fname)
    #quit()
#count=0
#for line in fhandle:
    #line=line.rstrip()
    #if not line.startswith('X-DSPAM-Confidence:'):
    #    continue
    #    t = line.find("0")
    #    number = float(line[t:])
    	#count +=1
    	#total = total + number
#average = total/count
#print("Average spam confidence:",average)
