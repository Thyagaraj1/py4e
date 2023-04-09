#list are in order
#A list can hold many items & keeps those items in order until we do something to change the order
#A list can be sorted (i.e change it's order)
#The sort method(unlike in strings) means 'sortyourself'
friends=['Manju', 'Kiran','Yogi']
print(friends[1])
#Kiran
friends.sort()
print(friends)
#['Kiran', 'Manju', 'Yogi']
print(friends[1])
#Manju

x=[5,2,3,1,4]
print(x[3])
#1
x.sort()
print(x)
#[1, 2, 3, 4, 5]
print(x[3])
#4
