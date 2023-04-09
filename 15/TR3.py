def f(x):
    return ((x&35 != 0) or (x&22 != 0)) <= ( (x&15 == 0) <= (x&a != 0) )


for a in range(0, 100):
    if all(f(x) for x in range(0, 100)):
        print(a)
        break
