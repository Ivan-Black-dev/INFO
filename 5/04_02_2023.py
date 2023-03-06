def alg(n):
    b = bin(n)[2:]
    s = b.count('1')
    if s % 2 == 0:
        r = '1' + b[2:] + '0'
    else:
        r = '11' + b[2:] + '1'
    return int(r, 2)

minR = 10**10
N = 0
for n in range(1, 10000):
    r = alg(n)
    if r > 25 and minR > r:
        N = n
        minR = r
            
print(N, minR)
