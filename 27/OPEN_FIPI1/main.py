ot = 50

with open('27_A.txt') as file:
    n, m = [int(i) for i in file.readline().split()]
    punkts = []
    for i in file.readlines():
        punkts.append([int(j) for j in i.split()])

for punkt in punkts:
    summ = 0
    for i in punkts:
        summ += 
