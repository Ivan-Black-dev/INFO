def add1(n):
    return int(str(n) + '1')

def f(s, e):
    if s == e:
        return 1
    elif s > e:
        return 0
    else:
        return f(s+1, e) + f(add1(s), e)


print(f(1, 555))
