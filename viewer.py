import sqlite3

conn = sqlite3.connect("pychronicle.db")
cursor = conn.cursor()

cursor.execute("SELECT line_number, variable_name, variable_value FROM execution")
rows = cursor.fetchall()

print("Execution Timeline")
print("------------------")

for row in rows:
    print(f"Line {row[0]} | {row[1]} = {row[2]}")

conn.close()