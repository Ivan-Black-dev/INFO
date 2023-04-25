def f(s, e):
    if s == e:
        return 1
    if s > e:
        return 0
    else:
        return f(s+3, e) + f(s+1, e) + f(s*3, e)
print(f(1, 34))
