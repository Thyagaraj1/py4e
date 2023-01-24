#Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and  rate).

#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0


def computepay(hr,rate):
    if hr<=40:  #No need to call the arguments as fhr here as we have parameters hr and rate and the value from the arguments will be given as input
        pay=hr*rate
    else :
        pay=((40*rate)+((hr-40)*(1.5*rate)))
    return(pay)

try:
    fhr=float(input('Enter Hours: '))
    frate=float(input('Enter rate: '))
except:
    print('Please Enter numberic value')
    quit()
totalpay=computepay(fhr, frate)
print('Pay:', totalpay)

#same as below
def computepay(hh, rr):
  if hours <= 40 :#but it not neccessory to use hours here we can use hh which is a paramenter
    retval = rate * hours
  else:
    retval = 40 * rate + (hours - 40) * 1.5 * rate
  return retval

h = input('Enter Hours: ')
r = input('Enter Rate: ')
rate = float(r)
hours = float(h)
pay = computepay(hours, rate)
print('Pay:', pay)

##store and reuse with loop 
def script():
    # program code here...
    restart =input("Would you like to restart this program?")
    if restart == "yes" or restart == "y":
        script()
    if restart == "n" or restart == "no":
        print("Script terminating. Goodbye.")
script()
