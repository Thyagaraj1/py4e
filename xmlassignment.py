#In this assignment you will write a Python program somewhat similar to 
#http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, 
#read the XML data from that URL using urllib and then parse and 
#extract the comment counts from the XML data, compute the sum of the numbers in the file.
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1658635.xml (Sum ends with 24)
#You do not need to save these files to your folder since your program will read the data directly from the URL. Note: 
#Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

import xml.etree.ElementTree as ET 
import urllib.request,urllib.parse,urllib.error 
#from bs4 import BeautifulSoup 

url=input('Url: ')
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/comments_42.xml'
xml=urllib.request.urlopen(url).read() #string data  
objectdata=ET.fromstring(xml) #converting into object data of element-tree  
#line 1338, in XML
   # parser.feed(text)
#TypeError: a bytes-like object is required, not 'HTTPResponse' #read() was missing 
comment=objectdata.findall('comments/comment') #finding all the comments below comments 
#print(comment)
#[<Element 'comment' at 0x000001F49378F6F0>, <Element 'comment' at 0x000001F49378F330>, <Element 'comment' at 0x000001F49378F420>, <Element 'comment' at 0x000001F49378F510>, <Element 'comment' at 0x000001F49378F790>, <Element 'comment' at 0x000001F49378F880>, <Element 'comment' at 0x000001F49378F970>, <Element 'comment' at 0x000001F49378FA60>, <Element 'comment' at 0x000001F49378FB50>, 
#<Element 'comment' at 0x000001F49378FC40>, <Element 'comment' at 0x000001F49378FD30>, <Element 'comment' at 0x000001F49378FE20>, <Element 'comment' at 0x000001F49378FF10>, <Element 'comment' at 
#0x000001F4937AC040>, <Element 'comment' at 0x000001F4937AC130>, <Element 'comment' at 0x000001F4937AC220>, <Element 'comment' at 0x000001F4937AC310>, <Element 'comment' at 0x000001F4937AC400>, <Element 'comment' at 0x000001F4937AC4F0>, <Element 'comment' at 0x000001F4937AC5E0>, <Element 'comment' at 0x000001F4937AC6D0>, <Element 'comment' at 0x000001F4937AC7C0>, <Element 'comment' at 0x000001F4937AC8B0>, <Element 'comment' at 0x000001F4937AC9A0>, <Element 'comment' at 0x000001F4937ACA90>, <Element 'comment' at 0x000001F4937ACB80>, <Element 'comment' at 0x000001F4937ACC70>, <Element 'comment' at 0x000001F4937ACD60>, <Element 'comment' at 0x000001F4937ACE50>, <Element 'comment' at 0x000001F4937ACF40>, <Element 'comment' at 0x000001F4937AD030>, <Element 'comment' at 0x000001F4937AD120>, <Element 'comment' at 0x000001F4937AD210>, <Element 'comment' at 0x000001F4937AD300>, <Element 'comment' at 0x000001F4937AD3F0>, <Element 'comment' at 0x000001F4937AD4E0>, <Element 'comment' at 0x000001F4937AD5D0>, <Element 'comment' at 0x000001F4937AD6C0>, <Element 'comment' at 0x000001F4937AD7B0>, <Element 'comment' at 0x000001F4937AD8A0>, <Element 'comment' at 0x000001F4937AD990>, <Element 'comment' at 0x000001F4937ADA80>, <Element 'comment' at 0x000001F4937ADB70>, <Element 'comment' at 0x000001F4937ADC60>, <Element 'comment' at 0x000001F4937ADD50>, <Element 'comment' at 0x000001F4937ADE40>, <Element 'comment' at 0x000001F4937ADF30>, <Element 'comment' at 0x000001F4937AE020>, <Element 'comment' at 0x000001F4937AE110>, <Element 'comment' at 0x000001F4937AE200>]
print('Count: ',len(comment))
#Count:  50

sum=0
for items in comment:
    #print('Name: ',items.find('name').text)
    #print('count: ',items.find('count').text)
#Name:  Romina
#count:  97
    count=items.find('count').text
    sum=sum+int(count)
    #print(sum)
#97
#194
#etc
#2553
print(sum)
#2553




