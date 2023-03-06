def alg(s):
    while ('555' in s) or ('888' in s):
        s = s.replace('555', '8', 1)
        s = s.replace('888', '55', 1)
    return s

a = set()
for i in range(2, 1000):
    res = alg('5' * i)
    a.add(res)

print(a, len(a))
