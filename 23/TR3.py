def f(s, e, u):
    if s == e and u == 1:
        return 1
    if s > e or u > 1:
        return 0
    else:
            return f(s+1, e, u) + f(s+2, e, u) + f(s*2, e, u+1) + f(s*3, e, u+1)

print(f(1, 11, 0))
