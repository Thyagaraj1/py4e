import json #Importing the json library 
data='''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

#The above data is in the format of dictionaries with in dictionaries {}
#Here we can see keys which will be inform of strings 
# we have python dictionary with name,phone and email keywords 
#values are chuck, another dictionary and another dictionary 
#{"name":"Chuck","phone":{"type":"intl","number":"+1 734 303 4456"},"email":{"hide":"yes"}}

#converting string data into object data(element tree)
#Asking json to load the string data 
objectdata=json.loads(data)#asking json library to convert string data to object data, here object data is in python dictionary--data structure 
print(objectdata) #object data here is python dictionary -->data structure 
#{'name': 'Chuck', 'phone': {'type': 'intl', 'number': '+1 734 303 4456'}, 'email': {'hide': 'yes'}}
print('Name:',objectdata['name']) #dict['key'],object data is dictionary here 
print('Hide:',objectdata['email']['hide']) #dict['key']subof['key'] dict['email']sub hide
#Name: Chuck
#Hide: yes this is attribute in xml format. In xml we use get method objectdata('email').get('hide')