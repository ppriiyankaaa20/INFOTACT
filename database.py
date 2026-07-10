import sqlite3

conn = sqlite3.connect("pychronicle.db")
cursor = conn.cursor()

# Week 1 table
cursor.execute("""
CREATE TABLE IF NOT EXISTS variables(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    variable_name TEXT
)
""")

# Week 2 table
cursor.execute("""
CREATE TABLE IF NOT EXISTS execution(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    line_number INTEGER,
    variable_name TEXT,
    variable_value TEXT
)
""")

conn.commit()

print("Database Created Successfully")
print("Execution Table Created Successfully")

conn.close()