# password generator
import random
n = int(input(" password length : "))
def key_gen(lenghth):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm' \
               'QWERTYUIOPASDFGHJKLZXCVBNM0123456789' \
               '/*-+!@#$%^&*()=\[]{}_?><'
    passw = ''
    for i in range(n):
        passw += random.choice(alphabet)
    return passw
passw = key_gen(n)
print(passw)

