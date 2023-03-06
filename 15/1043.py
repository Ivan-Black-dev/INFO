def f(x, y):
    return (y + 2*x < a) or (x > 20) or (y > 30)

for a in range(-100, 100):
    if all( [f(x, y) for x in range(1, 100) for y in range(1, 100)]):
        print(a)
        break
