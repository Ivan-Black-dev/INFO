def f(x):
    return ( ((x & 13 != 0) or (x & a == 0)) <= ( x & 13 != 0 )) or (x & 13 != 0) or (x & a != 0) or (x & 39 == 0)

for a in range(1, 200):
    if all( [f(x) for x in range(1, 200)] ):
        print(a)
        break
