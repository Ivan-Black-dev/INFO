from itertools import product as p

c = 1
for n in p('АВЛОР', repeat=4):
    s = ''.join(n)
    if s[0] == 'Л':
        print(c, s)
        input()
    c += 1
