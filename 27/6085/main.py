def ch3(n):
    c = 0
    while n > 2:
        if n % 3 == 0:
            c += 1
            n /= 3
        else:
            break
    if c > 6:
        return 6
    return c

def ostat8(n):
    if n % 8 == 0:
        return 0
    else:
        return 8 - n % 8


with open('B.txt') as file:
    f = [int(i) for i in file.readlines()]

d = [[0 for i in range(0, 6+1)] for i in range(0, 8+1)]
f1 = f[15s:]

count = 0
for i in range(len(f1)):
    dy = ch3(f[i])
    dx = f[i] % 8
    d[dx][dy] += 1

    n = f1[i]
    y = ostat8(n)
    x = 6 - ch3(n)
    for x1 in range(x, 6):
        count += d[y][x1]
print(count)



