# testing read file v 1.1
file = open("/home/kyrylo/Desktop/qwerty.txt", 'r')
cont = file.read()
print(cont)
print(len(cont))
for line in cont:
    print(line)
file.close()