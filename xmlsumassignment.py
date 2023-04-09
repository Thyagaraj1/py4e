import urllib.request,urllib.parse,urllib.error 
import xml.etree.ElementTree as ET 

url=input('url: ')
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/comments_1658635.xml'
xml=urllib.request.urlopen(url).read() #opening and reading #string data 
objectdata=ET.fromstring(xml) #converting into element-tree object data from string data 
#<comments>
#<comment>
#<name>Keemaya</name>
#<count>100</count>
#</comment>
comment=objectdata.findall('comments/comment') #searching for comment tag below comments tags 
#print(comment)
#print('Count',len(comment))

sum=0
for items in comment:
    number=items.find('count').text
    sum=sum+int(number)
    #le>
    #sum=sum+int(number) # if sum=0 is not defined 
    #TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'int'
print(sum)
#2524