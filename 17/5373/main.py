with open('17-339.txt') as file:
    data = [int(i) for i in file]

minP = 200000000
for n in data:
    if n > 0 and n% 19 == 0:
        minP = min(n, minP)
    
count = 0
maxS = -9999999999
for i in range(1, len(data)):
    n1 = data[i-1]
    n2 = data[i]
    if n1 + n2 < minP:
        count += 1
        maxS = max(maxS, n1+n2)
print(count, abs(maxS))
