#comparison operative with single way

x=5
if x==5:
    print('Equals to 5')
if x>4:
    print('Greater than 4')
if x>=5:
    print('Greater than or equals to 5')
if x<6:
    print('less than 6')
if x<=5:
    print('Less than or equal to 5')
if x!=6:
    print('Not equal to 6')

#Equals to 5
#Greater than 4
#Greater than or equals to 5
#less than 6
#Less than or equal to 5
#Not equal to 6


#Two way decision
x=5
if x>5:
    print('Bigger')
else:
    print('smaller')

#smaller

#Three way decision
x=4
if x<2:
    print('smaller')
elif x<10:
    print('Medium')
else:
    print('Large')
#Medium


#
while True:
    # main program
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break


##
def script():
    # program code here...
    restart =str(input("Would you like to restart this program?"))
    if restart == "yes" or restart == "y":
        script()
    if restart == "n" or restart == "no":
        print("Script terminating. Goodbye.")
script()
