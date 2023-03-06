def alg(n):
    a = bin(n)[2:]
    lN = a[1]
    rN = a[len(a)-2]
    a += rN + lN
    return int(a, 2)


for i in range(2, 100):
    if alg(i) > 100:
        print(i)
        break
