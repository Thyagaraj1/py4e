#Open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words using the split() method.
#The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
#You can download the sample data at

file=input('Enter file name: ')
try:
    fhandle=open(file)
except:
    print('Please enter valide file name')
    quit()
word_list=list() #or []
for line in fhandle:
    words=line.rstrip().split()
    for element in words:
        if element in word_list:
            continue
        else:
            word_list.append(element)
word_list.sort()
print(word_list)
listtostr=' '.join(map(str,word_list))
#print(listtostr)

with open('listtostr.txt','w') as output_file:
    output_file.write(listtostr)
fhandle.close()
output_file.close()
