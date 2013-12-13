"""takes the text file where each time a voter voted is on a new line and compines it into a single line where only the year and type of elections the voter voted in is preserved"""

filename=raw_input('what is the name of the VoterHistoryDataReport file?? ')

f=open(filename)
#name of completed file
fb=open('Completefile.txt','w')

# Legend for each line in Completefile
#voterid|partycode|countyPrecinct|Municipality|Ward|District|2002|2003|2004|2005|2006|2007|2008|2009|2010|2011|2012|/n

#election types
# MUN=Municiple
# ANS=Annual School
# FIR=fire
# SPE=Special school
# PRI=primary
# RUM=Run-off municiple
# GEN=General
# REM=Recall municiple

#party_Codes=['CNV','REP','RFP','LIB','DEM','UNA','GRE','U','NAT','CON']

#municipalities:['BAYONNE','EAST NEWARK','GUTTENBERG','HARRISON','HOBOKEN','JERSEY CITY','KEARNY','NORTH BERGEN','SECAUCUS','UNION CITY','WEEHAWKEN','WEST NEW YORK']

# wards=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']

# districts=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34']



#ls=[2002|2003|2004|2005|2006|2007|2008|2009|2010|2011|2012]


#this isn't the shortest way to do it but it only has to be run once. And it doesn't run in Ram

a=f.readline()
def extract(a,ls):
    if '2002' in a[38]:
        ls[0]=ls[0]+a[-4]+'/'
    elif '2003' in a[38]:
        ls[1]=ls[1]+a[-4]+'/'
    elif '2004' in a[38]:
        ls[2]=ls[2]+a[-4]+'/'
    elif '2005' in a[38]:
        ls[3]=ls[3]+a[-4]+'/'
    elif '2006' in a[38]:
        ls[4]=ls[4]+a[-4]+'/'
    elif '2007' in a[38]:
        ls[5]=ls[5]+a[-4]+'/'
    elif '2008' in a[38]:
        ls[6]=ls[6]+a[-4]+'/'
    elif '2009' in a[38]:
        ls[7]=ls[7]+a[-4]+'/'
    elif '2010' in a[38]:
        ls[8]=ls[8]+a[-4]+'/'
    elif '2011' in a[38]:
        ls[9]=ls[9]+a[-4]+'/'
    elif '2012' in a[38]:
        ls[10]=ls[10]+a[-4]+'/'



while a!='Total Number Of Voters: 342694\r\n':
    b=a.split('|')
    if b[2]=='RE':
        b[2]="REP"
    elif b[2]=='DE':
        b[2]="DEM"
    ls=['','','','','','','','','','','']
    while b[0]==a.split('|')[0]:
        b=a.split('|')
        last=a
        extract(b,ls)
        a=f.readline()
    line=last[:last.replace('|','/',37).find('|')+1]
    for x in ls:
        line+=x+'|'
    fb.write(line+'\n')
        
    


f.close()
fb.close()
print 'Done'
print "please checkout 'Completefile.txt'"
    
