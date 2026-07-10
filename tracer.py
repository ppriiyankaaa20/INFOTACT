import sys
import sqlite3

# Connect to database
conn = sqlite3.connect("pychronicle.db")
cursor = conn.cursor()

# Clear previous execution data
cursor.execute("DELETE FROM execution")
conn.commit()


def trace_function(frame, event, arg):
    if event == "line":
        line = frame.f_lineno

        for var, value in frame.f_locals.items():
            cursor.execute(
                """
                INSERT INTO execution(line_number, variable_name, variable_value)
                VALUES (?, ?, ?)
                """,
                (line, var, str(value))
            )

    return trace_function


def main():
    x = 10
    y = 20
    z = x + y
    print(z)


# Start tracing
sys.settrace(trace_function)

main()

# Stop tracing
sys.settrace(None)

# Save data
conn.commit()
conn.close()