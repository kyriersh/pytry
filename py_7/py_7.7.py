#practice with module itertools
from itertools import count
for i in count(3):
    print(i)
    if i >= 11:
        break
