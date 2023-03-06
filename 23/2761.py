def f(s, e, c):
    if s == e and c == 6:
        return 1
    elif s > e or c > 6:
        return 0
    else:
        return f(s+1, e, c+1) + f(s+2, e, c+1) + f(s*2, e, c+1)

print(f(1, 20, 0))
