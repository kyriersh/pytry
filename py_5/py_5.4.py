names = ['john', 'oscar', 'jacob']
file = open("/home/kyrylo/Desktop/names.txt", "w")
file.write(str(names))

file.close()
file = open("/home/kyrylo/Desktop/names.txt", "r")
print(file.read())
file.close()
