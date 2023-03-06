from functools import *


def m(h):
    return h+1, h+2, h+3, h*2

@lru_cache(None)
def g(h):
    if h > 37:
        return 'w'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all((g(i) == 'p1' or g(i) == 'p2') for i in m(h)):
        return 'v2'


for s in range(1, 40):
    if g(s) == 'v2':
        print(s)


#19: 18
#20: 9 17
#21: 14




