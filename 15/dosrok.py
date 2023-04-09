def f(x):
    return (x&39 == 0) or ( (x&11 == 0) <= (not x&a == 0))


for a in range(0, 100):
    if all(f(x) for x in range(0, 100)):
        print(a)
