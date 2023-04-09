from functools import lru_cache
import sys

def m(h):
    c1, c2 = h
    r = []
    if c1 > c2:
        tr = c1//3
        for i in range(1, tr+1):
            r.append((c1-i, c2+i))
    else:
        tr = c2//3
        for i in range(1, tr+1):
            r.append((c1+i, c2-i))
    return r

@lru_cache(None)
def g(h):
    c1, c2 = h
    if c1 == c2:
        return 'w'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all(g(i) in ['p1', 'p2'] for i in m(h)):
        return 'v2'

sys.setrecursionlimit(5000)
for c1 in range(1, 50):
    for c2 in range(1, c1):
        if (c1 % 2 == 0) ^ (c2 % 2 == 0):
            if 40 <= c1+c2 <= 50:
                print(g((c1, c2)))
