def alg(n):
    n = n * 10 + n % 10
    n = bin(n)[2:]
    countOne = n.count('1')
    if countOne % 2 == 0:
        n += '0'
    else:
        n += '1'
    return int(n ,2)

for n in range(0, 100):
    res = alg(n)
    if res > 413:
        print(n)
        break
