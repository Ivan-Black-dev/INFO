def d(n,m):
    return not n%m


def f(x):
    return (d(x, (a-21)) and d(x, (40-a))) <= d(x, 90)

for a in range(22, 40):
    if all(f(x) for x in range(1, 100)):
        print(a)
