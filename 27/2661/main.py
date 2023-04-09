with open('27_B.txt') as file:
    n = int(file.readline())
    par = []
    for i in file.readlines():
        par.append([int(j) for j in i.split()])

minOst = [10**100]*3
maxSum = 0
for p in par:
    n1, n2 = p
    r = abs(n1-n2)
    minOst[r%3] = min(r, minOst[r%3])
    maxSum += min(p)
print(maxSum, minOst)
