def alg(s):
    s = '>' + '0' * 39 + '1' * n + '2' * 39
    while '>1' in s or '>2' in s or '>0' in s:
        s = s.replace('>1', '22>', 1)
        s = s.replace('>2', '2>', 1)
        s = s.replace('>0', '1>', 1)
    return s

def summ(s):
    s = s.replace('>', '')
    return sum( [int(i) for i in s] )

def pr(n):
    d = 2
    while d*d <= n and n%d != 0:
        d += 1
    return d*d > n


for n in range(0, 100):
    res = alg(n)
    if pr(summ(res)):
        print(n, summ(res))
