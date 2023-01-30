#Basic program
#Write a program to ask for friends name and execute as Happy new year: friend name
#ex: >Manju
#>Yogi
#>Kiran
#>done
#Happy New year: Manju
#Happy New year: Yogi
#Happy New year: Kiran

#1st simple asking for name and giving the happy new year

Name=str(input('Enter your friend name:'))
print('Happy New year:',Name)

#Enter your friend name:Manju
#Happy New year: Manju


#Using return keyword works if not will not work
def script():
    if name==('done'):
        quit()
    return('Happy New year:')
name=str(input('Enter your friend name:'))
print(script(),name)

#Enter your friend name:g
#Happy New year: g

#else :
    #script()
 #File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\Excersise_1.py", line 25, in script
    #script()
  #[Previous line repeated 996 more times]
#RecursionError: maximum recursion depth exceeded

#Using basic store and reuse function to execute the same
def script():
    if name==('done'):
        quit()
    print('Happy New year:')
name=str(input('Enter your friend name:'))
print(script(),name)

#Enter your friend name:g
#Happy New year:
#None g

##Using store and reuse with multiple parameter
def function(parameter1,parameter2):
    if name==('done'):
        quit()
    nam=parameter1,parameter2
    return nam
name1=str(input("Enter your friend name:"))
name2=str(input("Enter your frined name:"))
output=function(name1,name2)
print("Happy New year",output)


#Enter your friend name:g
#Enter your frined name:h
#Happy New year ('g', 'h')


#Best option to for use case
#while is indefinite loop
#using while loop for the same
while True:
    name=str(input("Enter your friend's name:"))
    if name=='done':
        break
    print("Happy new year",name)

#Enter your friend's name:Yogi
#Happy new year Yogi
#Enter your friend's name:Kiran
#Happy new year Kiran
#Enter your friend's name:Manju
#Happy new year Manju
#Enter your friend's name:done
#Program to run or stop the loop
while True:
    while True:
        restart=str(input('would you like to restart(y/n):'))
        if restart in ('y', 'n'):
            break
        print('Invalid input')
    if restart=='y':
        continue
    else:
        print('Goodbye')
        break
#would you like to restart(y/n):h
#Invalid input
#would you like to restart(y/n):h
#Invalid input
#would you like to restart(y/n):g
#Invalid input
#would you like to restart(y/n):n
#Goodbye

#Using for loop to print happy new year
names=str(input("Enter your frind's name:"))
for name in names:
    print('Happy New year',name)

#Happy New year M
#Happy New year a
#Happy New year n
#Happy New year j
#Happy New year u

#
names=[str(input("Enter your friend's name:"))]
for name in names:
    print('Happy New year',name)


#Enter your frind's name:Manju
#Happy New year Manju


names=[input("Enter your frind's name:")]
for name in names:
    print('Happy New year',name)

#Enter your frind's name:manju
#Happy New year manju

#Enter your frind's name:'manju','kiran'
#Happy New year 'manju','kiran'


a=name1=input('Enter your friend name:')
b=name2=input('Enter your friend name:')
c=name3=input('Enter your friend name:')
d=name4=input('Enter your friend name:')

for name in [a,b,c,d]:
    print('Happy new year',name)


#Enter your friend name:Kiran
#Enter your friend name:Yogi
#Enter your friend name:Manju
#Enter your friend name:Vinay
#Happy new year Kiran
#Happy new year Yogi
#Happy new year Manju
#Happy new year Vinay
