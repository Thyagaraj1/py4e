#let say we want to get only keys or values we can do it by below method
jjj={'Manju':45,'Kiran':40,'Yogi':46}
#I want only keys then
print(list(jjj))
#['Manju', 'Kiran', 'Yogi']
#We can use inbuilt keyword-->keys() keyword
print(jjj.keys())
#dict_keys(['Manju', 'Kiran', 'Yogi'])
#when we want only values we can use --->values() keyword
print(jjj.values())
#dict_values([45, 40, 46])
#if we want to get the tuples we can use--->items() keyword
print(jjj.items())
#dict_items([('Manju', 45), ('Kiran', 40), ('Yogi', 46)])


#Bonus: Two iteration variables
jjj={'Manju':45,'Kiran':40,'Yogi':46}
# we can use two iteration variables keys and values
#for iteration_variable1, iteration_variable2 in jjj: #missed out on key word items()
    #print(iteration_variable1,iteration_variable2)
#File "C:\Users\taralilk\OneDrive - Cisco\Documents\py4e\Retrievinglistofkeysandvalues.py", line 20, in <module>
#for iteration_variable1, iteration_variable2 in jjj:
#ValueError: too many values to unpack (expected 2)
for iteration_variable1, iteration_variable2 in jjj.items():
    print(iteration_variable1,iteration_variable2)

#Manju 45
#Kiran 40
#Yogi 46
