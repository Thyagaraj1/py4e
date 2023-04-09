fname=input('Enter file name: ')
try:
    fhandle=open(fname)
except:
    print('Enter a valid file name')
    quit()
for line in fhandle:
    if not line.startswith('X-DSPAM-Confidence'):
        continue
    value=line.split()[0]
    print(value,total)
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
#X-DSPAM-Confidence:
