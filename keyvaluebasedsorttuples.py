a={'a':10,'b':1,'c':22,'a':1} #hypthotetically considering duplicates of key which is not true in case of dictionaries 
print(sorted(a.items()))
#[('a', 1), ('b', 1), ('c', 22)]
for k,v in sorted(a.items()): # keys will be unique in dict
    print(k,v)
#a 1 sorted based on keys a to c
#b 1
#c 22
    print(v,k)
#1 a but it all sorted based on keys
#1 b
#22 c

#sorting based on keys
d={'a':10,'b':1,'c':22,'d':10} #here we could see it has duplicate values but it will sort only based on keys
print(sorted(d.items()))
#[('a', 10), ('b', 1), ('c', 22), ('d', 10)]
for k,v in sorted(d.items()): # here it will sort based on the keys so default will be sorting on keys only
    print(k,v)
#a 10
#b 1
#c 22
#d 10

#sorting based on values
d={'a':10,'b':1,'c':22}
listoftuples=list()
for k,v in d.items(): # here we are not sorting directly as it takes keys as default
    listoftuples.append((v,k))
#print(listoftuples)
#[(10, 'a'), (1, 'b'), (22, 'c')]
# Now we can sort based on values as values are the first elements ex:(10,'a)
sort=sorted(listoftuples,reverse=True) #sorted(what i'm gonna sort, how i'm gonna sort )
#here inside sorted(what,How) #sorted(what=listoftuples,How=Hightolow)
print(sort)
#[(22, 'c'), (10, 'a'), (1, 'b')]

#Duplicate values
#Here it compares the values first if the values are same then it compares the 2nd element keys

d={'a':10,'b':1,'c':22,'d':10}
listoftuples=list()
for k,v in d.items(): #converting dict to tuples in for loop
    #listoftuples.append(v,k)
    listoftuples.append((v,k)) #to give two arguements use () inside the append()
print(listoftuples)
#listoftuples.append(v,k)
#TypeError: list.append() takes exactly one argument (2 given)
#[(10, 'a'), (1, 'b'), (22, 'c'), (10, 'd')]
sort=sorted(listoftuples,reverse=True)
print(sort)
#[(22, 'c'), (10, 'd'), (10, 'a'), (1, 'b')]
#here it compares the 10>10 so these are equal it goes to keys second element in tuples
# compares between a & d so d>a so it arrange in this order

d={'a':10,'b':1,'c':22,'d':10}
listoftuples=list()
for k,v in d.items():
    listoftuples.append((k,v))
sort=sorted(listoftuples,reverse=True)
print(sort)
#[('d', 10), ('c', 22), ('b', 1), ('a', 10)]
