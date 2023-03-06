from functools import *

import sys

sys.setrecursionlimit(20000)


def z(n):
    if len(bin((n))[2:]) > 1:
        r = '1' + '0' * len(bin(n)[3:])
        return int(r, 2)
    else:
        return n

@lru_cache(None)
def f(s, e):
    if s == e:
        return 1
    elif s < e:
        return 0
    else:
        return f(s-1, e) + f(z(s), e)

#print( f( int('10001', 2), int('1', 2) ) )

    


        
