def alg(s):
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01', '30', 1)
        s = s.replace('02', '3103', 1)
        s = s.replace('03', '1201', 1)
    return s

# 1 - 3
# 2 - 31123
# 3 - 123

# 1 - 59
# 2 - 40
# 3 - 66

# c1 - кол-во единиц
# c2 - кол-во двоек
# c3 - кол-во троек
'''
c2 * 2 + c3 = 59
c2 + c3 = 40
c1 + c2 * 2 + c3 = 66

Ответ 16?
'''
for c1 in range(1, 50):
    for c2 in range(1, 50):
        for c3 in range(1, 50):
            r = alg('0' + '1' * c1 + '2' * c2 + '3' * c3)
            if r.count('1') == 59 and r.count('2') == 40 and r.count('3') == 66:
                print(c1, c2, c3)
