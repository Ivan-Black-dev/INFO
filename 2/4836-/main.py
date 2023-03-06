def f(x, y, w, z):
    return ( ( w <= z) and ( (not x) <= y)) <= ((y == w) or (z and (not x)) )

print('x y z w f')
for x in {0, 1}:
    for y in {0, 1}:
        for w in {0, 1}:
            for z in {0, 1}:
                res = f(x, y, w, z)
                if (not res):
                    print(f'{x} {y} {w} {z} {int(res)}')
