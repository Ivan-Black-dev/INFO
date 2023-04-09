from itertools import product as p

c = 1
for n in p('ГЕКЭ023', repeat=4):
    s = ''.join(n)
    if s[0] in '023':
        fl = True
        for i in 'ГЕКЭ023':
            if i*2 in s:
                fl = False
                break
        if fl:
            print(c, s)
    c += 1
