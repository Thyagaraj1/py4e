#Write a program to prompt the user for hours and rate per hour to compute gross pay.

#Enter Hours: 35
#Enter Rate: 2.75
#Pay: 96.25
hours=float(input('Enter Hours: '))
rate=float(input('Enter Rate: '))
pay=hours*rate
print(pay)


#using try and except here

try:
    hours=float(input('Enter Hours: '))
    rate=float(input('Enter Rate: '))
    pay=hours*rate
    print(pay)
except:
    print('please enter numeric value')
    quit()
