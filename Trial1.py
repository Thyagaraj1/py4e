####################

def script(parameter1,parameter2):
    restart=input('Would you like to restart the program? y/n:' )
    if restart=='yes' or restart=='y':
        script(parameter1,parameter2)
    local_variable=parameter1+parameter2
    return local_variable

variable=script(5,4)
print(variable)

########################
def script(parameter1,parameter2):
    restart=input('Would you like to restart the program? y/n:' )
    if restart=='yes' or restart=='y':
        script(parameter1,parameter2)
    elif restart=='no' or restart=='n':
        print('Terminating the program')
        quit() #Using this will terminate the program without running further
    local_variable=parameter1+parameter2
    return local_variable

variable=script(5,4)
print(variable)





#Simple program to restart the program
def script():
    # program code here...
    restart =input("Would you like to restart this program?")
    if restart == "yes" or restart == "y":
        script()
    if restart == "n" or restart == "no":
        print("Script terminating. Goodbye.")
script()


#Would you like to restart the program? y/n:y
#Would you like to restart the program? y/n:n
#9
#Would you like to restart the program? y/n:y
#Would you like to restart the program? y/n:y
#Would you like to restart the program? y/n:n
#Terminating the program
