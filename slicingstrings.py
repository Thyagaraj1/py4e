s='Monty python'
print(s[0:4])#0 is index value which indicates starting from and 4 --upto not including
#Mont--0,1,2,3-index value and 1,2,3,4 characters

s=str(input('Any sentence:'))
print(s[2:4])#from index value 2 to 3 here upto 4 but not including it
#Any sentence:How you doning!
#w

#we're using colon(:) operator
#if we leave off the first number or last number of the slice, it is assumed to be the
#beginning or end of the string respectively
slice='Monty Python'
print(len(slice))
#12
print(slice[:2]) #intial value is not given which means it takes as beginning[0:2] --0,1
#Mo
print(slice[8:]) #staring from index value 8 which includes space as well to end of string
#thon
print(slice[:])
#Monty Python
print(slice[12:])
#            --Just a space no error thrown
print(slice[11:])
#n
print(slice[13:])
#            --Just a space no error thrown
