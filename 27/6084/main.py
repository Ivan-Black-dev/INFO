with open('27_A.txt') as file:
    n = int(file.readline())
    nums = [int(i) for i in file.readlines()]
r = 11

c = 0
for i in range(n-r):
    for j in range(i+r, n):
        n1, n2 = nums[i], nums[j]
        if (n1 + n2) % 13 == 0 and (n1*n2)% 1024 == 0:
            c += 1
print(c)
