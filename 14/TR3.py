def f(x, y, p):
    n1 = 3 * p**3 + 2 * p**2 + x * p + 8
    n2 = x * p**3 + x * p**2 + x * p + 9
    n3 = y * p**3 + y * p**2 + 2
    return n1 + n2 == n3

for p in range(10, 50):
    for x in range(0, p):
        for y in range(0, p):
            if f(x, y, p):
                print(y * p** 2 + y * p + x)
