n=5
while n>0:
    print(n)
    n=n-1
print('Blastoff!')

#5
#4
#3
#2
#1
#Blastoff!

while True:
    line=input('>')
    if line=='done':
        break
    print(line)
print('Done!')


#>d
#d
#>what's app
#what's app
#>Need more food
#Need more food
#>why you need
#why you need
#>done
#Done!

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
