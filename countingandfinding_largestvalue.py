#I'm writing a program to go through the each word and count the words including the repeated words
#first i will write a program to go through the line and then split it so that we can have words, in order to
# go through the words we use for loop and counts it using get method (dict)

fname=input('Enter file name: ')
if len(fname)<1:
    fname='words.txt'
try:
    fhandle=open(fname) #very essential don't keep open('fname') in strings again as it's not needed
except:
    print('Please enter valid file name')
    quit()
counts=dict()
for line in fhandle:
    #print('line:',line) #debugging
    words=line.split() # words-->mnemonic vairable name
    #print('words:',word) #debugging
    for word in words:
        #print('word:',word) #debugging
        counts[word]=counts.get(word,0)+1 #dict[key]=dict.get(key,defaultvalue)
        #we can use conventional method as well
        #if word not in words:
            #counts[word]=1
        #else:
            #counts[word]=counts[word]+1
print(counts)
#{'Writing': 1, 'programs': 2, 'or': 1, 'programming': 1, 'is': 2, 'a': 3, 'very': 2, 'creative': 1, 'and': 5, 'rewarding': 1, 'activity': 1, 'You': 1, 'can': 4, 'write': 1, 'for': 1, 'many': 2, 'reasons': 1, 'ranging': 2, 'from': 2, 'making': 1, 'your': 2, 'living': 1, 'to': 16, 'solving': 1, 'difficult': 1, 'data': 1, 'analysis': 1, 'problem': 2, 'having': 1, 'fun': 1, 'helping': 1, 'someone': 1, 'else': 1, 'solve': 1, 'This': 1, 'book': 1, 'assumes': 1, 'that': 4, '{\\em': 1, 'everyone}': 1, 'needs': 1, 'know': 2, 'how': 2, 'program': 1, 'once': 1, 'you': 4, 'program,': 1, 'will': 1, 'figure': 1, 'out': 1, 'what': 2, 'want': 1, 'do': 5, 'with': 2, 'newfound': 1, 'skills': 1, 'We': 2, 'are': 3, 'surrounded': 1, 'in': 2, 'our': 5, 'daily': 1, 'lives': 1, 'computers': 5, 'laptops': 1, 'cell': 1, 'phones': 1, 'think': 1, 'of': 5, 'these': 1, 'as': 1, 'personal': 1, 'assistants': 1, 'who': 1, 'take': 1, 'care': 1, 'things': 3, 'on': 2, 'behalf': 2, 'The': 1, 'hardware': 1, 'current-day': 1, 'essentially': 1, 'built': 1, 'continuously': 1, 'ask': 1, 'us': 2, 'the': 6, 'question': 1, 'What': 1, 'would': 2, 'like': 2, 'me': 1, 'next': 2, 'Our': 1, 'fast': 1, 'have': 1, 'vasts': 1, 'amounts': 1, 'memory': 1, 'could': 2, 'be': 1, 'helpful': 1, 'if': 1, 'we': 5, 'only': 1, 'knew': 2, 'language': 2, 'speak': 1, 'explain': 1, 'computer': 2, 'it': 1, 'If': 1, 'this': 1, 'tell': 1, 'tasks': 1, 'were': 1, 'reptitive': 1, 'Interestingly,': 1, 'kinds': 2, 'best': 1, 'often': 1, 'humans': 1, 'find': 1, 'boring': 1, 'mind-numbing': 1}

#largest_so_far=None
#for value in counts:
    #if largest_so_far is None:
        #largest_so_far=value
    #elif value>largest_so_far:
        #largest_so_far=value
#print(largest_so_far)
#{\em

#Now that we've counted using dictionary method
# we need to the largest word so far
#largest_so_far=None
#largest_word_so_far=None
#for key, value in counts.items():
    #if largest_so_far,largest_word_so_far is None:
        #largest_so_far,largest_word_so_far=value,key
    #elif value>largest_so_far,largest_word_so_far:
        #largest_so_far,largest_word_so_far=value,key
#print(largest_so_far,largest_word_so_far)
 #File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\countingandfinding_largestvalue.py", line 35
    #if largest_so_far,largest_word_so_far is None:
#SyntaxError: invalid syntax


largest_so_far=None
largest_word_so_far=None
for key, value in counts.items():
    if largest_so_far is None or value>largest_so_far: #if and elif statement in one sentence
        largest_word_so_far=key
        largest_so_far=value
print(largest_word_so_far,largest_so_far)
#to 16

 #if largest_so_far is None or value>largest_word_so_far: #if and elif statement in one sentence
#TypeError: '>' not supported between instances of 'int' and 'str'


#conventional mehtod to find the largest_word_so_far
#Biggestcount=None
#for value in counts:
    #if Biggestcount is None:
        #Biggestcount=value
    #elif value>Biggestcount:
        #Biggestcount=value
#print(Biggestcount)
#{\em


#using or statement in single sentence
l=None
for value in counts:
    if l is None or value>l:
        l=value
print(l)
#{\em

stuff = dict()
print(stuff.get('candy',-1))
