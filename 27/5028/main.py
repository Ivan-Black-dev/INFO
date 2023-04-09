'''
k = 5
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,3,4,5]
'''
k = 1000
with open('27_B.txt') as file:
    nums = [int(i) for i in file.readlines()]

buf = [0] * k
start = 1
minLen = 10**100
for i in range(len(nums)):
    num = nums[i]
    buf[num-1] += 1
    if 0 not in buf:
        for j in range(start, len(nums)-k):
            if buf[nums[j]-1] > 1:
                buf[nums[j]-1] -= 1
                start += 1
            else:
                break
        minLen = min(minLen, i-start+1)
        start = i
        buf = [0] * k
        
print(minLen)
