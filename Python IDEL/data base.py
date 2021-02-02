import sqlite3
conn = sqlite3.connect('student.db')
#create a cursor
c = conn.cursor()

#create a table
#c.execute("""CREATE TABLE students(
#	first_name text
	#last_name text
	#email text
	#phone num integer)
	#""")
c.execute(""" INSERT INTO students VALUES(

'karajohn906@gmail.com')""")
print('completed sucessfully')
#data types
#null
#Integer
#real
#text
#blob

#commit our command
conn.commit()
conn.close()
