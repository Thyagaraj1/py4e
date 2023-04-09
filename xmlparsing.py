import xml.etree.ElementTree as ET 
data='''<person>
            <name>Chuck</name>
            <phone type="intl">
                +1 734 303 4456
            </phone>
            <email hide="yes" />
        </person>'''

treeobject=ET.fromstring(data) #give me object data from the given string daata, object data will have elements or nodes 
print('Name:',treeobject.find('name').text)
print('Attr:',treeobject.find('email').get('hide'))


#treeobject=ET.fromstring(data) # we are asking ET library to give me object data from string data 
#same seen in 
#soupobject=BeautifulSoup(html,'html.parser') # we are asking BeautifulSoup library to give us object data from string data 
# for this BeautifulSoup library uses html.parser for this 
