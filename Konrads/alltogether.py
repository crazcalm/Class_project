"""putting the 2 sorted voter files together and creating the order commented below"""


# creates the list 


#FIRST,LAST,MIDDLE,SUFFIX,SEX,ST.NUM,ST.NAME,APT,CITY,ZIP,PHONE,DOB,PARTY,COUNTY
#COUNTYPRECINCT,MUNICIPALITY,WARD,DISTRICT,CONGRESSIONAL,LEGISLATIVE,
#FREEHOLDER,SCHOOL,FIRE,y2002,y2003,y2004,y2005,y2006,y2007,y2008,y2009,y2010,y2011,y2012



f=open('VHDRSorted.txt')
ff=open('AVLSorted.txt')
fb=open('FULLsearchlist.txt','w')

a=f.readline()
b=ff.readline()

while a!='':
    b=b.split('|')
    a=a.split('|')
    if len(b)!=25:
	b.insert(4,'')
    fb.write(a[4]+'|'+a[3]+'|'+a[5]+'|'+a[7]+'|'+a[8]+'|'+a[9]+'|'+a[12]+'|'+a[13]+'|'+a[16]+'|'+a[17]+'|'+a[37]+'|'+a[31]+'|'+a[2]+'|'+'HUDSON'+'|'+a[33]+'|'+a[34]+'|'+a[35]+'|'+a[36]+'|'+b[19]+'|'+b[20]+'|'+b[21]+'|'+b[22]+'|'+b[23]+'|'+a[38]+'|'+a[39]+'|'+a[40]+'|'+a[41]+'|'+a[42]+'|'+a[43]+'|'+a[44]+'|'+a[45]+'|'+a[46]+'|'+a[47]+'|'+a[48]+'|'+"\n")
    a=f.readline()
    b=ff.readline()


f.close()
ff.close()
fb.close()
