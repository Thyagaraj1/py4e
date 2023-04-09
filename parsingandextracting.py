#here we search for starts of something and pulling it out
#It's a lowlevel hardway in python
#It's combination of both .find() and [:] colon slice operator
#In python 3 all are unicode string but in python 2 there are two types regula strings and unicode string
data='From Stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos=data.find('@')
print(atpos)
#21
sppos=data.find(' ',atpos) #' ' space after at position
print(sppos)
#31
host=data[atpos+1:sppos] #In slicing it includes the first position number and excludes the last ex:[1:5] it takes as 1 to 4 as index number
print(host)  #makes sure no . dot in between data.[0:5] it's wrong it should be data[0:5]
#uct.ac.za


#
data='PickupMonitoring; -::getNotificationPolicy - result=1; NotificationInfo is [2,6,1,1]'
hyphenpos=data.find('-')
print(hyphenpos)
#18
#To find the second Hyphen we need to give little more as substring
hyphenpos=data.find('- ')
print(hyphenpos)
#43
scolonpos=data.find(';',hyphenpos)
print(scolonpos)
#53
host=data[hyphenpos+2:scolonpos]
print(host)
#result=1

#
data='PickupMonitoring; -::getNotificationPolicy - result=1; NotificationInfo is [2,6,1,1]'
hyphenpos=data.find('- ')
scolonpos=data.find(';',hyphenpos)
host=data[hyphenpos+2:scolonpos]
print(host)
#result=1


print(len('banana')*7)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])
#.ma

data='From Stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
npos=data.find('n')
print(npos)
atpos=data.find('@',npos)
print(atpos)
host=data[npos+2:atpos-1]
print(host)

#marquar
