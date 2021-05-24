#fibonacci
num = int(input())


def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        print(a)
        print(b)
        for i in range(0, n - 2):
            c = a + b
            print(c)
            a = b
            b = c


fibonacci(num)