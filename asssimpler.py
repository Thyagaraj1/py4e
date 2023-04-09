#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, 
#extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
#We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment
#Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah

#I need you to open an html link and in that link I need 3rd link anchor tag, and I need you to open it, do this for 4 times means open 1st--inside it open another inside it open another and inside from this open last 4 times and find the last link and the name on that link 

#AttributeError: 'str' object has no attribute 'contents' , only element has contents 

import urllib.request, urllib.parse,urllib.error 
from bs4 import BeautifulSoup # to clean the html 

pos=int(input('Position: '))-1 # as we are using index method , entered value-1 
count=int(input('Times: ')) #No of times to be repeat the task 
url=input('Enter Url: ')

for i in range(count): #How many times we need to run the loop, 4 times so range is 4 times 
    html=urllib.request.urlopen(url).read() #1st I will open the url and read it, using urllibrary 
    soup=BeautifulSoup(html,'html.parser') #2nd I will clean the html, using htmlparser from BeautifulSoup library 
    #print(soup) #debug to know what key needs to be used from soupobjec to search it 
#</head>
#<li style="margin-top: 25px;"><a href="http://py4e-data.dr-chuck.net/known_by_Aniqa.html">Aniqa</a></li>
    tags=soup('a') #Using a as keyword to search the anchor tag lines 
    tag=tags[pos].get('href',None) #It's getting the anchor tag from 3rd position of the url link 
    #print(tag)
#http://py4e-data.dr-chuck.net/known_by_Montgomery.html & 3 others as it runs 4 times 
    url=tag # which is nothing but url=http://py4e-data.dr-chuck.net/known_by_Montgomery.html from url=http://py4e-data.dr-chuck.net/known_by_Fikret.html
    #name=tag.contents[0]
    #print(name)
    #Traceback (most recent call last):
    #File "c:\Users\taralilk\OneDrive - Cisco\Documents\py4e\asssimpler.py", line 28, in <module>
    #name=tag.contents[0]
    #name=tag.contents
#AttributeError: 'str' object has no attribute 'contents' , only element has contents 
    #print(type(tag))
    #<class 'str'>
    #print(type(tags))
    #<class 'bs4.element.ResultSet'>
    name=tags[pos].contents[0]
    print(name)
#Position: 3
#Times: 4
#Enter Url: http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Montgomery
#Mhairade
#Butchi
#Anayah
