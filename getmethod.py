#syntax:- dict.get(key,defaultvalue) #key-value
names={'Yogi':1,'Kiran':3,'Manju':0}
print(names.get('Manju')) #Key should be as strings as in dictionary
#0
print(names.get('Thyaga'))
#None
print(names.get('Thyaga','Not available'))
#Not available
print(names.get('Kiran','Not available'))
#3

#
dict=dict()
names=['Manju','Kiran','Yogi','Manju','Yogi','Manju','manju']
for name in names:
    dict[name]=dict.get(name,0)+1 #dict.get(key,defaultvalue)
print(dict)
#{'Manju': 3, 'Kiran': 1, 'Yogi': 2, 'manju': 1}


#numbers=dict()
#number=['1':1,'2':2,'3':3,4:'4',5:'6'] # we are writing dict it should be in culry bracket
#number=['1','2','3','4','6']
#for num in number:
    #numbers[num]=numbers.get(num,0)+1
#print(numbers)

#File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\getmethod.py", line 22
#number=['1':1,'2':2,'3':3,4:'4',5:'6']
#SyntaxError: invalid syntax


#dict=dict() # soln {} issue with dict as it might be repeated it gives an error of it's not callable
#number=['Manju','Kiran','Yogi','Manju','Yogi','Manju','manju']
#for num in number:
    #dict[num]=dict.get(num,0)+1
#print(dict)
#Traceback (most recent call last):
  #File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\getmethod.py", line 33, in <module>
    #dict=dict()
        # ^^^^^^
#TypeError: 'dict' object is not callable


a={}
number=['1','2','3','4','4','5','7','1','1','1']
for num in number:
    a[num]=a.get(num,0)+1
print(a)
#{'1': 4, '2': 1, '3': 1, '4': 2, '5': 1, '7': 1}
