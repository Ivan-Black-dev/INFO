with open('27_B.txt') as file:
    n = int(file.readline())
    pars = []
    for line in file.readlines():
        pars.append([int(i) for i in line.split()])

k = 3
maxSum = 0
minOst = [10**1000]*k
for par in pars:
    c1, c2 = par
    r = abs(c1 - c2)
    minOst[r%k] = min(minOst[r%k], r)
    maxSum += max(par)
minOst[0] = 0
print(maxSum - minOst[maxSum%k])