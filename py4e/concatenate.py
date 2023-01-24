#Only strings are added to together strings + digits can't be added
#Inorder to add string and digits the string should be of digit string and it needs to be converted

x='Hi' #string with words
y='Thyagaraj'
z='abc'
concatenate=x+y+z
print(concatenate)

#HiThyagarajabc

#Inoder to have space either space can be provided or we need to add add extra variable with space which is not preffered
x='Hi ' #string with words
y=' Thyagaraj'
z=' abc'
concatenate=x+y+z
print(concatenate)


#concatenating the strings
x='Hi'
y='123'
print(x+y)

#Hi123


#Convert the digit integer to integer for adding two numberic values 

x='123'
ix=int(x)
y=123
print(ix+y)

#246


#concatenating the strings and digits
#TypeError: can only concatenate str (not "int") to str

#x='Hi'
#y=123
#print(x+y)

#Traceback (most recent call last):
  #File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\concatenate.py", line 31, in <module>
    #print(x+y)
        #  ~^~
#TypeError: can only concatenate str (not "int") to str

#x='123'
#y=123
#print(x+y)

#Traceback (most recent call last):
  #File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\concatenate.py", line 33, in <module>
    #print(x+y)
        #  ~^~
#TypeError: can only concatenate str (not "int") to str
#x='Hi' #string with words
#y='Thyagaraj'
#z='abc'
#concatenate=x+y+z
#print(concatenata)

# if spellings are wrong and output not defined
#Traceback (most recent call last):
  #File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\concatenate.py", line 8, in <module>
    #print(concatenata)
        #  ^^^^^^^^^^^
#NameError: name 'concatenata' is not defined. Did you mean: 'concatenate'?
