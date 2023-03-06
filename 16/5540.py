import sys

sys.setrecursionlimit(10_000)


def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n - 1) + 1


print(f(3303)/f(3300))
