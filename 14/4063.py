x = 7**103 + 6 * 7**104 - 3 * 7**57 + 98
s = ''
while x:
    s += str(x % 7)
    x //= 7
s = s[::-1]
print(s)
print(s.count('6'))
