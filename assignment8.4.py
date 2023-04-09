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
    print('Please enter valid file name')
    quit()
list=list()#give me an empty list
for line in fhandle:
    #print(line)
    #But soft what light through yonder window breaks
    #these extra lines added by for loop
    #It is the east and Juliet is the sun

    #Arise fair sun and kill the envious moon

    #Who is already sick and pale with grief
    line=line.rstrip()
    #print(line)
    #But soft what light through yonder window breaks
    #It is the east and Juliet is the sun
    #Arise fair sun and kill the envious moon
    #Who is already sick and pale with grief
    words=line.split()
    #print(words)
    #['But', 'soft', 'what', 'light', 'through', 'yonder', 'window', 'breaks']
    #['It', 'is', 'the', 'east', 'and', 'Juliet', 'is', 'the', 'sun']
    #['Arise', 'fair', 'sun', 'and', 'kill', 'the', 'envious', 'moon']
    #['Who', 'is', 'already', 'sick', 'and', 'pale', 'with', 'grief']
    for word in words:
        #print(word)
        #But
        #soft
        #what
        #light
        #through
        #yonder
        #window
        #breaks
        #It
        #is
        #the
        #east
        #and
        #Juliet
        #is
        #the
        #sun
        #Arise
        #fair
        #sun
        #and
        #kill
        #the
        #envious
        #moon
        #Who
        #is
        #already
        #sick
        #and
        #pale
        #with
        #grief
        if word in list:
            continue
        else:
            list.append(word)
list.sort()
print(list)

listToStr= ' '.join(map(str, list))



with open('Output.txt','w') as output_file:
    output_file.write(listToStr)
    #Arise But It Juliet Who already and breaks east envious fair grief is kill light moon pale sick soft sun the through what window with yonder
fhandle.close()
output_file.close()


#
fname = input("Enter file name: ")
fh = open(fname)
lst = list()                       # list for the desired output
for line in fh:                    # to read every line of file romeo.txt
    word= line.rstrip().split()    # to eliminate the unwanted blanks and turn the line into a list of words
    for element in word:           # check every element in word
        if element in lst:         # if element is repeated
            continue               # do nothing
        else :                     # else if element is not in the list
            lst.append(element)    # append
lst.sort()                         # sort the list (de-indent indicates that you sort when the loop ends)
print(lst)
