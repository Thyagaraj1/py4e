#Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay
#which takes two parameters (hours and  rate).
#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

#if hours<40
#Math Normal pay=hours*rate
#if hours>40
#Overtime pay= (40*rate)+((hours-40)*(1.5*rate))

try:
    hours=float(input("Enter hours:"))
    rate=float(input("Enter rate:"))
except:
    print('Please enter numeric value')
    quit()

if hours<=40:
    pay=hours*rate
elif hours>40:
    pay=(40*rate)+((hours-40)*(1.5*rate))
print(pay)

###########
def function(parameter1, parameter2):
    local_variable=parameter1+parameter2
    return local_variable
variable=function(3,4)
print(variable)

## store and reusing the function with return statement
##the operation part is second one and all these willbe stored
#reuse of these will be done with calling the function with arugument
def computepay(hours,rate): #def parameters
    if hours<40: #operation part
        pay=hours*rate
    elif hours>40:
        pay=((40*rate)+((hours-40)*(1.5*rate)))
    return pay
try:
    fhours=float(input("Enter hours:"))
    frate=float(input("Enter rate:"))
except:
    print("Enter Numeric value")
    quit()
totalpay=computepay(fhours,frate)
print(totalpay)

##It shounld not be restart==n like this it should be a string like restart='n'
def function():
    restart=str(input("would you like to restart(y/n):"))
    if restart=='y' or restart=='yes':
        function()
    elif restart=='n' or restart=='no':
        print("terminating")
function()
