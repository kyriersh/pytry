# fizz buzz
a = int(input())
for x in range(1, a):
    if x % 3 == 0 and x % 5 == 0:
        print("solo learn")
    elif x % 3 == 0:
        print("solo")
    elif x % 5 == 0 :
        print("learn")
    elif x % 2 != 0:
        print(x)
