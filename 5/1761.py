def alg(n):
    nBin = bin(n)[2:][::-1]
    return int(nBin, 2)

for n in range(100, 0, -1):
    res = alg(n)
    if res == 9:
        print(n)
        break
