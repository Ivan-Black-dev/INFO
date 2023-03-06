#1 +1
#2 +2
#3 *2
from functools import *
def m(h):
    x, k = h
    r = []
    if k != 1:
        r.append((x+1, 1))
    if k != 2:
        r.append((x+2, 2))
    if k != 3:
        r.append((x*2, 3))
    return r
    

@lru_cache(None)
def g(h):
    x, k = h
    if x >= 43:
        return 'w'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all((g(i) == 'p1' or g(i) == 'p2') for i in m(h)):
        return 'v2'


for s in range(1, 44):
    if g((s, 0)) == 'v2':
        print(s)
