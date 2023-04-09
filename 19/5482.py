from functools import *

def m(h):
    c1, c2 = h
    return [(c1 + 2, c2), (c1 * 2, c2), (c1, c2 + 2), (c1, c2 * 2)]


@lru_cache(None)
def g(h):
    c1, c2 = h
    if c1 + c2 >= 231:
        return 'w'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all( (g(i) == 'p1' or g(i) == 'p2') for i in m(h)):
        return 'v2'
    
for s in range(1, 214):
    print(g((17, s)), s, 17+s)

#19) 106 - 
#20) 53 105
#21) 96
