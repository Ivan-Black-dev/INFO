with open('17-257.txt') as file:
    data = [ int(i.replace('\n', '')) for i in file.readlines()[:-1]]

maxNum = 0
for num in data:
    if num % 2 == 1:
        maxNum = max(maxNum, num)


count = 0
minSum= 10000000000
for i in range(1, len(data)):
    n1 = data[i-1]
    n2 = data[i]
    if 2 * (n1 + n2) > maxNum:
        count += 1
        minSum = min(minSum, n1 + n2)
print(count, minSum)
