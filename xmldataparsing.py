#importing xml library
import xml.etree.ElementTree as ET
data='''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" /> 
</person>'''

#Triple quote-->Multiple line strings
#Attribute will associate with start Tag 
#object data will be inform of element-tree 
#we have string data need to convert it into objectdata using xml library 
objectdata=ET.fromstring(data) #object data in form of element-tree 
#print(objectdata)
#<Element 'person' at 0x000001CF7435D030>
print('Name: ',objectdata.find('name').text)
print('phone: ',objectdata.find('phone').text)
print('Attribute: ',objectdata.find('email').get('hide'))
#Name:  Chuck
#phone:
#    +1 734 303 4456

#Attribute:  yes

import xml.etree.ElementTree as ET 
data='''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

#string data needs to be converted into object data which will have Element tree 
objectdata=ET.fromstring(data) #object will be in the form of element-tree 
#print(objectdata)
#<Element 'stuff' at 0x0000025F85DDD260>
#Here we have multiple child tags or two child tags 
#print('user: ', objectdata.findall('users/user')) #list of element or tags
#user:  [<Element 'user' at 0x000002740BAC1350>, <Element 'user' at 0x000002740BAC1440>]
user=objectdata.findall('users/user') #searching for all user tags below users 
#print('user:',user)#list of user tags 
#user: [<Element 'user' at 0x000001B296991350>, <Element 'user' at 0x000001B296991440>]
print('count: ',len(user))
#count:  2
#Inoder to read the list of tags which has two child tags we user for loop 
for items in user:
    print(items)
#<Element 'user' at 0x000001A127371350>
#<Element 'user' at 0x000001A127371440>
    print('Name: ',items.find('name').text)
    print('Id: ',items.find('id').text)
    print('Attribute: ',items.get('x'))

#count:  2
#<Element 'user' at 0x000001F2D88D1300>
#Name:  Chuck
#Id:  001
#Attribute:  2
#<Element 'user' at 0x000001F2D88D13F0>
#Name:  Brent
#Id:  009
#Attribute:  7
