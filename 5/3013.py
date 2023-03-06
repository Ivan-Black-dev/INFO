def alg(n):
    n = bin(n - 1)[2:].zfill(8)
    n = n.replace('1', '2')
    n = n.replace('0', '1')
    n = n.replace('2', '0')
    return int(n, 2)

for n in range(1, 256):
    if alg(n) == 204:
        print(n)
