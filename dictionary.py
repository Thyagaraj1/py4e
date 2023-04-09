x='banana'
#print(x[6])
#IndexError: list index out of range
y='a' in x
print(y)
#True

x='word is full'
y=x.split()
#print(y[3])
#IndexError: list index out of range
z='word' in x
print(z)
#True


#Dictionaries
purse=dict()
purse['Money']=12
purse['Candy']=3
purse['tissues']=75
print(purse)
#{'Money': 12, 'Candy': 3, 'tissues': 75}, it could be assigned in any order unlike list
purse['Candy']=purse['Candy']+2
print(purse)
#{'Money': 12, 'Candy': 5, 'tissues': 75}


#Dictionary literals(Constants)
jjj={'Manju':5,'Kiran':7,'Yogi':8}
print(jjj)
#{'Manju': 5, 'Kiran': 7, 'Yogi': 8}
ooo={}
print(ooo)
#{}


#Many counts with Dictionary
#One common user of dictionary is counting how often we see something
ccc=dict()
ccc['csev']=1
ccc['cwen']=1
print(ccc)
#{'csev': 1, 'cwen': 1}
ccc['cwen']=ccc['cwen']+1
print(ccc)
#{'csev': 1, 'cwen': 2}
#print(ccc['Thyaga'])
#Traceback (most recent call last):
  #File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\dictionary.py", line 48, in <module>
    #print(ccc['Thyaga'])
#KeyError: 'Thyaga'
x='Thyaga' in ccc
print(x)
#False


#when we encounter a new name, we need to add a new entry in the dictionary and if this the second or later time we have seen the name, we simply ass on to the count in the dictionary under that name.
count={} or dict()
names=['Manju','Kiran','Yogi','Thyaga','Kiran','Manju','Yogi','Manju','manju'] # data
for name in names:
    #print('name',name) # debugging options
    #name Manju
    #name Kiran
    #name Yogi
    #name Thyaga
    #name Kiran
    #name Manju
    #name Yogi
    #name Manju
    #name manju
    if name not in count:
        #print('add if not in dict', name) #debugging options
        #add if not in dict Manju
        #add if not in dict Kiran
        #add if not in dict Yogi
        #add if not in dict Thyaga
        #add if not in dict manju
        count[name]=1
        #{'Manju': 1} # example
    else:
        count[name]=count[name]+1 # if it's repeating in dictionary
    #print(count)
    #{'Manju': 1}
    #{'Manju': 1, 'Kiran': 1}
    #{'Manju': 1, 'Kiran': 1, 'Yogi': 1}
    #{'Manju': 1, 'Kiran': 1, 'Yogi': 1, 'Thyaga': 1}
    #{'Manju': 1, 'Kiran': 2, 'Yogi': 1, 'Thyaga': 1}
    #{'Manju': 2, 'Kiran': 2, 'Yogi': 1, 'Thyaga': 1}
    #{'Manju': 2, 'Kiran': 2, 'Yogi': 2, 'Thyaga': 1}
    #{'Manju': 3, 'Kiran': 2, 'Yogi': 2, 'Thyaga': 1}
    #{'Manju': 3, 'Kiran': 2, 'Yogi': 2, 'Thyaga': 1, 'manju': 1}
print(count)
#{'Manju': 3, 'Kiran': 2, 'Yogi': 2, 'Thyaga': 1, 'manju': 1}
