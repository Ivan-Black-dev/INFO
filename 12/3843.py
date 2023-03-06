def alg(s):
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01', '30', 1)
        s = s.replace('02', '3103', 1)
        s = s.replace('03', '1201', 1)
    return s


for c1 in range(1, 50):
    for c2 in range(1, 50):
        for c3 in range(1, 50):
            r = alg('0' + '1' * c1 + '2' * c2 + '3' * c3)
            if r.count('1') == 42 and r.count('2') == 31 and r.count('3') == 59:
                print(c1, c2, c3)
