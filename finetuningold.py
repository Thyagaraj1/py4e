#Old conventional finding and slicing method to extract 
x='From thyagaraj@gmail.com Sat Jan 5 09:14:16 2008'
atpos=x.find('@')
lpos=x.find(' ',atpos)
host=x[atpos+1:lpos]
print(host)
#gmail.com

email=x.split()[1]
pieces=email.split('@')[1]# Delimeter
print(pieces)
#gmail.com

#How to extract using Regexp version
import re 
x='From thyagaraj@gmail.com Sat Jan 5 09:14:16 2008'
y=re.findall('@([^ ]*)',x) 
print(y)
#['gmail.com']
#@( )-->Starts from after @ 
#[^ ]--> ^--Not and space ,Everything but space. Match non-block character 
#*--->Match zero or more 
y=re.findall('@(\S+)',x) # or ('@(\S*)',x)
print(y)
#['gmail.com']
y=re.findall('@(\S*)',x) 
print(y)
#['gmail.com']

#Fine tuning 
y=re.findall('^From .*@([^ ]*)',x)
print(y)
#['gmail.com']
#^From-->Staring with From, matching the line in the begining 
#.*@-->Any no of character upto @ 
#( )-->begin extracting from after @
#[^ ]--> ^--not,  space, Everything but space 
#*- repeat zero or more times 