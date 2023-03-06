def fact(n):
    res = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            res.append(d)
            if n // d != d:
                res.append(n//d)
        d += 1
    return sorted(set(res))


def s(n):
    dels = fact(n)
    if len(dels) < 2:
        return 0
    else:
        return dels[-1] + dels[-2]

n = 10_000_000
c = 0

while c != 5:
    if (s(n) < 100_000) and (n % 1000 == 112):
        print(s(n))
        c += 1
    #print(s(n))
    n += 1
