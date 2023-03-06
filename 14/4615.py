x = 12**34 + 7 * 12**26 - 3 * 12**16 + 2 * 12**5 + 552
p = 12
a = '0123456789ABCD'
s = set()
while x:
    s.add(a[x%p])
    x //= p
print(s)
print(len(s))
