#decorator
def decor(func):
    def wrap():
        print("###")
        func()
        print("###")

    return wrap


def print_bill():
    print("BILL DATA GOES HERE")


decorated = decor(print_bill)
decorated()