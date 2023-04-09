from functools import *


def m(h):
    c1, c2 = h
    r = []
    if c1 <= c2:
        for i in range(1, c1+1):
            r.append( (c1+i, c2) )
    if c2 <= c1:
        for i in range(1, c2+1):
            r.append( (c1, c2+i) )
    return r

@lru_cache(None)
def g(h):
    c1, c2 = h
    if sum(h) > 45:
        return 'w'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all((g(i) in ['p1', 'p2']) for i in m(h)):
        return 'v2'


ms = 45
for c1 in range(1, 45):
    for c2 in range(1, 45):
        if g( (c1, c2) ) == 'p1':
          ms = min(ms, c1+c2)
print('19)', ms)

r = []
for c1 in range(1, 41):
    if g( (5, c1) ) == 'p2':
        r.append(c1)
print('20)', min(r), max(r))


r = []
for c1 in range(1, 41):
    if g( (5, c1) ) == 'v2':
        r.append(c1)
print('21)', min(r))
