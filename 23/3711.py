def d(n):
    return int(bin(n)[2:][:-1], 2)

def f(s, e):
    if s == e:
        return 1
    elif s < e:
        return 0
    else:
        return f(s-1, e) + f(d(s), e)

print( f(int('100001', 2) , int('100', 2))) 
