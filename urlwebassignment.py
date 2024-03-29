#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, 
#extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
#We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment
#Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup 

pos = int(input("Position: "))-1 #For The Position
count = int(input("Times: ")) #For the Times
url = input("Enter URL: ") #For The URL

for i in range(count): #Desired times the loop should run
    html = urllib.request.urlopen(url).read() #Taking html from the web address
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a') #Only taking tag from the html file
    tag = tags[pos].get('href',None) #Only taking desired position string value from the tags list & only taking the url address
    print(tag)
    url = tag #Redefining the desired positioned url as the new url for running the loop for desired times
    name = tags[pos].contents[0] #Taking only the content from the desired positioned string
    #print(name) #Printing the name
#Montgomery
#Mhairade
#Butchi
#Anayah
#print(name)
#Anayah