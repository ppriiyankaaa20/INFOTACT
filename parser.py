import ast
import sqlite3

# Connect to database
conn = sqlite3.connect("pychronicle.db")
cursor = conn.cursor()

# Read sample.py
with open("sample.py", "r") as file:
    code = file.read()

# Convert code to AST
tree = ast.parse(code)
cursor.execute("delete from variables")
conn.commit()
# Find variables and store them
for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        variable = node.targets[0].id

        print("Variable Found:", variable)

        cursor.execute(
            "INSERT INTO variables(variable_name) VALUES(?)",
            (variable,)
        )

conn.commit()
conn.close()

print("Variables Saved Successfully")