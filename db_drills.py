"""
Let learn to mess with this database!
"""

import sqlite3

def test(): #works
	#You are my model!	

	conn = sqlite3.connect("example.db")
	c = conn.cursor()

	for index, value in enumerate(c.execute('SELECT * FROM voters3')):
		print index, value


def headers(): # works
	# Prints out the name of the columns

	conn = sqlite3.connect("example.db")
	c = conn.cursor()

	for value in c.execute('PRAGMA table_info(voters3)'):
		print value[0], value[1]


def test2():
	"""
	-Can search for multiple things at the same time.
	-Has AND and OR operators
	-Like (seems to) look for patterns within strings
	-Is really fast!
	"""
	conn = sqlite3.connect("example.db")
	c = conn.cursor()

	for index, value in enumerate(c.execute('SELECT first_name, middle_name, last_name, street_number, street_name, city, state, zip_5, zip_4,'
								+' election_types, election_categories'
								+'  FROM voters3 WHERE first_name = ? AND election_types LIKE ?', ("MARCUS","%MUN%"))):
		print index, value

		if index >= 10:
			break

headers()
test2()
