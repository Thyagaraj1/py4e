import urllib.request,urllib.parse,urllib.error
fhandle=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts=dict()
for line in fhandle: #line in bytes or UTF-8 decoding into Unicode or strings 
    words=line.decode().split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)
#{'But': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1, 'yonder': 1, 'window': 1, 'breaks': 1, 'It': 1, 'is': 3, 'the': 3, 'east': 1, 'and': 3, 'Juliet': 1, 'sun': 2, 'Arise': 1, 'fair': 1, 'kill': 1, 'envious': 1, 'moon': 1, 'Who': 1, 'already': 1, 'sick': 1, 'pale': 1, 'with': 1, 'grief': 1}
print(sorted(counts.items()))
#[('Arise', 1), ('But', 1), ('It', 1), ('Juliet', 1), ('Who', 1), ('already', 1), ('and', 3), ('breaks', 1), ('east', 1), ('envious', 1), ('fair', 1), ('grief', 1), ('is', 3), ('kill', 1), ('light', 1), ('moon', 1), ('pale', 1), ('sick', 1), ('soft', 1), ('sun', 2), ('the', 3), ('through', 1), ('what', 1), ('window', 1), ('with', 1), ('yonder', 1)]
for k,v in sorted(counts.items()):
    print(k,v)
#Arise 1
#But 1
#It 1
#Juliet 1
#Who 1
#already 1
#and 3
#etc
sort=sorted([(v,k) for k,v in counts.items()],reverse=True)
print(sort)
#[(3, 'the'), (3, 'is'), (3, 'and'), (2, 'sun'), (1, 'yonder'), (1, 'with'), (1, 'window'), (1, 'what'), (1, 'through'), (1, 'soft'), (1, 'sick'), (1, 'pale'), (1, 'moon'), (1, 'light'), (1, 'kill'), (1, 'grief'), (1, 'fair'), (1, 'envious'), (1, 'east'), (1, 'breaks'), (1, 'already'), (1, 'Who'), (1, 'Juliet'), (1, 'It'), (1, 'But'), (1, 'Arise')]
for v,k in sort[:3]:
    print(v,k)
#3 the
#3 is
#3 and