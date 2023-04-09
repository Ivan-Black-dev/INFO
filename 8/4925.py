from itertools import product as p

c = 0
for n in p('0123456', repeat=7):
    s = ''.join(n)
    if (s[0] != '0') and (s[0] not in ['3', '5']) and (not (('22' in s) and ('44' in s))):
        c += 1

print(c)
