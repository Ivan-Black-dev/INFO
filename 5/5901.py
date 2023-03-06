def alg(n):
    n = n - bin(n)[2:].count('0')
    b = bin(n)[2:]
    b = b[-3:] + b
    return int(b, 2)

res = []

for n in range(1, 1000):
    r = alg(n)
    if r > 224:
        res.append(r)
print(min(res))
