from itertools import product as p


c = 0
for n in p('012345678', repeat=5):
    if n[0] != '0':
        s = ''.join(n)
        if int(s[0]) % 2 == 0 and s[-1] not in {'1', '8'} and s.count('3') <= 1:
            c += 1
print(c)
