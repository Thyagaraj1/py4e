#Arguments and parameters are the inputs
#A parameter is a varible listed inside the parenthesis in the function definition.
#An argument is the value that is sent to the function when it is called
#here lang is a parameter listed inside the parenthesis of the function greet, and en, fr and es are the arguments which are sent to function greet which becomes greet('en') instead of lang inside the function when it is called
def greet(lang): #grert (store and resuse) is a thing we named and #lang is a variable, parameter or place holder
    if lang=='es': #lang is a parameter
        print('Hello') #def is a keyword which stores the code but doesn't excecute it unless invoked
    elif lang=='fr':
        print('Maaan')
    else:
        print('Hello')
greet('en') #calling the funciton with the argument #Argument1  #greet is a fucntion
greet('fr') #Argument2
greet('es') #Argument3

#Hello
#Maaan
#Hello

#Return function
#check out in the notes for basic idea
Big=max('Hello word')
print(Big)
#w, how we are getting this output coz we've inbuilt codes which runs andreturn function excecute the return statement then w is assigned to Big

def greet(): #Trivial function with no parameter
    return('Hello') #Hello is the residual value
print(greet(),'Thyagaraj')
print(greet(), 'Boss')

#Hello Thyagaraj
#Hello Boss

#Multiple parameter/argument
#we can have morethan 1 parameter in the function definition
#we simply add more 'arguments' when we call the function
def addtwo(a,b):#def is a defining the function, addtwo is a function , a, b are the parameters
    added=a+b #added --we are making it as a local variable , added--local variable
    return added #return statement, it is a specical statement that cab be used inside a function as we've used here or method
x=addtwo(3,5) #addedtwo here we are calling the function #x is varible, #3,5 are the arguments given to function
print(x)

#8

#Rewriting the above as per below
def function(parameter1, parameter2):#defining the function function()
    local_variable=parameter1+parameter2
    return local_variable #using return statement inside function ,which return the local_variable value(after computing) to the x which is assigned to x
varible=function(5,5)#5,5 are the Argument1 and Argument2 respectively
print(varible)

#10


##
def script():
    # program code here...
    restart =input("Would you like to restart this program?")
    if restart == "yes" or restart == "y":
        script()
    if restart == "n" or restart == "no":
        print("Script terminating. Goodbye.")
script()
