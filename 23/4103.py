'''
import sys

res = set()

sys.setrecursionlimit(10_000)

def f(s, c):
    if s % 2 == 0 and s < 100:
        res.add(s)
        return None
    else:
        f(s+3, c+1)
        f(s*3, c+1)

f(3, 0)
print(res)
'''

def f(s, e):
    if s == e:
        return 1
    if s > e:
        return 0
    return f(s+3, e) + f(s*3, e)

c = 0
for i in range(6, 101, 2):
    if f(3, i) != 0:
        c += 1
print(c)

