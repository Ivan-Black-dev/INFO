def f(x,y,w,z):
    return  not(w == y) and (z <= w) and (not x)

print('x y w z')
for x in {0, 1}:
    for y in {0, 1}:
        for w in {0, 1}:
            for z in {0, 1}:
                r = f(x, y, w, z)
                if r:
                    print(x, y, w, z, '1')
