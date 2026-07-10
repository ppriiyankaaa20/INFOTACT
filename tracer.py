import sys

def trace_function(frame, event, arg):
    print("TRACE:", event, "Line:", frame.f_lineno)
    return trace_function

def main():
    x = 10
    y = 20
    z = x + y
    print(z)

sys.settrace(trace_function)
main()
sys.settrace(None)