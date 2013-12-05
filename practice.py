import time, sqlite3
from bs4 import BeautifulSoup             # A web scraping tool

def main():
	start = time.clock()
	tags = parse_html_table("Report.html")
	create_db_table()
	organize_info()
	#for count, item in enumerate(data_parser("hudson")):
	#	for index,value in enumerate(item[:-1]):
	#		pass
			#print "Index: %s\t%s: %s" % (index, tags[index + 1][0], value)
		#print "\n\n"
		#if count ==2:
		#	break
	print "\n\nThe list does end..."
	endtime = time.clock() - start
	print endtime

def access_db():

	pass

def organize_info(): # write later

	tempt1 = []
	tempt2 = []
	tempt_count =0

	for count, item in enumerate(data_parser("hudson")):

		if count == 0:
			tempt1 = list(item)
			tempt2.append(item[38])
			tempt2.append(item[39])
			tempt2.append(item[40])
			tempt2.append(item[41])
			tempt2.append(item[42])

		else:
			if tempt1[0] == item[0]:
				tempt2.append(item[38])
				tempt2.append(item[39])
				tempt2.append(item[40])
				tempt2.append(item[41])
				tempt2.append(item[42])

			else:
				#print "voter id: %s" % (tempt1[0])
				#print "len(tempt2): %s \t %s" % (len(tempt2), tempt2)
				#print "\n"
				create_entry(tempt1, tempt2)
				tempt1 = list(item)
				tempt2= []
				tempt2.append(item[38])
				tempt2.append(item[39])
				tempt2.append(item[40])
				tempt2.append(item[41])
				tempt2.append(item[42])
				#print "\n\n"
			
			#if count>20:
			#	break

def create_entry(info, stack):
	
	result = []
	stack.insert(0,"I need the count to start from one")
	
	election_dates = ""
	election_names = ""
	election_types = ""
	election_catog = ""
	ballot_types   = ""

	for count, value in enumerate(stack):
		if count% 5 == 0 and count != 0:
			#print "Intented: %s, %s, %s, %s, %s" % (stack[count-4], stack[count-3], stack[count-2]\
			#		, stack[count-1], stack[count])

			election_dates += stack[count-4] + ", "
			election_names += stack[count-3] + ", "
			election_types += stack[count-2] + ", "
			election_catog += stack[count-1] + ", "
			ballot_types   += stack[count  ] + ", "

	#print "info string: %s, %s, %s, %s, %s\n" % (election_dates[:-2], election_names[:-2],\
	#	election_types[:-2], election_catog[:-2], ballot_types[:-2])

	election_dates = election_dates[:-2]
	election_names = election_names[:-2]
	election_types = election_types[:-2]
	election_catog = election_catog[:-2]
	ballot_types   = ballot_types[:-2]

	info[38] = election_dates
	info[39] = election_names
	info[40] = election_types
	info[41] = election_catog
	info[42] = ballot_types

	for index, value in enumerate(info):
		#print index, value
		
		# unwanted info
		if index == 10 or index == 11 or (index >=13 and index <=15)\
			or (index >= 20 and index <=30) or index ==43:

			#print "\nnot keeping: %s\n" % (index)
			pass
			
		else:
			result.append(info[index])

	#print "len(result): %s" % (len(result))
	insert_into_db(result)
 


def insert_into_db(info): # write later

	conn = sqlite3.connect("example.db")
	c = conn.cursor()
	
	c.execute("INSERT INTO voters3 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"\
				,(info))

	conn.commit()
	conn.close()
	

def create_db_table(): #Not finished...
	tags = parse_html_table("Report.html")
	conn = sqlite3.connect("example.db")
	c = conn.cursor()
	"""
	A key to show which tags hold which info

	voter_id             = tags[1]
	status_code          = tags[2]
	party_code           = tags[3]
	last_name            = tags[4]
	first_name           = tags[5]
	middle_name          = tags[6]
	prefix               = tags[7]
	suffix               = tags[8]
	sex                  = tags[9]
	street_number        = tags[10]
	street_name          = tags[13]
	city                 = tags[17]
	state                = tags[18]
	zip_5                = tags[19]
	zip_4                = tags[20]
	birth_date           = tags[32]
	date_registered      = tags[33]
	county               = tags[34]
	municipality         = tags[35]
	ward                 = tags[36]
	district             = tags[37]
	phone_number         = tags[38]
	election_dates       = tags[39]
	election_names       = tags[40]
	election_types       = tags[41]
	election_categories  = tags[42]
	ballot_types         = tags[43]
	"""
	c.execute('''CREATE TABLE voters3
(voter_id text, status_code text, party_code text, last_name test, first_name text,
middle_name text, prefix text, suffix text, sex text, street_number text, street_name text, city text, state text,
zip_5 text, zip_4 text, birth_date text, date_registered text, county text, municipality text,
ward text, district text, phone_number text, election_dates text, election_names text,
election_types text, election_categories text, ballot_types text)''')
	conn.commit()
	print "I think the table was made..."

		

def parse_html_table(file_name):
    file = open(file_name, "r")
    soup = BeautifulSoup(file)           # creating a bs4 object
    tbody_tag = soup.find_all("tbody")   # creates a list of all the 'tbody'
    
    stack_2d = []                        # A list that will hold tuple of size 3
    inner_stack = []

    for i, value in enumerate(tbody_tag):
        #print i, len(value)
        if len(value)> 20:
			index = i

    #print tbody_tag[index]
   
    for string in tbody_tag[index].strings:  # Lets me interate over the string in the html
        
        inner_stack.append(string)    
        
        if len(inner_stack) == 3:
            stack_2d.append(tuple(inner_stack))  # (field name, field type, size)
            inner_stack = []
            
    return stack_2d                             #note: string are in Unicode...

def data_parser(data):
    """
    This is a sample of a parser we could use.
    The indexes between the html list and the data list
    seem to be off by 1.
    """
    file = open(data, "r")
    tempt = "blah, blah, blah"
    while tempt != '':
        tempt = file.readline()
        yield tempt[:-1].split("|")

    print "!!!!!!!!!!!!!!!!STOPPED!!!!!!!!!!!!!!!!!"

    """
    file = open(data, "r").readlines(1024)     #my small computer cant handle the entire file at once...

    for index, line in enumerate(file):
        file[index] = line.split("|")
    """
    #return file

if __name__=="__main__":
    """
    test =  parse_html_table("Report.html")
    for index, value in enumerate(test):
        print index, value
        raw_input()

    test2 = data_parser("hudson")
    for index, value in enumerate(test2):
        print index + 1, value
        if index > 3:
            break
    """
    main()
