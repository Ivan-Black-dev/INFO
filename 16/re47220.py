import sys

sys.setrecursionlimit(2023)

def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n-1)

print(f(2023)/f(2020))
