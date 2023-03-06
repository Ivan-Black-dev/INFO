def alg(c1, c2, c3):
    s = '0' + '1' * c1 + '2' * c2 + '3' * c3
    while ('01' in s) or ('02' in s) or ('03' in s):
        s = s.replace('01', '302')
        s = s.replace('02', '3103')
        s = s.replace('03', '20')
    return s

start = 0
end = start + 100
for s1 in range(start, end):
    for s2 in range(start, end):
        for s3 in range(start, end):
            res = alg(s1, s2, s3)
            if res.count('1') == 18 and res.count('2') == 39 and res.count('3') == 25:
                print(s1, s2, s3)
                break
#3839: 17
#3840: 18
#3841: 21
