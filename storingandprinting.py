while True:
    inp=input('Enter your friend name: ')
    if inp=='done':
        break
    print('Happy New year:', inp)
#Enter your friend name: Manju
#Happy New year: Manju
#Enter your friend name: Kiran
#Happy New year: Kiran
#Enter your friend name: Yogi
#Happy New year: Yogi
#Enter your friend name: done

friends=list()
while True:
    inp=input('Enter your friend name: ')
    if inp=='done':
        break
    friends.append(inp)
print('Happy New year:', friends)
#Enter your friend name: Manju
#Enter your friend name: Kiran
#Enter your friend name: Yogi
#Enter your friend name: done
#Happy New year: ['Manju', 'Kiran', 'Yogi']
for friend in friends:
    print('Happy New year:', friend)
#Happy New year: Manju
#Happy New year: Kiran
#Happy New year: Yogi

#To find the smallest
smallest=None
for value in [8,2,3,4,7,9]:
    if smallest is None:
        smallest=value
        #smallest-->8
    elif value<smallest:
        #8<8,2<8(Holds true),3<2,4<2,7<2,9<2
        smallest=value
        #smallest-->2
        print(smallest)
        #2
print('smallest', smallest)
#smallest 2

#Finding using listing method
value=[8,2,3,4,7,9]
print(min(value))
#2

#Finding using while loop for inputs provided by users
value=list()
while True:
    inp=input('Enter a number: ')
    if inp=='done':
        break
    value.append(inp)
print(min(value))
#Enter a number: 7
#Enter a number: 4
#Enter a number: 7
#Enter a number: 38
#Enter a number: 589
#Enter a number: 48
#Enter a number: 48
#Enter a number: 38
#Enter a number: 0
#Enter a number: 5
#Enter a number: 2
#Enter a number: 0.87
#Enter a number: .-75
#Enter a number: done
#.-75
