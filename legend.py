#from bs4 import BeautifulSoup

party_code = ['CMV','REP','RFP','LIB','DEM','UNA','GRE','U','NAT','CON']

municipality =['BAYONNE','EAST NEWARK','GUTTENBERG','HARRISON','HOBOKEN',
'JERSEY CITY','KEARNY','NORTH BERGEN','SECAUCUS','UNION CITY','WEEHAWKEN',
'WEST NEW YORK']

ward = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']

district =['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', 
 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', 
 '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34']

congressional=['31','32','33']

year=['2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012']

election_type=['MUN','ANS','FIR','SPE','PRI','RUM','GEN','REM']


# MUN=Municiple
# ANS=Annual School
# FIR=fire
# SPE=Special school
# PRI=primary
# RUM=Run-off municiple
# GEN=General
# REM=Recall municiple

#def main():
#	
#	with open("Report.html", "r") as file:
#		soup = BeautifulSoup(file)
#	
#	test = soup.find_all("tbody", limit = 2)
#	filter = [str(i) for i in range(10)]
#	stack = [string.strip() for string in test[1].strings if string.strip()[0] in filter and len(string.strip()) > 9]
#	
#	for index, value in enumerate(stack):
#		tempt = value.split(",", 1)
#		stack[index] = (tempt[0], tempt[1].strip())
#	
#	return stack
#
#	
#election = main()
