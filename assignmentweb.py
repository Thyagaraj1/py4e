#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, 
#extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
#We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment
#Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah

import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup

pos=int(input('Postion: '))-1 #Coz in our problem it asked for position 3 in anchor tags but if we enter 3 it will take us to 4th position as it reads on the index number basis 0,1,2,3 so we are substracting -1 from it 
count=int(input('repeat: ')) #Repeating the process 4 times asking for how many times we should repeat the process 
url=input('Enter url: ')

#tags[pos] # here we are giving index value so we are inputting -1 at the begining it self, Index-->0,1,2,3 we need only three that is index 2 
for i in range(count): #Here we are running the for loop for 4 times as per the count using range #everything under will run 4 times 
    html=urllib.request.urlopen(url).read() #Sending request for opening of url using urllibrary 
    soup=BeautifulSoup(html,'html.parser') #Asking the BeautifulSoup library to clean the html using htmlparser
#print(soup)
#Enter url: http://py4e-data.dr-chuck.net/known_by_Fikret.html
#<html>
#</center>
#<li style="margin-top: 82px;"><a href="http://py4e-data.dr-chuck.net/known_by_Atal.html">Atal</a></li>
#<li style="margin-top: 72px;"><a href="http://py4e-data.dr-chuck.net/known_by_Callun.html">Callun</a></li>
    tags=soup('a') #read through only tags with 'a' 
    tag=tags[pos].get('href',None) #get the anchor tag using href which is at position 3 ,#after that we need it to run again using the obtained anchor tag get the next anchor tag at pos 3, this process shoule repeat 4 times. as we have already given the how many times the program should run only thing we need to ask is to change the url from place the obtained url 
    #print(tag)
#http://py4e-data.dr-chuck.net/known_by_Montgomery.html
#http://py4e-data.dr-chuck.net/known_by_Montgomery.html
#http://py4e-data.dr-chuck.net/known_by_Montgomery.html
#http://py4e-data.dr-chuck.net/known_by_Montgomery.html
    #tag=url # it will yeild bad results as it gives url=url #providing the obtained new url(anchor tag) at position 3 as we need to run through it 
    #name=tags[pos].contents
    #print(name)
#['Montgomery']
#['Montgomery']
#['Montgomery']
#['Montgomery']
    #name=tags[pos].contents[0]
    #print(name)
#Montgomery
#Montgomery
#Montgomery
#Montgomery
    url=tag #providing the obtained new url(anchor tag) at position 3 as we need to run through it 
    #print(tag)
#http://py4e-data.dr-chuck.net/known_by_Montgomery.html
#http://py4e-data.dr-chuck.net/known_by_Mhairade.html
#http://py4e-data.dr-chuck.net/known_by_Butchi.html
#http://py4e-data.dr-chuck.net/known_by_Anayah.html
    name=tags[pos].contents[0] #Asking the give the contenst of index 0 at tags position 3 
    #print(name)
#Montgomery
#Mhairade
#Butchi
#Anayah
print(name)
#Anayah

#Postion: 18
#repeat: 7
#Enter url: http://py4e-data.dr-chuck.net/known_by_Taniesha.html
#Hussain