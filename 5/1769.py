def alg(n):
    return int(bin(n)[2:][::-1], 2)


for n in range(1000, 10000):
    if alg(n) == 29:
        print(n)
        break
    
