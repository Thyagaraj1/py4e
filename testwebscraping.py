import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup
url=input('Enter url: ')
fhandle=urllib.request.urlopen(url).read()
#print('fhandle: ', fhandle) #debugging 
#fhandle:  b'<html>\r\n<head>\r\n  <title>Dr. Charles R. Severance Home Page</title>\r\n  <meta name="verify-v1" content="WQuA2ZPREiCyTlgNh/fv0jvzKJxrpzlagjiPaakSNH0=" />\r\n<style type="text/css">\r\nbody { background: black; font-family: Arial,Helvetica,Verdana,Sans-Serif; color: white;}\r\nbody table { font-size: 11pt; }\r\na:link, a:visited, a:active { color: gray; text-decoration: none; font-weight: bold}\r\na:hover { color:orange }\r\nstrong {color: orange; }\r\nem {color: yellow; font-style: normal;}\r\n\r\n#twitter_div {\r\ncolor: yellow;\r\ntext-align: center;\r\n}\r\n#twitter_div ul {\r\ndisplay: inline;\r\nfornt-size: 75%;\r\nmargin:0px 0px 0px 0px;\r\npadding:0px 0px 0px 0px;\r\nlist-style-type: none;\r\n}\r\n#twitter_div p {\r\nmargin:0px 0px 0px 0px;\r\ntext-align: center;\r\n}\r\n</style>\r\n<link rel="alternate" type="application/rss+xml" title="RSS" href="https://www.dr-chuck.com/csev-blog/index.rdf" />\r\n<link rel="alternate" type="application/atom+xml" title="Atom" href="https://www.dr-chuck.com/csev-blog/atom.xml" />\r\n<meta name="google-trans
soupobject=BeautifulSoup(fhandle,'html.parser') #which in turn asking to clean the html file 

#extracting anchor tag
tags=soupobject('a') 
#print('tags: ',tags)
for tag in tags: #it will look for lines only with a 
    print(tag.get('href',None)) #it gets the href="  "-->data 

with open('check.txt','w') as check:
    check.write(fhandle.decode())
check.close()

with open('tags.txt','w') as tagsfile:
    tagsfile.write(tag.get('href',None))
tagsfile.close