#Extracting from the text
text='Your Ref: SNOW INC000000004332724 | Our Ref: INCV00724702 | Priority: 3 - Moderate  Status: New'
#1st method
ipos=text.find('Moderate')
lpos=text.find('Status')
host=text[ipos:(lpos-1)]
print(host)
#Moderate

#How could we have used split here
words=text.split()
#print(len(words))
#15
#print(words)
#['Your', 'Ref:', 'SNOW', 'INC000000004332724', '|', 'Our', 'Ref:', 'INCV00724702', '|', 'Priority:', '3', '-', 'Moderate', 'Status:', 'New']
index=words.index('Moderate')
#print(index)
#12
print(words[index])
#Moderate

#3rd method same as 1st method only we have used index here 
index=text.index('Moderate') #same as using find and doing the same stuff
print(index)
#74
print(len('Moderate'))
#8
print(text[74:74+8])
#Moderate
