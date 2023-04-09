#find operator--.find('substring')
#ex:- banana --index value 0,1,2,3,4,5

fruit='banana'
pos=fruit.find('na') #str.find(sub[,start[,end]])
print(pos)

#2 --here 2 is index value, #find() finds the 1st occurance of the substring

aa=fruit.find('z') #str.find(sub[,start[,end]])
print(aa)

#-1 -- #if the substring is not found, find() returns -1
