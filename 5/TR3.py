def s(n):
    return sum([int(i) for i in str(n)])


def a(n):
    b = bin(n)[2:]
    if s(n) % 2 != 0:
        b += '1'
    else:
        b += '0'
    return int(b, 2)


def alg(n):
    return a(a(a(n)))


# 10**7, 10**9
'''
c = 0
for i in range(10**7 + 5 * 10**6, 10**9):
    n = alg(i)
    if 123_456_789 <= n <= 1_987_654_321:
        c += 1
    if n > 1_987_654_321:
        break
print(c)
'''
