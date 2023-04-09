from itertools import product as p

c = 1
r = []
for n in p('ДЕЙНПТЬЯ', repeat=4):
    s = ''.join(n)
    if len(set(s)) == len(s):
        fl = True
        for i in 'ЯЕ':
            if i in s:
                fl = False
                break
        if fl:
            r.append(c)
    c += 1

print(max(r))
