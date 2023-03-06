from itertools import product as p


for c in zip(p('ГЕКЭ023', repeat=4), range(1, 10000)):
    i, n = c
    s = ''.join(i)
    if s[0] == '0':
             print(n, s)
             input()
    
