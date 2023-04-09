#Objects are king of variables that have capabilities that are king of grafter on to or buit ino them

#String library
#Python has a no of string functions (.lower)which are in the string library
#These functions are already buit into every string-we invoke them by appending(adding the function )
# the function to the string variable #greet.lower() --Here invoking inbuilt string function .lower by adding the function to string variable (greet)
#These functions don't modify the original string, instead they return a new string that has been altered


#example
greet='Hello Bob' #string assgined to greet #greet--string variable
zap=greet.lower() #This is just a copy of the greet #.lower -- is a inbuilt function
print(zap)
#hello bob  --Here all the upper case converte to lower case
print(greet)
#Hello Bob --#Point 3, these strings remains same

string_variable='Hello Bob' #always remember to name variable in one letter, no space allowed
converting_by_invoking_inbuilt_function=string_variable.lower() #string variable+lower() #appending the inbuilt function with string variable
print(converting_by_invoking_inbuilt_function)
#hello bob
print(string_variable) #Point 3, these strings remains same
#Hello Bob  #Point 3, these strings remains same


print('Hi there'.lower())
#hi there  # Hi there is a legit object, we've lower method inside of it 
