def d(n,m):
    return not n%m

def f(x):
    B = 70 <= x <= 80
    return d(x, 12) and B and (not d(x, a))

res = set()
for a in range(1, 1000):
    if all(f(x) == 0 for x in range(1, 1000)):
        res.add(a)
print(len(res))
