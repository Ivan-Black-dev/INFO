with open('17.txt') as file:
    data = [int(i) for i in file.readlines()]

min103 = 100000
for num in data:
    if num % 103 == 0:
        min103 = min(min103, num)

maxSum = 0
count = 0
for i in range(1, len(data)):
    n1, n2 = data[i-1], data[i]
    if abs(n1 - n2) % min103 == 0 and (n1 + n2) % 2 == 0:
            print(n1, n2)
            count += 1
            maxSum = max(maxSum, n1 + n2)

print(count, maxSum)
