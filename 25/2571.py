def alg(n):
    r = []
    d = 1
    while d**2 <= n:
        if n % d == 0:
            r.append(d)
            if d != n//d:
                r.append(n//d)
        d += 1
    return sorted(r)



for n in range(190201, 190221):
    r = alg(n)
    if len(r) == 4:
        print(r[-1], r[-2])
        
