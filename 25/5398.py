def mask(z1):
    return int(f'12345{z1}76')

chisla = set()
for i in range(10, 10000):
    chisla.add( str(i)[1:])
chisla.add('')

r = []
for i in chisla:
    res = mask(i)
    if res % 73 == 0:
        r.append([res, res // 73])
    if len(r) == 5:
        break
print(sorted(r))
