def f(x):
    P = 25 <= x <= 120
    Q = 54 <= x <= 75
    A = x1 <= x <= x2
    return (Q <= ( P == Q )) or ( (not P) <= A )

for x1 in range(1, 150):
    stop = False
    for x2 in range(x1, 150):
        if all( [f(x) for x in range(0, 200)] ):
            print(x1, x2, x2 - x1)
            stop = True
            break
    if stop:
        break
