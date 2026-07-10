import sys

def trace_function(frame, event, arg):
    if event == "line":
        print(f"Event: {event}")
        print(f"Line Number: {frame.f_lineno}")
        print("---------------------")
    return trace_function

sys.settrace(trace_function)

x = 10
y = 20
z = x + y

print(z)

sys.settrace(None)   # Stop tracing
import sys
import sqlite3

# Connect to database
conn = sqlite3.connect("pychronicle.db")
cursor = conn.cursor()

def trace_function(frame, event, arg):
    if event == "line":

        line = frame.f_lineno

        for var, value in frame.f_locals.items():

            cursor.execute("""
                INSERT INTO execution(line_number, variable_name, variable_value)
                VALUES (?, ?, ?)
            """, (line, var, str(value)))

            conn.commit()

            print(f"Line {line} | {var} = {value}")

    return trace_function


def main():
    x = 10
    y = 20
    z = x + y
    print(z)


sys.settrace(trace_function)

main()

sys.settrace(None)

conn.close()