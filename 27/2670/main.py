with open('27_B.txt') as file:
    n = int(file.readline())
    troyks = []
    for line in file.readlines():
        troyks.append(sorted([int(i) for i in line.split()]))

maxSum = 0
minOst = [10**10] * 4
for t in troyks:
    maxSum += t[-1]
    r2 = abs(t[1] - t[2])
    r3 = abs(t[0] - t[2])
    minOst[r2%4] = min(minOst[r2%4], r2)
    minOst[r3%4] = min(minOst[r3%4], r3)
minOst[0] = 0
print(maxSum, minOst)
