count=0
sum=0
print('before',count)
for the_num in [0,1,2,3,4,5,6]:
    count=count=1
    sum=sum+the_num
    print(count,the_num,sum)
print('after',count,sum)


#before 0
#1 0 0
#1 1 1
#1 2 3
#1 3 6
#1 4 10
#1 5 15
#1 6 21
#after 1 21

a=num1=float(input('Enter a number:'))
b=num2=float(input('Enter a number:'))
c=num3=float(input('Enter a number:'))
d=num4=float(input('Enter a number:'))
e=num5=float(input('Enter a number:'))
f=num6=float(input('Enter a number:'))

count=0
sum=0
avg=0
for the_num in [a,b,c,d,e,f]: #iterative variable in variable
    count=count+1
    sum=sum+the_num
    avg=sum/count
    print(count,sum,avg)
print('after',count,avg)


#Enter a number:2
#Enter a number:4
#Enter a number:6
#Enter a number:8
#Enter a number:10
#Enter a number:12
#1 2.0 2.0
#2 6.0 3.0
#3 12.0 4.0
#4 20.0 5.0
#5 30.0 6.0
#6 42.0 7.0
#after 6 7.0
