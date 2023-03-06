def f(s, e):
    if s == e:
        return 1
    if s > e or s == 60:
        return 0
    else:
        return f(s+5, e) + f(s*5, e)

print(f(5, 30) * f(30, 280))
