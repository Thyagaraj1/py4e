#Able to count a letter but not the word
sentence=str(input('Enter a sentence:'))
word='you'
count=0
for word in sentence:
    if word=='you':
        count=count+1
print(count)
#Enter a sentence:you
#0


#write a program to count a word=='you' using the for loop for input sentence
#chatgpt
sentence = input("Enter a sentence: ")
word = "you"
count = 0

words = sentence.split()
for w in words:
    if w.lower() == word:
        count += 1 #count=count+1 written as count+=1

print("The word '" + word + "' appeared " + str(count) + " times in the sentence.")

#This code takes the input sentence from the user and splits it into individual words using the split function.
#Then, it loops through each word and checks if it's equal to the target word "you".
#If so, it increments the count. Finally, it prints the result.



#Able to count a letter but not the word
sentence=str(input('Enter a sentence:'))
count=0
for letter in sentence:
    if letter=='y':
        count=count+1
print(count)
#Enter a sentence:you
#1

#Able to count a letter but not the word
a=chat1=str(input('Enter chat:'))
b=chat1=str(input('Enter chat:'))
c=chat1=str(input('Enter chat:'))
d=chat1=str(input('Enter chat:'))
e=chat1=str(input('Enter chat:'))
count=0
for word in [a,b,c,d,e]:
    if word=='you':
        count=count+1
print(count)
#Enter chat:you
#Enter chat:you
#Enter chat:you
#Enter chat:you
#Enter chat:you
#5


#Able to count a letter but not the word
a=chat1=str(input('Enter chat:'))
b=chat1=str(input('Enter chat:'))
c=chat1=str(input('Enter chat:'))
d=chat1=str(input('Enter chat:'))
e=chat1=str(input('Enter chat:'))
count=0
for letter in [a,b,c,d,e]:
    if letter=='y':
        count=count+1
print(count)

#Enter chat:you
#Enter chat:you
#Enter chat:you
#Enter chat:you
#Enter chat:you
#0
