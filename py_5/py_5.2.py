# testing read file v 1.1

file = open("/home/kyrylo/Desktop/pull_ups.txt", 'r')
n = int(input())
list = file.readlines()
print(list[n])
file.close()
