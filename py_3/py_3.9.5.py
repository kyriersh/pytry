# practice with continue
a = int(input('start:'))
b = int(input('stop:'))
c = int(input('step:'))
for x in range(a,b,c):
    if x % 2 == 0 :
        continue
    print(x)
