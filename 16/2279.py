def f(n):
    if n > 20:
        return n**3 + n
    elif n % 2 == 0:
        return 3*f(n+1) + f(n+3)
    else:
        return f(n+2) + 2 * f(n+3)

c = 0
for n in range(1, 1001):
    r = str(f(n))
    if r.count('1') == 0:
        c += 1
print(c)
