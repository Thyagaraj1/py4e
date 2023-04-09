word=str(input('Enter a word:'))
if word=='Many':
    print('All right, Many')
if word<'Many':
    print('Your word,'+word+',comes before Many')
elif word>'Many':
    print('Your word,'+word+',comes after Many')
else:
    print('All right,Many')

#Enter a word:Hi # apparently lower case letters are bigger than the upper case letters
#Your word,Hi,comes before banana

#Enter a word:hi #apparently lower case letters are bigger than the upper case letters
#Your word,hi,comes after Many

word=str(input('Enter a word:'))
if word=='many':
    print('All right, many')
if word<'many':
    print('Your word,'+word+',comes before many')
elif word>'many':
    print('Your word,'+word+',comes after many')
else:
    print('All right,many')

#Enter a word:hi ##apparently lower case letters are bigger than the upper case letters
#Your word,hi,comes before many


#max--Function to find the maximum
big=max('Hello world')
print(big)
#we are passing a string and asking max  to find the largest of something
#w -coz apparently lower case letters are bigger than the upper case letters


#Min function
tiny=min('Hello world')
print(tiny)
