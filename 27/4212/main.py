with open('27_A.txt') as file:
    n = int(file.readline())
    num = [int(i) for i in  file.readlines()]

maxSum = 0
minLen = 10**100
for s in range(n):
    for e in range(s, n):
        summ = sum(num[s:e])
        if summ % 69 == 0:
            if summ > maxSum:
                maxSum = summ
                minLen = min(minLen, e-1-s)
print(minLen)