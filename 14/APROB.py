n = 2 * (729**1021) - 2 * (243**1022) + (81**1023) - 2 * (27 ** 1024) - 1025

def con(n, o):
    r = ''
    while n:
        r += str(n%o)
        n //= o
    return r[::-1]
print(con(n, 3).count('0'))
