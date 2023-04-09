filehandle=open('mailbox.txt')
count=0
for line in filehandle:
    line=line.rstrip()
    if not line.startswith('From:'):
        count+=1
        continue
    print(count,line)
#18 From: Vivek Ranjan (viveranj) <viveranj@cisco.com>
#69 From: Sourajit Hazra (souhazra) <souhazra@cisco.com>
#96 From: Janaka PERERA <janakaperera@hsbc.co.nz>
#120 From: Lisa Castillo -X (liscasti) <liscasti@cisco.com>
