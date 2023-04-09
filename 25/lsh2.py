def mask(z1, z2):
    return int(f'7{z1}6{z2}1')

zs = set()
for i in range(0, 10**8+1):
    zs.add(str(i)[1:])
