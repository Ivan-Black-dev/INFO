def fact(n):
    d = 2
    res = []
    while d*d <= n:
        if n % d == 0:
            res.append(d)
            if n % (n//d) == 0:
                res.append(n//d)
        d += 1
    return list(set(res))

def p(li):
    res = 1
    for i in li:
        res *= i
    return res


dels = []
for i in range(174457, 174505+1):
    f = fact(i)
    if len(f) == 2:
        dels.append((f[0], f[1]))


for i in range(len(dels)-1):
    for j in range(len(dels)-i-1):
        if p(dels[j]) > p(dels[j+1]):
            dels[j], dels[j+1] = dels[j+1], dels[j]

for i in dels:
    print(min(i), max(i))
