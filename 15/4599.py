def f(x):
    P = 15 <= x <= 30
    Q = 5 <= x <= 60
    A = a1 <= x <= a2
    return ((not Q) or P) and A

m = 0
for a1 in range(1, 100):
    for a2 in range(a1, 100):
        if all( [f(x) == 0 for x in range(1, 100)] ):
            if a2 - a1 > m:
                m = a2 - a1
                print(a1, a2)
print(m)
