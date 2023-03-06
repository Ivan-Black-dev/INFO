def con(n, os):
    a =  [str(i) for i in range(0, 10)] + [chr(i) for i in range(ord('a'), ord('z')+1)] + [chr(i) for i in range(ord('A'), ord('Z')+3)]
    s = ''
    while n:
        s += a[n%os]
        n //= os
    return s[::-1]

n = 7 * 512**3200 + 6*256**3100 - 5 * 64**3000 - 4*8**2900 - 1542
res = con(n, 64)
print(res.count('0'))
