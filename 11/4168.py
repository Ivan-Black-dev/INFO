def f(x):
    n = 7**500 + 7**200 - 7**50 - x
    if n > 0:
        s = ''
        while n:
            s += str(int(n%7))
            n //= 7
        c = 0
        for i in s:
            c += int(i)
        return c
    else:
        return None

m = 0
for x in range(0, 1000):
    s = ''
    n = x
    while n:
        s += str(n%7)
        n //= 7
    m = max(m, f(int(s[::-1])))
