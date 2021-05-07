# password generator
import random
n = int(input(" ssword length : "))
def key_gen(lenghth):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm' \
               'QWERTYUIOPASDFGHJKLZXCVBNM0123456789' \
               '/*-+!@#$%^&*()=\[]{}_?><'
    passw = ''
    for i in range(n):
        symbol = random.choice(alphabet)
        passw = passw + symbol
    return passw
passw = key_gen(n)
print(passw)

