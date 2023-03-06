from functools import *


def m(h):
    return h + 1, h * 2


@lru_cache(None)
def g(h):
    if 50 <= h <= 70:
        return 'w'
    if h > 70:
        return 'p1'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all((g(i) == 'p1' or g(i) == 'p2') for i in m(h)):
        return 'v2'

for s in range(1, 100):
    if g(s) == 'v2':
        print(s)


# 19) 13
# 20) 24 47
# 21) 46
