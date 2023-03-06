def f(x, y):
    return ( 75 != 2*x + 3*y ) or (a > 3*x) or (a > 2*y)

for a in range(0, 100):
    if all( [f(x, y) for x in range(0, 100) for y in range(0, 100)]):
        print(a)
        break
