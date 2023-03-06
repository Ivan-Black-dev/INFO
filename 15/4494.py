def f(x, y):
    return ( 2*y + x != 70 ) or (x < y) or (a < x)

for a in range(0, 1000):
    if all( [f(x, y) for x in range(0, 100) for y in range(0, 100)] ):
        print(a)
