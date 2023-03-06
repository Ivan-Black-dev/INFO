def alg(n):
    c1 = n // 100
    c2 = (n//10) % 10
    c3 = n % 10
    s1 = c1 * c2
    s2 = c2 * c3
    if s1 >= s2:
        res = str(s2) + str(s1)
    else:
        res = str(s1) + str(s2)
    return res

for n in range(999, 100-1, -1):
    if alg(n) == '621':
        print(n)
        break
