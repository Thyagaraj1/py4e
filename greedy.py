#Using Non-greedy sign ? 

#Greedy when we use + and * as these two are greedy and pushes both ways 
import re
x='From: Using the : Character'
y=re.findall('^F.+:',x)
print(x)
#From: Using the : Character

#Non-greedy 
import re
x='From: Using the : Character'
y=re.findall('^F.+?:',x)
print(y)
#['From:']
#^F-->starts from or should match at the begining of the line 
#.-->Any character
#+-->Repeated One or more time, >=1, .+ -->any character should be one or more times repeated 
#?-->Non-greedy

#above can be writter using the regular expression as ^F.\S+:
import re
x='From: Using the : Character'
y=re.findall('^F.\S+:',x)
print(y)
#['From:']

import re
x='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y=re.findall('\S+?@\S+',x)
print(y)
#['stephen.marquard@uct.ac.za']