def f(x, y, z, w):
    return w and ((z or y) == (z and x))


print('x y z w f')
for x in {0, 1}:
    for y in {0, 1}:
        for z in {0, 1}:
            for w in {0, 1}:
                r = f(x, y, z, w)
                if not r:
                    print(x, y, z, w, int(r))
