#single chile tags 
import xml.etree.ElementTree as ET 
data='''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

treeobject=ET.fromstring(data) #give me object data from the given string daata, object data will have elements or nodes 
print('Name:',treeobject.find('name').text)
print('Attr:',treeobject.find('email').get('hide'))

#Multiple child tags
#we use for loop to runs through multiple child tags 
#Triple quote-->Multiple line string 

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

#I have to convert the string data into object(tree,elementtree) data [list of trees ] using xml library
objectdata=ET.fromstring(data)
#Searching for all the user tag below users from elementtree object data or list of tags or elements
user=objectdata.findall('users/user') #Searching for all the user tag below users
print('count: ',len(user))

for item in user: #it will run twice as we have list of elements of user twice or two child tags 
    print('Name: ',item.find('name').text)
    print('id: ',item.find('id').text)
    print('Attribute:',item.get('x'))




