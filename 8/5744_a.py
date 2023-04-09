from itertools import product as p

def pr(n):
    d = 2
    while d*d <= n:
        if n % d == 0:
            break
        d += 1
    return d*d > n

def ch(n):
    s = n
    ch = '0246'
    cCh = 0
    for i in ch:
        cCh += s.count(i)
    return cCh >= 3

c = 0
for s in p('0123456', repeat=5):
    s = ''.join(s)
    if s[0] != '0':
        sumCh = sum([int(i) for i in s])
        if pr(sumCh) and ch(s):
            c += 1
print(c)
