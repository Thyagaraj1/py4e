#search and replace# replace('old','new')
greet='Hello Bob'
rplc=greet.replace('Bob','Jane')
print(rplc)
#Hello Jane
rplc=greet.replace('o','X')
print(rplc)
#HellX BXb

#replace fun is like a 'search and replace' operation in a word processor
#It replaces all occurances of the search string with replacement string


#Often when we're searching for a string using find() we first convert the string to lower() case so
#we can search a string regardless of case.
#find operator
fruit='BanaNa'
lfruit=fruit.lower()
ffruit=lfruit.find('N') #substring so It's not N it's 'N' as in substring
print(ffruit)
#-1

fruit='BanaNa'
ffruit=fruit.find('N') #substring so It's not N it's 'N' as in substring
print(ffruit)
#4
fruit='name I have'
rfruit=fruit.replace('I','we')
print(rfruit)
