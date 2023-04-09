#Conventional method of looping to find avg
#Algorithemic method
#It will not take up more space only one value at all time is fixed to variables
#userful in case when we have millions of number as it's less space consuming
total=0
count=0
while True:
    inp=input('Enter a number: ')
    #3,9,5, done
    if inp=='done':
        break
    count=count+1
    print(count)
    #1,2,3
    value=float(inp)
    print(value)
    #3.0, 9.0, 5.0
    total=total+value
    print(total)
    #3.0, 12.0, 17.0
avg=total/count
print('avg',avg)
#avg 5.666666666666667
#Enter a number: 3
#1
#3.0
#3.0
#Enter a number: 9
#2
#9.0
#12.0
#Enter a number: 5
#3
#5.0
#17.0
#Enter a number: done
#avg 5.666666666666667


#How can we leverage list for this operation
#data structure method
#It will consumer space as we keep on giving the input it will takes and append in list
#userful where less than thousands of number are evaluated
numlist=list()#give me an empty list [] []
while True:
    inp=input('Enter a number: ')
    #3, 5, 9, done
    if inp=='done':
        break
    value=float(inp)
    print(value)
    #3.0, 5.0, 9.0
    numlist.append(value)
    print(numlist)
    #[3.0, 5.0, 9.0]
avg=sum(numlist)/len(numlist)
print('avg', avg)

#Enter a number: 3
#3.0
#[3.0]
#Enter a number: 5
#5.0
#[3.0, 5.0]
#Enter a number: 9
#9.0
#[3.0, 5.0, 9.0]
#Enter a number: done
#avg 5.666666666666667
