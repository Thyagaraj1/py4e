greet='          Hi bob'
lstrip=greet.lstrip()
print(lstrip)



#Stripping whitespace-.strip()

greet='  Hello Bob  ' #strips works for spacebar not for Underline as space
lstrp=greet.lstrip()
print(lstrp)
rstrp=greet.rstrip()
print(rstrp)
strp=greet.strip()
print(strp)

#Hello Bob
#  Hello Bob
#Hello Bob




#>>> greet=' Hello Bob '
#>>> greet.lstrip()
#'Hello Bob '


greet='Hello Bob'
strip=greet.strip('Hello')
print(strip)

# Bob


greet='Hello Bob'
strip=greet.strip('Bob')
print(strip)
#Hello


#Sometimes we want to take a string and rename whitespace at the beginning and/or end
#lstring() and rstring() remove whitespace at the left or right
#strip() removes both beginning and ending whitespace
#strip('bob') used to strip any sub string or string from the input
