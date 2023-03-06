from functools import *


def m(h):
    return h+1, h*2


@lru_cache(None)
def g(h):
    if 20 <= h <= 30:
        return 'w'
    if h > 30:
        return 'p1'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all((g(i) == 'p1' or g(i) == 'p2') for i in m(h)):
        return 'v2'

for s in range(1, 35):
    if g(s) == 'v1':
        print(s)

# 19) 5
# 20) 9 17
# 21) 16
