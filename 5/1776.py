def alg(n):
    nBin = bin(n)[2:]
    if n % 2 == 0:
        nBin += '00'
    else:
        nBin += '11'
    return int(nBin, 2)

for i in range(0, 100):
    res = alg(i)
    if res > 115:
        print(i)
        break
