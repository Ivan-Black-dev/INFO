def f(x):
    P = 5 <= x <= 100
    Q = 15 <= x <= 25
    R = 35 <= x <= 50
    A = a1 <= x <= a2
    return (P <= Q) or ( (not A) <= (R) )

m = 1000
for a1 in range(1, 150):
    for a2 in range(a1, 150):
        if all([f(x) for x in range(1, 150)]):
            if a2 - a1 < m:
                m = a2 - a1
                print(a1, a2)
print(m)
