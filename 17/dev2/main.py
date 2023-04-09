with open('17.txt') as file:
    nums = [int(i) for i in file.readlines()]

min123 = 10**10
for num in nums:
    if num % 123 == 0:
        min123 = min(num, min123)


def chek(n):
    return n%2023 >= min123


count = 0
maxSum = 0
for i in range(1, len(nums)):
    n1, n2 = nums[i-1], nums[i]
    if chek(n1) ^ chek(n2):
        count += 1
        maxSum = max(maxSum, n1+n2)

print(count, maxSum)
