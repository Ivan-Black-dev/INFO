def con(n, o):
    res = ''
    while n:
        res += str(n%o)
        n //= o
    return res[::-1]


def sumN(n):
    return sum([int(i) for i in n])

for x in range(1, 1000):
    n = 27**7 - 3**11 + 36 - x
    s = con(n, 3)
    if sumN(s) == 22:
        print(x)
        break
