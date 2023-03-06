def alg(n):
    b = bin(n)[2:]
    b = b.zfill(8)
    b = b.replace('1', '2')
    b = b.replace('0', '1')
    b = b.replace('2', '0')
    return int(b, 2) - n

for i in range(0, 256):
    res = alg(i)
    if res == 113:
        print(i)
        break
