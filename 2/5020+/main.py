def f(x, y, z):
    return (not(y) or z) and (not( z and x))

print('x y z f')
for x in {0, 1}:
    for y in {0, 1}:
        for z in {0, 1}:
            res= f(x, y, z)
            if res:
                print(f'{x} {y} {z} {int(res)}')
