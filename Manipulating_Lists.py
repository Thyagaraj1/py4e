#Concatenating the lists using +

#strings Concatenation
fruit='Banana'
type='is a fruit'
concatenate=fruit+type
print(concatenate)
#Bananais a fruit
#Lists concatenate
names=['Manju','Kiran','Yogi']
lastname=['K','C','R']
concatenate=names+lastname
print(concatenate)
#['Manju', 'Kiran', 'Yogi', 'K', 'C', 'R']

a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=a+b
print(c)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#Slicing of Lists
x='Banana'
print(x[1:2])
#a

x=['Manju','Kiran','Yogi']
print(x[0:1])
#['Manju']

#a=123456 # we can't slice integers in this Non-collection formate
#print(a[0:2])
#Traceback (most recent call last):
 # File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\Manipulating_Lists.py", line 33, in <module>
    #print(a[0:2])
        #  ~^^^^^
#TypeError: 'int' object is not subscriptable


a=[1,2,3,4,5]
#index--> 0,1,2,3,4
print(a[0:2])
#[1, 2] integers in list formate can be sliced



a=[1,2,3,4,5]
#index--> 0,1,2,3,4
print(a[2:])
#[1, 2, 3, 4, 5]


a=[1,2,3,4,5]
#index--> 0,1,2,3,4
print(a[:3])
#[3, 4, 5]



a=[1,2,3,4,5]
#index--> 0,1,2,3,4
print(a[:])
#[1, 2, 3, 4, 5]


#Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license" for more information.
#>>> x=list()
#>>> type(x)
#<class 'list'>
#>>> dir(x)
#['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', #'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
