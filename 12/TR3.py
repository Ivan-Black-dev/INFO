def f(s):
    while '00' not in s:
        if '001' in s:
            s = s.replace('011', '101', 1)
        else:
            s = s.replace('01', '40', 1)
            s = s.replace('02', '20', 1)
            s = s.replace('0222', '1401', 1)
    return s


for c in range(10, 1000):
    s = f('0' + '1' * c + '2' * c + '0')
    if s.count('1') == 6 and s.count('2') == 9:
        print(s.count('4'), c)
