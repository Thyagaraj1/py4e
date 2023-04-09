#split breaks a string into parts and produces a list of strings. we think there of words.
#String--->List of strings by split

abc='with three words'
stuff=abc.split()
print(stuff)
#['with', 'three', 'words']
print(len(stuff))
#3
for w in stuff:
    print(w)
#with
#three
#words

#Use of delimiter-->Hint
line='first;second;third'
thing=line.split() #--> Using only whitespaces
print(thing)
#['first;second;third']
print(len(thing))
#1
thing=line.split(';')# Using delimiter ;
print(thing)
#['first', 'second', 'third']
print(len(thing))
#3
print(thing[1]) #subof 1
#second


#Large white space is considered as one white space
line='A lot            of whitespace'
thing=line.split()
print(thing)
#['A', 'lot', 'of', 'whitespace']
print(len(thing))
#4
print(thing[2])
#of
