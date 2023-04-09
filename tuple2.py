#Most useful cases of tuple 
#Assigning the two variables or more at same time to constants
(x,y)=(1,2) #Math form 
print(y)
#2

# This method is nothing but below in string method 
x=1 #x--->1
y=2 #y--->2
print(2)
#2

#Tuples and dictionaries 
#items() used to get tuples 
d=dict()
d['Key1']=1 #value is 1
d['key2']=2 #value is assigned as 2
print(d)
#{'Key1': 1, 'key2': 2}
for key,value in d.items():
    print(key,value)
#Key1 1
#key2 2
tuple=d.items()
print(tuple)
#dict_items([('Key1', 1), ('key2', 2)]) #two tuples with parenthesis 

