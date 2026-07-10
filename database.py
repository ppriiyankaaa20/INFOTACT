import sqlite3

conn = sqlite3.connect("pychronicle.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS variables(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    variable_name TEXT
)
""")

conn.commit()

conn.close()

print("Database Created Successfully")