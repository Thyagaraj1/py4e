count=0
print('before',count)
for the_num in [0,1,2,3,4,5]: #iterative variable in variable
    count=count+1
    print(count,the_num)
print('after',count)

#before 0
#1 0
#2 1
#3 2
#4 3
#5 4
#6 5
#after 6


#write a program to european to american lift system
floor=int(input('which floor are you?:'))
efloor=floor+1
print('The current floor is', efloor)

#which floor are you?:2
#The current floor is 3
