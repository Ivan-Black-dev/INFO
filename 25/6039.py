from fnmatch import *

def ch(n):
    c = 0
    if n % 117 == 0:
        c += 1
    if n % 119 == 0:
        c += 1
    if n % 121 == 0:
        c += 1
    return c == 1

for i in range(1058129, 10**8):
    if ch(i):
        if fnmatch(str(i), '1?58*129'):
            print(i, i/121, i/119, i/117)
