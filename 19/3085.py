from functools import *
import sys

def m(h):
    c1, c2 = h
    r = [(c1 - 1, c2), (c1, c2 - 1)]
    if c1 % 2 == 0:
        r.append((c1//2, c2))
    else:
        r.append((c1//2+1, c2))
    if c2 % 2 == 0:
        r.append((c1, c2//2))
    else:
        r.append((c1, c2//2+1))
    return r

@lru_cache(None)
def g(h):
    c1, c2 = h
    if c1 + c2 <= 20:
        return 'w'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all((g(i) == 'p1' or g(i) == 'p2') for i in m(h)):
        return 'v2'

sys.setrecursionlimit(20_000)
for s in range(10, 50):
    print(g((10, s)))
