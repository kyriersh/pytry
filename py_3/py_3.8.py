# while Loops(sum of digit)
n = int(input())
sum = 0

while n > 0:
    sum += n % 10
    n //= 10

print(sum)
i = 1
while i <=10:

    i+=1
    if i % 2 == 0:

        continue
    print(i)