import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore ssl certificate errors 
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter url address: ')
fhandle=urllib.request.urlopen(url,context=ctx).read()
soupobject=BeautifulSoup(fhandle,'html.parser') #asking soup to go through html and clean up all unwanted erros 

#Anchor tag finding
tags=soupobject('a')
for tag in tags:
    print(tag.get('href',None))
    
#Enter url address: https://www.dr-chuck.com/
#https://www.learnerprivacy.org/
#https://www.si.umich.edu/
#etc