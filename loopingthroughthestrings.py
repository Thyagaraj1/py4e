
name='Thyagaraj'
letter=name[4]
print(letter)
#g
name='Thyagaraj'
x=3
print(name[x-3])
#T

name='Thyagaraj'
print(len(name))
#9
#looping through the string letter by letter
name='Thyagaraj'
index=0
while index<len(name):
    x=name[index]
    print(index,x)
    index+=1
#0 T
#1 h
#2 y
#3 a
#4 g
#5 a
#6 r
#7 a
#8 j

name='Shashi'
index=-1
for char in name:
    index+=1
    print(index,char)

#0 S
#1 h
#2 a
#3 s
#4 h
#5 i
