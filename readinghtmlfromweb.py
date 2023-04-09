import urllib.request,urllib.parse,urllib.error
fhandle=urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhandle:
    print(line.decode().strip())
#<h1>The First Page</h1>
#<p>
#If you like, you can switch to the
#<a href="http://www.dr-chuck.com/page2.htm">
#Second Page</a>.
#</p>