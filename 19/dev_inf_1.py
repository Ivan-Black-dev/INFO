from functools import *

def m(h):
    r = [h-1]
    if h % 2 == 0:
        r.append(h//2)
    return r


@lru_cache(None)
def g(h):
    h
    if h<= 12:
        return 'w'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all((g(i) == 'p1' or g(i) == 'p2') for i in m(h)):
        return 'v2'
    
for s in range(150, 13, -1):
    if g(s) == 'v2':
        print(s)
