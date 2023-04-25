from itertools import *

for n in range(0, 3+1):  # кол-во цифр за @; n = 0, 1, 2, 3
    for x in '0123456789':
        for y in product('13579', repeat = n):
            y = ''.join(y)
            d = int(f'78{x}56{y}321')
            if d%279 == 0:
                print(d, d//279)
