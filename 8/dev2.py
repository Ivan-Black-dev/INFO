from itertools import product as p

def chek(n):
    fl = True

    if not(n[-1] in 'BCD'):
        fl = False
    if not (n[1] in 'ABC'):
        fl = False
    if not (n[0] != n[1]):
        fl = False
    if n[2] in 'BCD':
        if not(n[0] in 'AE'):
            fl = False
    if n[2] in 'AE':
        if not(n[0] in 'BCD'):
            fl = False
    return fl

c = 0
for n in p('ABCDE', repeat=4):
    if chek(n):
        c += 1
print(c)
