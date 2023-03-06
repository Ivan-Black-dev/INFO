with open('17.txt') as file:
    data = [ int(i.replace('\n', '')) for i in file.readlines() ]


sr = sum(data)/len(data)

c = 0
mS = 0
for i in range(1, len(data)):
    n1, n2 = data[i-1], data[i]
    if n1 > sr or n2 > sr:
        mS = max(n1+n2, mS)
        c += 1
print(c, mS)
