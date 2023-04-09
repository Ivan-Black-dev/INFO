def alg(n):
    b = bin(n)[2:]
    if n % 2 ==0:
        return int('10' + b, 2)
    else:
        return int('1' + b + '01', 2)

m = 0
for n in range(1, 9):
    m = max(alg(n), m)
print(m)
