def f(start, end):
    d = [0] * (end * 3 + 1)
    d[start] = 1
    for i in range(start, end + 1):
        d[i + 1] += d[i]
        d[i * 2] += d[i]
    return d[end]

print((f(2, 14) * f(14, 29))-f(2, 15))
