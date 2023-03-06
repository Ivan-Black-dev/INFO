def ch3(n):
    c = 0
    while n > 2:
        if n % 3 == 0:
            c += 1
            n /= 3
        else:
            break
    return c


with open('27A.txt') as file:
    f = [int(i) for i in file.readlines()]

d = [[0 for i in range(0, 6+1)] for i in range(0, 8+1)]
f1 = f[15:]

count = 0
for i in range(len(f1)):
    dy = ch3(f1[i])
    dx = f1[i] % 8
    d[dx][dy] += 1

    n = f[i]
    ost8 = n % 8
    c3 = ch3(n)
    y = ost8
    if y == 8:
        y = 0
    x = c3
    count += d[y][x]
print(count)



