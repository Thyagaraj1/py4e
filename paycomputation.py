#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

hours=int(input('Enter the hours:'))
rate=int(input('Enter the rate:'))
if hours<=40:
    pay=hours*rate
elif hours>40:
    pay=((40*rate)+((hours-40)*(1.5*rate)))
print(pay)

#Enter the hours:45
#Enter the rate:10
#475.0


##tryandexcept
try:
    hours=int(input('Enter the hours:'))
    rate=int(input('Enter the rate:'))
except:
    print('please enter a numberic value')
    quit()
if hours<=40:
    pay=hours*rate
elif hours>40:
    pay=((40*rate)+((hours-40)*(1.5*rate)))
print(pay)

#Enter the hours:h
#please enter a numberic value
