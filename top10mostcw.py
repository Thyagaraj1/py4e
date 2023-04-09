#Here we going to get the top10 most common words
fname=input('Enter file name: ')
if len(fname)<1:
    fname='romeo.txt'
try:
    fhandle=open(fname)
except:
    print('Enter valid file name: ')
    quit()
dict=dict()
for line in fhandle:
    words=line.split()
    for word in words:
        dict[word]=dict.get(word,0)+1
#print(dict)
#{'But': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1, 'yonder': 1, 'window': 1, 'breaks': 1, 'It': 1, 'is': 3, 'the': 3, 'east': 1, 'and': 3, 'Juliet': 1, 'sun': 2, 'Arise': 1, 'fair': 1, 'kill': 1, 'envious': 1, 'moon': 1, 'Who': 1, 'already': 1, 'sick': 1, 'pale': 1, 'with': 1, 'grief': 1}
listoftuples=list()
for k,v in dict.items(): #converting into tuples and using for loop to go throught the dict
    listoftuples.append((v,k))
#print(listoftuples)
#[(1, 'But'), (1, 'soft'), (1, 'what'), (1, 'light'), (1, 'through'), (1, 'yonder'), (1, 'window'), (1, 'breaks'), (1, 'It'), (3, 'is'), (3, 'the'), (1, 'east'), (3, 'and'), (1, 'Juliet'), (2, 'sun'), (1, 'Arise'), (1, 'fair'), (1, 'kill'), (1, 'envious'), (1, 'moon'), (1, 'Who'), (1, 'already'), (1, 'sick'), (1, 'pale'), (1, 'with'), (1, 'grief')]

#sorting to get high to low values not keys
listoftuples=sorted(listoftuples,reverse=True) #(what,How), descending order of values if the values are same then it sorts based on keys ex: y>w
#print(listoftuples)
#[(3, 'the'), (3, 'is'), (3, 'and'), (2, 'sun'), (1, 'yonder'), (1, 'with'), (1, 'window'), (1, 'what'), (1, 'through'), (1, 'soft'), (1, 'sick'), (1, 'pale'), (1, 'moon'), (1, 'light'), (1, 'kill'), (1, 'grief'), (1, 'fair'), (1, 'envious'), (1, 'east'), (1, 'breaks'), (1, 'already'), (1, 'Who'), (1, 'Juliet'), (1, 'It'), (1, 'But'), (1, 'Arise')]
#print(listoftuples[:10]) #top 10 tuples
#[(3, 'the'), (3, 'is'), (3, 'and'), (2, 'sun'), (1, 'yonder'), (1, 'with'), (1, 'window'), (1, 'what'), (1, 'through'), (1, 'soft')]
for value,key in listoftuples[:10]:
    print(value,key)
#3 the
#3 is
#3 and
#2 sun
#1 yonder
#1 with
#1 window
#1 what
#1 through
#1 soft

#fliping of the listoftuples in list , so we use sort high to low 
#flip=listoftuples.reverse()
#print(flip)
#None
