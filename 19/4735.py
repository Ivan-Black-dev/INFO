from functools import *

def m(h):
    c1, c2 = h
    return [(c1 + 2, c2), (c1 * 2, c2), (c1, c2 + 2), (c1, c2 * 2)]

@lru_cache(None)
def g(h):
    c1, c2 = h
    if 63 <= c1 + c2 <= 74:
        return 'w'
    if c1 + c2 > 74:
        return 'p1'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all( (g(i) == 'p1' or g(i) == 'p2') for i in m(h)):
        return 'v2'

for s in range(1, 48):
    if g((15, s)) == 'v2':
        print(s)

#19) 3
#20) 2 30
#21) 14
