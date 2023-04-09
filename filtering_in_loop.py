for the_num in [13,25,2,38,1]:
    if the_num>20:
        print('larger number',the_num)

#larger number 25
#larger number 38
#thins to be learnt is when  we have huge number how to import it and filter it out

a=str(input('Enter any thing:'))
b=str(input('Enter any thing:'))
c=str(input('Enter any thing:'))
d=str(input('Enter any thing:'))
e=str(input('Enter any thing:'))
for the_sen in [a,b,c,d,e]:
    if the_sen=='e':
        print('sentence with letter e',the_sen)
    


#example
big=max('Hello world')
print(big)

#finding the max using
a=str(input('Enter any thing:'))
b=str(input('Enter any thing:'))
c=str(input('Enter any thing:'))
d=str(input('Enter any thing:'))
e=str(input('Enter any thing:'))

for words in [a,b,c,d,e]:
    big=max(words)
    print(big)

#Enter any thing:Hi buddy!
#Enter any thing:How you doing
#Enter any thing:1
#Enter any thing:what's up
#Enter any thing:My name is thyagaraj
#y
#y
#1
#w
#y


#what we could do is
a=str(input('Enter any thing:'))
b=str(input('Enter any thing:'))
c=str(input('Enter any thing:'))
d=str(input('Enter any thing:'))
e=str(input('Enter any thing:'))

#concatenate all the input
concatenate=a+b+c+d+e
big=max(concatenate)
print(big)

#Enter any thing:Industrialist
#Enter any thing:Entrepreneur
#Enter any thing:woke
#Enter any thing:drwan
#Enter any thing:repelled
#w
