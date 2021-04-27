# fizz buzz
a = int(input())
for x in range(1, a, 2):
    if x % 3 == 0 and x % 5 == 0:
        print("solo learn")
        continue
    elif x % 3 == 0:
        print("solo")
        continue
    elif x % 5 == 0 :
        print("learn")
        continue
    else:
        print(x)
