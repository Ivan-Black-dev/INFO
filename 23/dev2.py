def f(s, e):
    if s == e:
        return 1
    if s < e:
        return 0
    else:
        return f(s-1, e) + f(s//2, e)

print(f(89, 30) * f(30, 7))
