import re
with open('testreexp.txt') as fhanlde:
    for line in fhanlde:
        line=line.rstrip()
        if re.search('^X-\S+:',line): #starts with X, have hyphen - should match nonwhitespace char
            print(line) #one or more times >=1 and followed by :
#X-Content-Type-Message-Body: text/plain; charset=UTF-8
#X-Content-Type-Message-Body: text/plain; charset=UTF-8
#X-DSPAM-Processed: Fri Jan  4 11:10:22 2008
#X-DSPAM-Confidence: 0.7606
#X-DSPAM-Probability: 0.0000

#outof 
#tent Type-Outer-Envelope: text/plain; charset=UTF-8
#X-Content-Type-Message-Body: text/plain; charset=UTF-8
#Content-Type: text/plain; charset=UTF-8
#X-DSPAM-Result Innocent
#X DSPAM-Processed: Sat Jan  5 09:14:16 2008
#X-DSPAM-Confidence 0.8475
#X-DSPAM Probability: 0.0000
#X-Content Type-Outer-Envelope: text/plain; charset=UTF-8
#X-Content-Type-Message-Body: text/plain; charset=UTF-8
#Content-Type: text/plain; charset=UTF-8
#X-DSPAM-Result  Innocent
#X-DSPAM-Processed: Fri Jan  4 11:10:22 2008
#X-DSPAM-Confidence: 0.7606
#X-DSPAM-Probability: 0.0000