def pr(n):
    d = 2
    while d*d <= n and n%d != 0:
        d += 1
    return d*d > n

n = 1
for i in range(3532000, 3532160+1):
    if pr(i):
        print(n, i)
        n += 1
