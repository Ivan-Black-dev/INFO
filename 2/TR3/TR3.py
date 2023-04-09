def f(x, y, w, z):
    return ((x <= y) or (z <= w)) and ((z == y) <= (w == x))

print('x y w z f')
for x in {0, 1}:
    for y in {0, 1}:
        for w in {0, 1}:
            for z in {0, 1}:
                r = f(x, y, w, z)
                if not r:
                    print(x, y, w, z, int(r))
