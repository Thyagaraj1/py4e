#None--Is a value that we can distinctly detect different than numbers
#is--operator --not
#is not--logical operator
#is --it's not used when we are using the double equals(==)usually used for True,False or None
smallest=None
print('before')
for value in [2,3,4,540,1000,1,2]:
    if smallest is None:#statement is true for first case #This statement (is False) Not holds true as the smallest = 2 and it's not None, quashed out
        smallest=value  #smallest--2 (samllest=2),
    elif value<smallest: #value=3<smallest=2 ,this statement is also False for 2nd case, #even if both the statements are False the assigned value remains same
        smallest=value
    print(value,smallest) #1st case value=2, smallest=2, #for second case smallest assigned value remains same unless and untill it is changed or other value is assigned
print('After',smallest)


#before
#2 2
#3 2
#4 2
#540 2
#1000 2
#1 1
#2 1
#After 1

smallest=None
for value in  [2,3,4,540,1000,1,2]:
    if smallest is None:
        smallest=value
    elif value<smallest:
        smallest=value
print(smallest)

#1

largest_so_far=-1
print('before',largest_so_far)
for value in [2,3,4,540,1000,1,2]:
    if value>largest_so_far:
        largest_so_far=value
    print(largest_so_far,value)
print('After',largest_so_far)

#before -1
#2 2
#3 3
#4 4
#540 540
#1000 1000
#1000 1
#1000 2
#After 1000


#Finding the largest using the None
largest_so_far=None
for value in [2,3,4,540,1000,1,2]:
    if largest_so_far is None:
        largest_so_far=value
    elif value>largest_so_far:
        largest_so_far=value
print(largest_so_far)


#1000
