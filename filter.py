filename=raw_input('what is the name of the VoterHistoryDataReport file?? ')

f=open(filename)
#name of completed file
fb=open('Completefile.txt','w')

# Legend for each line in Completefile
#voterid|partycode|countyPrecinct|Municipality|Ward,District|MUN|ANS|FIR|SPE|PRI|RUM|GEN|REM|/n

#election types
# MUN=Municiple
# ANS=Annual School
# FIR=fire
# SPE=Special school
# PRI=primary
# RUM=Run-off municiple
# GEN=General
# REM=Recall municiple

#party Codes
# CNV
# RE/REP
# RFP
# LIB
# DE/DEM
# UNA
# GRE
# U
# NAT
# CON

#municipalities:
# BAYONNE
# EAST NEWARK
# GUTTENBERG
# HARRISON
# HOBOKEN
# JERSEY CITY
# KEARNY
# NORTH BERGEN
# SECAUCUS
# UNION CITY
# WEEHAWKEN
# WEST NEW YORK

#this isn't the shortest way to do it but it only has to be run once. And it doesn't run in Ram

a=f.readline()
while a!='Total Number Of Voters: 342694\r\n':
    b=a.split('|')
    if b[2]=='RE':
        b[2]="REP"
    elif b[2]=='DE':
        b[2]="DEM"
    ls=['MUN','ANS','FIR','SPE','PRI','RUM','GEN','REM']
    templine=b[0]+'|'+b[2]+'|'+b[33]+"|"+b[34]+"|"+b[35]+"|"+b[36]
    while b[0]==a.split('|')[0]:
        t=a.split('|')[-4]
        if t in ls:
            ls[ls.index(t)]=False
        a=f.readline()
    for x in ls:
        if not x:
            templine+='|'+'T'
        else:
            templine+='|'+'F'
    fb.write(templine+'|'+'\n')



f.close()
fb.close()
print 'Done'
print "please checkout 'Completefile.txt'"
    
