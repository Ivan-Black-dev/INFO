with open('17.txt') as file:
    nums = [int(i) for i in file.readlines()]

c3 = 0
for i in nums:
    if i % 3 == 0:
        c3 += 1

maxSum = 10**10 * -1
count = 0
for i in range(1, len(nums)):
    n1, n2 = nums[i-1], nums[i]
    if (n1 < 0 or n2 < 0) and (n1 + n2 < c3):
        maxSum = max(maxSum, n1 + n2)
        count += 1

print(count, maxSum)
