#Concatenating strings
a='hello'
b=a+'there'
print(b)
#hellothere
c=a+' '+'there'#' '--here it should have a space
print(c)
#hello there


#Using (in) as a logical operator
#we've used (in) for iterative variable but here it act as logical operator
#like: ? questioning, == or !=
fruit='banana'
'n' in fruit
#C:\Users\taralilk>python
#Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license" for more information.
#>>> fruit='banana'
#>>> 'n' in fruit
#True
#>>> 'm' in fruit
#False
#>>> 'nan' in fruit
#True
if 'a' in fruit:  #in logical expression
    print('Found it!')
#Found it!
if 'm' in fruit:
    print('Found it! as it is false')
#      Nothing printed as it indicates it's false
#The (in) expression is a logical expression that returns True or False and can be used in an if statement 
