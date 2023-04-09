import json 
data='''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

#List of dictionaries
#converting string data into object data 
objectdata=json.loads(data) #string data 
print(objectdata) #object data is List of dictionaries to go through it we will iterate using for loop 
#[{'id': '001', 'x': '2', 'name': 'Chuck'}, {'id': '009', 'x': '7', 'name': 'Brent'}]
print('Count: ',len(objectdata)) #in case of xml we search for tags under tag (users/user), we use findall method 
#Count:  2
for items in objectdata:
    #print(items)
#{'id': '001', 'x': '2', 'name': 'Chuck'}
#{'id': '009', 'x': '7', 'name': 'Brent'}
    print('Name:',items['name']) #items sub name 
    print('ID: ',items['id'])
    print('Attribute: ',items['x'])
#Name: Chuck
#ID:  001
#Attribute:  2
#Name: Brent
#ID:  009
#Attribute:  7

    #for item in items:
       # print(item)
#id
#x
