#Tuples are comparable
#>>> (1,2,3)>(2,1,1) #from python 
#False
x=(1,2,3)>(2,1,1)
print(x)
False
#it will compare the first to first then if it's false that's it, it will ignore the rest won't 
#compare the rest of two
y=(1,9,8)>(2,1,1)
print(y)
#False
z=('time','energy','result')>('time','energy','work')
print(z)
#False
#In above case it will compare the 1st as it's same then it goes to 2nd one as second is also same 
#then it will compare the 3rd one here result>work
#which in turn it takes only r>w, as it's not true false will be output 
x=(2,1,1)>(1,9,7)
print(x)
#True