from itertools import count, cycle
from math import ceil


for el in count(ceil(3)):
    if el > 10:
        break
    else:
        print(int(el))

c = 1
for el in cycle('CAT'):
    if c > 9:
        break
    print (el)
    c += 1
