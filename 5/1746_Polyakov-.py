def alg(n):
    n = bin(n)[2:]
    one = n.count('1')
    zero = n.count('0')
    if one > zero:
        n += '1'
    else:
        n += '0'
    return int(n, 2)


maxNum = 0
for i in range(0, 44):
    res = alg(i)
    maxNum = max(maxNum, res)
print(maxNum)
        
