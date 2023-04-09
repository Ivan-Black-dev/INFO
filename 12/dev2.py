def alg(s):
    while '01' in s:
        if '1' in s:
            s = s.replace('1', '10', 1)
        if '01' in s:
            s = s.replace('01', '1000')
    return s

for n in range(1, 1000):
    s = alg('0'*n + '1')
    if s.count('0') >= 100:
        print(n)
        break
