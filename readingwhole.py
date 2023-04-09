fhand=open('mailbox.txt')
inp=fhand.read()
print(len(inp))
print(inp[0:20]) #colon operator slicing
#812
#De: Thyagaraj Aralil

fhandle=open('mailbox.txt')
inp=fhandle.read()
print(len(inp))
print(inp[0:1])

#812
#D

with open('mailbox.txt') as fhandle:
    inp=fhandle.read()
    print(inp[0:30])
