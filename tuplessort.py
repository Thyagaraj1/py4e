#Sorting of the tuples using keys 
#The very fact of storing in the dictionary is the keys will be unique and values keep on adding 
# if the keys repeats 
#we can't put the same key in more than once 
#we sort the dictionary by the key using items()method and sortes() function 
#dict={'a':10,'b':1,'c':22,'a':2} #taking dictionaries 
#a=dict.items() #converting into tuples 
#print(a) 
#dict_items([('a', 10), ('b', 1), ('c', 22)])
#dict_items([('a', 2), ('b', 1), ('c', 22)]) # if I add 'a':2 again in the dict it will consider it last one 
#as keys should be unique and not repeated 

dict={'a':10,'b':1,'c':22}
contuple=dict.items()
print(contuple)
#dict_items([('a', 10), ('b', 1), ('c', 22)])
sort=sorted(contuple)
print(sort)
#[('a', 10), ('b', 1), ('c', 22)]
#sorts based on keys 

a={'1':3,'4':1}
a.items() #converting to tuples 
sort=sorted(a.items()) #it's better to assign the a.items() in variable as we can easily call out 
print(sort)
#[('1', 3), ('4', 1)]


#trial 
a={'a':10,'b':1,'c':22,'a':1} #the mail fact of dict are it won't have duplicate keys
#as it will have unique keys, but to simply for the trying it
# it will consider the lastly assigned key and value as same as variables given values 
#x=2 #x-->2
#x=4 #x-->4
#print(x) lastly assigned value will be considered as the previous one is disgarded as it only occuy one value at a time 
#4
print(sorted(a.items())) #here .items() converting to tuples and then sorted() sorting the tuples 
#[('a', 1), ('b', 1), ('c', 22)]



