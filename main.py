import sqlite3

conn = sqlite3.connect("pychronicle.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM variables")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()