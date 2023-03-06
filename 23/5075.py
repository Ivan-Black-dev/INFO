def f(s, e, p):
    if s == e:
        return 1
    elif s > e or s == 28:
        return 0
    else:
        res = f(s+3, e, False) + f(s*2, e, False)
        if p:
            return res
        else:
            return res + f(s+1, e, True) 

print(f(4, 10, False) * f(10, 93, False))
