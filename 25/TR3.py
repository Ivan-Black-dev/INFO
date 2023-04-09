def mask(v, z):
    return int(f'1{v}7246{z}1')


zNum = []
for i in range(10, 10**4):
    zNum.append(str(i)[1:])
zNum = list(set(zNum))
zNum.append('')

r = []
for z in zNum:
    for v in range(0, 10):
        m = mask(v, z)
        if m % 4173 == 0:
            r.append(m)
print(r)
