fname = input("Enter file name: ")
fh = open(fname)

count = 0
total = 0.0

for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    #value = float(line.split()[1])#here we are saying split() only substring 1
    words=line.split()
    exwords=words[1]
    value=float(exwords)
    total = total + value

average = total / count

print("Average spam confidence:", average)


#C:\Users\taralilk\OneDrive - Cisco\Documents\py4e>python assign7.2.py
#Enter file name: mbox-short.txt
#Average spam confidence: 0.7507185185185187

#The program first prompts the user for a file name using the input() function, and then opens the file using the open() function.

#It then initializes two variables: count to keep track of the number of lines that match the pattern, and total to accumulate the floating-point values from these lines.

#The program then iterates through the lines in the file using a for loop, and for each line, checks if it starts with the string "X-DSPAM-Confidence:".
#If not, the program continues to the next line. If it does match, the program increments the count variable and extracts the floating-point value from the line using the split() function,
#which splits the line into a list of words (using whitespace as the separator) and selects the second word (at index 1) which is the floating-point value. The #value is then converted to a float and added to the total.

#After processing all the lines in the file, the program computes the average by dividing the total by the count and stores the result in the average variable.

#Finally, the program prints the average spam confidence using the print() function.


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

#Using list with split method

fname = input("Enter file name: ")
fh = open(fname)

total=list()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    value = float(line.split()[1])#here we are saying split() only substring 1
    total.append(value)
    #print(total)
    #words=line.split()
    #exwords=words[1]
    #value=float(exwords)

average = sum(total) / len(total)

print("Average spam confidence:", average)
