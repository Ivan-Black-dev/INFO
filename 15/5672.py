def d(n,m):
    return not n%m

def f(x):
    A = a1 <= x <= a2
    B = 10 <= x <= 40
    return A or (B <= (not d(x, 6)))

minLen = 10**10
se = (0, 0)
for a1 in range(1, 1000):
    for a2 in range(a1, 100):
        if all(f(x) for x in range(1, 1000)):
            if a2 - a1 < minLen:
                minLen = a2 - a1
                se = (a1, a2)
