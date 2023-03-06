def alg(n):
    # 1
    if n % 2 == 0:
        n /= 2
    else:
        n -= 1
    # 2
    if n % 3 == 0:
        n /= 3
    else:
        n -= 1
    # 3
    if n % 5 == 0:
        n /= 5
    else:
        n -= 1
    return n

count = 0
for i in range(2, 10000):
    if alg(i) == 3:
        count += 1
print(count)
