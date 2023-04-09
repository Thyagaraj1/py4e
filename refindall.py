#Matching and extracting the data 
#re.search()--> Only used to find true or false
#re.findall()--> Actually used for find matching strings and extract the same 
import re
x='My 2 favourite numbers are 19 & 42'
#y=re.search('[0-9]{3,4}',x)
#print(y)
#<re.Match object; span=(3, 4), match='2'>
#None
y=re.findall('[0-9]+',x) #filter should be in ' ' 
print(y)
#['2', '19', '42']
y=re.findall('[AEIOU]+',x)#find uppercase vowels in x,we are asking find the given matching substring
print(y)
#[]