from functools import *

minL = 100**100

@lru_cache(None)
def f(s, e, w):
    global minL
    if s == e:
        minL = min(minL, len(w))
        return None
    if s > e:
        return None
    else:
        f(s+1, e, w+'1')
        f(s+5, e, w+'2')
        f(s*3, e, w+'3')


print(f(1, 227, ''))
