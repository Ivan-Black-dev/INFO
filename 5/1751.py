def alg(b):
    b -= 1
    n = bin(b)[2:]
    n = n.zfill(8)
    n = n.replace('1', '2')
    n = n.replace('0', '1')
    n = n.replace('2', '0')
    return int(n, 2)

for n in range(1, 256):
    res = alg(n)
    if res == 143:
        print(n)
        break
