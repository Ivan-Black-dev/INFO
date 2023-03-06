def fact(n):
    res = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            res.append(d)
            if n % (n//d) == 0:
                res.append(n//d)
        d += 1
    return sorted(list(set(res)))


for n in range(157898, 157990+1):
    r = fact(n)
    if len(r) == 4:
        print(r[-1], r[-2])
