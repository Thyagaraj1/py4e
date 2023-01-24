#Example  how it can be used
#astr=('Hello bob')
#istr=int(astr)
#print('First',istr)


#Traceback (most recent call last):
  #File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\tryandexcept.py", line 3, in <module>
    #istr=int(astr)
        # ^^^^^^^^^
#ValueError: invalid literal for int() with base 10: 'Hello bob'


#Using try and except
astr=('Hello bob')
try:
    istr=int(astr)  #trying to converting to integer
except:
    istr=-1
print('First',istr)

#First -1

#Usual practise have already used in input and other formate in the previous classes for tryandexcept

astr=('Hello bob')
try:
    istr=int(astr) #trying to converting to integer
    print('First',istr)
except:
    print('Please enter a numberic value')
    quit()
#Please enter a numberic value


#Convert elevator floop, using try and except to avoid if someone enter the letters instead of numbers
try:
    inp=int(input('Europe floor?'))
    usf=(inp)+1
    print('Us floor', usf)
except:
    print('please enter a numberic value')
    quit()
