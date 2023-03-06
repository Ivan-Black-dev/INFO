n = (8**888) + (16 * 16**1616) - (2**444)
s = ''
mN = 0
while n:
    r = n%8
    mN = max(mN, r)
    s += str(r)
    n //= 8
print(s.count(str(mN)))
