# practice with text, count char in text and percentage
def count_char(text, char):
    count = 0
    for i in text:
        if i == char:
            count+=1
    return count
filename = input(" enter filename : ")
ch = input(" input char : ")
with open(filename) as f :
    text = f.read()
print(count_char(text, ch))
for char in "qwertyuiopasdfghjklzxcvbnm":
    perc = 100 * count_char(text, char)/len(text)
    print("{0} - {1}%".format(char,round(perc,2)))
