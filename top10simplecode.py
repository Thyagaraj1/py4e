with open('romeo.txt') as fhandle:
    dict=dict()
    for line in fhandle:
        words=line.split()
        for word in words:
            dict[word]=dict.get(word,0)+1
        #to sort inorder to have value first value,key and high to low
    sort=sorted([(v,k) for k,v in dict.items()],reverse=True)
    #instead of below method we can use above sentence

    #listoftuples=list()
    #for k,v in dict.items(): #converting into tuples and using for loop to go throught the dict
        #listoftuples.append((v,k)) #arranging in value,key order
    #hightolowsort=sorted(listoftuples,reverse=True)
    #print(hightolowsort)
    #[(3, 'the'), (3, 'is'), (3, 'and'), (2, 'sun'), (1, 'yonder'), (1, 'with'), (1, 'window'), (1, 'what'), (1, 'through'), (1, 'soft'), (1, 'sick'), (1, 'pale'), (1, 'moon'), (1, 'light'), (1, 'kill'), (1, 'grief'), (1, 'fair'), (1, 'envious'), (1, 'east'), (1, 'breaks'), (1, 'already'), (1, 'Who'), (1, 'Juliet'), (1, 'It'), (1, 'But'), (1, 'Arise')]

    for v,k in sort[:10]:
        print(v,k)
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
