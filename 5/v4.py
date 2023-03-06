def alg(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '1' + b + '0'
    else:
        b = '11' + b + '10'
    return int(b, 2)


def s(n):
    return sum([int(i) for i in str(n)])


for n in range(0, 100):
    r = s(alg(n))
    if r > 17:

        print(n, r)
