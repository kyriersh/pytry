# practice with text
def count_char(text, char):
    count = 0
    for i in text:
        if i == char:
            count+=1
    return count
filename = input(" enter filename : ")
with open(filename) as f :
    text = f.read()
print(count_char(text,"r"))