#Using in to select lines
#we can look for a string anywhere in a line as our selection criteria
fhandle=open('mailbox.txt')
for line in fhandle:# line is a iterative funciton, fhandle it's a variable
    line=line.rstrip()
    if not '@cisco.com' in line:
        continue
    print(line)
#Email: taralilk@cisco.com
#From: Vivek Ranjan (viveranj) <viveranj@cisco.com>
#To: businessenhanced@vodafone.nz; Sourajit Hazra (souhazra) <souhazra@cisco.com>
#Cc: cisco-hsbc-d2o-collab-incident-management(mailer list) <cisco-hsbc-d2o-collab-incident-management@cisco.com>; hsbc-cms-attach(mailer list) <hsbc-cms-attach@cisco.com>; Judith OGBORNE <judithogborne@hsbc.co.nz>; Janaka PERERA <janakaperera@hsbc.co.nz>
#viveranj@cisco.com
#From: Sourajit Hazra (souhazra) <souhazra@cisco.com>
#Cc: cisco-hsbc-d2o-collab-incident-management(mailer list) <cisco-hsbc-d2o-collab-incident-management@cisco.com>; hsbc-cms-attach(mailer list) <hsbc-cms-attach@cisco.com>; Judith OGBORNE <judithogborne@hsbc.co.nz>; Janaka PERERA <janakaperera@hsbc.co.nz>
#Email: munikuma@cisco.com
#To: Lisa Castillo -X (liscasti) <liscasti@cisco.com>; Andy Krawczyk (akrawczy) <akrawczy@cisco.com>; Judith OGBORNE <judithogborne@hsbc.co.nz>; businessenhanced@vodafone.nz; cisco-hsbc-d2o-collab-incident-management(mailer list) <cisco-hsbc-d2o-collab-incident-management@cisco.com>
#From: Lisa Castillo -X (liscasti) <liscasti@cisco.com>
#To: Andy Krawczyk (akrawczy) <akrawczy@cisco.com>; Judith OGBORNE <judithogborne@hsbc.co.nz>; cisco-hsbc-d2o-collab-incident-management(mailer list) <cisco-hsbc-d2o-collab-incident-management@cisco.com>

fhandle=open('mailbox.txt')
for line in fhandle:
    line=line.rstrip()
    if line.startswith('@cisco.com'):
        print(line)
#No results found as it is used only to filterout the prefix

fhandle=open('mailbox.txt')
for line in fhandle:
    line=line.rstrip()
    if not line.startswith('@cisco.com'):
        continue
        print(line)
#No results found as it is used only to filterout the prefix

fhandle=open('mailbox.txt')
for line in fhandle:
    line=line.rstrip()
    if not '@cisco.com' in line:
        continue
    print(line)

#Email: taralilk@cisco.com
#From: Vivek Ranjan (viveranj) <viveranj@cisco.com>
#To: businessenhanced@vodafone.nz; Sourajit Hazra (souhazra) <souhazra@cisco.com>
#Cc: cisco-hsbc-d2o-collab-incident-management(mailer list) <cisco-hsbc-d2o-collab-incident-management@cisco.com>; hsbc-cms-attach(mailer list) <hsbc-cms-attach@cisco.com>; Judith OGBORNE <judithogborne@hsbc.co.nz>; Janaka PERERA <janakaperera@hsbc.co.nz>
#viveranj@cisco.com
#From: Sourajit Hazra (souhazra) <souhazra@cisco.com>
#Cc: cisco-hsbc-d2o-collab-incident-management(mailer list) <cisco-hsbc-d2o-collab-incident-management@cisco.com>; hsbc-cms-attach(mailer list) <hsbc-cms-attach@cisco.com>; Judith OGBORNE <judithogborne@hsbc.co.nz>; Janaka PERERA <janakaperera@hsbc.co.nz>
#Email: munikuma@cisco.com
#To: Lisa Castillo -X (liscasti) <liscasti@cisco.com>; Andy Krawczyk (akrawczy) <akrawczy@cisco.com>; Judith OGBORNE <judithogborne@hsbc.co.nz>; businessenhanced@vodafone.nz; cisco-hsbc-d2o-collab-incident-management(mailer list) <cisco-hsbc-d2o-collab-incident-management@cisco.com>
#From: Lisa Castillo -X (liscasti) <liscasti@cisco.com>
#To: Andy Krawczyk (akrawczy) <akrawczy@cisco.com>; Judith OGBORNE <judithogborne@hsbc.co.nz>; cisco-hsbc-d2o-collab-incident-management(mailer list) <cisco-hsbc-d2o-collab-incident-management@cisco.com>
