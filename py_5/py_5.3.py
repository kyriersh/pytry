# write/read
file = open("/home/kyrylo/Desktop/test.txt", "w")
file.write("new text file")
file.close()
file = open("/home/kyrylo/Desktop/test.txt", "r")
print(file.read())
file.close()