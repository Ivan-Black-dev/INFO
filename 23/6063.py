def f(s, e):
    if s == e:
        return 1
    elif s > e or '5' in str(s):
        return 0
    else:
        return f(s+1, e) + f(s+3, e) + f(s*3, e)
print(f(1, 49))
