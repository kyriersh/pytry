# password generator
import random
n = int(input(" password length : "))
def key_gen(lenghth):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm' \
               'QWERTYUIOPASDFGHJKLZXCVBNM' \
               '0123456789' \
               '/*-+!@#$%^&*()=\[]{}_?><'
    passw = ''
    for i in range(n):
        passw += random.choice(alphabet)
    return passw
passw = key_gen(n)
print("your password : " + passw)
file = open("test1.txt", "a")
file.write("your password : " + passw)
file.close()
