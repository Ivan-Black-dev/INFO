def alg(n):
    a = n
    n = bin(n)[2:]
    n = n.zfill(8)
    n = n.replace('1', '2')
    n = n.replace('0', '1')
    n = n.replace('2', '0')
    n = int(n, 2)
    return n - a


for n in range(0, 256):
    if alg(n) == 99:
        print(n)
