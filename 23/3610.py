def f(s, e):
    if s == e:
        return 1
    elif s > e:
        return 0
    else:
        return f(s*2, e) + f(s*3, e)

print(f(8, 96) * f(96, 3456))
