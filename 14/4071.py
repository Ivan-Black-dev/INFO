x = 6**203 + 5 * 6**405 - 3 * 6**144 + 76
p = 6
s = 0
while x:
    s += x%p
    x //= p
print(s)
