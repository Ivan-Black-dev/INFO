def add1(n):
    return int('1' + bin(n)[2:], 2)

def f(s, e):
    if s == e:
        return 1
    if s > e:
        return 0
    else:
        return f(s+1, e) + f(add1(s), e)

print( f( int('100', 2), int('110001', 2) ) )
