v = []

for i in range(10**5):
    v.append(str(i)[1:])

def m(z1, z2):
    return int(f'19{z1}105{z2}9')

v = set(v)
for z1 in v:
    for z2 in v:
        n = m(z1, z2)
        if n % 9601 == 0 and n <= 10**10:
            print(n, n/9601)
