def add2(n):
    return int(str(n) + '2')

def f(s, e):
    if s == e:
        return 1
    if s > e:
        return 0
    else:
        return f(s+2, e) + f(add2(s), e)

print(f(2, 900))
