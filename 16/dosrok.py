def f(n):
    if n >= 2025:
        return n
    else:
        return n + 3 + f(n+3)
