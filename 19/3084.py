from functools import *
import sys

sys.setrecursionlimit(2000)

def m(h):
    return h+1, h*2, h*3

@lru_cache(None)
def g(h):
    if 43 <= h <= 72:
        return 'w'
    if h > 72:
        return 'p1'
    if any(g(i) == 'w' for i in m(h)):
        return 'p1'
    if all(g(i) == 'p1' for i in m(h)):
        return 'v1'
    if any(g(i) == 'v1' for i in m(h)):
        return 'p2'
    if all((g(i) == 'p1' or g(i) == 'p2') for i in m(h)):
        return 'v2'


for i in range(1, 43):
    if g(i) == 'v2':
        print(i)
