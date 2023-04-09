from functools import *

def m(h):
    c1, c2 = h
    return [(c1+1, c2), (c1*2, c2), (c1, c2+1), (c1, c2*2)]

@lru_cache(None)
def g(h):
    c1, c2 = h
    if 40 <= c1 + c2 <= 49:
        return 'w'
    if c1 + c2 >= 50:
        return 'p1'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all(( g(i) == 'p1' or g(i) == 'p2' ) for i in m(h)):
        return 'v2'


for s in range(1, 26):
    if g((14, s)) == 'v1':
        print(s)

#19) 24
#20) 2
#21) 8 22
