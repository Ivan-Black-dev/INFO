from functools import lru_cache
import sys


def m(h):
    c1, c2 = h
    return [(c1+c2, c2), (c1, c1+c2)]

@lru_cache(None)
def g(h):
    c1, c2 = h
    if c1 + c2 >= 212:
        return 'w'
    vh = m(h)
    if any(g(i) == 'w' for i in vh):
        return 'p1'
    if all(g(i) == 'p1' for i in vh):
        return 'v1'
    if any(g(i) == 'v1' for i in vh):
        return 'p2'
    if all(g(i) in ['p2'] for i in vh):
        return 'v2'

sys.setrecursionlimit(20_000)
for s in range(1, 212):
    if g((10, s)) == 'v2':
        print(s)
# 37 50
