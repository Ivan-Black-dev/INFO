def isP(n):
    d = 2
    while d*d<=n:
        if n % d == 0:
            break
        d += 1
    return d*d>n

def f(x):
    n1 = 5 * 18**3 + 6 * 18**2 + x * 18 + 3
    n2 = 4 * 18**2 + x * 18 + 9
    n3 = 5 * 18**3 + 7 * 18**2 + x * 18 + 1
    return n1 + n2 - n3

c = 0
for x in range(18):
    r = f(x)
    if isP(r):
        c += 1
print(c)
