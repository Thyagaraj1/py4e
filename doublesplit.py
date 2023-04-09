text='Thyagaraj Aralilkattedoddi Hanumanthaiah -X (taralilk - SYNOPHIC SYSTEMS PRIVATE LIMITED at Cisco) <taralilk@cisco.com> '
words=text.split()
print(words)
#['Thyagaraj', 'Aralilkattedoddi', 'Hanumanthaiah', '-X', '(taralilk', '-', 'SYNOPHIC', 'SYSTEMS', 'PRIVATE', 'LIMITED', 'at', 'Cisco)', '<taralilk@cisco.com>']
index=words.index('<taralilk@cisco.com>')
print(index)
#12
sdomain=words[12]
print(sdomain)
#<taralilk@cisco.com>
split=sdomain.split('@')[1]
print(split)
#cisco.com>
ssplit=split.split('>')[0]
print(ssplit)
#cisco.com

#How we can do it in efficient way
s1=text.split()[12]#index should be used to find the position
s2=s1.split('@')[1]
print(s2)
#cisco.com>
#'list' object has no attribute 'split'
#index=s1.index('<taralilk@cisco.com>')
#print(index)
#12
#s3=s1[12]
s4=s2.split('>')[0]
print(s4)
#cisco.com

#Conventional method with out split
f1=text.find('@')
f2=text.find('m>')
o=text[f1+1:f2+1]
print(o)
#cisco.com

friends = [ 'Joseph', 'Glenn', 'Sally' ]
print(friends[2:])

x = list(range(5))
print(x)
#[0, 1, 2, 3, 4]
