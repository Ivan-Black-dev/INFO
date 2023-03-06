from itertools import product as p
k = 0
for i in p('ШКОЛА', repeat = 3):
    s = ''.join(i)
    if s.count('К') == 1:
        k += 1
print(k)
