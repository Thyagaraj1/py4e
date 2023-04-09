#There are number of Functions built into python that takes Lists as parameter
#we done the similar operation using for loop
num=[3,4,8,7,6,1,2]
print(len(num))
#7
print(max(num))
#8
print(min(num))
#1
print(sum(num))
#31
print(sum(num)/len(num))
#4.428571428571429
z='q'
alpha=[z,'c','d','da','a','n','m','M'] #c--->should be string unless it is defined as c=1 something
print(len(alpha))
#8
print(max(alpha))
#q
print(min(alpha))
#M
#print(sum(alpha))
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(sum(alpha)/len(alpha))
#TypeError: unsupported operand type(s) for +: 'int' and 'str'


#In for loop we did write like
variable=[3,4,8,7,6,1,2]
count=0
sum=0
for iterativevariable in variable:
    count+=1
    sum+=iterativevariable
    avg=sum/count
print(count,sum,avg)
#7 31 4.428571428571429

variable=[3,4,8,7,6,1,2]
for iterativevariable in variable:
    if iterativevariable>7:
        print('largernumber',iterativevariable)
#largernumber 8
