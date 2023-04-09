def f(a, b):
    if a == 0 and b == 0:
        return 0
    if a > b:
        return f(a-1, b) + b
    if a <= b and b > 0:
        return f(a, b-1) + a


def fact(n):
    r = []
    d = 1
    while d**2 <= n:
        if n % d == 0:
            r.append(d)
            if n//d != d:
                r.append(n//d)
        d += 1
    return r
'''
for a in range(1000, 1010):
    for b in range(1000, 1010):
        print(f(a, b))

'''
