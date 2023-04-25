'''with open('TEST.txt') as file:
    n = int(file.readline())
    nums = [int(i) for i in file.readlines()]

c = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if (nums[i] * nums[j]) % 6 == 0:
            c += 1
print(c)
'''

k2 = 0
k3 = 0
k6 = 0
with open('27_B.txt') as file:
    n = int(file.readline())
    for i in range(n):
        num = int(file.readline())
        if num % 6 == 0:
            k6 += 1
        elif num % 2 == 0:
            k2 += 1
        elif num % 3 == 0:
            k3 += 1
ost = n - k6
res = k6 * (k6 - 1) // 2
res += k6 * ost
res += k2 * k3
print(res)
