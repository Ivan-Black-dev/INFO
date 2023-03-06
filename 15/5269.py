def f(x):
    P = 117 <= x <= 158
    Q = 129 <= x <= 180
    A = x1 <= x <= x2
    return (P) <= ( (Q and (not A)) <= (not P) )
minL = 10000
for x1 in range(100, 200):
    for x2 in range(x1, 200):
        if all( [f(x) for x in range(0, 200)] ):
            if x2 - x1 < minL:
                minL = x2-x1
                print(x1, x2)
print(minL)
