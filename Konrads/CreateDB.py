""" from the text file Fullsearchlist.txt then creates an sql document that can easily be imported into a database with ".read ./voterdb.sql"""


f=open('FULLsearchlist.txt')
fb=open('voterdb.sql','w')

text="FIRST text,LAST text,MIDDLE text,SUFFIX text,SEX text,ST_NUM text,ST_NAME text,APT text,CITY text,ZIP text,PHONE text,DOB text,PARTY text,COUNTY text,COUNTYPRECINCT text,MUNICIPALITY text,WARD text,DISTRICT text,CONGRESSIONAL text,LEGISLATIVE text,FREEHOLDER text,SCHOOL text,FIRE text,y2002 text,y2003 text,y2004 text,y2005 text,y2006 text,y2007 text,y2008 text,y2009 text,y2010 text,y2011 text,y2012 text);"

text=text.lower()

fb.write("PRAGMA foreign_keys=OFF;"+"\n")
fb.write("BEGIN TRANSACTION;"+"\n")
fb.write("CREATE TABLE voterdb ("+text+"\n")

t="INSERT INTO \"voterdb\" VALUES("

a=f.readline()
while a!='':
    a=a.split('|')
    fb.write(t+str(a[:-1])[1:-1]+");"+"\n")
    a=f.readline()

fb.write("COMMIT;")

fb.close()
f.close()
