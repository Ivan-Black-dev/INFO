with open('17.txt') as file:
    nums = [int(i) for i in file.readlines()]

c100 = 0
for num in nums:
    if num % 100 == 0:
        c100 += 1

c = 0
aMax = -10**10
for i in range(1, len(nums)):
    n1, n2 = nums[i-1], nums[i]
    if n1 < 0 or n2 < 0:
        if n1 + n2 < c100:
            c += 1
            aMax = max(aMax, n1+n2)
print(c, aMax)
