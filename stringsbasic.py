#looking inside strings
#'banana'--0,1,2,3,4,5 index values for 'banana'
#Index values must be an integer and starts with zero 0
#[]--index operator
#We can get any single character in string using index specified in [1] index operator
#The index value can be expression that is computed (ex:x-1)


#example
fruit='banana' #mnemonic variable #b-0,a-1,n-2,a-3,n-4,a-5
letter=fruit[1]
print(letter)
#a

fruit='banana'
x=3
letter=fruit[x-1]
print(letter)
#n

name='Thyagaraj'
print(name[3])
#a
name='Thyagaraj'
x=2
print(name[x-1])
#h

#character too far
#zot='abc'
#print(zot[5])


#Traceback (most recent call last):
 # File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\stringsbasic.py", line 25, in <module>
    #print(zot[5])
    #      ~~~^^^
#IndexError: string index out of range

#strings have length
fruit='banana'
print(len(fruit))
#6

#len()- is a built in function which gives the lenth of the string
#function is some stored code that we use. A function takes some input and produces an output
fruit='banana'
x=len(fruit)
print(x)
#6
