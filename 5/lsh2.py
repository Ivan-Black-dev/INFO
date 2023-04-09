def alg(n):
    b = bin(n)[2:]
    s = b.count('1')
    if s % 2 == 0:
        b = '10' + b[:-2] + '00'
    if s % 2 != 0:
        b = '11' + b[:-2] + '11'
    return int(b, 2)

m = set()
for n in range(100, 201):
    r = alg(n)
    if r % 3 == 0:
        m.add(r)
print(sum(m))
