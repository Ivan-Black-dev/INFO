def f(s, e, p):
    if s > e:
        return 0
    if s == e:
        return 1
    res = f(s+3, e, 2) + f(s*2, e, 3)
    if p != 1:
        res += f(s+1, e, 1)
    return res

print(f(3, 30, 0))
