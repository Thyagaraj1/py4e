#while function by default it's an indefinite loop
#for function by defaulr it's an definite loop

#Finite loop and infinite loop
#definite loop and we are ending the loop here
n=5
while n>0:
    print(n)
    n=n-1
#5
#4
#3
#2
#1

#example of indefinite loop
#n=5
#while n>0:
    #print(n)
    #n=n+1
#1 Statement to get out of loop
#Statement to get out of the loop is break
#Breaking out of the loop
#break Statement ends the current loop and jumps to the Statement immediately following the loop
###test case
while True:
    line=input('>')
    if line!='done':
        break
    print(line)
print('Done!')
#>done
#done
#>done
#done
#>d

############
while True:
    line=input('>')
    if line=='done':
        break
    print(line)

#>Hi There
#Hi There
#>hi what's app
#hi what's app
#>New
#New
#>done
 #worked example
while True:
    restart=str(input('would you like to restart(y/n):'))
    if restart in ('y','n'):
        break
    print("Invalid input")
    if restart==y or restart==yes:
        continue
    else:
        print('script terminating, Goodbye.')
        break


##Continue statement
#The continue statement jumps the current loop iterationa and jumps to the top of the loop
while True:
    line =input('>')
    if line[0]=="#":
        continue
    if line=='done':
        break
    print(line)
print('Done!')


#>#
#>#
#>#
#>#
#>#
#>what's up
#what's up
#>How you doing!
#How you doing!
#>done
#Done!
