def alg(n):
    b = bin(n)[2:]
    l = b.count('1')
    if l % 2 == 1:
        b += '1'
    else:
        b += '0'
    l = b.count('1')
    if l % 2 == 1:
        b += '1'
    else:
        b += '0'
    return int(b, 2)



for n in range(1, 1000):
    res = alg(n)
    if res > 80:
        print(n, res)
        break
