#Definite loop iterate through the members of set
#for loop is a definite loop

#As far as in while loop we saw that we either use logical condition like(n>0,n=n-1) or
#break statement if the logical condition is not used to make it as finite loop

#Indefinite loop
#Using logical condition
#n=5
#while n>0:
    #print('definiteloop')
    #n=n-1
#print('It exits when logical condition is false')

#Using break statement
#while True:
    #line=input('>')
    #if line[0]=='#':
        #continue
    #if line=='done':
        #break
    #print(line)
#print('Done!')


#definite loop
for i in [3,4,2,1]: #for is keyword, i--iteration variable, in--reserved word
    print(i)
print('Blastoff!')

#3
#4
#2
#1
#Blastoff!

#A definite loop with strings
friends=['Manju','Kiran','Yogi','Vinay']  #frinds--variable
for friend in friends:                     #friend--iterative variable
    print('Happy New year:',friend)
print('Done!')

#Write a program to pop happy new year ___given friend name in input
friends=[input('Enter your friend names-like x,y,z:')]
for friend in friends:
    print('Happy New year:', friend)
print('Done!')

#Enter your friend names-like x,y,z:Manju,kiran,Yogi
#Happy New year: Manju,kiran,Yogi
#Done!


#Loopidoms are used to find the Max,largest and smallest etc

#Write a program to pop happy new year ___given friend name in input
friends=[input("Enter your friend names-like ('x','y','z'):")]
for friend in friends:
    print('Happy New year:', friend)
print('Done!')


#Enter your friend names-like ('x','y','z'):'Manju', 'Kiran','Yogi'
#Happy New year: 'Manju', 'Kiran','Yogi'
#Done!
