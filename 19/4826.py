from functools import *
import sys

sys.setrecursionlimit(20_000)

def m(h):
    # s = 1: +1
    # s = 2: +2
    # s = 3: *2
    c, s = h
    r = []
    if s != 1:
        r.append( (s+1, 1) )
    if s != 2:
        r.append( (s+2, 2) )
    if s != 3:
        r.append( (s*2, 3) )
    return r


@lru_cache(None)
def g(h):
    c, _ = h
    if c >= 68:
        return 'w'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all((g(i) == 'p1' or g(i) == 'p2') for i in m(h)):
        return 'v2'


for s in range(50, 67):
    print(g((s, 0)))
