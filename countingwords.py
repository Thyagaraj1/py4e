#Here we are gonna counts the words in text line where we gonna split it to list and then use get method to find the exact counts
count=dict()
print('Enter line of text: ')
line=input(' ') # or line=input('Enter line of text: ')
words=line.split()
print('words:',words) #debugging method
for word in words:
    count[word]=count.get(word,0)+1 #dict.get(key, defaultvalue)
print(count)
#counts of any particular word can be found by below method
print(count.get('car')) #print(count.get('car','Not available'))
#Enter line of text:
 #Thyagaraj is gonna get a car which drives him around the city with out any issues being seen with the car so he feel comfortable to ride it
#words: ['Thyagaraj', 'is', 'gonna', 'get', 'a', 'car', 'which', 'drives', 'him', 'around', 'the', 'city', 'with', 'out', 'any', 'issues', 'being', 'seen', 'with', 'the', 'car', 'so', 'he', 'feel', 'comfortable', 'to', 'ride', 'it']
#{'Thyagaraj': 1, 'is': 1, 'gonna': 1, 'get': 1, 'a': 1, 'car': 2, 'which': 1, 'drives': 1, 'him': 1, 'around': 1, 'the': 2, 'city': 1, 'with': 2, 'out': 1, 'any': 1, 'issues': 1, 'being': 1, 'seen': 1, 'so': 1, 'he': 1, 'feel': 1, 'comfortable': 1, 'to': 1, 'ride': 1, 'it': 1}
#2


#Definite loops and dictionaries
counts={'Thyaga':12,'Manju':30,'kiran':35,'Yogi':84}
#Let say i want to know the value i don't need key but for loop by default goes throug keys
#Even when we need to get the values the for loop goes through the keys and get the output
print(counts.get('Thyaga'))
#12
#but for to get the all the outputs at once
for key in counts:
    print(key,counts[key])
#Thyaga 12
#Manju 30
#kiran 35
#Yogi 84


#
