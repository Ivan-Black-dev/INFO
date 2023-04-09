with open('27_A.txt') as file:
    n = int(file.readline())
    nums = [int(i) for i in file.readlines()]

c = 0
for i in range(n):
    for j in range(i+1, n):
        n1, n2 = nums[i], nums[j]
        if (n1 + n2) % 5 == 0 and (n1*n2) % 2048 == 0:
            c += 1
print(c)
