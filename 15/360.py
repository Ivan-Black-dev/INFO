def f(x):
    P = 10 <= x <= 25
    Q = 15 <= x <= 30
    R = 25 <= x <= 40
    A = a1 <= x <= a2
    return (Q <= (not R)) and A and (not P)

m = 0
for a1 in range(1, 100):
    for a2 in range(a1, 100):
        if all([f(x) == 0 for x in range(1, 100)]):
            if m < a2 - a1:
                m = a2 - a1
                print(a1, a2)
print(m)
