from functools import *


def m(c1, c2):
    res = []
    if c1 < c2:
        for i in range(1, c1+1):
            res.append((c1+i, c2))
    else:
        for i in range(1, c2+1):
            res.append((c1, c2+i))
    return res

@lru_cache(None)
def g(n):
    c1, c2 = n
    if c1+c2 > 45:
        return 'w'
    if any(g(i) == 'w' for i in m(c1, c2)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(c1, c2)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(c1, c2)):
        return 'p2'
    if all((g(i) == 'p1' or g(i) == 'p2') for i in m(c1, c2)):
        return 'v2'

r = []  
for c1 in range(1, 45):
    for c2 in range(45, 0, -1):
        if g( (c1, c2) ) == 'p1':
            r.append(c1 + c2)
print(min(r))

# 19) 22
# 20) 24 33
# 21) 20
