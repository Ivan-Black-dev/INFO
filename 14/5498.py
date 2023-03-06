counter = 0
for x in range(0, 100):
    n1 = 1 * x**4 + 3 * x**3 + 1 * x**2 + 5 * x + 2
    n2 = 7 * 100**3 + x * 100**2 + 2 * 100 + 5
    s = n1 + n2
    if s % 11 == 0:
        counter += 1
print(counter)
