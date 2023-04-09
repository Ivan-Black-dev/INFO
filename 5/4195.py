def d(n, m):
    return not n%m

def f(x):
    return (not(d(x, 16) == d(x, 24))) <= d(x, a)

for a in range(1, 100):
    if all(f(x) for x in range(1, 100)):
        print(a)
