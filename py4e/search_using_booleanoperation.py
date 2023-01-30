#True and False are constant in python
#search using boolean variable
#let say i need to search value '3' in the series of Nos, I can't go on searching so I write a programm for this.

found=False
print('before',found)
for value in [31,25,78,3,12,4,3.12]: #iteration variable in variable
    if value==3:
        found=True
    print(found,value)
print('after',found)


#before False
#False 31
#False 25
#False 78
#True 3
#True 12
#True 4
#True 3.12
#after True

#break v/s quit() the program as soon as it found the value

found=False
for value in [31,3.12,25,78,3,12,4]:
    if value==3:
        found=True
        break
    print(found,value)
print(found)

#False 31
#False 3.12
#False 25
#False 78
#True


found=False
for value in [31,3.12,25,78,3,12,4]:
    if value==3:
        found=True
        break
print(found)


#True
######

found=False
for value in [31,3.12,25,78,3,12,4]:
    if value==3:
        found=True
        quit() #when we use quit() and try running programs below it execute as it will quit running the program any other program below will not be considered.
    print(found,value)
print(found)

#False 31
#False 3.12
#False 25
#False 78
