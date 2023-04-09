#List are mutuable
#strings are immutable
fruit='Banana' #strings are immutable, Non collection  can have only one varible
#fruit[0]='b'
print(fruit)
#Banana
lfruit=fruit.lower()
print(lfruit)
#banana
#Traceback (most recent call last):
  #File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\List.py", line 4, in <module>
    #fruit[0]='b'
    #~~~~~^^^
#TypeError: 'str' object does not support item assignment

friends=['kiran','Manju','Yogi'] #Lists are mutable , (list) collection can have multiple variables
print(friends)
#['kiran', 'Manju', 'Yogi']
friends[1]='Thyagaraj'
print(friends)
#['kiran', 'Thyagaraj', 'Yogi']

Digits=[1,2,3,4,5,6,7]
Digits[3]=3
print(Digits)
#[1, 2, 3, 3, 5, 6, 7]


#The length of lists gives us the no of elements with in the square bracket, where as for normal strings it gives letters
friends=['kiran','Manju','Yogi']
lfriends=len(friends)
print(lfriends)
#3 which gives no of elements in list

#length of the string
fruit='Banana'
print(len(fruit))
#6 which gives no of letters in string
