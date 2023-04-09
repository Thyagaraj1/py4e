with open('mbox-short.txt') as input_file:
    count=0
    for line in input_file:
        if line.startswith('From'):
            count+=1
    print(count)

#54

#Wrong counts
#Not preferred much as it won't give proper results on
with open('mbox-short.txt') as input_file:
    count=0
    for line in input_file:
        if not line.startswith('From'):
            continue
        count+=1
    print(count)
#54

with open('mbox-short.txt') as input_file:
    count=0
    for line in input_file:
        line=line.rstrip()
        if not 'From' in line:
            continue
        count+=1
    print(count)
#54
