#input function

name=input('who are you:')
print('welcome', name) #, (comma) indicates the space here --provide space

#welcome Thyagaraj

#Converting user input
#Let say we are using european lift system, where ground floor =0.If we got to
#america uf syooise we want to know on which floor we are in?
#For this we are writing a programm

#Convert elevator floop
inp=input('Europe floor?') #here we will get the in the form of string digit input which needs to be converted
usf=int(inp)+1  #string digit input is converted to integer here
print('Us floor', usf)

#input is 2
#Us floor 3

#Convert elevator floop, using try and except to avoid if someone enter the letters instead of numbers
try:
    inp=int(input('Europe floor?'))
    usf=(inp)+1
    print('Us floor', usf)
except:
    print('please enter a numberic value')
    quit()


#input is a
#output: please enter a numberic value


#Convert elevator floop, error if type conversion is not done
inp=input('Europe floor?') #here we will get the in the form of string digit input which needs to be converted
#inp='1'
#usf='1'+1 which won't work
usf=inp+1  #string digit input should be converted to integer here
print('Us floor', usf)


#Europe floor?1
#raceback (most recent call last):
  #File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\userinput.py", line 24, in <module>
    #usf=inp+1  #string digit input is converted to integer here
        #~~~^~
#TypeError: can only concatenate str (not "int") to str
