#'\'-->Backlash is used as a escape character in regular expression
#If we want a special regular expression characte to just behave normally (most of the time) 
#we prefix '\'

import re
x='we just received $10.00 for cookies.'
y=re.findall('\$[0-9.]+',x)
print(y)
#['$10.00']



#thyagaraj@gmail.com
#re.match() in regular expression
import re 
email=input('Enter your email address:')
pattern=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b" #'[a-zA-Z_0-9]\-\.+@[a-z]+\.[a-z]{2,3}'

if re.match(pattern,email):
    print('Valid mail ID:',email)
else:
    print('Invalid mail id')
#Valid mail ID: thyagaraj@gmail.com











#Extracting email domains: You can also use re.match() to extract the domain name from an email address
import re

email = "example@email.com"
pattern = r"\b[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Z|a-z]{2,})\b"

match = re.match(pattern, email)

if match:
    domain = match.group(1)
    print(domain)




#Checking for specific email domains: You can use re.match() to check if an email address belongs to a specific domain.
import re

email = "example@email.com"
domain = "email.com"
pattern = r"\b[A-Za-z0-9._%+-]+@" + re.escape(domain) + r"\b"

if re.match(pattern, email):
    print("Email address belongs to " + domain)
else:
    print("Email address does not belong to " + domain)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)