#http://py4e-data.dr-chuck.net/comments_42.html

import urllib.request,urllib.parse,urllib.error 
import re
url=input('Enter url address: ')
fhandle=urllib.request.urlopen(url)
for line in fhandle:
    line=line.decode().rstrip()
    #print('Line: ',line)
#Line:  <html>
#Line:  <head>
#Line:  <title>Welcome to the comments assignment from www.py4e.com</title>
#Line:
#Line:  <tr><td>Romina</td><td><span class="comments">97</span></td></tr>
#Line:  <tr><td>Laurie</td><td><span class="comments">97</span></td></tr>
#Line:  <tr><td>Bayli</td><td><span class="comments">90</span></td></tr>

    if re.findall('[0-9]+',line):
        print(line)
#<title>Welcome to the comments assignment from www.py4e.com</title>
#<h1>This file contains the sample data for testing</h1>
#<table border="2">
#<tr><td>Romina</td><td><span class="comments">97</span></td></tr>
#<tr><td>Laurie</td><td><span class="comments">97</span></td></tr>
#<tr><td>Bayli</td><td><span class="comments">90</span></td></tr>
#<tr><td>Siyona</td><td><span class="comments">90</span></td></tr>
#<tr><td>Taisha</td><td><span class="comments">88</span></td></tr>
#<tr><td>Alanda</td><td><span class="comments">87</span></td></tr>
#<tr><td>Ameelia</td><td><span class="comments">87</span></td></tr>
#<tr><td>Prasheeta</td><td><span class="comments">80</span></td></tr>

