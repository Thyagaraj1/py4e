#Parsing-For loop and going through a file
with open('mbox-short.txt') as fhandle:
    count=0
    for line in fhandle:
        line=line.rstrip()
        if not line.startswith('From'):
            continue
        words=line.split()
        #print(words)
        #['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
        #['From:', 'stephen.marquard@uct.ac.za']
        #['From', 'louis@media.berkeley.edu', 'Fri', 'Jan', '4', '18:10:48', '2008']
        #['From:', 'louis@media.berkeley.edu']
        #.
        #.
        #['From:', 'cwen@iupui.edu']
        #index=words.index('anyrequired word')# can be used for find the position
        #print(index)
        modified_content=words[0]
        print(words[1])
        #stephen.marquard@uct.ac.za
        #etc
        count+=1
    print(count)
    #54
with open('H.txt','w') as output_file:
    #output_file.write(words) #words-->list
    #write() argument must be str, not list
    output_file.write(modified_content) #Only words[0] works as it treated as strings


fhandle.close()
output_file.close()



#exaple of string writing
with open('input.txt') as input_file:
    content=input_file.read()
    modified_content=content.replace('Controller','PRI')
    print(modified_content,'\n',len(modified_content))

    #At this stage it will be only in read formate and it's executed as output but inorder for us to write in theoutput to the file
    # we need to execute the write command
with open('output.txt','w') as output_file:
    output_file.write(modified_content)

input_file.close()
output_file.close()
