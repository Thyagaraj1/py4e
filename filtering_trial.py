a=str(input('Enter any thing:'))
b=str(input('Enter any thing:'))
c=str(input('Enter any thing:'))
d=str(input('Enter any thing:'))
e=str(input('Enter any thing:'))
for the_sen in [a,b,c,d,e]: #No need of [] to a=[str(input())] as we've not called as names or some other variable
    print('Happy New year', the_sen) #we've already kept the variable in [] as [a,b,c,d,e]

#Enter any thing:Thyaga
#Enter any thing:Manju
#Enter any thing:Yogi
#Enter any thing:Kiran
#Enter any thing:Me
#Happy New year Thyaga
#Happy New year Manju
#Happy New year Yogi
#Happy New year Kiran
#Happy New year Me

#C:\>python
#Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license" for more information.
#>>> help(str.isupper)
#Help on method_descriptor:

#isupper(self, /)
    #Return True if the string is an uppercase string, False otherwise.

    #A string is uppercase if all cased characters in the string are uppercase and
    #there is at least one cased character in the string.


#Using list
#give me an empty list
friends=list()
while True:
    inp=input('Enter your friend name: ')
    if inp=='done':
        break
    friends.append(inp)
print('Happy New year', friends)
#Happy New year ['Thyaga', 'Manju', 'Kiran', 'Yogi']
