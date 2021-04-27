# practice with def
def range_floats(start, stop, step):
    start = float(input(" input start : "))
    stop = float(input(" input stop : "))
    step = float(input(" input step : "))
    while start < stop:
        start+=step
        print(start)
range_floats("a","b","c")

