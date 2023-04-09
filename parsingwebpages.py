#webscraping-when Program or script pretends like browser and extract information,data and HTML codes from websites
#webscraping is a process of using bots to extract content and data from websites 
#webscraping extracts underlying HTML code and data stored in database 
#why we are not using ourown program with Regex,split() and find() method for parsing in HTML is 
#that HTML have lots of syntax errors and it will work only for first 2-pages after it won't work
#properly so we use built in BeautifulSoup-->Library 
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
url=input('Enter url address: ')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')#what it does is it goes through whole html file and 
#It takes all the nasty bits from webpage and cleans them up and made like a little pretty tree of things 

#Retrieve all of the anchor tags-->Links which direct us to webpages 
tags=soup('a')
for tag in tags:
    print(tag.get('href',None))
#http://www.dr-chuck.com/page2.htm

#Enter url address: https://en.wikipedia.org/wiki/Alexandra_Daddario
#bodyContent
#/wiki/Main_Page
#/wiki/Wikipedia:Contents
#/wiki/Portal:Current_events
#/wiki/Special:Random
#/wiki/Wikipedia:About
#//en.wikipedia.org/wiki/Wikipedia:Contact_us
#https://donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en
#etc plenty 