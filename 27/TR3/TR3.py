with open('27-B.txt') as file:
    f = [int(i) for i in file.readlines()]

# 2187 = 3**7

def ch3(n):
    c = 0
    while n % 3 == 0:
        c += 1
        n //= 3
    if c > 7:
        return 7
    return c


f1 = f[18:]

d = [[0 for i in range(7)] for i in range(8)]

s = 0
for i in range(len(f1)):
    x = ch3(f[i])
    y = f[i] % 8
    for x1 in range(x):
        d[y][x1] += 1

    x = ch3(f1[i])
    y = f1[i] % 8
    s += d[y][-x]
print(s)
