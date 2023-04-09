#It's a real common problem to be scanning through file and want to know only the lines that starts with a prefix
#Prefixs -- Keyword--.starts with ()
line='Please have a nice day'
pfx=line.startswith('Please')
print(pfx)
#True
pfx=line.startswith('p')
print(pfx)
#False
line='Notify the message'
pfx=line.startswith('n')
print(pfx)
#False
pfx=line.startswith('N')
print(pfx)
#True



sentence='do help me to understand the function'
pfx=sentence.startswith('do')
print(pfx)
#True
