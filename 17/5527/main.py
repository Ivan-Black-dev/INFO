with open('17-345.txt') as f:
    data = [int(i) for i in f]


def getLastNum(n):
    return int(str(n)[-2:])

minP = 999999999
maxP = -999999999
for n in data:
    if getLastNum(n) == 52:
        minP = min(minP, n)
        maxP = max(maxP, n)
raz = maxP - minP    

count = 0
maxS = -9999999999999
for i in range(1, len(data)):
    n1 = data[i-1]
    n2 = data[i]
    if (n1 < raz) ^ (n2 < raz):
        count += 1
        maxS = max(maxS, n1+n2)

print(count, maxS)
        
    
