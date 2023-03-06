def alg(n):
    b = bin(n)[2:]
    if b.count('0') < b.count('1'):
        b += '0'
    else:
        b += '1'
    l = len(str(b))

    if l % 2 == 0:
        iskl = {l//2, l//2-1}
    else:
        iskl = {l//2-1, l//2, l//2+1}

    res = ''    
    for i in range(0, l):
        if i in iskl:
            pass
        else:
            res += b[i]
    return int(res, 2)


count = 0
for i in range(4, 100000):
    if alg(i) == 58:
        count += 1
print(count)
