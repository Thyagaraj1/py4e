#http://py4e-data.dr-chuck.net/comments_42.html
import urllib.request,urllib.parse,urllib.error 
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Why do we get SSL certificate error?
#An SSL certificate error occurs when a web browser can't verify the SSL certificate installed on a site. Rather than connect users to your website, the browser will display an error message, warning users that the site may be insecure

url=input('Enter url address: ')
fhandle=urllib.request.urlopen(url,context=ctx).read()
soupobject=BeautifulSoup(fhandle,'html.parser')#Requesting to clean the html using html.parser from BeautifulSoup

#print(soupobject) #debug
#Enter url address: http://py4e-data.dr-chuck.net/comments_42.html
#<html>
#<head>
#<title>Welcome to the comments assignment from www.py4e.com</title>
#</head>
#<tr><td>Romina</td><td><span class="comments">97</span></td></tr>
#<tr><td>Laurie</td><td><span class="comments">97</span></td></tr>
#<tr><td>Bayli</td><td><span class="comments">90</span></td></tr>
#<tr><td>Siyona</td><td><span class="comments">90</span></td></tr>
#<tr><td>Taisha</td><td><span class="comments">88</span></td></tr>

sum=0
tags=soupobject('span')
for tag in tags:
    #print(tag.contents)
#Enter url address: http://py4e-data.dr-chuck.net/comments_42.html
#['97']
#['97']
#['90']
#['90']
    sum=sum+int(tag.contents[0])
print(sum)
    
