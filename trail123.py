import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

#url = 'http://python-data.dr-chuck.net/known_by_Conar.html'
url=input('Enter url ')
html=urllib.request.urlopen(url).read()
soupobject=BeautifulSoup(html,'html.parser')
#print(soupobject)

tags=soupobject('a')
for tag in tags:
    print(tag.get('href',None))