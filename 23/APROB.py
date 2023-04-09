def f(s, e):
    if s == e:
        return 1
    if s < e:
        return 0
    else:
        return f(s - 2, e) + f(s // 2, e)


print(f(40, 10) * f(10, 2))
