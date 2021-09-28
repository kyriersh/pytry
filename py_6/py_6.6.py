#List comprehension
numbs = [i**2 for i in range(10)
         if i**2 % 2 ==0]

print(numbs)
n = int(input())

numbs = [i**1 for i in range(n)
         if i % 3 == 0 and i % 5 == 0]
print(numbs)