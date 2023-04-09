def f(n):
    if n < 3:
        return 1
    if n % 2 != 0:
        return f(n-1) + n
    if n % 2 == 0:
        return f(n-3) + 2*n

print(f(2048) - f(2041))
