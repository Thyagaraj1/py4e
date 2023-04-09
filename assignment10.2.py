#write a program to read through the mbox-short.txt & figure out the distribution by hour of the day
#for each of the messages. You can pull the hour out from the 'From'line by finding the time and then
#splitting the string a second time by using colon
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname=input('Enter file name: ')
if len(fname)<1:
    fname='mbox-short.txt'
try:
    fhandle=open(fname)
except:
    print('Enter valid file name')
    quit()
dict=dict()
for line in fhandle:
    #if line=='': continue
    words=line.split()
    if len(words)<2 or words[0]!='From': continue
    #print('words: ', words) example below
    #words:  ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
    #etc
    time=words[5]
    #print('time: ',time)
    #time:  09:14:16
    #etc
    #hour=time[:2] #conventional method
    #print(hour)
    hours=time.split(':')[0]
    #print(hours)
    #09
    dict[hours]=dict.get(hours,0)+1
#print(dict)
#{'09': 2, '18': 1, '16': 4, '15': 2, '14': 1, '11': 6, '10': 3, '07': 1, '06': 1, '04': 3, '19': 1, '17': 2}
for k,v in sorted(dict.items()):
    print(k,v)
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1
sort=sorted([(v,k) for k,v in dict.items()],reverse=True)
#print(sort)
#[(6, '11'), (4, '16'), (3, '10'), (3, '04'), (2, '17'), (2, '15'), (2, '09'), (1, '19'), (1, '18'), (1, '14'), (1, '07'), (1, '06')]
for v,k in sort[:3]:
    print(v,k)
#6 11
#4 16
#3 10
