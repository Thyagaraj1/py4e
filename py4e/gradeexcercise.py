#write a programm to prompt for a score b/n 0.0 and 1.0. If the score is out of range, print an error
#if the score is b/n 0.0 & 1.0, print a grade using the following.
#score grade
#>=0.9 A
#>=0.8 B
#>=0.7 C
#>=0.6 D
#<0.6  F
#If the user eter a value outof range, print a suitable error msg and exit
#For the test enter a score 0.85

try:
    score=float(input('Enter score:'))
except:
    print('Please enter a numberic value')
    quit()
if score<0.0 or score>1.0:
    print ('Only numbers less than 1 and bigger than O are allowed')
    quit()
elif score>=0.9:
    x='A'
elif score>=0.8:
    x='B'
elif score>=0.7:
    x='C'
elif score>=0.6:
    x='D'
elif score<0.6:
    x='F'
print(x)


#can be writtern as below
try:
    score=float(input('Enter score:'))
except:
    print('Please enter a numberic value')
    quit()

if score> 1:
    print ('Only numbers less than 1 and bigger than O are allowed')
    quit()
elif score< 0:
    print ('Negative score not allowed ')

elif score >= 0.9:
    print ('A')
elif score >= 0.8:
    print ('B')
elif score >= 0.7:
    print ('C')
elif score >= 0.6:
    print ('D')
elif score < 0.6:
    print ('F')


#Tips:
#Don't use if s<0.0: or s>1.0:
#It should be if s<0.0 or s>1.0
#grade system of our education
