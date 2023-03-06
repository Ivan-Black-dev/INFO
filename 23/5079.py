def f(s, e, p):
    if s == e:
        return 1
    elif s > e or s == 12 or s == 20:
        return 0
    else:
        res = f(s+1, e, False) + f(s+2, e, False)
        if p:
            return res
        else:
            return res + f(s*3, e, True)

print(f(2, 15, False) * f(15, 30, False) * f(30, 38, False))
