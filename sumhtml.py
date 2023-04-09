#http://py4e-data.dr-chuck.net/comments_42.html
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url=input('Enter url address: ')
html=urllib.request.urlopen(url).read()
soupobject=BeautifulSoup(html,'html.parser') #clening html using html.parser
#print(soupobject)
#Enter url address: http://py4e-data.dr-chuck.net/comments_42.html
#<html>
#<tr>
#<td>Name</td><td>Comments</td>
#</tr>
#<tr><td>Romina</td><td><span class="comments">97</span></td></tr>
#<tr><td>Laurie</td><td><span class="comments">97</span></td></tr>
#<tr><td>Bayli</td><td><span class="comments">90</span></td></tr>
#tr><td>Siyona</td><td><span class="comments">90</span></td></tr>
sum=0
tags=soupobject('span')
for tag in tags:
    #print(tag)
#<span class="comments">97</span>
#<span class="comments">97</span>
#<span class="comments">90</span>
#<span class="comments">90</span>
    #print(tag.get('class',None))
#['comments']
#['comments']
#['comments']
#['comments']
    #print(tag.contents)
#['90']
#['90']
#['88']
    sum=sum+int(tag.contents[0])
print(sum)
#2553
print(type(tag.contents))
#<class 'list'>