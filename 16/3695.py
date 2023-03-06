from functools import *


@lru_cache(None)
def f(n):
    if n <= 5:
        return n
    elif n > 5 and n % 3 == 0:
        return n + f((n/3) + 2)
    else:
        return n + f(n+3)


for n in range(6, 10000):
    try:
        res = f(n)
        if res > 1000:
            print(n)
    except:
        pass
