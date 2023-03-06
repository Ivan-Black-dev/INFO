def con(n, os):
    a = [str(i) for i in range(0, 10)]
    res = ''
    while n:
        res += a[n%os]
        n //= os
    return res[::-1]

n = 7*729**543 - 6*81**765 - 5*9**987 - 20
res = con(n, 9)
print(res.count('8'))
