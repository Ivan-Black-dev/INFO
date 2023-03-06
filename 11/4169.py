def c(x, n):
    s = ''
    while x:
        s += str(int(x%n))
        x //= n
    return int(s[::-1])

counter = 0
for i in range(10000000, 1000000000):
    if len(hex(i)) <= 8 and len(oct(i)) >= 11 and str(i)[-1] == '5':
        counter += 1
print(counter)
