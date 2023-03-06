def d(n, m):
    return not n%m

def f(x):
    return ((d(x, 2) <=  (not d(x, 5))))or (x + a >= 90)


for a in range(1, 200):
    if all(f(x) for x in range(1, 200)):
        print(a)
