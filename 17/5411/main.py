with open('17.txt') as file:
    data = [ int(i) for i in file.readlines()]

count = 0
sa = sum(data)/len(data)
maxSum = data[0] + data[1]
for i in range(2, len(data)):
    p1, n1, n2, p2 = data[i-3], data[i-2], data[i-1], data[i]
    if p1 * p2 < n1 * n2:
        maxSum = max(maxSum, n1 + n2)
        if n1 > sa or n2 > sa:
            count += 1

print(maxSum, count)
        
