def fact(n):
    d = 2
    res = []
    while d*d <= n:
        if n % d == 0:
            res.append(d)
            if d != n // d:
                res.append(n//d)
        d += 1
    return sorted(res)
            
def P(n):
    dels = fact(n)
    #print(dels)
    if len(dels) < 5:
        return 0
    else:
        dels = dels[:5]
        #print(dels)
        res = 1
        for i in dels:
            res *= i
        return res


n = 200_000_000
c = 0
while c != 5:
    p = P(n)
    if str(p)[-1] == '1' and p <= n:
        print(p, fact(n)[4])
        c += 1
    n += 1
    
