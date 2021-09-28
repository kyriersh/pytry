# my function "def"
a = int(input(" input 1 : "))
b = int(input(" input 2 : "))

def my_func1():

    for x in range(a, b, 1):
        if x % 2 == 0:
            print("qwerty")
        else:
            print(x)
my_func1()
#
user_name = str(input(" name : "))
def name_welcome():
    print(user_name + " Welcome !")
name_welcome()