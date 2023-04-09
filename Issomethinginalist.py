#Here we will be asking is something in a list
#Python provides two operators that let us check if an item ins in a list
#These are logical operators they returns True or False ,they donot modify the list
x=[1,2,3,4,5,6]
y=2 in x
print(y)
#True
z=20 in x
print(z)
#False
a=20 not in x
print(a)
#True
#b=x.find(5) #Not right as list are mutable no need to copy it and write it
#print(b)
#'list' object has no attribute 'find'
#c=['a','b','c']
#c.find('a') # we can't use find operator in list
#print(c)

fruit='bana2na'
pos=fruit.find('na')
print(pos)
#2
