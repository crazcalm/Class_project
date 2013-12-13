"""
Let learn to mess with this database!
"""

import sqlite3, os

def test(): #works
	#You are my model!	

	conn = sqlite3.connect("voterdb.db")
	c = conn.cursor()

	for index, value in enumerate(c.execute('SELECT * FROM voterdb')):
		print index, value
		if index >2:
			break


def headers(): # works
	# Prints out the name of the columns

	conn = sqlite3.connect("voterdb.db")
	c = conn.cursor()

	for value in c.execute('PRAGMA table_info(voterdb)'):
		print value[0], value[1]


def test2(query= []):

	clear_file()
	"""
	-Can search for multiple things at the same time.
	-Has AND and OR operators
	-Like (seems to) look for patterns within strings
	-Is really fast!
	"""
	
	filter = ("party", "district", "ward", "municipality", "congressional")
	filter2 = tuple([str(i) for i in range(2002,2013)])
	stack = [query[item].lower() for item in filter if item in query]
	print stack

	stack.extend([query["type"].lower() if num in query.itervalues() else "" for num in filter2])
	print "len(stack)", len(stack)
	print stack

	conn = sqlite3.connect("voterdb.db")
	c = conn.cursor()

	result = ""
	
	for index, value in enumerate(c.execute('SELECT *  FROM voterdb WHERE party LIKE  ? AND district LIKE ? AND ward LIKE ?'
								+' AND municipality LIKE ? AND congressional LIKE ? AND y2002 LIKE ? '
								+ ' AND y2003 LIKE ?  AND y2004 LIKE ?  AND y2005 LIKE ?  AND y2006 LIKE ?'
								+ ' AND y2007 LIKE ?  AND y2008 LIKE ?  AND y2009 LIKE ?  AND y2010 LIKE ?'
								+ ' AND y2012 LIKE ?  AND y2012 LIKE ?', ("%"+stack[0]+"%","%"+stack[1]+"%","%"+stack[2]+"%",
									"%"+stack[3]+"%","%"+stack[4]+"%","%"+stack[5]+"%","%"+stack[6]+"%",
									"%"+stack[7]+"%","%"+stack[8]+"%","%"+stack[9]+"%","%"+stack[10]+"%",
									"%"+stack[11]+"%","%"+stack[12]+"%","%"+stack[13]+"%","%"+stack[14]+"%",
									"%"+stack[15]+"%"))):
		print index, value

		"""
		result += ""
		if index >100:
			write_file(result)
			result = ""

	if len(result)> 1:
		write_file(result)
		"""
		if index >= 3:
			break

	print "Did you run?"
	
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
#test()
