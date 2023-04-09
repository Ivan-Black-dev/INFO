'''zset = set()
for i in range(10, 1000):
    zset.add(str(i)[1:])

def mask(z, v1, v2):
    return int(f'{z}1{v1}542{v2}')

zset.add('')
r = []
for z in zset:
    for v1 in range(10):
        for v2 in range(10):
            n = mask(z, v1, v2)
            if n <= 10**8:
                if n % 2084 == 0:
                    r.append((n, n//2084))
r = sorted(r)
for i in r:
    print(i)
'''
from fnmatch import *
for x in range(2084, 10**8+1, 2084):
    if fnmatch(str(x), '*1?542?'):
        print(x, x//2084)
