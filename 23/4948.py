def f(s, e, p):
    if s > e:
        return 0
    if s == e:
        return 1
    if p:
        return f(s+1, e, False) + f(s+2, e, False)
    else:
        return f(s+1, e, False) + f(s+2, e, False) + f(s*2, e, True)

print(f(1, 15, False))
