def f(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return f(n/2)
    else:
        return 1 + f(n-1)

c = 0
for n in range(1, 501):
    if f(n) == 3:
        c += 1
print(c)
