import math

with open('27_A.txt') as file:
    n, m = [int(i) for i in file.readline().split()]
    punkts = []
    for i in file.readlines():
        h = [int(j) for j in i.split()]
        punkts.append(h)

minC = 10**100
for punkt in range(n):
    cost = 0
    for j in range(n):
        r = abs(punkts[punkt][0] - punkts[j][0])
        k = math.ceil(punkts[j][1]/m)
        cost += r*k
    minC = min(minC, cost)
print(minC)
