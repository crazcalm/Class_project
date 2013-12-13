"""
Let learn to mess with this database!
"""

import sqlite3, os

def test(): #works
	#You are my model!	

	conn = sqlite3.connect("example.db")
	c = conn.cursor()

	for index, value in enumerate(c.execute('SELECT * FROM voters3')):
		print index, value


def headers(): # works
	# Prints out the name of the columns

	conn = sqlite3.connect("voterdb.db")
	c = conn.cursor()

	for value in c.execute('PRAGMA table_info(m)'):
		print value[0], value[1]


def test2(query):

	clear_file()
	"""
	-Can search for multiple things at the same time.
	-Has AND and OR operators
	-Like (seems to) look for patterns within strings
	-Is really fast!
	"""
	filter = ("party_code", "sex", "county", "municipality", "ward", "district", "election_dates")
	stack = [query[item] for item in filter if item in query]
	print stack
	
	conn = sqlite3.connect("example.db")
	c = conn.cursor()

	result = ""

	for index, value in enumerate(c.execute('SELECT voter_id, first_name, middle_name, last_name, prefix, suffix, phone_number,'
								+' street_number, street_name, city, state, zip_5, zip_4, election_names,'
								+'election_dates, sex  FROM voters3 WHERE party_code LIKE  ? AND sex LIKE ? AND county LIKE ?'
								+' AND municipality LIKE ? AND ward LIKE ? AND district LIKE ? '
								+ ' AND election_dates LIKE ?', ("%"+stack[0]+"%","%"+stack[1]+"%","%"+stack[2]+"%",
									"%"+stack[3]+"%","%"+stack[4]+"%","%"+stack[5]+"%","%"+stack[6]+"%"))):
		#print index, value
		voter_id = value[0]
		name = " ".join(value[1:6])
		address = " ".join(value[7:12])
		phone_number = value[6]
		elections =[": ".join(i) for i in zip(value[13].split(","),value[14].split(","))]
		elections = ",".join(elections)
		sex = value[15]
		
		"""
		print voter_id
		print phone_number
		print name
		print address
		print elections
		print sex
		print "\n\n"
		"""
		result += "Voter ID: %s\nName: %s\nSex: %s\nPhone Number:%s\nAddress: %s\nVoter History\n%s\n\n" % \
					(voter_id, name, sex, phone_number, address, elections)
		
		if index >100:
			write_file(result)
			result = ""

	if len(result)> 1:
		write_file(result)
		#if index >= 20:
			#break

def clear_file():
	
	current_dir = os.getcwd()
	os.chdir(current_dir+"/static")
	if os.path.exists("test.txt"):
		with open("test.txt", "wt") as f:
			f.write("")
	os.chdir(current_dir)
	
def write_file(result):
	current_dir = os.getcwd()
	os.chdir(current_dir+"/static")
	if os.path.exists("test.txt"):
		with open("test.txt", "a") as f:
			f.write(result)
	os.chdir(current_dir)
headers()
#test2()
