#socket-->urllib
#parsing-->BeautifulSoup
#open and read url-->urllib 
#parsing using BeautifulSoup and cleaning nasty bit of code, and giving pretty code to soup object
#what needs to be extracted for anchor tags--links
#using for loop 
#using getmethod-->print(dict.get(key,defaultvalue))

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
url=input('Enter url address: ') #need to open and read this url address
file=urllib.request.urlopen(url).read() #I'm sending a request using urllibrary to open url and read it as well
#x=BeautifulSoup(file,'file.parser') #x-soup object
  #File "C:\Users\taralilk\AppData\Local\Programs\Python\Python311\Lib\site-packages\bs4\__init__.py", line 249, in __init__
    #raise FeatureNotFound(
#bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: file.parser. Do you need to install a parser library?
x=BeautifulSoup(file,'html.parser')

#To get the anchor tags
tags=x('a') #extract the tags from x--soup object which is being parsed and cleaned 
for tag in tags:
    print(tag.get('href',None))
#/wiki/Vinod_Kambli
#/wiki/Sachin_Tendulkar
#None
#/wiki/Sunil_Gavaskar
#/wiki/New_Zealand_national_cricket_team
#/wiki/Daryl_Mitchell_(New_Zealand_cricketer)
#etc