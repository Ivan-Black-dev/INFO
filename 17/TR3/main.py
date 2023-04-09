def ch(n1, n2):
    return (str(n1)[-1] == str(n2)[-1]) and ((n1%3 == 0) ^ (n2%3 == 0))




with open('17.txt') as file:
    nums = [int(i) for i in file.readlines()]


m3 = 10**10
for i in nums:
    if str(i)[-1] == '3':
        m3 = min(m3, i)
m3 = m3**2

count = 0
mSq = -10**10
for i in range(1, len(nums)):
    n1, n2 = nums[i-1], nums[i]
    if ch(n1, n2) and n1**2 + n2**2 <= m3:
        count += 1
        mSq = max(mSq, n1**2 + n2**2)
print(count, mSq)
