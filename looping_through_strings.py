fruit='banana' #variable
index=0  #iterative variable
while index<len(fruit): #indefinite loop
    x=fruit[index]
    print(index,x)
    index=index+1
#0 b
#1 a
#2 n
#3 a
#4 n
#5 a

fruit='Mango'
print(fruit[3])
#g

fruit='kiwi'
print(len(fruit))
#4

fruit='Orange'
index=0
while index<len(fruit):
    x=fruit[index]
    print(index,x)
    index=index+1

#0 O
#1 r
#2 a
#3 n
#4 g
#5 e
#Unless we don't want to know the position of the character, jsut need to go through the all the characters then

fruit='apple' #fruit is a variable
for char in fruit:#char is a iterative variable
    print(char)
#a
#p
#p
#l
#e

#If we want to write a program to know the position using for loop
fruit='pomegranate'
index=-1
for char in fruit:
    index=index+1
    print(index,char)

#0 p
#1 o
#2 m
#3 e
#4 g
#5 r
#6 a
#7 n
#8 a
#9 t
#10 e

fruit='pomegranate'
print(len(fruit))
#11

fruit='pomegranate'
index=None
for char in fruit:
    if index is None:
        index=index+1
    print(index,char)
#Traceback (most recent call last):
  #File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\looping_through_strings.py", line 74, in <module>
    #index=index+1
    #  ~~~~~^~
#TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
