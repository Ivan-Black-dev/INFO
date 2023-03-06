from functools import *

res = set()

@lru_cache(None)
def f(s, e, c):
    global res
    if s == e:
        res.add(c)
        return 1
    elif s > e:
        return 0
    else:
        return f(s+1, e, c+1) + f(s+5, e, c+1) + f(s*3, e, c+1)

f(1, 227, 0)
print(min(res))
