def f(b):
    c1 = b.count('1')
    c0 = b.count('0')
    if c0 == c1:
        b += b[-1]
    elif c0 > c1:
        b += '1'
    else:
        b += '0'
    return b


def alg(n):
    b = bin(n)[2:]
    return int(f(f(f(b))))


for i in range(101, 1000):
    res = alg(i)
    if res % 2 == 0 and res % 4 != 0:
        print(i)
        break
    
