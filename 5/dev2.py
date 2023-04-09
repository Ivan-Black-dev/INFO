def alg(n):
    b = bin(n)[2:]
    sumC = b.count('1')
    if sumC % 2 == 0:
        b = '1' + b[:-2] + '01'
    else:
        b = '1' + b[2:] + '10'
    return int(b, 2)

maxR = 0

for n in range(1, 1000000):
    r = alg(n)
    if r <= 100:
        maxR = max(maxR, r)
print(maxR)
