#Finding the largest using the None
largest_so_far=None
for value in [2,3,4,540,1000,1,2]:
    if largest_so_far is None:
        largest_so_far=value
    elif vaue>largest_so_far:
        largest_so_far=value
print(largest_so_far)


##1000

##
largest_so_far=-1
print('before',largest_so_far)
for the_num in [1,54,65,7,87,89,34,21,3,2]: #iterative variable in variable
    if the_num>largest_so_far:
        largest_so_far=the_num
    print(largest_so_far,the_num)
print('after',largest_so_far)

a=num1=int(input("Enter 1st number "))
b=num2=int(input("Enter 2nd number "))
c=num3=int(input("Enter 3rd number "))
d=num4=int(input("Enter 4th number "))

largest_so_far=-1
for the_num in [a,b,c,d]:  #the_num is a iterative variable , [a,b,c,d] are variables
    if the_num>largest_so_far:
        largest_so_far=the_num
print(largest_so_far)

#Enter 1st number 5
#Enter 2nd number 4
#Enter 3rd number 3
#Enter 4th number 2
#5

##########

a=num1=int(input("Enter 1st number "))
b=num2=int(input("Enter 2nd number "))
c=num3=int(input("Enter 3rd number "))
d=num4=int(input("Enter 4th number "))


def function(parameter1,parameter2,parameter3,parameter4):
    if parameter2>parameter1:
        largest=parameter2
        return largest
    if parameter3>parameter2:
        largest=parameter3
        return largest
    if parameter4>parameter3:
        largest=parameter4
        return largest
    if parameter1>parameter4:
        largest=parameter1
        return largest

largest_so_far=function(a,b,c,d)
print(largest_so_far)


#Enter 1st number 5
#Enter 2nd number 4
#Enter 3rd number 3
#Enter 4th number 2
#5


##
a=num1=int(input("Enter 1st number "))
b=num2=int(input("Enter 2nd number "))
c=num3=int(input("Enter 3rd number "))
d=num4=int(input("Enter 4th number "))

def CompareNumbers(a, b , c, d):
    if(b > a):
        largest=b
        return largest
    if(c > b):
        largest= c
        return largest
    if(d > c):
        largest= d
        return largest
    if a>d:
        largest=a
        return largest

e= CompareNumbers(a, b, c, d)

print(e)

#Enter 1st number 5
#Enter 2nd number 4
#Enter 3rd number 3
#Enter 4th number 2
#5
