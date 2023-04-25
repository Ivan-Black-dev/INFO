from itertools import product as p

def mask(s, v):
    return int(f'123{s}45{v}67')

r = []
for n in range(0, 4):
    for s in p('02468', repeat=n):
        for v in range(10):
            s = ''.join(s)
            num = mask(s, v)
            if num%257 == 0:
                r.append(num)

for i in sorted(r):
    print(i, i//257)
