with open('17-271.txt') as file:
    data = [int(i.replace('\n', '')) for i in file.readlines()[:-1]]


def getLastNum(n):
    return int(str(n)[-1])

sa = sum(data)/len(data)

#data = [12, 18, 2, -15, 11, 16]
count = 0
maxSum = -10000000
for i  in range(1, len(data)):
    n1 = data[i]
    n2 = data[i-1]
    #print(n1, n2, getLastNum(n1), getLastNum(n2))
    if getLastNum(n1) + getLastNum(n2) == 7:
            count += 1
            if n1 < sa and n2 < sa:
                maxSum = max(maxSum, n1+n2)
print(count, maxSum)
