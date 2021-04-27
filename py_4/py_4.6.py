# practice with def
def range_floats(start, stop, step):
    start = float(input(" input start : "))
    stop = float(input(" input stop : "))
    step = float(input(" input step : "))
    while start < stop:
        start+=step
        print(start)
range_floats("a","b","c")

def r_f(start, stop, step):
    while start < stop :
        yield start
        start+=step
for x in r_f(1,3,0.2):
    print(x)
