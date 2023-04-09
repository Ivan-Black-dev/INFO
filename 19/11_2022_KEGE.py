from functools import *

def m(h):
    r = []
    if h + 1 <= 60:
        r.append(h+1)
    if h + 2 <= 60:
        r.append(h+2)
    if h * 2 <= 60:
        r.append(h*2)
    return r


@lru_cache(None)
def g(h):
    if h >= 51:
        return 'w'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all( (g(i) == 'p1' or g(i) == 'p2') for i in m(h)):
        return 'v2'
    if any(g(i) == 'v2' for i in m(h)):
        return 'p3'
    if all(g(i) in ['p1', 'p2', 'p3'] for i in m(h)):
        return 'v3'

for s in range(1, 51):
    #if g(s) == 'p3':
    print(s, g(s))
