#To find how many times 'a' is repeated in a word or sentence
#None can't be used with integer for any operations ex:count+None,count=0
#file name as looping_&_counting.py is not valid and not recognizable

sentence=str(input('Enter a sentence:'))
count=0
for letter in sentence:
    if letter=='a':
        count=count+1
print(count)


#Enter a sentence:where you're heading
#1

#Using this method we could able to find the letter in a sentence not in multiple outputs
#wrong method to find
a=chat1=str(input('Enter chat:'))
b=chat1=str(input('Enter chat:'))
c=chat1=str(input('Enter chat:'))
d=chat1=str(input('Enter chat:'))
e=chat1=str(input('Enter chat:'))
count=0
for word in [a,b,c,d,e]:
    if word=='you':
        count=count+1
    print(word,count)
print(count)

#Enter chat:Hey there
#Enter chat:Hi how you doing
#Enter chat:I'm good thank you, How you are?
#Enter chat:I'm fine
#nter chat:what's your plan on weekend
#Hey there 0
#Hi how you doing 0
#I'm good thank you, How you are? 0
#I'm fine  0
#what's your plan on weekend  0
#0

#wrong method to find
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


#Enter chat:Hey there
#Enter chat:Hi how you doing
#Enter chat:I'm good thank you, How you are?
#Enter chat:I'm fine
#Enter chat:what's your plan on weekend
#0


#########
sentence=str(input("Enter a sentence:"))
count=0
for letter in sentence:
    if letter=='a': #iterative variable finding in variable
        count=count+1
    print(letter,count)
print(count)

#Enter a sentence:where you're heading

#w 0
#h 0
#e 0
#r 0
#e 0
#  0
#y 0
#o 0
#u 0
#' 0
#r 0
#e 0
  #0
#h 0
#e 0
#a 1
#d 1
#i 1
#n 1
#g 1
#1


sentence=str(input('Enter a sentence:'))
count=0
for word in sentence:
    if word=='you':
        count=count+1
print(count)
