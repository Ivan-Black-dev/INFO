from math import ceil

with open('27_A.txt') as file:
    n = int(file.readline())
    punkts = []
    for i in file.readlines():
        x, y = [int(j) for j in i.split()]
        punkts.append((x,y))

minC = 10**100
for punkt in range(n):
    cost = 0
    for j in range(n):
        r = abs(punkts[punkt][0] - punkts[j][0])
        
        kont = ceil(punkts[j][1]/96)

        cost += kont*r
    minC = min(minC, cost)
print(minC)
