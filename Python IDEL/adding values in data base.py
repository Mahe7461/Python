import sqlite3
c=sqlite3.connect('customer.db')
conn=c.cursor
c.execute("""INSERT INTO cutomers4
VALUES('RAM','elder','karajohn906@gmail.com')""")
print('completed sucessfully')
c.commit()
c.close()
