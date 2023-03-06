def alg(n):
    ost = n % 2
    n = bin(n)[2:]
    if ost == 0:
        n += '01'
    else:
        n += '10'
    return int(n, 2)

for i in range(0, 100):
    res = alg(i)
    if res > 62:
        print(res)
        break
    
