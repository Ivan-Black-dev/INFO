#2663
with open('27_A.txt') as file:
    n = int(file.readline())
    pars = []
    for line in file.readlines():
        pars.append([int(i) for i in line.split()])

k = 3
minSum = 0
minOst = [10**10]*k
for par in pars:
    c1, c2 = par
    r = abs(c1 - c2)
    minOst[r%k] = min(r, minOst[r%k])
    minSum += min(par)

minOst[0] = 0
print(minSum, minOst)
print(minSum + minOst[3-(minSum%k)])
