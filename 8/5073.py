from itertools import product as p

count = 0
for i in p('CONST', repeat=16):
    s = ''.join(i)
    fl = True

    # Условие 1
    for j in 'CONST':
        if j*2 in s:
            fl = False

    # Условие 2
    if s[0] == 'S' or s[-1] == 'S':
        fl = False

    # Условие 3
    else:
        for j in range(len(s)):
            if s[j] == 'S' and s[j-1] == s[j+1]:
                fl = False

    if fl:
        count += 1
print(count)
