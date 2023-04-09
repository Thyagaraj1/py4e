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


#C:\Users\taralilk\OneDrive - Cisco\Documents\py4e>python try1.py
#*Feb 28 2023 12:21:50.261 UTC: %CONTROLLER-5-UPDOWN: PRI E1 0/1/1, changed state to up
#*Feb 28 2023 12:21:52.677 UTC: %MARS_NETCLK-3-HOLDOVER: Exiting Holdover for PRI E1 0/1/1
#*Feb 28 2023 13:03:24.252 UTC: %CONTROLLER-5-UPDOWN: PRI E1 0/1/1, changed state to down (RAI detected)
#*Feb 28 2023 13:03:24.424 UTC: %MARS_NETCLK-3-HOLDOVER: Entering Holdover for PRI E1 0/1/1
#*Feb 28 2023 13:03:25.252 UTC: %CONTROLLER-5-UPDOWN: PRI E1 0/1/1, changed state to up
#*Feb 28 2023 13:03:27.676 UTC: %MARS_NETCLK-3-HOLDOVER: Exiting Holdover for PRI E1 0/1/1 548






#with open('mailbox.txt') as fhandle:
#    inp=fhandle.read()
    #rplc=inp.replace('Feb','z')
    #line=len(rplc)
    #print(rplc,line)

#with open('mailbox.txt','w') as fhandle:
    #fhandle.write(rplc)
    #print(fhandle)


#C:\Users\taralilk\OneDrive - Cisco\Documents\py4e>python try1.py
#*z 28 2023 12:21:50.261 UTC: %CONTROLLER-5-UPDOWN: Controller E1 0/1/1, changed state to up
#*z 28 2023 12:21:52.677 UTC: %MARS_NETCLK-3-HOLDOVER: Exiting Holdover for Controller E1 0/1/1
#*z 28 2023 13:03:24.252 UTC: %CONTROLLER-5-UPDOWN: Controller E1 0/1/1, changed state to down (RAI detected)
# 296

# Open the input file in read mode
#with open('mailbox.txt', 'r') as fhandle:

    # Read the contents of the file into a variable
    #file_contents = fhandle.read()

    # Replace the word 'old_word' with 'new_word'
    #new_contents = file_contents.replace('Feb', 'z')

    #print(new_contents)

# Open the output file in write mode
#with open('mailbox.txt', 'w') as fhandle:

    # Write the modified contents to the output file
    #fhandle.write(new_contents)
    #print(fhandle)





#fhandle=str(open('mailbox.txt', 'w'))
#count=0
#for lines in fhandle:
    #count+=1
#rplc=fhandle.replace('Feb','z')
#len=len(fhandle)
#print(count,len)
